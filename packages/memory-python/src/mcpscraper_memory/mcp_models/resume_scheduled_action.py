from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field


class ResumeScheduledActionInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    id: str = Field(..., alias="id", description="The scheduled action id.")


class ResumeScheduledActionOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    ok: bool = Field(..., alias="ok", description="")
    next_run_at: str | None = Field(None, alias="nextRunAt", description="")
    code: str | None = Field(None, alias="code", description="Machine-readable denial code when the action cannot be resumed.")
    error: str | None = Field(None, alias="error", description="")
