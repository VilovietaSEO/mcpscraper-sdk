from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field


class ExtractUrlInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    url: str = Field(..., alias="url", description="Public http/https URL to extract.")
    screenshot: bool | None = Field(None, alias="screenshot", description="Capture a full-page screenshot and return it through the result contract. Large captures may be offloaded to an owned artifact.")
    screenshot_device: Literal["desktop", "mobile"] | None = Field(None, alias="screenshotDevice", description="Viewport for screenshot. desktop = 1440×900, mobile = 390×844.")
    extract_branding: bool | None = Field(None, alias="extractBranding", description="Extract brand colors, fonts, logo, and favicon via a rendered browser session.")
    include_featured_image: bool | None = Field(None, alias="includeFeaturedImage", description="Return the best featured image from Open Graph, Twitter, JSON-LD, or page content. For Wayback replay URLs, also returns the timestamp-matched archived image URL when available.")
    download_media: bool | None = Field(None, alias="downloadMedia", description="Deprecated alias for preserveMedia. Omit when using preserveMedia; when omitted, media preservation defaults to false.")
    media_types: list[Literal["image", "video", "audio"]] | None = Field(None, alias="mediaTypes", description="Which media types to download. Default all three.")
    delivery: Literal["auto", "inline", "artifact", "memory"] | None = Field(None, alias="delivery", description="Where to deliver the result. auto keeps small results inline and offloads large ones; artifact always returns an owned artifact; memory stores the full page in hosted Memory; inline returns a bounded response.")
    preserve_media: bool | None = Field(None, alias="preserveMedia", description="Preserve discovered media in the result workflow. This is the preferred replacement for downloadMedia.")
    deposit_to_vault: bool | None = Field(None, alias="depositToVault", description="Save the full page content into the user's MCP Memory vault server-side, embedded for semantic recall — the full body is NOT returned to chat.")
    vault_name: str | None = Field(None, alias="vaultName", description="Optional vault to deposit into. Defaults to the user's personal vault.")


class ExtractUrlOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    url: str = Field(..., alias="url", description="")
    title: Any = Field(..., alias="title", description="")
    headings: list[dict[str, Any]] = Field(..., alias="headings", description="")
    schema_block_count: int = Field(..., alias="schemaBlockCount", description="")
    entity_name: Any = Field(..., alias="entityName", description="")
    entity_types: list[str] = Field(..., alias="entityTypes", description="")
    nap_score: Any = Field(..., alias="napScore", description="")
    missing_schema_fields: list[str] = Field(..., alias="missingSchemaFields", description="")
    screenshot_saved: Any = Field(..., alias="screenshotSaved", description="")
    archive: Any = Field(..., alias="archive", description="")
    featured_image: Any = Field(..., alias="featuredImage", description="")
    memory: dict[str, Any] | None = Field(None, alias="memory", description="")
