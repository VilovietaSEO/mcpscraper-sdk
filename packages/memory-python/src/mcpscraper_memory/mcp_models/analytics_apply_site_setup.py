from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field


class AnalyticsApplySiteSetupInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    site_id: str = Field(..., alias="siteId", description="Authorized Analytics Site id owning the setup.")
    setup_id: str = Field(..., alias="setupId", description="Durable owner-bound setup id returned by an X-Ray setup operation; it is not a browser session id.")
    revision: int = Field(..., alias="revision", description="Exact current setup revision. Reload stale revisions before any mutation or canary.")
    confirmed: bool = Field(..., alias="confirmed", description="Confirms publishing this exact measurement manifest to the installed X-Ray tag runtime. This does not activate an experiment.")
    idempotency_key: str = Field(..., alias="idempotencyKey", description="Retry key; reuse only for this exact mutation.")


class AnalyticsApplySiteSetupOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    ok: bool = Field(..., alias="ok", description="")
    operation: str = Field(..., alias="operation", description="")
    setup: dict[str, Any] = Field(..., alias="setup", description="")
    next_action: str = Field(..., alias="nextAction", description="Exactly one safe next user or system action based on the current durable state.")
    billing_receipt: dict[str, Any] = Field(..., alias="billingReceipt", description="")
