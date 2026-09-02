from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field


class ArchiveArtifactTemplateInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="forbid")

    api_key: str | None = Field(None, alias="apiKey", description="")
    session_id: str | None = Field(None, alias="sessionId", description="")
    template_id: str = Field(..., alias="templateId", description="")
    archived: bool = Field(..., alias="archived", description="True to archive the template; false to restore it.")


class ArchiveArtifactTemplateOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="forbid")

    ok: bool = Field(..., alias="ok", description="")
    template: dict[str, Any] | None = Field(None, alias="template", description="")
    error: str | None = Field(None, alias="error", description="")
    error_code: Literal['invalid_request', 'not_found', 'conflict', 'template_archived', 'renderer_unavailable', 'artifact_unavailable', 'view_link_unavailable', 'internal_error'] | None = Field(None, alias="errorCode", description="")
    request_id: str | None = Field(None, alias="requestId", description="")
