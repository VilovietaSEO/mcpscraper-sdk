from typing import Annotated, Any, Literal, Union
from typing_extensions import NotRequired, Required, TypedDict
from pydantic import BaseModel, ConfigDict, Field, TypeAdapter


class MetaAdCreativeMediaInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=False)

    connection_id: Annotated[str, Field(min_length=1)] = Field(..., alias='connectionId', description='Tenant-owned Meta Marketing connectionId from list_service_connections.')
    ad_id: str = Field(..., alias='adId', description='Meta ad ID from the connected ad account. This is not an Ad Library archive ID.')
    image_mode: Union[Literal['inline_preview', 'resource_only', 'none'], None] = Field(None, alias='imageMode', description='inline_preview returns bounded MCP image content that a vision-capable client can inspect. resource_only returns descriptors/URLs only. none skips image delivery.')
    max_inline_images: Union[Annotated[int, Field(ge=1, le=4)], None] = Field(None, alias='maxInlineImages', description='Maximum creative image/thumbnail previews to attach as MCP image blocks. Default 2; maximum 4.')


MetaAdCreativeMediaOutputVariant1InlineImagesItem = TypedDict('MetaAdCreativeMediaOutputVariant1InlineImagesItem', {
    'sourceUrl': Required[str],
    'mimeType': Required[str],
    'bytes': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'contentIndex': Required[Annotated[int, Field(ge=1, le=9007199254740991)]],
})
MetaAdCreativeMediaOutputVariant1InlineImagesItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


