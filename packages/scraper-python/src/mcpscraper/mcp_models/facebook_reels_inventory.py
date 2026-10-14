from typing import Annotated, Any, Literal, Union
from typing_extensions import NotRequired, Required, TypedDict
from pydantic import BaseModel, ConfigDict, Field, TypeAdapter


class FacebookReelsInventoryInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=False)

    url: str = Field(..., alias='url', description='Public Facebook profile or Page URL whose Reel URLs should be collected. Do not pass an individual Reel, video, post, share, group, or event URL.')
    max_urls: Union[Annotated[int, Field(ge=1, le=2000)], None] = Field(None, alias='maxUrls', description='Maximum Reel URLs requested. Logged-out collection is capped at 60 even when this is higher; a valid saved Facebook browser profile can continue toward the requested maximum.')
    profile: Union[Annotated[str, Field(min_length=1)], None] = Field(None, alias='profile', description='Optional saved hosted browser profile name containing a Facebook login. Set one up with browser_profile_connect first. An expired or logged-out profile falls back to the anonymous 60-URL cap.')
    save_profile_changes: Union[bool, None] = Field(None, alias='saveProfileChanges', description='Save browser changes back to the hosted profile. Leave unset unless intentionally updating the saved Facebook login.')
    resume_urls: Union[Annotated[list[str], Field(max_length=2000)], None] = Field(None, alias='resumeUrls', description='Previously returned Reel URLs to retain and deduplicate while continuing an interrupted collection.')
    max_scrolls: Union[Annotated[int, Field(ge=0, le=250)], None] = Field(None, alias='maxScrolls', description='Safety ceiling for pagination attempts. Default 250; collection normally stops earlier at maxUrls or a Facebook access boundary.')
    scroll_delay_ms: Union[Annotated[int, Field(ge=250, le=5000)], None] = Field(None, alias='scrollDelayMs', description='Delay after each scroll before collecting the next DOM batch.')
    stable_scroll_limit: Union[Annotated[int, Field(ge=1, le=10)], None] = Field(None, alias='stableScrollLimit', description='Stop after this many consecutive pagination attempts add no Reel URLs.')


FacebookReelsInventoryOutputVariant1Browser = TypedDict('FacebookReelsInventoryOutputVariant1Browser', {
    'mode': Required[Literal['hosted']],
    'requestedMode': Required[Literal['hosted']],
    'profileName': Required[Union[str, None]],
    'profileSource': Required[Literal['hosted']],
})
FacebookReelsInventoryOutputVariant1Browser.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


FacebookReelsInventoryOutputVariant1PaginationStagesItem = TypedDict('FacebookReelsInventoryOutputVariant1PaginationStagesItem', {
    'stage': Required[str],
    'itemCount': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'addedCount': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'scrollY': Required[Union[Union[float, int], None]],
    'scrollHeight': Required[Union[Union[float, int], None]],
    'loginWallVisible': Required[bool],
    'dismissibleLoginOverlayVisible': Required[bool],
})
FacebookReelsInventoryOutputVariant1PaginationStagesItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


FacebookReelsInventoryOutputVariant1Pagination = TypedDict('FacebookReelsInventoryOutputVariant1Pagination', {
    'maxScrolls': Required[Annotated[int, Field(ge=0, le=250)]],
    'attemptedScrolls': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'stableScrolls': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'stableScrollLimit': Required[Annotated[int, Field(ge=1, le=10)]],
    'scrollDelayMs': Required[Annotated[int, Field(ge=250, le=5000)]],
    'stages': Required[list[FacebookReelsInventoryOutputVariant1PaginationStagesItem]],
})
FacebookReelsInventoryOutputVariant1Pagination.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


FacebookReelsInventoryOutputVariant1ItemsItem = TypedDict('FacebookReelsInventoryOutputVariant1ItemsItem', {
    'url': Required[str],
    'reelId': Required[str],
    'viewCountText': Required[Union[str, None]],
    'anchorText': Required[Union[str, None]],
    'firstSeenStage': Required[str],
})
FacebookReelsInventoryOutputVariant1ItemsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


