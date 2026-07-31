from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field


class ArchiveScheduledRunInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    api_key: str | None = Field(None, alias="apiKey", description="")
    session_id: str | None = Field(None, alias="sessionId", description="")
    run_id: str = Field(..., alias="runId", description="")
    archived: bool = Field(..., alias="archived", description="True to archive the result; false to restore it.")


class ArchiveScheduledRunOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")
