from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field


class ImageAssetSearchInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    vault: str | None = Field(None, alias="vault", description="Exact accessible Memory vault name; omit only when this tool documents a safe active-vault default.")
    query_text: str | None = Field(None, alias="queryText", description="Semantic text query for image retrieval; it may be combined with one image-query source.")
    query_asset_id: str | None = Field(None, alias="queryAssetId", description="Stored image asset to use as the visual search query; use only one image-query source.")
    query_url: str | None = Field(None, alias="queryUrl", description="Public HTTPS image URL to use as the visual search query; use only one image-query source.")
    query_image_base64: str | None = Field(None, alias="queryImageBase64", description="Bounded base64 image bytes to use as the visual search query; use only one image-query source.")
    project_id: str | None = Field(None, alias="projectId", description="Opaque image project identifier returned by an image project tool.")
    folder_id: str | None = Field(None, alias="folderId", description="Opaque image folder identifier; omit only when the project root is intended.")
    source_kind: Literal['upload', 'scrape', 'screenshot', 'instagram', 'external_url', 'import'] | None = Field(None, alias="sourceKind", description="Provenance category used to filter or label governed image assets.")
    source_host: str | None = Field(None, alias="sourceHost", description="Normalized source hostname filter without a URL path.")
    mime_type: Literal['image/jpeg', 'image/png', 'image/webp', 'image/gif'] | None = Field(None, alias="mimeType", description="Exact media-type filter, such as image/png; omit for every supported image type.")
    tags: list[str] | None = Field(None, alias="tags", description="Canonical tag filter or tag set; use the appropriate vocabulary-listing tool before writing new tags.")
    created_after: str | None = Field(None, alias="createdAfter", description="Inclusive ISO 8601 lower bound for asset creation time.")
    created_before: str | None = Field(None, alias="createdBefore", description="Exclusive ISO 8601 upper bound for asset creation time.")
    limit: int | None = Field(None, alias="limit", description="Maximum rows or records to return on this page; use the returned cursor for more.")
    include_preview: bool | None = Field(None, alias="includePreview", description="When true, mint a short-lived authorized preview URL with the metadata result.")


class ImageAssetSearchOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    ok: Literal[True, False] = Field(..., alias="ok", description="")
    results: list[dict[str, Any]] | None = Field(None, alias="results", description="")
    count: float | None = Field(None, alias="count", description="")
    code: str | None = Field(None, alias="code", description="")
    error: str | None = Field(None, alias="error", description="")
