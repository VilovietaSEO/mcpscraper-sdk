from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field, model_serializer


class MemoryExportInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    vault: str | None = Field(None, alias="vault", description="Vault to export. Optional; defaults to the session active vault, then the first vault the caller is entitled to.")


class MemoryExportOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    ok: bool | None = Field(None, alias="ok", description="True when the export succeeded; false on auth/scope error.")
    vault: str | None = Field(None, alias="vault", description="The vault that was actually exported (after defaulting).")
    count: float | None = Field(None, alias="count", description="Total number of notes returned in the dump.")
    notes: list[dict[str, Any]] | None = Field(None, alias="notes", description="Every note in the vault with full content. Present when ok is true. Can be large.")
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
