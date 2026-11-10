from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field, model_serializer


class MemoryGetInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    vault: str | None = Field(None, alias="vault", description="Vault to read from. Optional; defaults to the session active vault, then the first vault the caller is entitled to. Ignored when shareId is given.")
    path: str | None = Field(None, alias="path", description="Exact vault-relative note path to read, e.g. projects/q3-plan (as returned by memory-list or recall). Required unless shareId is given.")
    share_id: str | None = Field(None, alias="shareId", description="Read a note shared with you and accepted, by its shareId (from note-inbox or list-shared-with-me), instead of vault+path.")


class MemoryGetOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    ok: bool | None = Field(None, alias="ok", description="True when the note was found and returned; false on error or not-found.")
    note: dict[str, Any] | None = Field(None, alias="note", description="The full note. Present when ok is true.")
    error: str | None = Field(None, alias="error", description="Human-readable failure reason when ok is false (e.g. \"note not found\").")
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
