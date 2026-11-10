from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field, model_serializer


class MemorySuggestInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    query: str = Field(..., alias="query", description="Partial text typed so far, e.g. \"what is the best r\".")
    limit: int | None = Field(None, alias="limit", description="Max suggestions to return. Optional; default 8.")


class MemorySuggestOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    ok: bool | None = Field(None, alias="ok", description="True when the lookup ran; false on auth error.")
    suggestions: list[dict[str, Any]] | None = Field(None, alias="suggestions", description="Title matches ordered prefix-first then most-recent. Present when ok is true; may be empty.")
    error: str | None = Field(None, alias="error", description="Human-readable failure reason when ok is false.")
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
