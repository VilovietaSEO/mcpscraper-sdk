from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field


class BrowserTypeInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    session_id: str = Field(..., alias="session_id", description="The session id returned by browser_open or browser_list_sessions.")
    text: str = Field(..., alias="text", description="Text to type at the current focus. Click a field first to focus it.")
    delay: int | None = Field(None, alias="delay", description="Optional per-keystroke delay in ms for human-like typing.")


class BrowserTypeOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")
