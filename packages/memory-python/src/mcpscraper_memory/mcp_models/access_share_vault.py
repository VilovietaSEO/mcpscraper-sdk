from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field, model_serializer


class AccessShareVaultInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    vault: str = Field(..., alias="vault", description="Vault to share. The caller must control (be entitled to) this vault and hold write scope.")
    grantee_identity: str = Field(..., alias="granteeIdentity", description="Identity to grant access to (e.g. an email or user id).")
    scope: dict[str, Any] | None = Field(None, alias="scope", description="Entitlement scope to grant (read/write/export/index/admin/swap). Optional; omit for least-privilege read-only.")


class AccessShareVaultOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    ok: bool | None = Field(None, alias="ok", description="True when the entitlement was written; false on auth/scope error.")
    vault: str | None = Field(None, alias="vault", description="The vault that was shared.")
    grantee: str | None = Field(None, alias="grantee", description="The identity that was granted access.")
    note: str | None = Field(None, alias="note", description="Guidance on next steps (e.g. the grantee still needs a key tied to this vault).")
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
