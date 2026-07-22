from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field


class ProvisionDefaultsInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    grantee_identity: str = Field(..., alias="granteeIdentity", description="Identity that should OWN the 16 default vaults (e.g. an email or user id).")
    issue_key: bool | None = Field(None, alias="issueKey", description="When true, also issue a new API key for the identity entitled to all 16 vaults and return its secret once. Default false.")
    plan: Literal["free", "pro", "team", "enterprise"] | None = Field(None, alias="plan", description="Subscription plan carried by the issued key. Optional; defaults to free. Only used when issueKey is true.")


class ProvisionDefaultsOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    ok: bool = Field(..., alias="ok", description="True when provisioning succeeded; false on auth/scope error.")
    identity: str | None = Field(None, alias="identity", description="Identity the vaults were provisioned for.")
    created: list[str] | None = Field(None, alias="created", description="Vault names newly created on this call (empty when all 16 already existed).")
    vaults: list[str] | None = Field(None, alias="vaults", description="All 16 default vault names the identity now owns.")
    key_id: str | None = Field(None, alias="keyId", description="Stable id of the issued key. Present only when issueKey was true.")
    secret: str | None = Field(None, alias="secret", description="The issued key secret — RETURNED ONCE. Present only when issueKey was true.")
    plan: str | None = Field(None, alias="plan", description="Plan assigned to the issued key. Present only when issueKey was true.")
    error: str | None = Field(None, alias="error", description="Human-readable failure reason when ok is false.")
