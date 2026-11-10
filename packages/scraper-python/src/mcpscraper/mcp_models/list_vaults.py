from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field, model_serializer


class ListVaultsInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")


class ListVaultsOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    ok: bool | None = Field(None, alias="ok", description="True when the listing succeeded; false on an auth/scope error.")
    active_account: str | None = Field(None, alias="activeAccount", description="The account these vaults belong to (your own identity unless you have switched into another account).")
    is_own_account: bool | None = Field(None, alias="isOwnAccount", description="True when the active account is your own; false when you have switched into an account someone invited you to.")
    vaults: list[dict[str, Any]] | None = Field(None, alias="vaults", description="Every vault visible in the active account, with role, addressable handle, and live storage usage. Present when ok is true.")
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
