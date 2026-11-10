from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field, model_serializer


class AccessRevokeKeyInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    key_id: str = Field(..., alias="keyId", description="Identifier of the key to revoke (from access-list-keys). Must be a key the caller owns or fully covers.")


class AccessRevokeKeyOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    ok: bool | None = Field(None, alias="ok", description="True when the revoke operation completed; false on auth/scope error or not-found.")
    key_id: str | None = Field(None, alias="keyId", description="The key that was targeted for revocation.")
    revoked: bool | None = Field(None, alias="revoked", description="True if the key is now revoked.")
    error: str | None = Field(None, alias="error", description="Human-readable failure reason when ok is false (e.g. \"key not found\").")
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
