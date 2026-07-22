"""Defines the abstract Strategy interface for transcript enrichment backends."""

from abc import ABC, abstractmethod
import json
import logging
import sys


class LLMStrategy(ABC):
    """Defines the contract for any transcript enrichment backend."""

    @abstractmethod
    def enrich(self, record: dict) -> dict:
        """Take a raw transcript record and return an enriched dictionary.

        Matching the video_id/cleaned_text/tech_terms/book_names schema.
        """
        raise NotImplementedError


class GeminiStrategy(LLMStrategy):
    """Concrete strategy wrapping the Gemini API for transcript enrichment."""

    def __init__(self, client, model_name: str, config):
        """Store the injected Gemini client, model name, and generation config."""
        self.client = client
        self.model_name = model_name
        self.config = config

    def enrich(self, record: dict) -> dict:
        """Not yet implemented; logic will be ported in the next step."""
        raise NotImplementedError

class MockLLMStrategy:
    """Fake strategy for testing TranscriptEnricher without a real API."""

    def enrich(self, record: dict) -> dict:
        """Return predictable enrichment data for testing."""
        return {
            "video_id": record["video_id"],
            "cleaned_text": record["raw_text"].strip(),
            "tech_terms": ["Python"],
            "book_names": [],
        }


class TranscriptEnricher:
    """Orchestrates the enrichment pipeline using an injected LLM backend."""

    def __init__(self, strategy: LLMStrategy):
        """Inject the enrichment strategy without depending on a vendor."""
        self.strategy = strategy

    def run(self):
        """Read JSONL from stdin, enrich each record, and write JSONL to stdout."""
        for line in sys.stdin:
            try:
                record = json.loads(line)
            except json.JSONDecodeError:
                logging.error("Skipping malformed JSON line: %s", line.strip())
                continue

            enriched = self.strategy.enrich(record)

            sys.stdout.write(json.dumps(enriched) + "\n")
            sys.stdout.flush()
