from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field


class GmailSendMessageInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    connection_id: str = Field(..., alias="connectionId", description="A Gmail connectionId from list_service_connections, with actionsEnabled true.")
    to: str = Field(..., alias="to", description="Recipient email address.")
    subject: str = Field(..., alias="subject", description="Email subject line.")
    body: str = Field(..., alias="body", description="Plain-text email body.")


class GmailSendMessageOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")
