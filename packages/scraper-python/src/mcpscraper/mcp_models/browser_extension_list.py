from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field


class BrowserExtensionListInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")


class BrowserExtensionListOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    ok: bool = Field(..., alias="ok", description="")
    tool: str = Field(..., alias="tool", description="")
    session_id: Any = Field(..., alias="session_id", description="")
    extensions: list[dict[str, Any]] = Field(..., alias="extensions", description="Every extension available to load via extension_names on browser_open.")
    count: int = Field(..., alias="count", description="")
