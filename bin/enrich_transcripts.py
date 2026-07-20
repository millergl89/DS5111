#!/usr/bin/env python3
"""Enrich transcript records using Gemini structured output."""

import json
import logging
import os
import sys
import argparse
from dotenv import load_dotenv
from google import genai
from google.genai import types
from lib.enrichment_strategy import GeminiStrategy, TranscriptEnricher

logging.basicConfig(
    filename="pipeline_audit.log",
    level=logging.INFO,
    format="%(asctime)s %(levelname)s:%(message)s",
)


def main():
    """Read transcript JSONL from stdin, enrich it, and write JSONL to stdout."""
    parser = argparse.ArgumentParser(
        description="Enrich transcript records from a JSONL stream using a selected LLM engine."
    )

    parser.add_argument(
        "--engine",
        default="gemini",
        help="Select the LLM engine used to enrich transcript records."
    )

    args = parser.parse_args()

    load_dotenv()

    api_key = os.getenv("GEMINI_API_KEY")

    if api_key is None:
        logging.critical("GEMINI_API_KEY is missing from environment.")
        sys.exit(1)

    client = genai.Client(api_key=api_key)

    schema = {
        "type": "object",
        "properties": {
            "video_id": {"type": "string"},
            "cleaned_text": {"type": "string"},
            "tech_terms": {
                "type": "array",
                "items": {"type": "string"},
            },
            "book_names": {
                "type": "array",
                "items": {"type": "string"},
            },
        },
        "required": ["video_id", "cleaned_text", "tech_terms", "book_names"],
    }

    config = types.GenerateContentConfig(
        response_mime_type="application/json",
        response_schema=schema,
    )

    if args.engine == "gemini":
        strategy = GeminiStrategy(
            client=client,
            model_name="gemini-2.5-flash",
            config=config,
        )
    else:
        raise ValueError(f"Unsupported engine: {args.engine}")

    enricher = TranscriptEnricher(strategy)
    enricher.run()


if __name__ == "__main__":
    main()
