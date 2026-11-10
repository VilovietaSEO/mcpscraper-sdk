from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field, model_serializer


class ListMemoryTagsInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    include_deprecated: bool | None = Field(None, alias="includeDeprecated", description="Include deprecated tags as well as active tags. Defaults true so the AI sees the complete vocabulary; pass false only for an active-only display.")


class ListMemoryTagsOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    ok: bool | None = Field(None, alias="ok", description="")
    tags: list[dict[str, Any]] | None = Field(None, alias="tags", description="")
    error: str | None = Field(None, alias="error", description="")
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
