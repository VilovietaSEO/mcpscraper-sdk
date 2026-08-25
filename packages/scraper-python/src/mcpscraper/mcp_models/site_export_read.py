from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field


class SiteExportReadInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    job_id: str = Field(..., alias="jobId", description="Site export job ID returned by extract_site, analyze_site_similarity, or audit_site.")
    page_id: str | None = Field(None, alias="pageId", description="Page ID returned by a manifest read. Omit to list the export manifest.")
    format: Literal['manifest', 'json', 'html', 'markdown'] | None = Field(None, alias="format", description="manifest lists page/image IDs; JSON, HTML, and Markdown read one page representation.")
    offset: int | None = Field(None, alias="offset", description="UTF-8 byte offset. Continue from nextOffset until it is null.")
    max_bytes: int | None = Field(None, alias="maxBytes", description="Maximum UTF-8 bytes returned in this window.")


class SiteExportReadOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    job_id: str = Field(..., alias="jobId", description="")
    page_id: Any = Field(..., alias="pageId", description="")
    format: Literal['manifest', 'json', 'html', 'markdown'] = Field(..., alias="format", description="")
    sha256: str = Field(..., alias="sha256", description="")
    text: str = Field(..., alias="text", description="")
    offset: int = Field(..., alias="offset", description="")
    total_bytes: int = Field(..., alias="totalBytes", description="")
    next_offset: Any = Field(..., alias="nextOffset", description="")