FacebookReelsInventoryOutputVariant1RecoverableErrorVariant1 = TypedDict('FacebookReelsInventoryOutputVariant1RecoverableErrorVariant1', {
    'stage': Required[str],
    'message': Required[str],
})
FacebookReelsInventoryOutputVariant1RecoverableErrorVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class FacebookReelsInventoryOutputVariant1(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    source_url: str = Field(..., alias='sourceUrl', description='')
    profile_url: str = Field(..., alias='profileUrl', description='')
    page_url: str = Field(..., alias='pageUrl', description='')
    profile_name: Union[str, None] = Field(..., alias='profileName', description='')
    browser: FacebookReelsInventoryOutputVariant1Browser = Field(..., alias='browser', description='')
    requested_max_urls: Annotated[int, Field(ge=1, le=2000)] = Field(..., alias='requestedMaxUrls', description='')
    effective_max_urls: Annotated[int, Field(ge=1, le=2000)] = Field(..., alias='effectiveMaxUrls', description='')
    anonymous_cap: Literal[60] = Field(..., alias='anonymousCap', description='')
    anonymous_cap_applied: bool = Field(..., alias='anonymousCapApplied', description='')
    saved_profile_requested: bool = Field(..., alias='savedProfileRequested', description='')
    authentication_status: Literal['authenticated', 'logged_out', 'unknown'] = Field(..., alias='authenticationStatus', description='')
    collected_url_count: Annotated[int, Field(ge=0, le=9007199254740991)] = Field(..., alias='collectedUrlCount', description='')
    resumed_url_count: Annotated[int, Field(ge=0, le=9007199254740991)] = Field(..., alias='resumedUrlCount', description='')
    newly_collected_url_count: Annotated[int, Field(ge=0, le=9007199254740991)] = Field(..., alias='newlyCollectedUrlCount', description='')
    complete: bool = Field(..., alias='complete', description='')
    partial: bool = Field(..., alias='partial', description='')
    stopped_reason: Literal['max_urls', 'anonymous_cap', 'deadline', 'login_wall', 'stable_scrolls', 'max_scrolls', 'no_scrolls', 'navigation_error', 'browser_error'] = Field(..., alias='stoppedReason', description='')
    pagination: FacebookReelsInventoryOutputVariant1Pagination = Field(..., alias='pagination', description='')
    items: list[FacebookReelsInventoryOutputVariant1ItemsItem] = Field(..., alias='items', description='')
    limitations: list[str] = Field(..., alias='limitations', description='')
    recoverable_error: Union[FacebookReelsInventoryOutputVariant1RecoverableErrorVariant1, None] = Field(..., alias='recoverableError', description='')
    extracted_at: str = Field(..., alias='extractedAt', description='')


FacebookReelsInventoryOutputVariant2DeliveryArtifactsItem = TypedDict('FacebookReelsInventoryOutputVariant2DeliveryArtifactsItem', {
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
FacebookReelsInventoryOutputVariant2DeliveryArtifactsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


FacebookReelsInventoryOutputVariant2DeliveryStorageFailureVariant1 = TypedDict('FacebookReelsInventoryOutputVariant2DeliveryStorageFailureVariant1', {
    'artifactId': Required[Union[str, None]],
    'outcome': Required[Literal['unknown', 'bytes-stored-metadata-pending', 'failed']],
})
FacebookReelsInventoryOutputVariant2DeliveryStorageFailureVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


FacebookReelsInventoryOutputVariant2Delivery = TypedDict('FacebookReelsInventoryOutputVariant2Delivery', {
    'mode': Required[Literal['artifact']],
    'status': Required[Literal['complete', 'partial', 'unavailable']],
    'retainedRepresentation': Required[Literal['formatted-tool-result']],
    'sourceIsError': Required[bool],
    'artifacts': Required[list[FacebookReelsInventoryOutputVariant2DeliveryArtifactsItem]],
    'downloadLinksOmitted': Required[bool],
    'scopeOmittedFields': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'storageFailure': Required[Union[FacebookReelsInventoryOutputVariant2DeliveryStorageFailureVariant1, None]],
    'nextAction': Required[str],
})
FacebookReelsInventoryOutputVariant2Delivery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


FacebookReelsInventoryOutputVariant2RecoveryOperation = TypedDict('FacebookReelsInventoryOutputVariant2RecoveryOperation', {
    'runId': Required[Union[Annotated[str, Field(max_length=200)], None]],
    'idempotencyKey': Required[Annotated[str, Field(max_length=512)]],
    'state': Required[Annotated[str, Field(max_length=100)]],
})
FacebookReelsInventoryOutputVariant2RecoveryOperation.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


FacebookReelsInventoryOutputVariant2Recovery = TypedDict('FacebookReelsInventoryOutputVariant2Recovery', {
    'idempotencyKey': NotRequired[Annotated[str, Field(max_length=512)]],
    'operationId': NotRequired[Annotated[str, Field(max_length=200)]],
    'runId': NotRequired[Annotated[str, Field(max_length=200)]],
    'jobId': NotRequired[Annotated[str, Field(max_length=200)]],
    'operation': NotRequired[FacebookReelsInventoryOutputVariant2RecoveryOperation],
})
FacebookReelsInventoryOutputVariant2Recovery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class FacebookReelsInventoryOutputVariant2(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    delivery: FacebookReelsInventoryOutputVariant2Delivery = Field(..., alias='delivery', description='')
    preview: str = Field(..., alias='preview', description='')
    scope: dict[str, Union[str, Union[float, int], bool, None]] = Field(..., alias='scope', description='')
    recovery: FacebookReelsInventoryOutputVariant2Recovery = Field(..., alias='recovery', description='')


# Union schema: validate external payloads with TypeAdapter(FacebookReelsInventoryOutput).
FacebookReelsInventoryOutput = Union[FacebookReelsInventoryOutputVariant1, FacebookReelsInventoryOutputVariant2]

_FacebookReelsInventoryInputAdapter = TypeAdapter(FacebookReelsInventoryInput)
_FacebookReelsInventoryOutputAdapter = TypeAdapter(FacebookReelsInventoryOutput)