from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field


class BrowserScrollInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    session_id: str = Field(..., alias="session_id", description="The session id returned by browser_open or browser_list_sessions.")
    delta_y: float | None = Field(None, alias="delta_y", description="Vertical scroll in wheel units. Positive scrolls down, negative up.")
    delta_x: float | None = Field(None, alias="delta_x", description="Horizontal scroll in wheel units.")
    x: float | None = Field(None, alias="x", description="X position to scroll at. Defaults to screen center.")
    y: float | None = Field(None, alias="y", description="Y position to scroll at. Defaults to screen center.")


class BrowserScrollOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")
