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
#!/usr/bin/env python3

import sys
import logging

logging.basicConfig(
    level=logging.INFO
)

def main():
    valid_youtube_id_chars = (
        "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        "abcdefghijklmnopqrstuvwxyz"
        "0123456789-_"
    )

    for line in sys.stdin:
        youtube_id = line.strip()

        if len(youtube_id) == 11 and all(
            char in valid_youtube_id_chars for char in youtube_id
        ):
            sys.stdout.write(youtube_id + "\n")
        else:
            logging.info(f"Invalid ID: {youtube_id}")

if __name__ == "__main__":
    main()
