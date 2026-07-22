from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field


class BrowserListSessionsInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    include_closed: bool | None = Field(None, alias="include_closed", description="Include closed sessions in the list.")


class BrowserListSessionsOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    ok: bool = Field(..., alias="ok", description="")
    tool: str = Field(..., alias="tool", description="")
    session_id: Any = Field(..., alias="session_id", description="")
    sessions: list[dict[str, Any]] = Field(..., alias="sessions", description="")
    count: int = Field(..., alias="count", description="")
