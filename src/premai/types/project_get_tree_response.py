# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["ProjectGetTreeResponse", "Project"]


class Project(BaseModel):
    id: str

    type: Literal["project", "dataset", "snapshot", "finetuning-job", "experiment"]

    children: Optional[List[object]] = None

    label: Optional[str] = None

    metadata: Optional[object] = None

    name: Optional[str] = None

    status: Optional[
        Literal[
            "processing", "completed", "failed", "pending", "queued", "running", "deploying", "succeeded", "deleted"
        ]
    ] = None


class ProjectGetTreeResponse(BaseModel):
    project: Project
