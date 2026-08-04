from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field


class ImageAssetMoveInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    vault: str | None = Field(None, alias="vault", description="")
    asset_id: str = Field(..., alias="assetId", description="")
    project_id: Any | None = Field(None, alias="projectId", description="")
    folder_id: Any | None = Field(None, alias="folderId", description="")


class ImageAssetMoveOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")
