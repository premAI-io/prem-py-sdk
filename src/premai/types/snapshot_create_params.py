# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["SnapshotCreateParams"]


class SnapshotCreateParams(TypedDict, total=False):
    dataset_id: Required[str]

    split_percentage: int
