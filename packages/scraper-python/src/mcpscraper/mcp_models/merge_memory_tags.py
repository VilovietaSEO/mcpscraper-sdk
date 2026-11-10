from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field, model_serializer


class MergeMemoryTagsInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    from_: str = Field(..., alias="from", description="The duplicate tag to retire.")
    into: str = Field(..., alias="into", description="The canonical tag to keep. Every note using \"from\" is retagged to this.")


class MergeMemoryTagsOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    ok: bool | None = Field(None, alias="ok", description="")
    from_: str | None = Field(None, alias="from", description="")
    into: str | None = Field(None, alias="into", description="")
    notes_retagged: float | None = Field(None, alias="notesRetagged", description="")
    aliases: list[str] | None = Field(None, alias="aliases", description="")
    description_copied: bool | None = Field(None, alias="descriptionCopied", description="")
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