MetaAdCreativeMediaOutputVariant1NextActionsItem = TypedDict('MetaAdCreativeMediaOutputVariant1NextActionsItem', {
    'tool': Required[Literal['facebook_ad_transcribe', 'facebook_video_transcribe', 'video_frame_analysis']],
    'args': Required[dict[str, Any]],
    'reason': Required[str],
})
MetaAdCreativeMediaOutputVariant1NextActionsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class MetaAdCreativeMediaOutputVariant1(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    ok: bool = Field(..., alias='ok', description='')
    ad_id: str = Field(..., alias='adId', description='')
    ad_name: Union[str, None] = Field(..., alias='adName', description='')
    ad_account_id: Union[str, None] = Field(..., alias='adAccountId', description='')
    creative_id: str = Field(..., alias='creativeId', description='')
    creative_name: Union[str, None] = Field(..., alias='creativeName', description='')
    effective_object_story_id: Union[str, None] = Field(..., alias='effectiveObjectStoryId', description='')
    source_facebook_post_id: Union[str, None] = Field(..., alias='sourceFacebookPostId', description='')
    object_story_id: Union[str, None] = Field(..., alias='objectStoryId', description='')
    page_id: Union[str, None] = Field(..., alias='pageId', description='')
    post_id: Union[str, None] = Field(..., alias='postId', description='')
    public_post_candidate_url: Union[str, None] = Field(..., alias='publicPostCandidateUrl', description='')
    public_post_status: Literal['unverified'] = Field(..., alias='publicPostStatus', description='')
    media_type: Literal['image', 'video', 'carousel', 'mixed', 'unknown'] = Field(..., alias='mediaType', description='')
    images: list[dict[str, Any]] = Field(..., alias='images', description='')
    videos: list[dict[str, Any]] = Field(..., alias='videos', description='')
    inline_images: list[MetaAdCreativeMediaOutputVariant1InlineImagesItem] = Field(..., alias='inlineImages', description='')
    next_actions: list[MetaAdCreativeMediaOutputVariant1NextActionsItem] = Field(..., alias='nextActions', description='')
    warnings: list[str] = Field(..., alias='warnings', description='')
    limitations: list[str] = Field(..., alias='limitations', description='')


MetaAdCreativeMediaOutputVariant2DeliveryArtifactsItem = TypedDict('MetaAdCreativeMediaOutputVariant2DeliveryArtifactsItem', {
    'artifactId': Required[str],
    'filename': Required[str],
    'contentType': Required[str],
    'bytes': Required[Union[float, int]],
    'sha256': Required[str],
    'expiresAt': Required[str],
    'capabilities': Required[list[str]],
    'downloadUrl': Required[Union[str, None]],
    'downloadUrlExpiresAt': Required[Union[str, None]],
    'downloadState': Required[Literal['available', 'local', 'unavailable']],
})
MetaAdCreativeMediaOutputVariant2DeliveryArtifactsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


MetaAdCreativeMediaOutputVariant2DeliveryAvailableExportsItem = TypedDict('MetaAdCreativeMediaOutputVariant2DeliveryAvailableExportsItem', {
    'artifactId': Required[str],
    'sourceArtifactId': Required[str],
    'filename': Required[Literal['result.md']],
    'contentType': Required[Literal['text/markdown; charset=utf-8']],
    'state': Required[Literal['on-demand']],
})
MetaAdCreativeMediaOutputVariant2DeliveryAvailableExportsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


MetaAdCreativeMediaOutputVariant2DeliveryStorageFailureVariant1 = TypedDict('MetaAdCreativeMediaOutputVariant2DeliveryStorageFailureVariant1', {
    'artifactId': Required[Union[str, None]],
    'outcome': Required[Literal['unknown', 'bytes-stored-metadata-pending', 'failed']],
})
MetaAdCreativeMediaOutputVariant2DeliveryStorageFailureVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


MetaAdCreativeMediaOutputVariant2Delivery = TypedDict('MetaAdCreativeMediaOutputVariant2Delivery', {
    'mode': Required[Literal['artifact']],
    'status': Required[Literal['complete', 'partial', 'unavailable']],
    'retainedRepresentation': Required[Literal['formatted-tool-result']],
    'sourceIsError': Required[bool],
    'artifacts': Required[list[MetaAdCreativeMediaOutputVariant2DeliveryArtifactsItem]],
    'availableExports': NotRequired[list[MetaAdCreativeMediaOutputVariant2DeliveryAvailableExportsItem]],
    'downloadLinksOmitted': Required[bool],
    'scopeOmittedFields': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'storageFailure': Required[Union[MetaAdCreativeMediaOutputVariant2DeliveryStorageFailureVariant1, None]],
    'nextAction': Required[str],
})
MetaAdCreativeMediaOutputVariant2Delivery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


MetaAdCreativeMediaOutputVariant2RecoveryOperation = TypedDict('MetaAdCreativeMediaOutputVariant2RecoveryOperation', {
    'runId': Required[Union[Annotated[str, Field(max_length=200)], None]],
    'idempotencyKey': Required[Annotated[str, Field(max_length=512)]],
    'state': Required[Annotated[str, Field(max_length=100)]],
})
MetaAdCreativeMediaOutputVariant2RecoveryOperation.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


MetaAdCreativeMediaOutputVariant2Recovery = TypedDict('MetaAdCreativeMediaOutputVariant2Recovery', {
    'idempotencyKey': NotRequired[Annotated[str, Field(max_length=512)]],
    'operationId': NotRequired[Annotated[str, Field(max_length=200)]],
    'runId': NotRequired[Annotated[str, Field(max_length=200)]],
    'jobId': NotRequired[Annotated[str, Field(max_length=200)]],
    'operation': NotRequired[MetaAdCreativeMediaOutputVariant2RecoveryOperation],
})
MetaAdCreativeMediaOutputVariant2Recovery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class MetaAdCreativeMediaOutputVariant2(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    delivery: MetaAdCreativeMediaOutputVariant2Delivery = Field(..., alias='delivery', description='')
    preview: str = Field(..., alias='preview', description='')
    scope: dict[str, Union[str, Union[float, int], bool, None]] = Field(..., alias='scope', description='')
    recovery: MetaAdCreativeMediaOutputVariant2Recovery = Field(..., alias='recovery', description='')


# Union schema: validate external payloads with TypeAdapter(MetaAdCreativeMediaOutput).
MetaAdCreativeMediaOutput = Union[MetaAdCreativeMediaOutputVariant1, MetaAdCreativeMediaOutputVariant2]

_MetaAdCreativeMediaInputAdapter = TypeAdapter(MetaAdCreativeMediaInput)
_MetaAdCreativeMediaOutputAdapter = TypeAdapter(MetaAdCreativeMediaOutput)