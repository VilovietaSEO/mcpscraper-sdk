from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field


class ImageAssetSearchInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    vault: str | None = Field(None, alias="vault", description="")
    query_text: str | None = Field(None, alias="queryText", description="")
    query_asset_id: str | None = Field(None, alias="queryAssetId", description="")
    query_url: str | None = Field(None, alias="queryUrl", description="")
    query_image_base64: str | None = Field(None, alias="queryImageBase64", description="")
    project_id: str | None = Field(None, alias="projectId", description="")
    folder_id: str | None = Field(None, alias="folderId", description="")
    source_kind: Literal["upload", "scrape", "screenshot", "instagram", "external_url", "import"] | None = Field(None, alias="sourceKind", description="")
    source_host: str | None = Field(None, alias="sourceHost", description="")
    mime_type: Literal["image/jpeg", "image/png", "image/webp", "image/gif"] | None = Field(None, alias="mimeType", description="")
    tags: list[str] | None = Field(None, alias="tags", description="")
    created_after: str | None = Field(None, alias="createdAfter", description="")
    created_before: str | None = Field(None, alias="createdBefore", description="")
    limit: int | None = Field(None, alias="limit", description="")
    include_preview: bool | None = Field(None, alias="includePreview", description="")


class ImageAssetSearchOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")
