from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field


class ImageAssetListInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    api_key: str | None = Field(None, alias="apiKey", description="Caller API key. Omit when the MCP request is already authenticated.")
    session_id: str | None = Field(None, alias="sessionId", description="Optional caller session identifier.")
    vault: str | None = Field(None, alias="vault", description="")
    project_id: str | None = Field(None, alias="projectId", description="")
    folder_id: str | None = Field(None, alias="folderId", description="")
    source_kind: Literal["upload", "scrape", "screenshot", "instagram", "external_url", "import"] | None = Field(None, alias="sourceKind", description="")
    source_host: str | None = Field(None, alias="sourceHost", description="")
    mime_type: Literal["image/jpeg", "image/png", "image/webp", "image/gif"] | None = Field(None, alias="mimeType", description="")
    tags: list[str] | None = Field(None, alias="tags", description="")
    created_after: str | None = Field(None, alias="createdAfter", description="")
    created_before: str | None = Field(None, alias="createdBefore", description="")
    limit: int | None = Field(None, alias="limit", description="")


class ImageAssetListOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")
