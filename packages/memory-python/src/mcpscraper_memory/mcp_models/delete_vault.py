from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field, model_serializer


class DeleteVaultInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    vault: str = Field(..., alias="vault", description="Exact name of the vault to delete. The caller must own this vault and hold admin scope on it.")


class DeleteVaultOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    ok: bool | None = Field(None, alias="ok", description="True when the vault was deleted; false on auth/scope/ownership error.")
    vault: str | None = Field(None, alias="vault", description="The deleted vault name. Present when ok is true.")
    deleted_notes: float | None = Field(None, alias="deletedNotes", description="Number of notes removed from the vault. Present when ok is true.")
    deleted_facts: float | None = Field(None, alias="deletedFacts", description="Number of facts (active + superseded) removed from the vault. Present when ok is true.")
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
