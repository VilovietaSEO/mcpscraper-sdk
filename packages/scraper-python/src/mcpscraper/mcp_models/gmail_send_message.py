from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field, model_serializer


class GmailSendMessageInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    confirmed: bool | None = Field(None, alias="confirmed", description="Set true only when the person explicitly authorized sending this exact email. If omitted, a 2026-capable client may ask for confirmation.")
    idempotency_key: str = Field(..., alias="idempotencyKey", description="Required stable key for this intended email. Reuse it only when retrying the same send after a lost response.")
    connection_id: str = Field(..., alias="connectionId", description="A Gmail connectionId from list_service_connections, with actionsEnabled true.")
    to: str = Field(..., alias="to", description="Recipient email address.")
    subject: str = Field(..., alias="subject", description="Email subject line.")
    body: str = Field(..., alias="body", description="Plain-text email body.")


class GmailSendMessageOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    ok: bool | None = Field(None, alias="ok", description="")
    result: Any | None = Field(None, alias="result", description="")
    error: Any | None = Field(None, alias="error", description="")
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
