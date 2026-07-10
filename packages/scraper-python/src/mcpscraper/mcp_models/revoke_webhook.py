from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field


class RevokeWebhookInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    id: str = Field(..., alias="id", description="Webhook id, from list-webhooks.")


class RevokeWebhookOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    ok: bool = Field(..., alias="ok", description="")
    revoked: bool | None = Field(None, alias="revoked", description="")
    error: str | None = Field(None, alias="error", description="")
