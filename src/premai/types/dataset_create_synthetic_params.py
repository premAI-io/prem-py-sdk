# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Required, TypedDict

from .._types import FileTypes, SequenceNotStr

__all__ = ["DatasetCreateSyntheticParams"]


class DatasetCreateSyntheticParams(TypedDict, total=False):
    name: Required[str]

    pairs_to_generate: Required[int]

    project_id: Required[str]

    chunk_size: int
    """Text chunk size for processing"""

    files: SequenceNotStr[FileTypes]
    """Optional: PDF, DOCX, etc."""

    pair_type: Literal["qa", "cot", "summary"]
    """Type of pairs to generate"""

    question_answer_guidance: str
    """Focus on..."""

    rules_and_constraints: str
    """Avoid..."""

    system_prompt: str
    """You are a helpful assistant..."""

    temperature: Optional[float]
    """0.0-1.0, controls randomness"""

    user_instructions: str
    """Generate Q&A pairs about..."""

    website_urls: SequenceNotStr[str]
    """Website URLs as array"""

    youtube_urls: SequenceNotStr[str]
    """YouTube URLs as array"""
