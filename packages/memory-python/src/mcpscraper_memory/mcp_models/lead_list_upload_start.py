from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field, model_serializer


class LeadListUploadStartInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    idempotency_key: str = Field(..., alias="idempotencyKey", description="Required stable key for this intended upload session. Reuse it only to retry the same upload-start call.")
    filename_hint: str | None = Field(None, alias="filenameHint", description="Optional display-only filename. It does not determine or authorize the uploaded format.")


class LeadListUploadStartOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    upload_id: str | None = Field(None, alias="uploadId", description="")
    status: Literal['awaiting_upload', 'ready'] | None = Field(None, alias="status", description="")
    upload_url: str | None = Field(None, alias="uploadUrl", description="")
    upload_page_url: str | None = Field(None, alias="uploadPageUrl", description="")
    accepted_formats: list[Literal['csv', 'tsv', 'xlsx']] | None = Field(None, alias="acceptedFormats", description="")
    accepted_content_types: list[str] | None = Field(None, alias="acceptedContentTypes", description="")
    max_bytes: int | None = Field(None, alias="maxBytes", description="")
    upload_url_expires_at: str | None = Field(None, alias="uploadUrlExpiresAt", description="")
    source_expires_at: str | None = Field(None, alias="sourceExpiresAt", description="")
    delivery: dict[str, Any] | None = Field(None, alias="delivery", description="")
    preview: str | None = Field(None, alias="preview", description="")
    scope: dict[str, Any] | None = Field(None, alias="scope", description="")
    recovery: dict[str, Any] | None = Field(None, alias="recovery", description="")

    @model_serializer(mode="wrap")
    def _serialize_response(self, handler, info):
        data = handler(self)
        for name, field in type(self).model_fields.items():
            if name not in self.model_fields_set:
                key = field.alias if info.by_alias and field.alias else name
                data.pop(key, None)
        return data
