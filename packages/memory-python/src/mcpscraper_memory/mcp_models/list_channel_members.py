from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field, model_serializer


class ListChannelMembersInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    vault: str = Field(..., alias="vault", description="The vault (channel) to list members of. You must own it.")


class ListChannelMembersOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    ok: bool | None = Field(None, alias="ok", description="True on success; false on auth/scope/ownership error.")
    owner: str | None = Field(None, alias="owner", description="The channel owner.")
    can_manage: bool | None = Field(None, alias="canManage", description="True if the caller is the owner (and so can call remove-channel-member).")
    members: list[dict[str, Any]] | None = Field(None, alias="members", description="Present when ok is true. Always includes at least the owner.")
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
