from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field


class BrowserExtensionDeleteInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    name: str = Field(..., alias="name", description="Name of the extension to remove, as returned by browser_extension_list.")


class BrowserExtensionDeleteOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")
