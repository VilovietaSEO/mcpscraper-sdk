from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field


class BrowserScreenshotInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    session_id: str = Field(..., alias="session_id", description="The session id returned by browser_open or browser_list_sessions.")


class BrowserScreenshotOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")
