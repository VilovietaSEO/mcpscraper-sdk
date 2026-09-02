from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field


class ImageAssetSaveInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="forbid")

    api_key: str | None = Field(None, alias="apiKey", description="Caller API key. Omit when the MCP request is already authenticated.")
    session_id: str | None = Field(None, alias="sessionId", description="Optional caller session identifier.")
    vault: str | None = Field(None, alias="vault", description="")
    project_id: str | None = Field(None, alias="projectId", description="")
    folder_id: str | None = Field(None, alias="folderId", description="")
    source_url: str | None = Field(None, alias="sourceUrl", description="Public HTTPS image URL. Private-network and redirect targets are rejected.")
    artifact_id: str | None = Field(None, alias="artifactId", description="Owned MCP Scraper artifact ID. Available through the aggregate MCP handoff.")
    image_base64: str | None = Field(None, alias="imageBase64", description="Bounded base64 image for clients without an upload transport; maximum decoded size is 20 MiB.")
    title: str = Field(..., alias="title", description="")
    description: str | None = Field(None, alias="description", description="")
    alt_text: str | None = Field(None, alias="altText", description="")
    tags: list[str] | None = Field(None, alias="tags", description="")
    source_ref: dict[str, Any] | None = Field(None, alias="sourceRef", description="")
    idempotency_key: str = Field(..., alias="idempotencyKey", description="Stable key for this logical save. Retrying the same request returns the same asset without another write.")


class ImageAssetSaveOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="forbid")

    ok: bool = Field(..., alias="ok", description="")
    asset: dict[str, Any] | None = Field(None, alias="asset", description="")
    reused_object: bool | None = Field(None, alias="reusedObject", description="")
    next_action: str | None = Field(None, alias="nextAction", description="")
    code: str | None = Field(None, alias="code", description="")
    error: str | None = Field(None, alias="error", description="")
