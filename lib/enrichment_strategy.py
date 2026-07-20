"""Defines the abstract Strategy interface for transcript enrichment backends."""
from abc import ABC, abstractmethod

class LLMStrategy(ABC):
    """Defines the contract for any transcript enrichment backend."""

    @abstractmethod
    def enrich(self, record: dict) -> dict:
        """Take a raw transcript record and return an enriched dict
        matching the video_id/cleaned_text/tech_terms/book_names schema."""
        raise NotImplementedError
