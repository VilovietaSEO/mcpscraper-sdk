from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field, model_serializer


class UpsertMemoryTagInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    tag: str = Field(..., alias="tag", description="Canonical tag name to create or curate.")
    description: str | None = Field(None, alias="description", description="Human-readable summary that distinguishes this record from similarly named records.")
    aliases: list[str] | None = Field(None, alias="aliases", description="Alternative spellings that should resolve to this canonical value.")
    status: Literal['active', 'deprecated'] | None = Field(None, alias="status", description="Lifecycle status used to filter or update the selected records.")


class UpsertMemoryTagOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    ok: bool | None = Field(None, alias="ok", description="")
    tag: dict[str, Any] | None = Field(None, alias="tag", description="")
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
