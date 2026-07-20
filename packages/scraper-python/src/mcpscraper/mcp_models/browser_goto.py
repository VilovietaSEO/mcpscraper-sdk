from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field


class BrowserGotoInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    session_id: str = Field(..., alias="session_id", description="The session id returned by browser_open or browser_list_sessions.")
    url: str = Field(..., alias="url", description="URL to navigate the browser to.")


class BrowserGotoOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")
