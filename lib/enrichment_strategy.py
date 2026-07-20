"""Defines the abstract Strategy interface for transcript enrichment backends."""
from abc import ABC, abstractmethod

class LLMStrategy(ABC):
    """Defines the contract for any transcript enrichment backend."""

    @abstractmethod
    def enrich(self, record: dict) -> dict:
        """Take a raw transcript record and return an enriched dict
        matching the video_id/cleaned_text/tech_terms/book_names schema."""
        raise NotImplementedError

class GeminiStrategy(LLMStrategy):
    """Concrete strategy wrapping the Gemini API for transcript enrichment."""

    def __init__(self, client, model_name: str, config):
        """Store the injected Gemini client, model name, and generation config."""
        self.client = client
        self.model_name = model_name
        self.config = config

    def enrich(self, record: dict) -> dict:
        """Not yet implemented — logic ported in the next step."""
        raise NotImplementedError
