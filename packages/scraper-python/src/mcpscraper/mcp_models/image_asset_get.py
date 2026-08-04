from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field


class ImageAssetGetInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    vault: str | None = Field(None, alias="vault", description="")
    asset_id: str = Field(..., alias="assetId", description="")
    include_preview: bool | None = Field(None, alias="includePreview", description="")


class ImageAssetGetOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")
