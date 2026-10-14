from typing import Annotated, Any, Literal, Union
from typing_extensions import NotRequired, Required, TypedDict
from pydantic import BaseModel, ConfigDict, Field, TypeAdapter


class FacebookPageIntelInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=False)

    page_id: Union[str, None] = Field(None, alias='pageId', description='Facebook advertiser/page ID. Use only a value returned by facebook_ad_search or copied from Ad Library.')
    library_id: Union[str, None] = Field(None, alias='libraryId', description='Facebook Ad Library archive ID. Use a value returned by facebook_ad_search, or a libraryId/adArchiveId visible in Ad Library.')
    query: Union[str, None] = Field(None, alias='query', description='Broad Ad Library keyword discovery when pageId/libraryId is not known. Results can mix unrelated advertisers; inspect matchConfidence, matchedAdvertisers, and warnings before analysis. One of pageId, libraryId, or query is required.')
    max_ads: Union[Annotated[int, Field(ge=1, le=200)], None] = Field(None, alias='maxAds', description='Maximum ads to inspect. Default 50, maximum 200.')
    country: Union[Annotated[str, Field(min_length=2, max_length=2)], None] = Field(None, alias='country', description='Two-letter Ad Library country code. Default US.')


FacebookPageIntelOutputVariant1MatchedAdvertisersItem = TypedDict('FacebookPageIntelOutputVariant1MatchedAdvertisersItem', {
    'name': Required[str],
    'adCount': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
})
FacebookPageIntelOutputVariant1MatchedAdvertisersItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


FacebookPageIntelOutputVariant1AdsItem = TypedDict('FacebookPageIntelOutputVariant1AdsItem', {
    'libraryId': Required[Union[str, None]],
    'status': Required[Union[str, None]],
    'creativeType': Required[Union[str, None]],
    'primaryText': Required[Union[str, None]],
    'headline': Required[Union[str, None]],
    'cta': Required[Union[str, None]],
    'startDate': Required[Union[str, None]],
    'landingUrl': Required[Union[str, None]],
    'domain': Required[Union[str, None]],
    'videoUrl': Required[Union[str, None]],
    'imageUrl': Required[Union[str, None]],
    'videoPoster': Required[Union[str, None]],
    'variations': Required[Union[Annotated[int, Field(ge=-9007199254740991, le=9007199254740991)], None]],
})
FacebookPageIntelOutputVariant1AdsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class FacebookPageIntelOutputVariant1(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    advertiser_name: Union[str, None] = Field(..., alias='advertiserName', description='')
    input_mode: Literal['pageId', 'libraryId', 'query'] = Field(..., alias='inputMode', description='')
    match_confidence: Literal['high', 'medium', 'low'] = Field(..., alias='matchConfidence', description='')
    match_reason: str = Field(..., alias='matchReason', description='')
    warnings: list[str] = Field(..., alias='warnings', description='')
    matched_advertisers: list[FacebookPageIntelOutputVariant1MatchedAdvertisersItem] = Field(..., alias='matchedAdvertisers', description='')
    total_ads: Annotated[int, Field(ge=0, le=9007199254740991)] = Field(..., alias='totalAds', description='')
    active_count: Annotated[int, Field(ge=0, le=9007199254740991)] = Field(..., alias='activeCount', description='')
    video_count: Annotated[int, Field(ge=0, le=9007199254740991)] = Field(..., alias='videoCount', description='')
    image_count: Annotated[int, Field(ge=0, le=9007199254740991)] = Field(..., alias='imageCount', description='')
    ads: list[FacebookPageIntelOutputVariant1AdsItem] = Field(..., alias='ads', description='')


FacebookPageIntelOutputVariant2DeliveryArtifactsItem = TypedDict('FacebookPageIntelOutputVariant2DeliveryArtifactsItem', {
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
FacebookPageIntelOutputVariant2DeliveryArtifactsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


FacebookPageIntelOutputVariant2DeliveryStorageFailureVariant1 = TypedDict('FacebookPageIntelOutputVariant2DeliveryStorageFailureVariant1', {
    'artifactId': Required[Union[str, None]],
    'outcome': Required[Literal['unknown', 'bytes-stored-metadata-pending', 'failed']],
})
FacebookPageIntelOutputVariant2DeliveryStorageFailureVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


FacebookPageIntelOutputVariant2Delivery = TypedDict('FacebookPageIntelOutputVariant2Delivery', {
    'mode': Required[Literal['artifact']],
    'status': Required[Literal['complete', 'partial', 'unavailable']],
    'retainedRepresentation': Required[Literal['formatted-tool-result']],
    'sourceIsError': Required[bool],
    'artifacts': Required[list[FacebookPageIntelOutputVariant2DeliveryArtifactsItem]],
    'downloadLinksOmitted': Required[bool],
    'scopeOmittedFields': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'storageFailure': Required[Union[FacebookPageIntelOutputVariant2DeliveryStorageFailureVariant1, None]],
    'nextAction': Required[str],
})
FacebookPageIntelOutputVariant2Delivery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


FacebookPageIntelOutputVariant2RecoveryOperation = TypedDict('FacebookPageIntelOutputVariant2RecoveryOperation', {
    'runId': Required[Union[Annotated[str, Field(max_length=200)], None]],
    'idempotencyKey': Required[Annotated[str, Field(max_length=512)]],
    'state': Required[Annotated[str, Field(max_length=100)]],
})
FacebookPageIntelOutputVariant2RecoveryOperation.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


FacebookPageIntelOutputVariant2Recovery = TypedDict('FacebookPageIntelOutputVariant2Recovery', {
    'idempotencyKey': NotRequired[Annotated[str, Field(max_length=512)]],
    'operationId': NotRequired[Annotated[str, Field(max_length=200)]],
    'runId': NotRequired[Annotated[str, Field(max_length=200)]],
    'jobId': NotRequired[Annotated[str, Field(max_length=200)]],
    'operation': NotRequired[FacebookPageIntelOutputVariant2RecoveryOperation],
})
FacebookPageIntelOutputVariant2Recovery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class FacebookPageIntelOutputVariant2(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    delivery: FacebookPageIntelOutputVariant2Delivery = Field(..., alias='delivery', description='')
    preview: str = Field(..., alias='preview', description='')
    scope: dict[str, Union[str, Union[float, int], bool, None]] = Field(..., alias='scope', description='')
    recovery: FacebookPageIntelOutputVariant2Recovery = Field(..., alias='recovery', description='')


# Union schema: validate external payloads with TypeAdapter(FacebookPageIntelOutput).
FacebookPageIntelOutput = Union[FacebookPageIntelOutputVariant1, FacebookPageIntelOutputVariant2]

_FacebookPageIntelInputAdapter = TypeAdapter(FacebookPageIntelInput)
_FacebookPageIntelOutputAdapter = TypeAdapter(FacebookPageIntelOutput)