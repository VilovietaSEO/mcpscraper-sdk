from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field, model_serializer


class ProvisionDefaultsInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    grantee_identity: str = Field(..., alias="granteeIdentity", description="Identity that should own the current default vaults, such as an email or user id.")
    issue_key: bool | None = Field(None, alias="issueKey", description="When true, issue a fresh API key for the default vaults and return its secret once. Default false. Repeating this call issues another key.")
    plan: Literal['free', 'pro', 'team', 'enterprise'] | None = Field(None, alias="plan", description="Subscription plan carried by the issued key. Optional; defaults to free. Only used when issueKey is true.")


class ProvisionDefaultsOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    ok: bool | None = Field(None, alias="ok", description="True when provisioning succeeded; false on auth/scope error.")
    identity: str | None = Field(None, alias="identity", description="Identity the vaults were provisioned for.")
    created: list[str] | None = Field(None, alias="created", description="Vault names newly created on this call; empty when every default vault already existed.")
    vaults: list[str] | None = Field(None, alias="vaults", description="Current default vault names the identity now owns.")
    key_id: str | None = Field(None, alias="keyId", description="Stable id of the issued key. Present only when issueKey was true.")
    secret: str | None = Field(None, alias="secret", description="The issued key secret — RETURNED ONCE. Present only when issueKey was true.")
    plan: str | None = Field(None, alias="plan", description="Plan assigned to the issued key. Present only when issueKey was true.")
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
