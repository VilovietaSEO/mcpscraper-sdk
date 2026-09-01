from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field


class ImageAssetGetInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="forbid")

    api_key: str | None = Field(None, alias="apiKey", description="Caller API key. Omit when the MCP request is already authenticated.")
    session_id: str | None = Field(None, alias="sessionId", description="Optional caller session identifier.")
    vault: str | None = Field(None, alias="vault", description="")
    asset_id: str = Field(..., alias="assetId", description="")
    include_preview: bool | None = Field(None, alias="includePreview", description="")


class ImageAssetGetOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")
