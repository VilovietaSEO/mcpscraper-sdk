from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field, model_serializer


class AccessSwapVaultInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    vault: str = Field(..., alias="vault", description="Vault to make active for the session. Must be an entitled vault and the key must hold \"swap\" scope.")


class AccessSwapVaultOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    ok: bool | None = Field(None, alias="ok", description="True when the active vault was set; false on auth/scope error.")
    active_vault: str | None = Field(None, alias="activeVault", description="The vault now active for the session.")
    session: str | None = Field(None, alias="session", description="The session the active vault was set for.")
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
