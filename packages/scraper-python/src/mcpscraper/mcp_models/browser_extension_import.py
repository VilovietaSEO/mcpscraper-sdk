from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field


class BrowserExtensionImportInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    store_url: str = Field(..., alias="store_url", description="Chrome Web Store URL of the extension to add, e.g. https://chromewebstore.google.com/detail/<slug>/<id>.")
    name: str = Field(..., alias="name", description="Short name to save this extension under, e.g. \"ani-ai\". Reuse it later in extension_names on browser_open.")


class BrowserExtensionImportOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    ok: bool = Field(..., alias="ok", description="")
    tool: str = Field(..., alias="tool", description="")
    session_id: Any = Field(..., alias="session_id", description="")
    name: str = Field(..., alias="name", description="The name this extension was saved under.")
    source_url: str = Field(..., alias="source_url", description="The store URL this extension was imported from.")
    size_bytes: Any = Field(..., alias="size_bytes", description="Size of the extension package in bytes.")
