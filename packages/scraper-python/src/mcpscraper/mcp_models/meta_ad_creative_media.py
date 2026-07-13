from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field


class MetaAdCreativeMediaInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    connection_id: str = Field(..., alias="connectionId", description="Tenant-owned Meta Marketing connectionId from list_service_connections.")
    ad_id: str = Field(..., alias="adId", description="Meta ad ID from the connected ad account. This is not an Ad Library archive ID.")
    image_mode: Literal["inline_preview", "resource_only", "none"] | None = Field(None, alias="imageMode", description="inline_preview returns bounded MCP image content that a vision-capable client can inspect. resource_only returns descriptors/URLs only. none skips image delivery.")
    max_inline_images: int | None = Field(None, alias="maxInlineImages", description="Maximum creative image/thumbnail previews to attach as MCP image blocks. Default 2; maximum 4.")


class MetaAdCreativeMediaOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")
