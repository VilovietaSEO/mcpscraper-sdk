from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field, model_serializer


class BrowserExtensionImportInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    store_url: str = Field(..., alias="store_url", description="Chrome Web Store URL of the extension to add, e.g. https://chromewebstore.google.com/detail/<slug>/<id>.")
    name: str = Field(..., alias="name", description="Short name to save this extension under, e.g. \"ani-ai\". Reuse it later in extension_names on browser_open.")


class BrowserExtensionImportOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    ok: bool | None = Field(None, alias="ok", description="")
    tool: str | None = Field(None, alias="tool", description="")
    session_id: Any | None = Field(None, alias="session_id", description="")
    name: str | None = Field(None, alias="name", description="The name this extension was saved under.")
    source_url: str | None = Field(None, alias="source_url", description="The store URL this extension was imported from.")
    size_bytes: Any | None = Field(None, alias="size_bytes", description="Size of the extension package in bytes.")
    delivery: dict[str, Any] | None = Field(None, alias="delivery", description="")
    preview: str | None = Field(None, alias="preview", description="")
    scope: dict[str, Any] | None = Field(None, alias="scope", description="")
    recovery: dict[str, Any] | None = Field(None, alias="recovery", description="")

    @model_serializer(mode="wrap")
    def _serialize_response(self, handler, info):
        data = handler(self)
        for name, field in type(self).model_fields.items():
            if name not in self.model_fields_set:
                key = field.alias if info.by_alias and field.alias else name
                data.pop(key, None)
        return data
