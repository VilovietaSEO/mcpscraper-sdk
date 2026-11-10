from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field, model_serializer


class MetaAdCreativeMediaInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    connection_id: str = Field(..., alias="connectionId", description="Tenant-owned Meta Marketing connectionId from list_service_connections.")
    ad_id: str = Field(..., alias="adId", description="Meta ad ID from the connected ad account. This is not an Ad Library archive ID.")
    image_mode: Literal['inline_preview', 'resource_only', 'none'] | None = Field(None, alias="imageMode", description="inline_preview returns bounded MCP image content that a vision-capable client can inspect. resource_only returns descriptors/URLs only. none skips image delivery.")
    max_inline_images: int | None = Field(None, alias="maxInlineImages", description="Maximum creative image/thumbnail previews to attach as MCP image blocks. Default 2; maximum 4.")


class MetaAdCreativeMediaOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    ok: bool | None = Field(None, alias="ok", description="")
    ad_id: str | None = Field(None, alias="adId", description="")
    ad_name: Any | None = Field(None, alias="adName", description="")
    ad_account_id: Any | None = Field(None, alias="adAccountId", description="")
    creative_id: str | None = Field(None, alias="creativeId", description="")
    creative_name: Any | None = Field(None, alias="creativeName", description="")
    effective_object_story_id: Any | None = Field(None, alias="effectiveObjectStoryId", description="")
    source_facebook_post_id: Any | None = Field(None, alias="sourceFacebookPostId", description="")
    object_story_id: Any | None = Field(None, alias="objectStoryId", description="")
    page_id: Any | None = Field(None, alias="pageId", description="")
    post_id: Any | None = Field(None, alias="postId", description="")
    public_post_candidate_url: Any | None = Field(None, alias="publicPostCandidateUrl", description="")
    public_post_status: str | None = Field(None, alias="publicPostStatus", description="")
    media_type: Literal['image', 'video', 'carousel', 'mixed', 'unknown'] | None = Field(None, alias="mediaType", description="")
    images: list[dict[str, Any]] | None = Field(None, alias="images", description="")
    videos: list[dict[str, Any]] | None = Field(None, alias="videos", description="")
    inline_images: list[dict[str, Any]] | None = Field(None, alias="inlineImages", description="")
    next_actions: list[dict[str, Any]] | None = Field(None, alias="nextActions", description="")
    warnings: list[str] | None = Field(None, alias="warnings", description="")
    limitations: list[str] | None = Field(None, alias="limitations", description="")
    delivery: dict[str, Any] | None = Field(None, alias="delivery", description="")
    preview: str | None = Field(None, alias="preview", description="")
    scope: dict[str, Any] | None = Field(None, alias="scope", description="")
    recovery: dict[str, Any] | None = Field(None, alias="recovery", description="")

    @model_serializer(mode="wrap")
    def _serialize_response(self, handler, info):
        data = handler(self)
        for name, field in type(self).model_fields.items():
            if name not in self.model_fields_set:
                key = field.alias if info.by_alias and field.alias else name
                data.pop(key, None)
        return data
