"""Main CLI logic and user interaction."""

import argparse
import sys

from .converter import convert_text


def validate_input(text: str) -> bool:
    """Check if input is not empty.

    Args:
        text: Text to validate

    Returns:
        True if text is non-empty (after stripping)
    """
    return bool(text.strip())


def parse_arguments() -> argparse.Namespace:
    """Parse command-line arguments.

    Returns:
        Parsed arguments namespace with text attribute
    """
    parser = argparse.ArgumentParser(
        prog="lingo",
        description="Convert text to NATO phonetic alphabet words",
    )
    parser.add_argument(
        "text",
        nargs="?",
        default=None,
        help="text to convert (optional, prompts if not provided)",
    )

    return parser.parse_args()


def get_input(args: argparse.Namespace) -> str | None:
    """Get user input from CLI arguments or prompt.

    Args:
        args: Parsed command-line arguments

    Returns:
        User input text or None if empty
    """
    if args.text:
        return args.text

    return input("Enter text to convert: ")


def main() -> None:
    """Run the lingo CLI application.

    Parses arguments, validates input, and converts text to phonetic output.

    Returns:
        None (exits with status code on error)
    """
    args = parse_arguments()

    user_input = get_input(args)

    if not user_input or not validate_input(user_input):
        print("✗ No input provided")
        sys.exit(1)

    convert_text(user_input)


if __name__ == "__main__":
    main()
