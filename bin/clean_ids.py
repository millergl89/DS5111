#!/usr/bin/env python3
"""Clean YouTube IDs from standard input."""

import logging
import sys

logging.basicConfig(level=logging.INFO)

VALID_YOUTUBE_ID_CHARS = (
    "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    "abcdefghijklmnopqrstuvwxyz"
    "0123456789-_"
)


def is_valid_youtube_id(youtube_id):
    """Return True when the value is a valid YouTube video ID."""
    return len(youtube_id) == 11 and all(
        char in VALID_YOUTUBE_ID_CHARS for char in youtube_id
    )


def main():
    """Read stdin and print only valid YouTube IDs."""
    for line in sys.stdin:
        youtube_id = line.strip()

        if is_valid_youtube_id(youtube_id):
            sys.stdout.write(youtube_id + "\n")
        else:
            logging.info("Invalid ID: %s", youtube_id)


if __name__ == "__main__":
    main()
