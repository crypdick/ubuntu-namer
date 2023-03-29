# type: ignore[attr-defined]
"""Awesome `ubuntu-namer` is a Python cli/package created with https://github.com/TezRomacH/python-package-template"""

from .__main__ import generate_name
from .names import ubuntu_names

# from importlib import metadata as importlib_metadata
#
#
# def get_version() -> str:
#     try:
#         return importlib_metadata.version(__name__)
#     except importlib_metadata.PackageNotFoundError:  # pragma: no cover
#         return "unknown"
#
#
# version: str = get_version()
