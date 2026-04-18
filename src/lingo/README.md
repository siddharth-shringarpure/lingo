# lingo Package

Core package for NATO phonetic alphabet conversion.

## Installation & Setup

This project uses **uv** for dependency management and running.
Using `uv` is recommended for consistent local setup, but commands can also be
run directly from an already-activated environment.

```bash
# Clone the repository
git clone https://github.com/siddharth-shringarpure/lingo
cd lingo

# Sync dependencies (creates virtual environment)
uv sync
```

## Quick Start

Convert text to NATO phonetic alphabet:

```bash
# With argument
uv run lingo "John Doe"

# Interactive mode (prompts for input)
uv run lingo
```

## Features

- Converts letters to NATO phonetic words (A → Alpha, B → Bravo, etc.)
- Case-insensitive (A and a both produce "Alpha")
- Handles spaces (creates blank lines between letters)
- Passes through non-letter characters as-is
- Fast and lightweight

## Development

### Running Tests

```bash
# Run all tests
uv run pytest

# Run specific test file
uv run pytest tests/test_converter.py -v

# Run with verbose output
uv run pytest -v
```

### Linting & Type Checking

```bash
# Check with Ruff
uv run ruff check src/ tests/

# Type check
uv run ty check
```

### Project Structure

```
lingo/
├── src/lingo/           # Main package
│   ├── __init__.py      # Package entrypoint
│   ├── main.py          # CLI logic
│   ├── converter.py     # Phonetic conversion
│   └── constants.py     # NATO phonetic map
├── tests/               # Test suite
│   ├── test_converter.py
│   ├── test_main.py
│   └── test_convert_text.py
├── pyproject.toml       # Dependencies & metadata
└── README.md            # This file
```

## Dependencies

- **Python**: ≥ 3.13
- **Development**: pytest (dev-only)
- **uv**