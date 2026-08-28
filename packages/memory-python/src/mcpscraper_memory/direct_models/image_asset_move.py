from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field


class ImageAssetMoveInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    api_key: str | None = Field(None, alias="apiKey", description="Caller API key. Omit when the MCP request is already authenticated.")
    session_id: str | None = Field(None, alias="sessionId", description="Optional caller session identifier.")
    vault: str | None = Field(None, alias="vault", description="")
    asset_id: str = Field(..., alias="assetId", description="")
    project_id: Any | None = Field(None, alias="projectId", description="")
    folder_id: Any | None = Field(None, alias="folderId", description="")


class ImageAssetMoveOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")
