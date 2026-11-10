from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field, model_serializer


class CreateWebhookInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    vault: str | None = Field(None, alias="vault", description="Vault this webhook writes into. Optional; defaults to \"Issues\".")
    label: str | None = Field(None, alias="label", description="Optional human-readable label to help you remember what this webhook is for, e.g. \"Website contact form\".")


class CreateWebhookOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    ok: bool | None = Field(None, alias="ok", description="")
    id: str | None = Field(None, alias="id", description="Webhook id, for listing/revoking later.")
    url: str | None = Field(None, alias="url", description="The full webhook URL — POST here to write a note.")
    vault: str | None = Field(None, alias="vault", description="")
    error: str | None = Field(None, alias="error", description="")
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
