from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field


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

    ok: bool = Field(..., alias="ok", description="")
    result: Any | None = Field(None, alias="result", description="")
    error: Any = Field(..., alias="error", description="")
