from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field


class BrowserClickInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    session_id: str = Field(..., alias="session_id", description="The session id returned by browser_open or browser_list_sessions.")
    x: float = Field(..., alias="x", description="X coordinate to click, in screenshot pixels. Use only coordinates from the latest browser_screenshot, browser_read, or browser_locate result; do not guess.")
    y: float = Field(..., alias="y", description="Y coordinate to click, in screenshot pixels. Use only coordinates from the latest browser_screenshot, browser_read, or browser_locate result; do not guess.")
    button: Literal["left", "right", "middle"] | None = Field(None, alias="button", description="Mouse button.")
    num_clicks: int | None = Field(None, alias="num_clicks", description="Number of clicks, e.g. 2 for double-click.")


class BrowserClickOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    ok: bool = Field(..., alias="ok", description="Whether the browser-agent action succeeded.")
    tool: str = Field(..., alias="tool", description="Browser Agent MCP tool that produced this response.")
    session_id: Any = Field(..., alias="session_id", description="Browser session id when the response is scoped to a session.")
    result: dict[str, Any] = Field(..., alias="result", description="Provider action result. Check ok and follow with browser_screenshot/browser_read when page state matters.")
    next_recommended_tool: Any = Field(..., alias="nextRecommendedTool", description="")
