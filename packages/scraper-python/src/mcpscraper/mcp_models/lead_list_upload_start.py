from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field


class LeadListUploadStartInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    idempotency_key: str = Field(..., alias="idempotencyKey", description="Required stable key for this intended upload session. Reuse it only to retry the same upload-start call.")
    filename_hint: str | None = Field(None, alias="filenameHint", description="Optional display-only filename. It does not determine or authorize the uploaded format.")


class LeadListUploadStartOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    upload_id: str = Field(..., alias="uploadId", description="")
    status: Literal['awaiting_upload', 'ready'] | None = Field(None, alias="status", description="")
    upload_url: str = Field(..., alias="uploadUrl", description="")
    upload_page_url: str = Field(..., alias="uploadPageUrl", description="")
    accepted_formats: list[Literal['csv', 'tsv', 'xlsx']] = Field(..., alias="acceptedFormats", description="")
    accepted_content_types: list[str] = Field(..., alias="acceptedContentTypes", description="")
    max_bytes: int = Field(..., alias="maxBytes", description="")
    upload_url_expires_at: str = Field(..., alias="uploadUrlExpiresAt", description="")
    source_expires_at: str = Field(..., alias="sourceExpiresAt", description="")
