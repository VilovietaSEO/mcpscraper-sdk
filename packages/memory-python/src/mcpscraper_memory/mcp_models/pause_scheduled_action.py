from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field


class PauseScheduledActionInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    id: str = Field(..., alias="id", description="The scheduled action id, from create-scheduled-action or list-scheduled-actions.")


class PauseScheduledActionOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    ok: bool = Field(..., alias="ok", description="")
    error: str | None = Field(None, alias="error", description="")
