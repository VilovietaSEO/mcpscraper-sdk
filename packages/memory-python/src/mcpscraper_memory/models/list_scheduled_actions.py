from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field


class ListScheduledActionsInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    api_key: str | None = Field(None, alias="apiKey", description="")
    session_id: str | None = Field(None, alias="sessionId", description="")


class ListScheduledActionsOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    ok: bool = Field(..., alias="ok", description="")
    actions: list[dict[str, Any]] | None = Field(None, alias="actions", description="")
    error: str | None = Field(None, alias="error", description="")
