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

    job_id: str = Field(..., alias="jobId", description="")
    status: Literal['pending', 'running', 'done', 'failed', 'cancelled'] = Field(..., alias="status", description="")
    status_tool: str = Field(..., alias="statusTool", description="")
    replayed: bool = Field(..., alias="replayed", description="")
