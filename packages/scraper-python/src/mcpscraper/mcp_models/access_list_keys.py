from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field, model_serializer


class AccessListKeysInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    vault: str | None = Field(None, alias="vault", description="Filter to keys entitled to this vault. Optional; omit to list across all vaults.")
    plan: str | None = Field(None, alias="plan", description="Filter to keys on this plan (free/pro/team/enterprise). Optional; omit to list all plans.")


class AccessListKeysOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    ok: bool | None = Field(None, alias="ok", description="True when the listing succeeded; false on auth/scope error.")
    keys: list[dict[str, Any]] | None = Field(None, alias="keys", description="Key metadata for the caller identity. NEVER includes secrets. Present when ok is true.")
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
