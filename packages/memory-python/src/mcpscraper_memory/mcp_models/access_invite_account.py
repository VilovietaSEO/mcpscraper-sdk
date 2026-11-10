from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field, model_serializer


class AccessInviteAccountInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    grantee_identity: str = Field(..., alias="granteeIdentity", description="Identity (email or user id) to invite into your full account.")
    scope: dict[str, Any] | None = Field(None, alias="scope", description="Permissions to grant across your account. Optional; defaults to read+write (read, write, export, index, swap).")
    revoke: bool | None = Field(None, alias="revoke", description="Set true to revoke an existing account invite for this grantee instead of granting one.")


class AccessInviteAccountOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    ok: bool | None = Field(None, alias="ok", description="True on success; false on auth/scope error.")
    grantee: str | None = Field(None, alias="grantee", description="The identity that was invited or revoked.")
    granted: dict[str, Any] | None = Field(None, alias="granted", description="The permissions now in effect for the grantee. Absent on revoke.")
    revoked: bool | None = Field(None, alias="revoked", description="True when an existing invite was removed.")
    note: str | None = Field(None, alias="note", description="Guidance on next steps for the grantee.")
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
