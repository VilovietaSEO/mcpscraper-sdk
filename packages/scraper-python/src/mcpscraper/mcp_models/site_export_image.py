from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field


class SiteExportImageInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    job_id: str = Field(..., alias="jobId", description="Site export job ID returned by extract_site, analyze_site_similarity, or audit_site.")
    image_id: str = Field(..., alias="imageId", description="Downloaded image ID returned by a site_export_read manifest.")


class SiteExportImageOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    job_id: str = Field(..., alias="jobId", description="")
    image_id: str = Field(..., alias="imageId", description="")
    source_page: Any | None = Field(None, alias="sourcePage", description="")
    source_url: Any | None = Field(None, alias="sourceUrl", description="")
    mime_type: str = Field(..., alias="mimeType", description="")
    bytes: int = Field(..., alias="bytes", description="")
    sha256: Any | None = Field(None, alias="sha256", description="")
