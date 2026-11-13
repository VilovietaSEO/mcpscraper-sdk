from typing import Annotated, Any, Literal, Union
from typing_extensions import NotRequired, Required, TypedDict
from pydantic import BaseModel, ConfigDict, Field, TypeAdapter


class MapsSearchInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=False)

    query: Annotated[str, Field(min_length=1)] = Field(..., alias='query', description='Business category, niche, or search term, e.g. "roofers".')
    location: Union[str, None] = Field(None, alias='location', description='Enter a US state name or code, e.g. Utah or UT, for a state-targeted search. Omit for direct search.')
    gl: Union[Annotated[str, Field(min_length=2, max_length=2)], None] = Field(None, alias='gl', description='Google country code inferred from location.')
    hl: Union[Annotated[str, Field(min_length=2, max_length=2)], None] = Field(None, alias='hl', description='Language inferred from user request.')
    max_results: Union[Annotated[int, Field(ge=1, le=50)], None] = Field(None, alias='maxResults', description='Number of candidates to return. Default 10, maximum 50.')
    include_services: Union[bool, None] = Field(None, alias='includeServices', description='Open organic Businesses profiles for configured services and areas served. For more than three requested results, first click More businesses. Does not collect review cards; plain searches use the Google Maps feed.')


MapsSearchOutputVariant1ResultsItem = TypedDict('MapsSearchOutputVariant1ResultsItem', {
    'position': Required[Annotated[int, Field(ge=1, le=9007199254740991)]],
    'name': Required[str],
    'placeUrl': Required[str],
    'cid': Required[Union[str, None]],
    'cidDecimal': Required[Union[str, None]],
    'rating': Required[Union[str, None]],
    'reviewCount': Required[Union[str, None]],
    'category': Required[Union[str, None]],
    'address': Required[Union[str, None]],
    'phone': Required[Union[str, None]],
    'hoursStatus': Required[Union[str, None]],
    'websiteUrl': Required[Union[str, None]],
    'directionsUrl': Required[Union[str, None]],
    'metadata': Required[list[str]],
    'services': Required[list[str]],
    'areasServed': Required[list[str]],
    'profileDetailsStatus': Required[Literal['collected', 'none_exist', 'unavailable', 'not_requested']],
})
MapsSearchOutputVariant1ResultsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class MapsSearchOutputVariant1(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    query: str = Field(..., alias='query', description='')
    location: Union[str, None] = Field(..., alias='location', description='')
    search_query: str = Field(..., alias='searchQuery', description='')
    search_url: str = Field(..., alias='searchUrl', description='')
    extracted_at: str = Field(..., alias='extractedAt', description='')
    requested_max_results: Annotated[int, Field(ge=1, le=50)] = Field(..., alias='requestedMaxResults', description='')
    result_count: Annotated[int, Field(ge=0, le=50)] = Field(..., alias='resultCount', description='')
    results: list[MapsSearchOutputVariant1ResultsItem] = Field(..., alias='results', description='')
    duration_ms: Annotated[int, Field(ge=0, le=9007199254740991)] = Field(..., alias='durationMs', description='')


MapsSearchOutputVariant2DeliveryArtifactsItem = TypedDict('MapsSearchOutputVariant2DeliveryArtifactsItem', {
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
MapsSearchOutputVariant2DeliveryArtifactsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


MapsSearchOutputVariant2DeliveryAvailableExportsItem = TypedDict('MapsSearchOutputVariant2DeliveryAvailableExportsItem', {
    'artifactId': Required[str],
    'sourceArtifactId': Required[str],
    'filename': Required[Literal['result.md']],
    'contentType': Required[Literal['text/markdown; charset=utf-8']],
    'state': Required[Literal['on-demand']],
})
MapsSearchOutputVariant2DeliveryAvailableExportsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


MapsSearchOutputVariant2DeliveryStorageFailureVariant1 = TypedDict('MapsSearchOutputVariant2DeliveryStorageFailureVariant1', {
    'artifactId': Required[Union[str, None]],
    'outcome': Required[Literal['unknown', 'bytes-stored-metadata-pending', 'failed']],
})
MapsSearchOutputVariant2DeliveryStorageFailureVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


MapsSearchOutputVariant2Delivery = TypedDict('MapsSearchOutputVariant2Delivery', {
    'mode': Required[Literal['artifact']],
    'status': Required[Literal['complete', 'partial', 'unavailable']],
    'retainedRepresentation': Required[Literal['formatted-tool-result']],
    'sourceIsError': Required[bool],
    'artifacts': Required[list[MapsSearchOutputVariant2DeliveryArtifactsItem]],
    'availableExports': NotRequired[list[MapsSearchOutputVariant2DeliveryAvailableExportsItem]],
    'downloadLinksOmitted': Required[bool],
    'scopeOmittedFields': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'storageFailure': Required[Union[MapsSearchOutputVariant2DeliveryStorageFailureVariant1, None]],
    'nextAction': Required[str],
})
MapsSearchOutputVariant2Delivery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


MapsSearchOutputVariant2RecoveryOperation = TypedDict('MapsSearchOutputVariant2RecoveryOperation', {
    'runId': Required[Union[Annotated[str, Field(max_length=200)], None]],
    'idempotencyKey': Required[Annotated[str, Field(max_length=512)]],
    'state': Required[Annotated[str, Field(max_length=100)]],
})
MapsSearchOutputVariant2RecoveryOperation.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


MapsSearchOutputVariant2Recovery = TypedDict('MapsSearchOutputVariant2Recovery', {
    'idempotencyKey': NotRequired[Annotated[str, Field(max_length=512)]],
    'operationId': NotRequired[Annotated[str, Field(max_length=200)]],
    'runId': NotRequired[Annotated[str, Field(max_length=200)]],
    'jobId': NotRequired[Annotated[str, Field(max_length=200)]],
    'operation': NotRequired[MapsSearchOutputVariant2RecoveryOperation],
})
MapsSearchOutputVariant2Recovery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class MapsSearchOutputVariant2(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    delivery: MapsSearchOutputVariant2Delivery = Field(..., alias='delivery', description='')
    preview: str = Field(..., alias='preview', description='')
    scope: dict[str, Union[str, Union[float, int], bool, None]] = Field(..., alias='scope', description='')
    recovery: MapsSearchOutputVariant2Recovery = Field(..., alias='recovery', description='')


# Union schema: validate external payloads with TypeAdapter(MapsSearchOutput).
MapsSearchOutput = Union[MapsSearchOutputVariant1, MapsSearchOutputVariant2]

_MapsSearchInputAdapter = TypeAdapter(MapsSearchInput)
_MapsSearchOutputAdapter = TypeAdapter(MapsSearchOutput)