from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field


class LocalSourcebookSubmissionStatusInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    submission_id: str = Field(..., alias="submissionId", description="The owner-scoped submission ID returned by local-sourcebook-capture.")


class LocalSourcebookSubmissionStatusOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")
