"""Tests successful YouTube transcript extraction."""

import io
import json
import sys

from youtube_transcript_api import YouTubeTranscriptApi

from bin.extract_transcripts import main


class MockTranscriptContainer:
    """Mimics the transcript object returned by the API."""

    def to_raw_data(self):
        return [
            {
                "start": 10.5,
                "text": "Automated container tracking loop text entry."
            }
        ]


def test_extract_transcripts_main_pipeline_stream(monkeypatch, capsys):
    """Verify main() processes stdin and outputs one JSONL object."""

    # Mock the YouTube API fetch call
    def stubbed_fetch_route(self, video_id):
        return MockTranscriptContainer()

    monkeypatch.setattr(
        YouTubeTranscriptApi,
        "fetch",
        stubbed_fetch_route
    )

    # Fake stdin
    monkeypatch.setattr(
        sys,
        "stdin",
        io.StringIO("fake_video_999\n")
    )

    # Run the script
    main()

    # Capture stdout
    captured_output = capsys.readouterr()

    stdout_lines = captured_output.out.strip().split("\n")

    assert len(stdout_lines) == 1

    parsed_json_line = json.loads(stdout_lines[0])

    assert parsed_json_line["video_id"] == "fake_video_999"
    assert "Automated container tracking" in parsed_json_line["raw_text"]
