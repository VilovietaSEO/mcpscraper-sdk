from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field, model_serializer


class SiteExportReadInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    job_id: str = Field(..., alias="jobId", description="Site export job ID returned by extract_site, analyze_site_similarity, or audit_site.")
    page_id: str | None = Field(None, alias="pageId", description="Page ID returned by a manifest read. Omit to list the export manifest.")
    format: Literal['manifest', 'json', 'html', 'markdown'] | None = Field(None, alias="format", description="manifest lists page/image IDs; JSON, HTML, and Markdown read one page representation.")
    offset: int | None = Field(None, alias="offset", description="UTF-8 byte offset. Continue from nextOffset until it is null.")
    max_bytes: int | None = Field(None, alias="maxBytes", description="Maximum UTF-8 bytes returned in this window.")


class SiteExportReadOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    job_id: str | None = Field(None, alias="jobId", description="")
    page_id: Any | None = Field(None, alias="pageId", description="")
    format: Literal['manifest', 'json', 'html', 'markdown'] | None = Field(None, alias="format", description="")
    sha256: str | None = Field(None, alias="sha256", description="")
    text: str | None = Field(None, alias="text", description="")
    offset: int | None = Field(None, alias="offset", description="")
    total_bytes: int | None = Field(None, alias="totalBytes", description="")
    next_offset: Any | None = Field(None, alias="nextOffset", description="")
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
