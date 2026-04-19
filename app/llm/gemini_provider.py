import os
from dotenv import load_dotenv
from app.llm.provider_interface import LLMProvider

load_dotenv()


class GeminiProvider(LLMProvider):
    def __init__(self):
        self.api_key = os.getenv("GEMINI_API_KEY", "").strip()
        # You can change model if needed
        self.model = os.getenv("GEMINI_MODEL", "gemini-1.5-flash")

    def available(self) -> bool:
        return bool(self.api_key)

    def complete(self, prompt: str) -> str:
        if not self.available():
            return ""

        try:
            import google.generativeai as genai

            # Configure API
            genai.configure(api_key=self.api_key)

            model = genai.GenerativeModel(self.model)

            response = model.generate_content(prompt)

            # ✅ Primary safe extraction
            if hasattr(response, "text") and response.text:
                return response.text.strip()

            # ✅ Fallback (some responses store parts differently)
            if hasattr(response, "candidates") and len(response.candidates) > 0:
                parts = response.candidates[0].content.parts
                if len(parts) > 0 and hasattr(parts[0], "text"):
                    return parts[0].text.strip()

            return ""

        except Exception as e:
            print("Gemini Error:", e)
            return ""