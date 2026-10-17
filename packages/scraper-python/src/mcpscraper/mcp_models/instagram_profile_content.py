from typing import Annotated, Any, Literal, Union
from typing_extensions import NotRequired, Required, TypedDict
from pydantic import BaseModel, ConfigDict, Field, TypeAdapter


class InstagramProfileContentInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=False)

    handle: Union[Annotated[str, Field(min_length=1)], None] = Field(None, alias='handle', description='Instagram handle, with or without @. Provide handle or url.')
    url: Union[str, None] = Field(None, alias='url', description='Instagram profile URL. Provide handle or url.')
    profile: Union[Annotated[str, Field(min_length=1)], None] = Field(None, alias='profile', description='Optional saved hosted browser profile name for authenticated Instagram access.')
    save_profile_changes: Union[bool, None] = Field(None, alias='saveProfileChanges', description='Save browser changes back to the hosted profile. Leave unset unless intentionally updating the saved login.')
    max_items: Union[Annotated[int, Field(ge=1, le=2000)], None] = Field(None, alias='maxItems', description='Maximum grid URLs to collect. Default 50, maximum 2000.')
    max_scrolls: Union[Annotated[int, Field(ge=0, le=250)], None] = Field(None, alias='maxScrolls', description='Maximum pagination scroll attempts. Default 10, maximum 250.')
    scroll_delay_ms: Union[Annotated[int, Field(ge=250, le=5000)], None] = Field(None, alias='scrollDelayMs', description='Delay after each scroll before collecting new links. Default 1200ms.')
    stable_scroll_limit: Union[Annotated[int, Field(ge=1, le=10)], None] = Field(None, alias='stableScrollLimit', description='Stop after this many consecutive scrolls with no new links.')


InstagramProfileContentOutputVariant1Browser = TypedDict('InstagramProfileContentOutputVariant1Browser', {
    'mode': Required[Literal['hosted']],
    'requestedMode': Required[Literal['hosted']],
    'profileName': Required[Union[str, None]],
    'profileSource': Required[Literal['hosted']],
    'profileDirConfigured': Required[bool],
    'executablePathConfigured': Required[bool],
})
InstagramProfileContentOutputVariant1Browser.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


InstagramProfileContentOutputVariant1TypeCounts = TypedDict('InstagramProfileContentOutputVariant1TypeCounts', {
    'post': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'reel': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'tv': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
})
InstagramProfileContentOutputVariant1TypeCounts.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


InstagramProfileContentOutputVariant1PaginationStagesItem = TypedDict('InstagramProfileContentOutputVariant1PaginationStagesItem', {
    'stage': Required[str],
    'itemCount': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'addedCount': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'scrollY': Required[Union[Union[float, int], None]],
    'scrollHeight': Required[Union[Union[float, int], None]],
})
InstagramProfileContentOutputVariant1PaginationStagesItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


InstagramProfileContentOutputVariant1Pagination = TypedDict('InstagramProfileContentOutputVariant1Pagination', {
    'maxItems': Required[Annotated[int, Field(ge=1, le=2000)]],
    'maxScrolls': Required[Annotated[int, Field(ge=0, le=250)]],
    'attemptedScrolls': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'stableScrolls': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'stableScrollLimit': Required[Annotated[int, Field(ge=1, le=10)]],
    'scrollDelayMs': Required[Annotated[int, Field(ge=250, le=5000)]],
    'reachedMaxItems': Required[bool],
    'reachedReportedPostCount': Required[bool],
    'finalScrollHeight': Required[Union[Annotated[int, Field(ge=-9007199254740991, le=9007199254740991)], None]],
    'stoppedReason': Required[Literal['max_items', 'reported_post_count', 'stable_scrolls', 'max_scrolls', 'no_scrolls']],
    'stages': Required[list[InstagramProfileContentOutputVariant1PaginationStagesItem]],
})
InstagramProfileContentOutputVariant1Pagination.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


