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

    ok: bool = Field(..., alias="ok", description="")
    ad_id: str = Field(..., alias="adId", description="")
    ad_name: Any = Field(..., alias="adName", description="")
    ad_account_id: Any = Field(..., alias="adAccountId", description="")
    creative_id: str = Field(..., alias="creativeId", description="")
    creative_name: Any = Field(..., alias="creativeName", description="")
    effective_object_story_id: Any = Field(..., alias="effectiveObjectStoryId", description="")
    source_facebook_post_id: Any = Field(..., alias="sourceFacebookPostId", description="")
    object_story_id: Any = Field(..., alias="objectStoryId", description="")
    page_id: Any = Field(..., alias="pageId", description="")
    post_id: Any = Field(..., alias="postId", description="")
    public_post_candidate_url: Any = Field(..., alias="publicPostCandidateUrl", description="")
    public_post_status: str = Field(..., alias="publicPostStatus", description="")
    media_type: Literal["image", "video", "carousel", "mixed", "unknown"] = Field(..., alias="mediaType", description="")
    images: list[dict[str, Any]] = Field(..., alias="images", description="")
    videos: list[dict[str, Any]] = Field(..., alias="videos", description="")
    inline_images: list[dict[str, Any]] = Field(..., alias="inlineImages", description="")
    next_actions: list[dict[str, Any]] = Field(..., alias="nextActions", description="")
    warnings: list[str] = Field(..., alias="warnings", description="")
    limitations: list[str] = Field(..., alias="limitations", description="")
