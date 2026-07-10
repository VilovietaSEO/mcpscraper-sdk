from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field


class AccessIssueKeyInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    grantee_identity: str = Field(..., alias="granteeIdentity", description="Identity that will own the newly issued key (e.g. an email or user id).")
    vaults: list[str] = Field(..., alias="vaults", description="Vaults the new key is entitled to; the caller must already hold each. At least one required.")
    scope: dict[str, Any] | None = Field(None, alias="scope", description="Scope grant (read/write/export/index/admin/swap). Optional; omit for least-privilege read-only.")
    plan: Literal["free", "pro", "team", "enterprise"] | None = Field(None, alias="plan", description="Subscription plan carried by the key. Optional; defaults to free.")
    expires_in_days: int | None = Field(None, alias="expiresInDays", description="Days until the key expires (1-3650). Optional; omit for a non-expiring key.")


class AccessIssueKeyOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    ok: bool = Field(..., alias="ok", description="True when the key was issued; false on auth/scope error.")
    key_id: str | None = Field(None, alias="keyId", description="Stable identifier of the issued key (safe to store/log).")
    secret: str | None = Field(None, alias="secret", description="The key secret — RETURNED ONCE and never retrievable again. Capture it immediately.")
    grantee: str | None = Field(None, alias="grantee", description="Identity the key was issued to.")
    vaults: list[str] | None = Field(None, alias="vaults", description="Vaults the issued key is entitled to.")
    scope: dict[str, Any] | None = Field(None, alias="scope", description="Normalized scope actually granted on the key.")
    plan: str | None = Field(None, alias="plan", description="Subscription plan assigned to the key.")
    expires_at: Any | None = Field(None, alias="expiresAt", description="ISO-8601 expiry timestamp, or null when the key does not expire.")
    error: str | None = Field(None, alias="error", description="Human-readable failure reason when ok is false.")
