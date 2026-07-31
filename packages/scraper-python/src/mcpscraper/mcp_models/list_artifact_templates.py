from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field


class ListArtifactTemplatesInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    status: Literal["active", "archived", "all"] | None = Field(None, alias="status", description="")


class ListArtifactTemplatesOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    ok: bool = Field(..., alias="ok", description="")
    presets: list[dict[str, Any]] | None = Field(None, alias="presets", description="")
    templates: list[dict[str, Any]] | None = Field(None, alias="templates", description="")
    error: str | None = Field(None, alias="error", description="")
    error_code: Literal["invalid_request", "not_found", "conflict", "template_archived", "renderer_unavailable", "artifact_unavailable", "view_link_unavailable", "internal_error"] | None = Field(None, alias="errorCode", description="")
    request_id: str | None = Field(None, alias="requestId", description="")
