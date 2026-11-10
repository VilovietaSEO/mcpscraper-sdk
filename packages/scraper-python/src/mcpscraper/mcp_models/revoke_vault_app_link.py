from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field, model_serializer


class RevokeVaultAppLinkInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")


class RevokeVaultAppLinkOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    ok: bool | None = Field(None, alias="ok", description="True when the request succeeded.")
    revoked: bool | None = Field(None, alias="revoked", description="True when an active Vault App link was revoked.")
    error: str | None = Field(None, alias="error", description="Human-readable error when the request cannot be completed.")
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
