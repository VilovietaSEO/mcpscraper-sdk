from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field


class ResumeScheduledActionInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    api_key: str | None = Field(None, alias="apiKey", description="")
    session_id: str | None = Field(None, alias="sessionId", description="")
    id: str = Field(..., alias="id", description="The scheduled action id.")


class ResumeScheduledActionOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    ok: bool = Field(..., alias="ok", description="")
    next_run_at: str | None = Field(None, alias="nextRunAt", description="")
    error: str | None = Field(None, alias="error", description="")
