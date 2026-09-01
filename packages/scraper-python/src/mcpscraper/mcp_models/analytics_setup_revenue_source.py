from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field


class AnalyticsSetupRevenueSourceInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    site_id: str = Field(..., alias="siteId", description="Authorized Analytics Site id.")
    action: Literal['continue', 'prepare', 'apply', 'verify'] | None = Field(None, alias="action", description="Lifecycle action. Continue reads an existing setup or prepares one when serviceConnectionRef is supplied.")
    setup_id: str | None = Field(None, alias="setupId", description="Owner-bound revenue setup id returned by prepare or the facade.")
    service_connection_ref: str | None = Field(None, alias="serviceConnectionRef", description="Already-authorized connected-account reference. Never supply a credential, token, or provider key.")
    role: Literal['primary', 'observation'] | None = Field(None, alias="role", description="Primary may create subscription outcomes; observation only compares provider evidence.")
    revision: int | None = Field(None, alias="revision", description="Exact current revenue setup revision; reload before retrying a stale mutation.")
    confirmed: bool | None = Field(None, alias="confirmed", description="Required only to apply the exact reviewed revision.")
    idempotency_key: str | None = Field(None, alias="idempotencyKey", description="Required for apply and verify. Reuse only for the identical operation.")


class AnalyticsSetupRevenueSourceOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    ok: bool = Field(..., alias="ok", description="")
    operation: str = Field(..., alias="operation", description="")
    setup: dict[str, Any] = Field(..., alias="setup", description="")
    next_action: str = Field(..., alias="nextAction", description="")
