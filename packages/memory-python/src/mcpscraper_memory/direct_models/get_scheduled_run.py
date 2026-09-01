from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field


class GetScheduledRunInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="forbid")

    api_key: str | None = Field(None, alias="apiKey", description="")
    session_id: str | None = Field(None, alias="sessionId", description="")
    run_id: str = Field(..., alias="runId", description="")


class GetScheduledRunOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")
