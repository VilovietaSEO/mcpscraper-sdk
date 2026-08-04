from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field


class LocalSourcebookRefreshInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    submission_id: str = Field(..., alias="submissionId", description="Owner-scoped listing submission to re-crawl and refresh.")


class LocalSourcebookRefreshOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")
