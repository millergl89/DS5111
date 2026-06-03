#!/usr/bin/env python3

import sys
import logging

logging.basicConfig(
    filename="pipeline_audit.log",
    level=logging.INFO
)

allowed = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789-_"

for line in sys.stdin:
    youtube_id = line.strip()

    if len(youtube_id) == 11 and all(char in allowed for char in youtube_id):
        sys.stdout.write(youtube_id + "\n")
    else:
        logging.info(f"Invalid ID: {youtube_id}")
