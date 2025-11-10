# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from .._types import FileTypes

__all__ = ["SnapshotCreateFromFilesParams"]


class SnapshotCreateFromFilesParams(TypedDict, total=False):
    label: Required[str]

    project_id: Required[str]

    training_file: FileTypes
    """JSONL training file"""

    validation_file: FileTypes
    """JSONL validation file"""
