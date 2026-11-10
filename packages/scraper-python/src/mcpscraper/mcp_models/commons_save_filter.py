from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field, model_serializer


class CommonsSaveFilterInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    name: str = Field(..., alias="name", description="User-facing name for this MCP personalization filter. Reusing a name updates the saved filter.")
    description: str | None = Field(None, alias="description", description="Optional note explaining when this filter should be used.")
    filter: dict[str, Any] = Field(..., alias="filter", description="Search/filter scope to save for this account, such as a category, trail, source domain, tags, or media constraints.")


class CommonsSaveFilterOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    ok: bool | None = Field(None, alias="ok", description="")
    data: Any | None = Field(None, alias="data", description="")
    error: str | None = Field(None, alias="error", description="")
    message: str | None = Field(None, alias="message", description="")
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