InstagramProfileContentOutputVariant1ItemsItem = TypedDict('InstagramProfileContentOutputVariant1ItemsItem', {
    'url': Required[str],
    'type': Required[Literal['post', 'reel', 'tv']],
    'shortcode': Required[str],
    'anchorText': Required[Union[str, None]],
    'firstSeenStage': Required[str],
})
InstagramProfileContentOutputVariant1ItemsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class InstagramProfileContentOutputVariant1(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    handle: str = Field(..., alias='handle', description='')
    profile_url: str = Field(..., alias='profileUrl', description='')
    page_url: str = Field(..., alias='pageUrl', description='')
    browser: InstagramProfileContentOutputVariant1Browser = Field(..., alias='browser', description='')
    profile_name: Union[str, None] = Field(..., alias='profileName', description='')
    reported_post_count: Union[Annotated[int, Field(ge=-9007199254740991, le=9007199254740991)], None] = Field(..., alias='reportedPostCount', description='')
    reported_post_count_text: Union[str, None] = Field(..., alias='reportedPostCountText', description='')
    follower_count_text: Union[str, None] = Field(..., alias='followerCountText', description='')
    following_count_text: Union[str, None] = Field(..., alias='followingCountText', description='')
    collected_content_count: Annotated[int, Field(ge=0, le=9007199254740991)] = Field(..., alias='collectedContentCount', description='')
    type_counts: InstagramProfileContentOutputVariant1TypeCounts = Field(..., alias='typeCounts', description='')
    pagination: InstagramProfileContentOutputVariant1Pagination = Field(..., alias='pagination', description='')
    limited: bool = Field(..., alias='limited', description='')
    limitations: list[str] = Field(..., alias='limitations', description='')
    items: list[InstagramProfileContentOutputVariant1ItemsItem] = Field(..., alias='items', description='')


InstagramProfileContentOutputVariant2DeliveryArtifactsItem = TypedDict('InstagramProfileContentOutputVariant2DeliveryArtifactsItem', {
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
InstagramProfileContentOutputVariant2DeliveryArtifactsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


InstagramProfileContentOutputVariant2DeliveryAvailableExportsItem = TypedDict('InstagramProfileContentOutputVariant2DeliveryAvailableExportsItem', {
    'artifactId': Required[str],
    'sourceArtifactId': Required[str],
    'filename': Required[Literal['result.md']],
    'contentType': Required[Literal['text/markdown; charset=utf-8']],
    'state': Required[Literal['on-demand']],
})
InstagramProfileContentOutputVariant2DeliveryAvailableExportsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


InstagramProfileContentOutputVariant2DeliveryStorageFailureVariant1 = TypedDict('InstagramProfileContentOutputVariant2DeliveryStorageFailureVariant1', {
    'artifactId': Required[Union[str, None]],
    'outcome': Required[Literal['unknown', 'bytes-stored-metadata-pending', 'failed']],
})
InstagramProfileContentOutputVariant2DeliveryStorageFailureVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


InstagramProfileContentOutputVariant2Delivery = TypedDict('InstagramProfileContentOutputVariant2Delivery', {
    'mode': Required[Literal['artifact']],
    'status': Required[Literal['complete', 'partial', 'unavailable']],
    'retainedRepresentation': Required[Literal['formatted-tool-result']],
    'sourceIsError': Required[bool],
    'artifacts': Required[list[InstagramProfileContentOutputVariant2DeliveryArtifactsItem]],
    'availableExports': NotRequired[list[InstagramProfileContentOutputVariant2DeliveryAvailableExportsItem]],
    'downloadLinksOmitted': Required[bool],
    'scopeOmittedFields': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'storageFailure': Required[Union[InstagramProfileContentOutputVariant2DeliveryStorageFailureVariant1, None]],
    'nextAction': Required[str],
})
InstagramProfileContentOutputVariant2Delivery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


InstagramProfileContentOutputVariant2RecoveryOperation = TypedDict('InstagramProfileContentOutputVariant2RecoveryOperation', {
    'runId': Required[Union[Annotated[str, Field(max_length=200)], None]],
    'idempotencyKey': Required[Annotated[str, Field(max_length=512)]],
    'state': Required[Annotated[str, Field(max_length=100)]],
})
InstagramProfileContentOutputVariant2RecoveryOperation.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


InstagramProfileContentOutputVariant2Recovery = TypedDict('InstagramProfileContentOutputVariant2Recovery', {
    'idempotencyKey': NotRequired[Annotated[str, Field(max_length=512)]],
    'operationId': NotRequired[Annotated[str, Field(max_length=200)]],
    'runId': NotRequired[Annotated[str, Field(max_length=200)]],
    'jobId': NotRequired[Annotated[str, Field(max_length=200)]],
    'operation': NotRequired[InstagramProfileContentOutputVariant2RecoveryOperation],
})
InstagramProfileContentOutputVariant2Recovery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class InstagramProfileContentOutputVariant2(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    delivery: InstagramProfileContentOutputVariant2Delivery = Field(..., alias='delivery', description='')
    preview: str = Field(..., alias='preview', description='')
    scope: dict[str, Union[str, Union[float, int], bool, None]] = Field(..., alias='scope', description='')
    recovery: InstagramProfileContentOutputVariant2Recovery = Field(..., alias='recovery', description='')


# Union schema: validate external payloads with TypeAdapter(InstagramProfileContentOutput).
InstagramProfileContentOutput = Union[InstagramProfileContentOutputVariant1, InstagramProfileContentOutputVariant2]

_InstagramProfileContentInputAdapter = TypeAdapter(InstagramProfileContentInput)
_InstagramProfileContentOutputAdapter = TypeAdapter(InstagramProfileContentOutput)