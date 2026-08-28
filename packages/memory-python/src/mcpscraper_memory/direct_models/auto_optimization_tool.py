from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field


class AutoOptimizationToolInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    api_key: str | None = Field(None, alias="apiKey", description="")
    session_id: str | None = Field(None, alias="sessionId", description="")
    mode: Literal['off', 'deterministic', 'full'] | None = Field(None, alias="mode", description="Omit to read the current setting. off stops automatic runs entirely; deterministic suggests using rules only and never charges; full adds AI judging and does charge.")


class AutoOptimizationToolOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    ok: bool = Field(..., alias="ok", description="")
    mode: str | None = Field(None, alias="mode", description="")
    changed: bool | None = Field(None, alias="changed", description="")
    costs_credits: bool | None = Field(None, alias="costsCredits", description="")
    options: dict[str, Any] | None = Field(None, alias="options", description="")
    error: str | None = Field(None, alias="error", description="")
