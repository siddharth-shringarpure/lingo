"""Tests for converter module."""

from lingo.converter import convert_letter


class TestConvertLetter:
    """Tests for convert_letter function."""

    def test_lowercase_letter(self) -> None:
        """Convert lowercase letter to phonetic word."""
        assert convert_letter("a") == "Alpha"
        assert convert_letter("z") == "Zulu"

    def test_uppercase_letter(self) -> None:
        """Convert uppercase letter to phonetic word (case insensitive)."""
        assert convert_letter("A") == "Alpha"
        assert convert_letter("Z") == "Zulu"

    def test_mixed_case(self) -> None:
        """Handle mixed case letters."""
        assert convert_letter("B") == "Bravo"
        assert convert_letter("b") == "Bravo"

    def test_all_letters(self) -> None:
        """Test all 26 letters map correctly."""
        expected = {
            "a": "Alpha",
            "b": "Bravo",
            "c": "Charlie",
            "d": "Delta",
            "e": "Echo",
            "f": "Foxtrot",
            "g": "Golf",
            "h": "Hotel",
            "i": "India",
            "j": "Juliett",
            "k": "Kilo",
            "l": "Lima",
            "m": "Mike",
            "n": "November",
            "o": "Oscar",
            "p": "Papa",
            "q": "Quebec",
            "r": "Romeo",
            "s": "Sierra",
            "t": "Tango",
            "u": "Uniform",
            "v": "Victor",
            "w": "Whiskey",
            "x": "X-ray",
            "y": "Yankee",
            "z": "Zulu",
        }
        for letter, phonetic in expected.items():
            assert convert_letter(letter) == phonetic

    def test_non_letter(self) -> None:
        """Non-letter characters return empty string."""
        assert convert_letter("1") == ""
        assert convert_letter("@") == ""
        assert convert_letter(" ") == ""
        assert convert_letter(".") == ""
        assert convert_letter("🤔") == ""

    def test_empty_string(self) -> None:
        """Empty string returns empty string."""
        assert convert_letter("") == ""
