from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field


class MarkScheduledRunOpenedInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    api_key: str | None = Field(None, alias="apiKey", description="")
    session_id: str | None = Field(None, alias="sessionId", description="")
    run_id: str = Field(..., alias="runId", description="")


class MarkScheduledRunOpenedOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")
