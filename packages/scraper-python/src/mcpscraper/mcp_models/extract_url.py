from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field


class ExtractUrlInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    url: str = Field(..., alias="url", description="Public http/https URL to extract.")
    screenshot: bool | None = Field(None, alias="screenshot", description="Capture a full-page screenshot. Large captures may be offloaded to an owned artifact.")
    screenshot_device: Literal['desktop', 'mobile'] | None = Field(None, alias="screenshotDevice", description="Viewport: desktop = 1440×900, mobile = 390×844.")
    extract_branding: bool | None = Field(None, alias="extractBranding", description="Extract brand colors, fonts, logo, and favicon via a rendered session.")
    include_featured_image: bool | None = Field(None, alias="includeFeaturedImage", description="Return the best featured image from Open Graph, Twitter, JSON-LD, or page content. Wayback URLs get the timestamp-matched archived image.")
    download_media: bool | None = Field(None, alias="downloadMedia", description="Deprecated alias for preserveMedia; omit when using preserveMedia.")
    media_types: list[Literal['image', 'video', 'audio']] | None = Field(None, alias="mediaTypes", description="Media types to download. Default all three.")
    max_media_assets: int | None = Field(None, alias="maxMediaAssets", description="Maximum media records to retain after filtering and variant collapse.")
    max_inline_images: int | None = Field(None, alias="maxInlineImages", description="Maximum images attached as AI-readable content blocks. All downloaded media stays available in the ZIP.")
    delivery: Literal['auto', 'inline', 'artifact', 'memory'] | None = Field(None, alias="delivery", description="auto offloads large results; artifact always returns an artifact; memory stores in hosted Memory; inline is bounded.")
    preserve_media: bool | None = Field(None, alias="preserveMedia", description="Collect media from static plus rendered page content, collapse responsive variants, attach bounded previews, and create an owner-scoped ZIP readable with archive_read.")
    deposit_to_vault: bool | None = Field(None, alias="depositToVault", description="Save the full page content into the user's MCP Memory vault, embedded for semantic recall — the full body is NOT returned to chat.")
    vault_name: str | None = Field(None, alias="vaultName", description="Optional vault to deposit into; defaults to the personal vault.")
    idempotency_key: str | None = Field(None, alias="idempotencyKey", description="Retry key: reuse after a timeout to avoid re-billing. New key per extraction.")


class ExtractUrlOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    url: str = Field(..., alias="url", description="")
    title: Any = Field(..., alias="title", description="")
    headings: list[dict[str, Any]] = Field(..., alias="headings", description="")
    schema_block_count: int = Field(..., alias="schemaBlockCount", description="")
    entity_name: Any = Field(..., alias="entityName", description="")
    entity_types: list[str] = Field(..., alias="entityTypes", description="")
    structured_data_logo: Any = Field(..., alias="structuredDataLogo", description="Logo declared by the selected Organization or LocalBusiness JSON-LD entity, separate from the rendered branding candidate ranking.")
    nap_score: Any = Field(..., alias="napScore", description="")
    missing_schema_fields: list[str] = Field(..., alias="missingSchemaFields", description="")
    screenshot_saved: Any = Field(..., alias="screenshotSaved", description="")
    screenshot_artifact: dict[str, Any] | None = Field(None, alias="screenshotArtifact", description="Owner-scoped private screenshot handoff created only when preserveMedia is true. Pass artifactId to image_asset_save to retain it in hosted Memory.")
    archive: Any = Field(..., alias="archive", description="")
    featured_image: Any = Field(..., alias="featuredImage", description="")
    branding: Any = Field(..., alias="branding", description="Rendered brand and proof evidence. logo is the site identity, logoVariants are the same mark family, and proofImages are separately typed body trust signals. Inspect confidence and evidence rather than treating uncertain relationships as facts.")
    media_assets: Any = Field(..., alias="mediaAssets", description="Backward-compatible flattened page-media inventory. Use media for completeness, warnings, and artifact delivery.")
    media: Any = Field(..., alias="media", description="Static-plus-rendered website media manifest with provenance, bounded image content-block indices, completion state, and owner-scoped ZIP delivery.")
    memory: dict[str, Any] | None = Field(None, alias="memory", description="")
    memory_images: dict[str, Any] | None = Field(None, alias="memoryImages", description="Governed hosted Memory image saves, present only for delivery:\"memory\" with preserveMedia:true.")
    delivery: dict[str, Any] | None = Field(None, alias="delivery", description="")
    local_path: str | None = Field(None, alias="localPath", description="Server-generated local report path, present only on an installed stdio server that successfully wrote the file.")
    artifact: dict[str, Any] | None = Field(None, alias="artifact", description="")
