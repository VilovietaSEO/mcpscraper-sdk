from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field, model_serializer


class SerpIdentityCreateInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    name: str = Field(..., alias="name", description="Stable caller-facing name, e.g. google-us-primary.")
    country: str | None = Field(None, alias="country", description="Two-letter country for the static network identity. Defaults to US.")


class SerpIdentityCreateOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    ok: bool | None = Field(None, alias="ok", description="")
    tool: str | None = Field(None, alias="tool", description="")
    session_id: str | None = Field(None, alias="session_id", description="Live Google takeover session opened on the new persistent identity.")
    watch_url: str | None = Field(None, alias="watch_url", description="Give this URL to the user so they can clear consent or CAPTCHA directly on google.com.")
    url: str | None = Field(None, alias="url", description="")
    identity: dict[str, Any] | None = Field(None, alias="identity", description="")
    next_steps: list[str] | None = Field(None, alias="next_steps", description="")
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
