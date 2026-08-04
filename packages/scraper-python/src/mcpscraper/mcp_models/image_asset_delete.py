from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field


class ImageAssetDeleteInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    vault: str | None = Field(None, alias="vault", description="")
    asset_id: str = Field(..., alias="assetId", description="")
    confirm_delete: bool = Field(..., alias="confirmDelete", description="Must be true after the caller has confirmed deletion.")


class ImageAssetDeleteOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")
