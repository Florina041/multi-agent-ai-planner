from __future__ import annotations

import os

from dotenv import load_dotenv

from app.llm.provider_interface import LLMProvider

load_dotenv()


class OpenAIProvider(LLMProvider):
    def __init__(self) -> None:
        self.api_key = os.getenv("OPENAI_API_KEY", "").strip()
        self.model = os.getenv("OPENAI_MODEL", "gpt-4o-mini")

    def available(self) -> bool:
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
            return response.output_text.strip()
        except Exception:
            return ""
