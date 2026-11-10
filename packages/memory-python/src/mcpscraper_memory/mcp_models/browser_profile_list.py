from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field, model_serializer


class BrowserProfileListInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    profile: str | None = Field(None, alias="profile", description="Profile whose saved logins to list. Omit to derive from email.")
    email: str | None = Field(None, alias="email", description="Account email used to derive the profile name when profile is not given.")
    domain: str | None = Field(None, alias="domain", description="Restrict to one site login, e.g. chatgpt.com. Use this to poll a single login until its status reads AUTHENTICATED.")
    connection_id: str | None = Field(None, alias="connection_id", description="A specific login connection id returned by browser_profile_connect, to poll just that one.")


class BrowserProfileListOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    ok: bool | None = Field(None, alias="ok", description="")
    tool: str | None = Field(None, alias="tool", description="")
    session_id: Any | None = Field(None, alias="session_id", description="")
    profile: str | None = Field(None, alias="profile", description="Profile these logins belong to.")
    connections: list[dict[str, Any]] | None = Field(None, alias="connections", description="All site logins saved in this profile, each with its current auth status and note.")
    count: int | None = Field(None, alias="count", description="")
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
