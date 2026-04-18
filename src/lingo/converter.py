"""Text-to-phonetic conversion logic."""

from .constants import PHONETIC_MAP


def convert_letter(letter: str) -> str:
    """Get NATO phonetic word for a letter.

    Args:
        letter: Single alphabetic character

    Returns:
        NATO phonetic word (eg: "Alpha" for "a"), empty string if not a letter
    """
    return PHONETIC_MAP.get(letter.lower(), "")


def convert_text(text: str) -> None:
    """Convert text to NATO phonetic alphabet and print results.

    Processes each character:
    - Letters: prints letter and phonetic word
    - Spaces: prints blank line
    - Other: prints character as-is

    Args:
        text: Text to convert

    """
    for char in text:
        match char:
            case _ if char.isspace():
                print()
            case _ if char.isalpha():
                phonetic_word = convert_letter(char)
                print(f"{char}: {phonetic_word}")
            case _:
                print(char)
