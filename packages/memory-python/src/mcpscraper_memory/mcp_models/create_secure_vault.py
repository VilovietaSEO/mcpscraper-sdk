from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field, model_serializer


class CreateSecureVaultInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    name: str = Field(..., alias="name", description="Vault name. Must match ^[A-Za-z0-9 _-]{1,48}$. Defaults to a name like \"Passwords\" if the caller has no preference.")


class CreateSecureVaultOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    ok: bool | None = Field(None, alias="ok", description="True when the vault was created; false on auth/scope/validation error.")
    vault: str | None = Field(None, alias="vault", description="The vault name. Present when ok is true.")
    created: bool | None = Field(None, alias="created", description="True if newly created; false if a vault with this name already existed for you (idempotent) — note this does NOT confirm the existing vault is secure-kind; check list-vaults if unsure.")
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
