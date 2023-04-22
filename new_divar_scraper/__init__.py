# type: ignore[attr-defined]
"""Scraper for divar with notifications for gmail & telegram."""

import os
import sys

sys.path.append(os.path.dirname(os.path.realpath(__file__)))

if sys.version_info >= (3, 8):
    from importlib import metadata as importlib_metadata
else:
    import importlib_metadata


def get_version() -> str:
    try:
        return importlib_metadata.version(__name__)
    except importlib_metadata.PackageNotFoundError:  # pragma: no cover
        return "unknown"


version: str = get_version()
