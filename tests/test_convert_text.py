"""Tests for convert_text function."""

import pytest

from lingo.converter import convert_text


class TestConvertText:
    """Tests for convert_text function."""

    def test_single_letter(self, capsys: pytest.CaptureFixture[str]) -> None:
        """Convert single letter outputs correctly."""
        convert_text("a")
        captured = capsys.readouterr()
        assert "a: Alpha" in captured.out

    def test_multiple_letters(self, capsys: pytest.CaptureFixture[str]) -> None:
        """Convert multiple letters outputs each on own line."""
        convert_text("abc")
        captured = capsys.readouterr()
        assert "a: Alpha" in captured.out
        assert "b: Bravo" in captured.out
        assert "c: Charlie" in captured.out

    def test_space_handling(self, capsys: pytest.CaptureFixture[str]) -> None:
        """Spaces create blank lines in output."""
        convert_text("a b")
        captured = capsys.readouterr()
        lines = captured.out.strip().split("\n")
        assert len(lines) == 3  # "a: Alpha", blank line, "b: Bravo"
        assert "a: Alpha" in captured.out
        assert "b: Bravo" in captured.out

    def test_special_characters(self, capsys: pytest.CaptureFixture[str]) -> None:
        """Non-letter characters print as-is."""
        convert_text("a1b")
        captured = capsys.readouterr()
        assert "a: Alpha" in captured.out
        assert "1" in captured.out
        assert "b: Bravo" in captured.out

    def test_case_insensitivity(self, capsys: pytest.CaptureFixture[str]) -> None:
        """Uppercase and lowercase letters convert to same phonetic word."""
        convert_text("A")
        captured_upper = capsys.readouterr()
        assert "Alpha" in captured_upper.out

        convert_text("a")
        captured_lower = capsys.readouterr()
        assert "Alpha" in captured_lower.out

    def test_mixed_input(self, capsys: pytest.CaptureFixture[str]) -> None:
        """Complex input with letters, numbers, punctuation."""
        convert_text("Hi!")
        captured = capsys.readouterr()
        assert "H: Hotel" in captured.out
        assert "i: India" in captured.out
        assert "!" in captured.out
