from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field


class BrowserExtensionImportInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    store_url: str = Field(..., alias="store_url", description="Chrome Web Store URL of the extension to add, e.g. https://chromewebstore.google.com/detail/<slug>/<id>.")
    name: str = Field(..., alias="name", description="Short name to save this extension under, e.g. \"ani-ai\". Reuse it later in extension_names on browser_open.")


class BrowserExtensionImportOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")
