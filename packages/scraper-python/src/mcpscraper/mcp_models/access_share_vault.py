from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field


class AccessShareVaultInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    vault: str = Field(..., alias="vault", description="Vault to share. The caller must control (be entitled to) this vault and hold write scope.")
    grantee_identity: str = Field(..., alias="granteeIdentity", description="Identity to grant access to (e.g. an email or user id).")
    scope: dict[str, Any] | None = Field(None, alias="scope", description="Entitlement scope to grant (read/write/export/index/admin/swap). Optional; omit for least-privilege read-only.")


class AccessShareVaultOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    ok: bool = Field(..., alias="ok", description="True when the entitlement was written; false on auth/scope error.")
    vault: str | None = Field(None, alias="vault", description="The vault that was shared.")
    grantee: str | None = Field(None, alias="grantee", description="The identity that was granted access.")
    note: str | None = Field(None, alias="note", description="Guidance on next steps (e.g. the grantee still needs a key tied to this vault).")
    error: str | None = Field(None, alias="error", description="Human-readable failure reason when ok is false.")
