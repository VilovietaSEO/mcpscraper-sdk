from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field


class BrowserLocateInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    session_id: str = Field(..., alias="session_id", description="The session id returned by browser_open or browser_list_sessions.")
    targets: list[dict[str, Any]] = Field(..., alias="targets", description="DOM targets to locate in the current viewport. Use selectors for exact elements, or text for visible text ranges.")


class BrowserLocateOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    ok: bool = Field(..., alias="ok", description="Whether the browser-agent action succeeded.")
    tool: str = Field(..., alias="tool", description="")
    session_id: Any = Field(..., alias="session_id", description="Browser session id when the response is scoped to a session.")
    url: Any = Field(..., alias="url", description="")
    title: Any = Field(..., alias="title", description="")
    viewport: Any = Field(..., alias="viewport", description="")
    replay: Any = Field(..., alias="replay", description="")
    targets: list[Any] = Field(..., alias="targets", description="")
    raw: Any | None = Field(None, alias="raw", description="")
