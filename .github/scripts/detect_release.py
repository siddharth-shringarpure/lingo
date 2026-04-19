"""Decide whether the current main-branch push should publish a release.

Publishes only when the package version increased since the previous push
and the matching release tag does not already exist.
"""

import os
import subprocess
import tomllib
from pathlib import Path

from packaging.version import Version


PYPROJECT_PATH = Path("pyproject.toml")


def _parse_version_from_pyproject(pyproject_text: str) -> Version:
    """Parse the project version from pyproject content.

    Args:
        pyproject_text: Full `pyproject.toml` content

    Returns:
        Parsed project version

    Raises:
        KeyError: If the version field is missing
        InvalidVersion: If the version is not PEP 440 compliant
        tomllib.TOMLDecodeError: If the TOML is invalid
    """
    parsed = tomllib.loads(pyproject_text)
    version_text = parsed["project"]["version"]
    return Version(version_text)


def _read_current_version() -> Version:
    """Read the current project version from disk.

    Returns:
        Parsed current project version
    """
    pyproject_text = PYPROJECT_PATH.read_text(encoding="utf-8")
    return _parse_version_from_pyproject(pyproject_text)


def _read_version_from_git_ref(git_ref: str) -> Version | None:
    """Read the project version from `pyproject.toml` at a Git revision.

    Args:
        git_ref: Git revision to inspect

    Returns:
        Parsed version if available, otherwise None
    """
    result = subprocess.run(
        ["git", "show", f"{git_ref}:pyproject.toml"],
        check=False,
        capture_output=True,
        text=True,
    )
    if result.returncode != 0:
        return None

    return _parse_version_from_pyproject(result.stdout)


def _has_usable_before_sha(value: str) -> bool:
    """Check whether GitHub provided a usable `before` SHA.

    Args:
        value: `github.event.before` value from the workflow event

    Returns:
        True if the value is non-empty and not the all-zero sentinel
    """
    return bool(value) and set(value) != {"0"}


def _tag_exists(tag_name: str) -> bool:
    """Check whether a release tag already exists.

    Args:
        tag_name: Tag name to look up

    Returns:
        True if the tag exists
    """
    result = subprocess.run(
        ["git", "rev-parse", "--verify", "--quiet", f"refs/tags/{tag_name}"],
        check=False,
        capture_output=True,
        text=True,
    )
    return result.returncode == 0


def _write_outputs(
    should_publish: bool,
    version: Version,
    tag_exists: bool,
) -> None:
    """Write release decision values to the GitHub Actions output file.

    Args:
        should_publish: Whether this push should publish a release
        version: Current project version
        tag_exists: Whether the matching tag already exists
    """
    output_path = Path(os.environ["GITHUB_OUTPUT"])
    lines = [
        f"should_publish={'true' if should_publish else 'false'}",
        f"version={version}",
        f"tag_exists={'true' if tag_exists else 'false'}",
    ]

    with output_path.open("a", encoding="utf-8") as file_handle:
        file_handle.write("\n".join(lines) + "\n")


def main() -> None:
    """Detect whether the current push should publish a new release."""
    current_version = _read_current_version()
    before_sha = os.environ.get("BEFORE_SHA", "")

    previous_version = None
    if _has_usable_before_sha(before_sha):
        previous_version = _read_version_from_git_ref(before_sha)

    # Publish only for a real version bump, and never reuse an existing tag.
    tag_name = f"v{current_version}"
    tag_exists = _tag_exists(tag_name)
    should_publish = (
        previous_version is None
        or current_version > previous_version
    )
    should_publish = should_publish and not tag_exists

    _write_outputs(
        should_publish=should_publish,
        version=current_version,
        tag_exists=tag_exists,
    )


if __name__ == "__main__":
    main()
