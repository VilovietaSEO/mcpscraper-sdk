from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field


class BrowserCloseInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    session_id: str = Field(..., alias="session_id", description="The session id returned by browser_open or browser_list_sessions.")


class BrowserCloseOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    ok: bool = Field(..., alias="ok", description="Whether the browser-agent action succeeded.")
    tool: str = Field(..., alias="tool", description="")
    session_id: Any = Field(..., alias="session_id", description="Browser session id when the response is scoped to a session.")
    closed: bool = Field(..., alias="closed", description="")
    raw: dict[str, Any] | None = Field(None, alias="raw", description="")
