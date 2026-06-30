#!/usr/bin/env python3
"""Enrich transcript records using Gemini structured output."""

import json
import logging
import os
import sys

from dotenv import load_dotenv
from google import genai
from google.genai import types


logging.basicConfig(
    filename="pipeline_audit.log",
    level=logging.INFO,
    format="%(asctime)s %(levelname)s:%(message)s",
)


def main():
    """Read transcript JSONL from stdin, enrich it, and write JSONL to stdout."""
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

    for line in sys.stdin:
        try:
            record = json.loads(line)
        except json.JSONDecodeError:
            logging.error("Skipping malformed JSON line: %s", line.strip())
            continue

        prompt = f"""
        Clean and enrich this transcript record.

        Return JSON with:
        - video_id
        - cleaned_text
        - tech_terms
        - book_names

        Transcript record:
        {json.dumps(record)}
        """

        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt,
            config=config,
        )

        sys.stdout.write(response.text.strip() + "\n")
        sys.stdout.flush()


if __name__ == "__main__":
    main()
