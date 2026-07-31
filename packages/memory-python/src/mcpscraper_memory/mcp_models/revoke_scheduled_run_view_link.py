from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field


class RevokeScheduledRunViewLinkInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    run_id: str = Field(..., alias="runId", description="")
    share_id: str = Field(..., alias="shareId", description="")


class RevokeScheduledRunViewLinkOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    ok: bool = Field(..., alias="ok", description="")
    revoked: bool | None = Field(None, alias="revoked", description="")
    error: str | None = Field(None, alias="error", description="")
    error_code: Literal["invalid_request", "not_found", "conflict", "template_archived", "renderer_unavailable", "artifact_unavailable", "view_link_unavailable", "internal_error"] | None = Field(None, alias="errorCode", description="")
    request_id: str | None = Field(None, alias="requestId", description="")
