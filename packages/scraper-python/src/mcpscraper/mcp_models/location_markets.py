from typing import Annotated, Any, Literal, Union
from typing_extensions import NotRequired, Required, TypedDict
from pydantic import BaseModel, ConfigDict, Field, TypeAdapter


class LocationMarketsInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=False)

    state: Union[Annotated[str, Field(min_length=2)], None] = Field(None, alias='state', description='US state abbreviation or full name, e.g. TN or Tennessee.')
    city: Union[Annotated[str, Field(min_length=1)], None] = Field(None, alias='city', description='Optional city-name filter, matched case-insensitively before the result limit.')
    zip: Union[str, None] = Field(None, alias='zip', description='Optional exact five-digit ZIP filter.')
    min_population: Union[Annotated[int, Field(ge=0, le=9007199254740991)], None] = Field(None, alias='minPopulation', description='Minimum hosted Census place population.')
    population_year: Union[Annotated[int, Field(ge=2020, le=2025)], None] = Field(None, alias='populationYear', description='Population estimate year from the hosted Census snapshot.')
    max_results: Union[Annotated[int, Field(ge=1, le=100)], None] = Field(None, alias='maxResults', description='Maximum markets to return, sorted by population descending.')
    include_zip_groups: Union[bool, None] = Field(None, alias='includeZipGroups', description='Include ZIP and county groups from the active hosted ZIP dataset.')


LocationMarketsOutputVariant1MarketsItem = TypedDict('LocationMarketsOutputVariant1MarketsItem', {
    'city': Required[str],
    'state': Required[str],
    'location': Required[str],
    'cityKey': Required[str],
    'censusName': Required[str],
    'population': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'populationYear': Required[Annotated[int, Field(ge=2020, le=2025)]],
    'estimatesBase2020': Required[Union[Annotated[int, Field(ge=0, le=9007199254740991)], None]],
    'zips': Required[list[str]],
    'counties': Required[list[str]],
})
LocationMarketsOutputVariant1MarketsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


LocationMarketsOutputVariant1SourcesProvenanceVariant1PopulationVariant1 = TypedDict('LocationMarketsOutputVariant1SourcesProvenanceVariant1PopulationVariant1', {
    'datasetId': Required[str],
    'sourceUrl': Required[Union[str, None]],
    'updatedAt': Required[Union[str, None]],
})
LocationMarketsOutputVariant1SourcesProvenanceVariant1PopulationVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


LocationMarketsOutputVariant1SourcesProvenanceVariant1ZipGroupsVariant1 = TypedDict('LocationMarketsOutputVariant1SourcesProvenanceVariant1ZipGroupsVariant1', {
    'datasetId': Required[str],
    'sourceUrl': Required[Union[str, None]],
    'updatedAt': Required[Union[str, None]],
})
LocationMarketsOutputVariant1SourcesProvenanceVariant1ZipGroupsVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


LocationMarketsOutputVariant1SourcesProvenanceVariant1 = TypedDict('LocationMarketsOutputVariant1SourcesProvenanceVariant1', {
    'population': Required[Union[LocationMarketsOutputVariant1SourcesProvenanceVariant1PopulationVariant1, None]],
    'zipGroups': Required[Union[LocationMarketsOutputVariant1SourcesProvenanceVariant1ZipGroupsVariant1, None]],
})
LocationMarketsOutputVariant1SourcesProvenanceVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


