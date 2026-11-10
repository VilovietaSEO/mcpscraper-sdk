from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field, model_serializer


class SiteExportImageInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    job_id: str = Field(..., alias="jobId", description="Site export job ID returned by extract_site, analyze_site_similarity, or audit_site.")
    image_id: str = Field(..., alias="imageId", description="Downloaded image ID returned by a site_export_read manifest.")


class SiteExportImageOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    job_id: str | None = Field(None, alias="jobId", description="")
    image_id: str | None = Field(None, alias="imageId", description="")
    source_page: Any | None = Field(None, alias="sourcePage", description="")
    source_url: Any | None = Field(None, alias="sourceUrl", description="")
    mime_type: str | None = Field(None, alias="mimeType", description="")
    bytes: int | None = Field(None, alias="bytes", description="")
    sha256: Any | None = Field(None, alias="sha256", description="")
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
