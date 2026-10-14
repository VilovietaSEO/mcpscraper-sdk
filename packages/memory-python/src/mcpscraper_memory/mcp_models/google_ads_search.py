from typing import Annotated, Any, Literal, Union
from typing_extensions import NotRequired, Required, TypedDict
from pydantic import BaseModel, ConfigDict, Field, TypeAdapter


class GoogleAdsSearchInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=False)

    query: Annotated[str, Field(min_length=1)] = Field(..., alias='query', description='A domain (e.g. getviktor.com) or advertiser/brand name to look up in Google Ads Transparency Center.')
    region: Union[Annotated[str, Field(min_length=2, max_length=2)], None] = Field(None, alias='region', description='Two-letter region code for where the ads are shown. Default US. Examples: US, CA, GB, AU.')
    max_results: Union[Annotated[int, Field(ge=1, le=20)], None] = Field(None, alias='maxResults', description='Maximum advertisers to return. Default 10, maximum 20.')


GoogleAdsSearchOutputVariant1AdvertisersItem = TypedDict('GoogleAdsSearchOutputVariant1AdvertisersItem', {
    'advertiserId': Required[Union[str, None]],
    'name': Required[Union[str, None]],
    'basedIn': Required[Union[str, None]],
    'domain': Required[Union[str, None]],
    'approxAdCount': Required[Union[Annotated[int, Field(ge=-9007199254740991, le=9007199254740991)], None]],
    'detailUrl': Required[Union[str, None]],
})
GoogleAdsSearchOutputVariant1AdvertisersItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


GoogleAdsSearchOutputVariant1WebsitesItem = TypedDict('GoogleAdsSearchOutputVariant1WebsitesItem', {
    'domain': Required[str],
    'detailUrl': Required[str],
})
GoogleAdsSearchOutputVariant1WebsitesItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class GoogleAdsSearchOutputVariant1(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    query: str = Field(..., alias='query', description='')
    region: str = Field(..., alias='region', description='')
    advertiser_count: Annotated[int, Field(ge=0, le=9007199254740991)] = Field(..., alias='advertiserCount', description='')
    advertisers: list[GoogleAdsSearchOutputVariant1AdvertisersItem] = Field(..., alias='advertisers', description='')
    website_count: Annotated[int, Field(ge=0, le=9007199254740991)] = Field(..., alias='websiteCount', description='')
    websites: list[GoogleAdsSearchOutputVariant1WebsitesItem] = Field(..., alias='websites', description='')


GoogleAdsSearchOutputVariant2DeliveryArtifactsItem = TypedDict('GoogleAdsSearchOutputVariant2DeliveryArtifactsItem', {
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
GoogleAdsSearchOutputVariant2DeliveryArtifactsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


GoogleAdsSearchOutputVariant2DeliveryStorageFailureVariant1 = TypedDict('GoogleAdsSearchOutputVariant2DeliveryStorageFailureVariant1', {
    'artifactId': Required[Union[str, None]],
    'outcome': Required[Literal['unknown', 'bytes-stored-metadata-pending', 'failed']],
})
GoogleAdsSearchOutputVariant2DeliveryStorageFailureVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


GoogleAdsSearchOutputVariant2Delivery = TypedDict('GoogleAdsSearchOutputVariant2Delivery', {
    'mode': Required[Literal['artifact']],
    'status': Required[Literal['complete', 'partial', 'unavailable']],
    'retainedRepresentation': Required[Literal['formatted-tool-result']],
    'sourceIsError': Required[bool],
    'artifacts': Required[list[GoogleAdsSearchOutputVariant2DeliveryArtifactsItem]],
    'downloadLinksOmitted': Required[bool],
    'scopeOmittedFields': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'storageFailure': Required[Union[GoogleAdsSearchOutputVariant2DeliveryStorageFailureVariant1, None]],
    'nextAction': Required[str],
})
GoogleAdsSearchOutputVariant2Delivery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


GoogleAdsSearchOutputVariant2RecoveryOperation = TypedDict('GoogleAdsSearchOutputVariant2RecoveryOperation', {
    'runId': Required[Union[Annotated[str, Field(max_length=200)], None]],
    'idempotencyKey': Required[Annotated[str, Field(max_length=512)]],
    'state': Required[Annotated[str, Field(max_length=100)]],
})
GoogleAdsSearchOutputVariant2RecoveryOperation.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


GoogleAdsSearchOutputVariant2Recovery = TypedDict('GoogleAdsSearchOutputVariant2Recovery', {
    'idempotencyKey': NotRequired[Annotated[str, Field(max_length=512)]],
    'operationId': NotRequired[Annotated[str, Field(max_length=200)]],
    'runId': NotRequired[Annotated[str, Field(max_length=200)]],
    'jobId': NotRequired[Annotated[str, Field(max_length=200)]],
    'operation': NotRequired[GoogleAdsSearchOutputVariant2RecoveryOperation],
})
GoogleAdsSearchOutputVariant2Recovery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class GoogleAdsSearchOutputVariant2(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    delivery: GoogleAdsSearchOutputVariant2Delivery = Field(..., alias='delivery', description='')
    preview: str = Field(..., alias='preview', description='')
    scope: dict[str, Union[str, Union[float, int], bool, None]] = Field(..., alias='scope', description='')
    recovery: GoogleAdsSearchOutputVariant2Recovery = Field(..., alias='recovery', description='')


# Union schema: validate external payloads with TypeAdapter(GoogleAdsSearchOutput).
GoogleAdsSearchOutput = Union[GoogleAdsSearchOutputVariant1, GoogleAdsSearchOutputVariant2]

_GoogleAdsSearchInputAdapter = TypeAdapter(GoogleAdsSearchInput)
_GoogleAdsSearchOutputAdapter = TypeAdapter(GoogleAdsSearchOutput)