"""Tests graceful handling of transcript extraction failures."""

import io
import sys

from youtube_transcript_api import YouTubeTranscriptApi

from bin.extract_transcripts import main


def test_extract_transcripts_handles_fetch_error(monkeypatch, capsys):
    """Verify the script handles API failures gracefully."""

    def stubbed_fetch_error(self, video_id):
        raise RuntimeError("mock fetch failure")

    monkeypatch.setattr(
        YouTubeTranscriptApi,
        "fetch",
        stubbed_fetch_error
    )

    monkeypatch.setattr(
        sys,
        "stdin",
        io.StringIO("bad_video_id\n")
    )

    main()

    captured_output = capsys.readouterr()

    assert captured_output.out == ""
