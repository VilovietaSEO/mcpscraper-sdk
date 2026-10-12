from typing import Annotated, Any, Literal, Union
from typing_extensions import NotRequired, Required, TypedDict
from pydantic import BaseModel, ConfigDict, Field, TypeAdapter


class GoogleAdsPageIntelInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=False)

    domain: Union[str, None] = Field(None, alias='domain', description="A website from google_ads_search.websites (e.g. getviktor.com). Preferred input: people know the website, not the advertiser's registered name. Resolves to whichever advertiser account runs ads for that domain.")
    advertiser_name: Union[str, None] = Field(None, alias='advertiserName', description='An advertiser name exactly as returned in google_ads_search.advertisers[].name (e.g. "PPS Plumbing Services"). Use when the user picked an advertiser rather than a website.')
    advertiser_id: Union[str, None] = Field(None, alias='advertiserId', description='Google Ads Transparency advertiser ID (starts with AR...). Only available if you already have one from a prior page-intel result — google_ads_search does NOT return advertiser IDs. Do not construct one yourself.')
    region: Union[Annotated[str, Field(min_length=2, max_length=2)], None] = Field(None, alias='region', description='Two-letter region code for where the ads are shown. Default US.')
    max_ads: Union[Annotated[int, Field(ge=1, le=200)], None] = Field(None, alias='maxAds', description='Maximum creatives to inspect and hydrate. Default 50, maximum 200. Prefer 25-50 for focused scans.')


GoogleAdsPageIntelOutputVariant1AdsItem = TypedDict('GoogleAdsPageIntelOutputVariant1AdsItem', {
    'creativeId': Required[Union[str, None]],
    'advertiserId': Required[Union[str, None]],
    'format': Required[Union[str, None]],
    'lastShown': Required[Union[str, None]],
    'detailUrl': Required[Union[str, None]],
    'landingDomain': Required[Union[str, None]],
    'imageUrls': Required[list[str]],
    'youtubeVideoId': Required[Union[str, None]],
    'videoUrl': Required[Union[str, None]],
    'variations': Required[Union[Annotated[int, Field(ge=-9007199254740991, le=9007199254740991)], None]],
})
GoogleAdsPageIntelOutputVariant1AdsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class GoogleAdsPageIntelOutputVariant1(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    advertiser_id: Union[str, None] = Field(..., alias='advertiserId', description='')
    advertiser_name: Union[str, None] = Field(..., alias='advertiserName', description='')
    domain: Union[str, None] = Field(..., alias='domain', description='')
    region: str = Field(..., alias='region', description='')
    total_creatives: Annotated[int, Field(ge=0, le=9007199254740991)] = Field(..., alias='totalCreatives', description='')
    video_count: Annotated[int, Field(ge=0, le=9007199254740991)] = Field(..., alias='videoCount', description='')
    image_count: Annotated[int, Field(ge=0, le=9007199254740991)] = Field(..., alias='imageCount', description='')
    text_count: Annotated[int, Field(ge=0, le=9007199254740991)] = Field(..., alias='textCount', description='')
    ads: list[GoogleAdsPageIntelOutputVariant1AdsItem] = Field(..., alias='ads', description='')


GoogleAdsPageIntelOutputVariant2DeliveryArtifactsItem = TypedDict('GoogleAdsPageIntelOutputVariant2DeliveryArtifactsItem', {
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
GoogleAdsPageIntelOutputVariant2DeliveryArtifactsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


GoogleAdsPageIntelOutputVariant2DeliveryStorageFailureVariant1 = TypedDict('GoogleAdsPageIntelOutputVariant2DeliveryStorageFailureVariant1', {
    'artifactId': Required[Union[str, None]],
    'outcome': Required[Literal['unknown', 'bytes-stored-metadata-pending', 'failed']],
})
GoogleAdsPageIntelOutputVariant2DeliveryStorageFailureVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


GoogleAdsPageIntelOutputVariant2Delivery = TypedDict('GoogleAdsPageIntelOutputVariant2Delivery', {
    'mode': Required[Literal['artifact']],
    'status': Required[Literal['complete', 'partial', 'unavailable']],
    'retainedRepresentation': Required[Literal['formatted-tool-result']],
    'sourceIsError': Required[bool],
    'artifacts': Required[list[GoogleAdsPageIntelOutputVariant2DeliveryArtifactsItem]],
    'downloadLinksOmitted': Required[bool],
    'scopeOmittedFields': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'storageFailure': Required[Union[GoogleAdsPageIntelOutputVariant2DeliveryStorageFailureVariant1, None]],
    'nextAction': Required[str],
})
GoogleAdsPageIntelOutputVariant2Delivery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


GoogleAdsPageIntelOutputVariant2RecoveryOperation = TypedDict('GoogleAdsPageIntelOutputVariant2RecoveryOperation', {
    'runId': Required[Union[Annotated[str, Field(max_length=200)], None]],
    'idempotencyKey': Required[Annotated[str, Field(max_length=512)]],
    'state': Required[Annotated[str, Field(max_length=100)]],
})
GoogleAdsPageIntelOutputVariant2RecoveryOperation.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


GoogleAdsPageIntelOutputVariant2Recovery = TypedDict('GoogleAdsPageIntelOutputVariant2Recovery', {
    'idempotencyKey': NotRequired[Annotated[str, Field(max_length=512)]],
    'operationId': NotRequired[Annotated[str, Field(max_length=200)]],
    'runId': NotRequired[Annotated[str, Field(max_length=200)]],
    'jobId': NotRequired[Annotated[str, Field(max_length=200)]],
    'operation': NotRequired[GoogleAdsPageIntelOutputVariant2RecoveryOperation],
})
GoogleAdsPageIntelOutputVariant2Recovery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class GoogleAdsPageIntelOutputVariant2(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    delivery: GoogleAdsPageIntelOutputVariant2Delivery = Field(..., alias='delivery', description='')
    preview: str = Field(..., alias='preview', description='')
    scope: dict[str, Union[str, Union[float, int], bool, None]] = Field(..., alias='scope', description='')
    recovery: GoogleAdsPageIntelOutputVariant2Recovery = Field(..., alias='recovery', description='')


# Union schema: validate external payloads with TypeAdapter(GoogleAdsPageIntelOutput).
GoogleAdsPageIntelOutput = Union[GoogleAdsPageIntelOutputVariant1, GoogleAdsPageIntelOutputVariant2]

_GoogleAdsPageIntelInputAdapter = TypeAdapter(GoogleAdsPageIntelInput)
_GoogleAdsPageIntelOutputAdapter = TypeAdapter(GoogleAdsPageIntelOutput)