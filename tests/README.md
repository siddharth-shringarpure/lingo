# Test Suite

Comprehensive test suite for the lingo project using pytest.

## Running Tests

```bash
# Run all tests
uv run pytest

# Run all tests with verbose output
uv run pytest -v

# Run specific test file
uv run pytest tests/test_converter.py -v

# Run single test class
uv run pytest tests/test_converter.py::TestConvertLetter -v

# Run single test
uv run pytest tests/test_converter.py::TestConvertLetter::test_lowercase_letter -v
```


## Adding New Tests

1. Create test file in `tests/` directory: `test_module_name.py`
2. Use class-based organization: `class TestClassName:`
3. Follow naming convention: `test_specific_functionality`
4. Add docstrings describing what the test does
5. Use type hints on all functions

Example:
```python
def test_new_feature(self) -> None:
    """Brief description of what is tested."""
    result = function_to_test("input")
    assert result == "expected"
```

## Notes

- Use `uv run pytest` to run tests (no need to activate venv manually)
- pytest is installed as a dev dependency via uv
- All tests use type hints and descriptive docstrings
