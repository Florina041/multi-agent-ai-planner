from __future__ import annotations

from app.llm.provider_interface import LLMProvider


class GeminiProvider(LLMProvider):
    def available(self) -> bool:
        return False

    def complete(self, prompt: str) -> str:
        return ""
