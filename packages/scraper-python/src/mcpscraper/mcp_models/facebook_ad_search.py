from typing import Annotated, Any, Literal, Union
from typing_extensions import NotRequired, Required, TypedDict
from pydantic import BaseModel, ConfigDict, Field, TypeAdapter


class FacebookAdSearchInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=False)

    query: Annotated[str, Field(min_length=1)] = Field(..., alias='query', description='Advertiser, brand, competitor, niche, or keyword to search in Facebook Ad Library.')
    country: Union[Annotated[str, Field(min_length=2, max_length=2)], None] = Field(None, alias='country', description='Two-letter Ad Library country code. Default US. Examples: US, CA, GB, AU.')
    max_results: Union[Annotated[int, Field(ge=1, le=20)], None] = Field(None, alias='maxResults', description='Maximum advertisers to return. Default 10, maximum 20. Prefer tighter search terms over maxing this out.')


FacebookAdSearchOutputVariant1AdvertisersItem = TypedDict('FacebookAdSearchOutputVariant1AdvertisersItem', {
    'name': Required[Union[str, None]],
    'pageId': Required[Union[str, None]],
    'pageUrl': Required[Union[str, None]],
    'adCount': Required[Union[Annotated[int, Field(ge=-9007199254740991, le=9007199254740991)], None]],
    'libraryId': Required[Union[str, None]],
    'sampleLibraryId': Required[Union[str, None]],
})
FacebookAdSearchOutputVariant1AdvertisersItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class FacebookAdSearchOutputVariant1(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    query: str = Field(..., alias='query', description='')
    advertiser_count: Annotated[int, Field(ge=0, le=9007199254740991)] = Field(..., alias='advertiserCount', description='')
    advertisers: list[FacebookAdSearchOutputVariant1AdvertisersItem] = Field(..., alias='advertisers', description='')


FacebookAdSearchOutputVariant2DeliveryArtifactsItem = TypedDict('FacebookAdSearchOutputVariant2DeliveryArtifactsItem', {
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
FacebookAdSearchOutputVariant2DeliveryArtifactsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


FacebookAdSearchOutputVariant2DeliveryAvailableExportsItem = TypedDict('FacebookAdSearchOutputVariant2DeliveryAvailableExportsItem', {
    'artifactId': Required[str],
    'sourceArtifactId': Required[str],
    'filename': Required[Literal['result.md']],
    'contentType': Required[Literal['text/markdown; charset=utf-8']],
    'state': Required[Literal['on-demand']],
})
FacebookAdSearchOutputVariant2DeliveryAvailableExportsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


FacebookAdSearchOutputVariant2DeliveryStorageFailureVariant1 = TypedDict('FacebookAdSearchOutputVariant2DeliveryStorageFailureVariant1', {
    'artifactId': Required[Union[str, None]],
    'outcome': Required[Literal['unknown', 'bytes-stored-metadata-pending', 'failed']],
})
FacebookAdSearchOutputVariant2DeliveryStorageFailureVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


FacebookAdSearchOutputVariant2Delivery = TypedDict('FacebookAdSearchOutputVariant2Delivery', {
    'mode': Required[Literal['artifact']],
    'status': Required[Literal['complete', 'partial', 'unavailable']],
    'retainedRepresentation': Required[Literal['formatted-tool-result']],
    'sourceIsError': Required[bool],
    'artifacts': Required[list[FacebookAdSearchOutputVariant2DeliveryArtifactsItem]],
    'availableExports': NotRequired[list[FacebookAdSearchOutputVariant2DeliveryAvailableExportsItem]],
    'downloadLinksOmitted': Required[bool],
    'scopeOmittedFields': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'storageFailure': Required[Union[FacebookAdSearchOutputVariant2DeliveryStorageFailureVariant1, None]],
    'nextAction': Required[str],
})
FacebookAdSearchOutputVariant2Delivery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


FacebookAdSearchOutputVariant2RecoveryOperation = TypedDict('FacebookAdSearchOutputVariant2RecoveryOperation', {
    'runId': Required[Union[Annotated[str, Field(max_length=200)], None]],
    'idempotencyKey': Required[Annotated[str, Field(max_length=512)]],
    'state': Required[Annotated[str, Field(max_length=100)]],
})
FacebookAdSearchOutputVariant2RecoveryOperation.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


FacebookAdSearchOutputVariant2Recovery = TypedDict('FacebookAdSearchOutputVariant2Recovery', {
    'idempotencyKey': NotRequired[Annotated[str, Field(max_length=512)]],
    'operationId': NotRequired[Annotated[str, Field(max_length=200)]],
    'runId': NotRequired[Annotated[str, Field(max_length=200)]],
    'jobId': NotRequired[Annotated[str, Field(max_length=200)]],
    'operation': NotRequired[FacebookAdSearchOutputVariant2RecoveryOperation],
})
FacebookAdSearchOutputVariant2Recovery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class FacebookAdSearchOutputVariant2(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    delivery: FacebookAdSearchOutputVariant2Delivery = Field(..., alias='delivery', description='')
    preview: str = Field(..., alias='preview', description='')
    scope: dict[str, Union[str, Union[float, int], bool, None]] = Field(..., alias='scope', description='')
    recovery: FacebookAdSearchOutputVariant2Recovery = Field(..., alias='recovery', description='')


# Union schema: validate external payloads with TypeAdapter(FacebookAdSearchOutput).
FacebookAdSearchOutput = Union[FacebookAdSearchOutputVariant2, FacebookAdSearchOutputVariant1]

_FacebookAdSearchInputAdapter = TypeAdapter(FacebookAdSearchInput)
_FacebookAdSearchOutputAdapter = TypeAdapter(FacebookAdSearchOutput)