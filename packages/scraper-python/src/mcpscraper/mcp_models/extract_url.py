from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field


class ExtractUrlInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    url: str = Field(..., alias="url", description="Public http/https URL to extract.")
    screenshot: bool | None = Field(None, alias="screenshot", description="Capture a full-page screenshot, saved to ~/Downloads/mcp-scraper/screenshots/ and returned inline.")
    screenshot_device: Literal["desktop", "mobile"] | None = Field(None, alias="screenshotDevice", description="Viewport for screenshot. desktop = 1440×900, mobile = 390×844.")
    extract_branding: bool | None = Field(None, alias="extractBranding", description="Extract brand colors, fonts, logo, and favicon via a rendered browser session.")
    download_media: bool | None = Field(None, alias="downloadMedia", description="Extract and download page media (images/video/audio) to ~/Downloads/mcp-scraper/media/. Ad/tracking noise is filtered automatically.")
    media_types: list[Literal["image", "video", "audio"]] | None = Field(None, alias="mediaTypes", description="Which media types to download. Default all three.")
    allow_local: bool | None = Field(None, alias="allowLocal", description="Allow localhost and private-network URLs. Local development only.")
    deposit_to_vault: bool | None = Field(None, alias="depositToVault", description="Save the full page content into the user's MCP Memory vault server-side, embedded for semantic recall — the full body is NOT returned to chat.")
    vault_name: str | None = Field(None, alias="vaultName", description="Optional vault to deposit into. Defaults to the user's personal vault.")


class ExtractUrlOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")
