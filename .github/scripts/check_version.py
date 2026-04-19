"""Validate the package version used in CI.

Ensures that `pyproject.toml` uses a strict `major.minor.patch` version and
that the version is not lower than the relevant base revision.
"""

import os
import re
import subprocess
import tomllib
from pathlib import Path

from packaging.version import Version


PYPROJECT_PATH = Path("pyproject.toml")
SEMVER_PATTERN = re.compile(r"^\d+\.\d+\.\d+$")


def _read_version_text(pyproject_text: str) -> str:
    """Read the raw project version from pyproject content.

    Args:
        pyproject_text: Full `pyproject.toml` content

    Returns:
        Raw project version string
    """
    parsed = tomllib.loads(pyproject_text)
    return parsed["project"]["version"]


def _read_current_version_text() -> str:
    """Read the raw project version from disk.

    Returns:
        Raw project version string
    """
    return _read_version_text(PYPROJECT_PATH.read_text(encoding="utf-8"))


def _read_version_text_from_git_ref(git_ref: str) -> str | None:
    """Read the raw project version from `pyproject.toml` at a Git revision.

    Args:
        git_ref: Git revision to inspect

    Returns:
        Raw project version string if available, otherwise None
    """
    result = subprocess.run(
        ["git", "show", f"{git_ref}:pyproject.toml"],
        check=False,
        capture_output=True,
        text=True,
    )
    if result.returncode != 0:
        return None

    return _read_version_text(result.stdout)


def _get_base_sha() -> str | None:
    """Pick the base revision to compare against in CI.

    Returns:
        Base SHA for the current event, otherwise None
    """
    pull_request_base_sha = os.environ.get("PR_BASE_SHA", "")
    if pull_request_base_sha:
        return pull_request_base_sha

    before_sha = os.environ.get("BEFORE_SHA", "")
    if before_sha and before_sha != "0" * 40:
        return before_sha

    return None


def _validate_semver(version_text: str) -> Version:
    """Validate that the project version uses strict `major.minor.patch`.

    Args:
        version_text: Raw project version string

    Returns:
        Parsed version object

    Raises:
        ValueError: If the version is not strict `major.minor.patch`
    """
    if not SEMVER_PATTERN.fullmatch(version_text):
        raise ValueError(
            "Version must use strict major.minor.patch format: "
            f"{version_text}"
        )

    return Version(version_text)


def main() -> None:
    """Validate the current version against CI rules."""
    current_version_text = _read_current_version_text()
    current_version = _validate_semver(current_version_text)

    base_sha = _get_base_sha()
    if not base_sha:
        return

    base_version_text = _read_version_text_from_git_ref(base_sha)
    if base_version_text is None:
        return

    base_version = _validate_semver(base_version_text)
    if current_version < base_version:
        raise ValueError(
            "Version must not be lower than the base revision: "
            f"{current_version} < {base_version}"
        )


if __name__ == "__main__":
    main()
