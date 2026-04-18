"""Tests for argument parsing."""

import sys

from lingo.main import parse_arguments


class TestParseArguments:
    """Tests for parse_arguments function."""

    def test_text_argument(self) -> None:
        """Parse with text argument."""
        original_argv = sys.argv
        try:
            sys.argv = ["lingo", "hello world"]
            args = parse_arguments()
            assert args.text == "hello world"
        finally:
            sys.argv = original_argv

    def test_no_text_argument(self) -> None:
        """Parse with no text argument."""
        original_argv = sys.argv
        try:
            sys.argv = ["lingo"]
            args = parse_arguments()
            assert args.text is None
        finally:
            sys.argv = original_argv

    def test_text_with_spaces(self) -> None:
        """Parse text with spaces."""
        original_argv = sys.argv
        try:
            sys.argv = ["lingo", "hello world"]
            args = parse_arguments()
            assert args.text == "hello world"
        finally:
            sys.argv = original_argv

    def test_single_letter(self) -> None:
        """Parse single letter."""
        original_argv = sys.argv
        try:
            sys.argv = ["lingo", "a"]
            args = parse_arguments()
            assert args.text == "a"
        finally:
            sys.argv = original_argv
