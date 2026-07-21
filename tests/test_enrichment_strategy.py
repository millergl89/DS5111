import io
import json
import sys

from lib.enrichment_strategy import MockLLMStrategy, TranscriptEnricher


def test_transcript_enricher_run(monkeypatch, capsys):
    """Verify TranscriptEnricher processes stdin and writes enriched JSONL."""
    fake_input = json.dumps(
        {
            "video_id": "ds5111_v001",
            "raw_text": "hello world",
        }
    )

    monkeypatch.setattr(
        sys,
        "stdin",
        io.StringIO(fake_input),
    )

    strategy = MockLLMStrategy()
    enricher = TranscriptEnricher(strategy)
    enricher.run()

    captured = capsys.readouterr()
    output_lines = captured.out.strip().split("\n")

    assert len(output_lines) == 1

    parsed = json.loads(output_lines[0])
    assert parsed["video_id"] == "ds5111_v001"
    assert parsed["cleaned_text"] == "hello world"
