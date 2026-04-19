import os
from dotenv import load_dotenv
from app.llm.provider_interface import LLMProvider

load_dotenv()


class OpenAIProvider(LLMProvider):
    def __init__(self):
        self.api_key = os.getenv("OPENAI_API_KEY", "").strip()
        self.model = os.getenv("OPENAI_MODEL", "gpt-4o-mini")

    def available(self):
        return bool(self.api_key)

    def complete(self, prompt: str) -> str:
        if not self.available():
            return ""

        try:
            from openai import OpenAI

            client = OpenAI(api_key=self.api_key)

            response = client.responses.create(
                model=self.model,
                input=prompt,
                max_output_tokens=400,
            )

            # ✅ PRIMARY (works in most cases)
            if hasattr(response, "output_text") and response.output_text:
                return response.output_text.strip()

            # ✅ FALLBACK (safe parsing)
            if hasattr(response, "output") and len(response.output) > 0:
                content = response.output[0].content
                if len(content) > 0 and hasattr(content[0], "text"):
                    return content[0].text.strip()

            return ""

        except Exception as e:
            print("OpenAI Error:", e)  # helpful for debugging
            return ""