LocationMarketsOutputVariant1Sources = TypedDict('LocationMarketsOutputVariant1Sources', {
    'census': Required[str],
    'zipGroups': Required[Union[str, None]],
    'locationDataSource': Required[Literal['hosted', 'local', 'none']],
    'locationDataVersion': Required[Union[str, None]],
    'locationDataUpdatedAt': Required[Union[str, None]],
    'provenance': Required[Union[LocationMarketsOutputVariant1SourcesProvenanceVariant1, None]],
})
LocationMarketsOutputVariant1Sources.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class LocationMarketsOutputVariant1(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    state: str = Field(..., alias='state', description='')
    city: Union[str, None] = Field(..., alias='city', description='')
    zip: Union[str, None] = Field(..., alias='zip', description='')
    min_population: Annotated[int, Field(ge=0, le=9007199254740991)] = Field(..., alias='minPopulation', description='')
    population_year: Annotated[int, Field(ge=2020, le=2025)] = Field(..., alias='populationYear', description='')
    max_results: Annotated[int, Field(ge=1, le=100)] = Field(..., alias='maxResults', description='')
    count: Annotated[int, Field(ge=0, le=9007199254740991)] = Field(..., alias='count', description='')
    markets: list[LocationMarketsOutputVariant1MarketsItem] = Field(..., alias='markets', description='')
    sources: LocationMarketsOutputVariant1Sources = Field(..., alias='sources', description='')
    warnings: list[str] = Field(..., alias='warnings', description='')


LocationMarketsOutputVariant2DeliveryArtifactsItem = TypedDict('LocationMarketsOutputVariant2DeliveryArtifactsItem', {
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
LocationMarketsOutputVariant2DeliveryArtifactsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


LocationMarketsOutputVariant2DeliveryAvailableExportsItem = TypedDict('LocationMarketsOutputVariant2DeliveryAvailableExportsItem', {
    'artifactId': Required[str],
    'sourceArtifactId': Required[str],
    'filename': Required[Literal['result.md']],
    'contentType': Required[Literal['text/markdown; charset=utf-8']],
    'state': Required[Literal['on-demand']],
})
LocationMarketsOutputVariant2DeliveryAvailableExportsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


LocationMarketsOutputVariant2DeliveryStorageFailureVariant1 = TypedDict('LocationMarketsOutputVariant2DeliveryStorageFailureVariant1', {
    'artifactId': Required[Union[str, None]],
    'outcome': Required[Literal['unknown', 'bytes-stored-metadata-pending', 'failed']],
})
LocationMarketsOutputVariant2DeliveryStorageFailureVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


LocationMarketsOutputVariant2Delivery = TypedDict('LocationMarketsOutputVariant2Delivery', {
    'mode': Required[Literal['artifact']],
    'status': Required[Literal['complete', 'partial', 'unavailable']],
    'retainedRepresentation': Required[Literal['formatted-tool-result']],
    'sourceIsError': Required[bool],
    'artifacts': Required[list[LocationMarketsOutputVariant2DeliveryArtifactsItem]],
    'availableExports': NotRequired[list[LocationMarketsOutputVariant2DeliveryAvailableExportsItem]],
    'downloadLinksOmitted': Required[bool],
    'scopeOmittedFields': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'storageFailure': Required[Union[LocationMarketsOutputVariant2DeliveryStorageFailureVariant1, None]],
    'nextAction': Required[str],
})
LocationMarketsOutputVariant2Delivery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


LocationMarketsOutputVariant2RecoveryOperation = TypedDict('LocationMarketsOutputVariant2RecoveryOperation', {
    'runId': Required[Union[Annotated[str, Field(max_length=200)], None]],
    'idempotencyKey': Required[Annotated[str, Field(max_length=512)]],
    'state': Required[Annotated[str, Field(max_length=100)]],
})
LocationMarketsOutputVariant2RecoveryOperation.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


LocationMarketsOutputVariant2Recovery = TypedDict('LocationMarketsOutputVariant2Recovery', {
    'idempotencyKey': NotRequired[Annotated[str, Field(max_length=512)]],
    'operationId': NotRequired[Annotated[str, Field(max_length=200)]],
    'runId': NotRequired[Annotated[str, Field(max_length=200)]],
    'jobId': NotRequired[Annotated[str, Field(max_length=200)]],
    'operation': NotRequired[LocationMarketsOutputVariant2RecoveryOperation],
})
LocationMarketsOutputVariant2Recovery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class LocationMarketsOutputVariant2(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    delivery: LocationMarketsOutputVariant2Delivery = Field(..., alias='delivery', description='')
    preview: str = Field(..., alias='preview', description='')
    scope: dict[str, Union[str, Union[float, int], bool, None]] = Field(..., alias='scope', description='')
    recovery: LocationMarketsOutputVariant2Recovery = Field(..., alias='recovery', description='')


# Union schema: validate external payloads with TypeAdapter(LocationMarketsOutput).
LocationMarketsOutput = Union[LocationMarketsOutputVariant1, LocationMarketsOutputVariant2]

_LocationMarketsInputAdapter = TypeAdapter(LocationMarketsInput)
_LocationMarketsOutputAdapter = TypeAdapter(LocationMarketsOutput)