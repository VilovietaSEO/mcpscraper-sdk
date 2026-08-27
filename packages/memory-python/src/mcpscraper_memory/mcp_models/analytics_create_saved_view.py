from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field


class AnalyticsCreateSavedViewInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    site_id: str = Field(..., alias="siteId", description="Analytics Site id returned by analytics_list_sites.")
    name: str = Field(..., alias="name", description="Saved report name.")
    settings: dict[str, Any] = Field(..., alias="settings", description="Complete versioned report settings validated by the same canonical parser as REST and exports.")
    is_default: bool | None = Field(None, alias="isDefault", description="Make this the operator default for the report family.")
    idempotency_key: str = Field(..., alias="idempotencyKey", description="Caller-owned idempotency key. Reuse it only when retrying the same logical mutation.")


class AnalyticsCreateSavedViewOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    ok: bool = Field(..., alias="ok", description="")
    view: dict[str, Any] = Field(..., alias="view", description="")
