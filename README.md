# lingo

[![CI](https://github.com/siddharth-shringarpure/lingo/actions/workflows/ci.yml/badge.svg)](https://github.com/siddharth-shringarpure/lingo/actions/workflows/ci.yml)

A command-line tool for converting text to NATO phonetic alphabet words.

## Quickstart

```bash
# Install dependencies and create the local environment
uv sync

# Convert text
uv run lingo "hello world"

# Or run interactively
uv run lingo
```

## What It Does

- Converts letters to NATO phonetic words
- Treats upper and lower case the same
- Prints spaces as blank lines
- Leaves non-letter characters unchanged


## License

See LICENSE file for details.
