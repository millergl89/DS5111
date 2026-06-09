"""Tests for clean_ids.py."""

import io
import platform
import sys

import pytest

from bin.clean_ids import main


def test_script_execution(monkeypatch, capsys):
    """Test one valid ID and one invalid ID."""
    fake_input = io.StringIO("kcFsuxaJ1es\nasd123\n")
    monkeypatch.setattr(sys, "stdin", fake_input)

    main()

    captured = capsys.readouterr()
    assert captured.out == "kcFsuxaJ1es\n"


def test_good_bad_good(monkeypatch, capsys):
    """Test valid, invalid, valid input."""
    fake_input = io.StringIO("kcFsuxaJ1es\nbad\nABCDEFGHIJK\n")
    monkeypatch.setattr(sys, "stdin", fake_input)

    main()

    captured = capsys.readouterr()
    assert captured.out == "kcFsuxaJ1es\nABCDEFGHIJK\n"


def test_bad_lines_only(monkeypatch, capsys):
    """Test that bad IDs produce no standard output."""
    fake_input = io.StringIO("bad\n1234567890\n123456789012\n")
    monkeypatch.setattr(sys, "stdin", fake_input)

    main()

    captured = capsys.readouterr()
    assert captured.out == ""


def test_running_on_linux():
    """Test that the OS is Linux."""
    assert platform.system() == "Linux"


def test_python_version():
    """Test that Python version is at least 3.10."""
    assert sys.version_info >= (3, 10)


@pytest.mark.xfail
def test_expected_to_fail():
    """Example expected failure test."""
    assert 1 == 2


@pytest.mark.skip(reason="Example skipped test for future feature.")
def test_skipped_example():
    """Example skipped test."""
    assert True


@pytest.mark.parametrize(
    "youtube_id,expected",
    [
        ("kcFsuxaJ1es", "kcFsuxaJ1es\n"),
        ("1234567890", ""),
        ("123456789012", ""),
        ("ABCDEFGHIJK", "ABCDEFGHIJK\n"),
    ],
)
def test_parametrized_ids(monkeypatch, capsys, youtube_id, expected):
    """Test multiple YouTube ID cases."""
    fake_input = io.StringIO(youtube_id + "\n")
    monkeypatch.setattr(sys, "stdin", fake_input)

    main()

    captured = capsys.readouterr()
    assert captured.out == expected
