from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field


class BrowserExtensionListInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")


class BrowserExtensionListOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")
