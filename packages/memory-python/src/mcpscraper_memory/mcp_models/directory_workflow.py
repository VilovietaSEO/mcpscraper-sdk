from typing import Annotated, Any, Literal, Union
from typing_extensions import NotRequired, Required, TypedDict
from pydantic import BaseModel, ConfigDict, Field, TypeAdapter


class DirectoryWorkflowInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=False)

    query: Annotated[str, Field(min_length=1)] = Field(..., alias='query', description='Business category, niche, or keyword to search on Google Maps for every market. Do not include the city.')
    idempotency_key: Annotated[str, Field(min_length=8, max_length=200)] = Field(..., alias='idempotencyKey', description='Required unique opaque ID for this intended directory job (a UUID is ideal). Reuse the same value only when retrying the same call after a timeout; use a new value for every intentional rerun. This prevents a lost response from creating or charging for a duplicate job.')
    state: Union[Annotated[str, Field(min_length=2)], None] = Field(None, alias='state', description='US state abbreviation or name used to select Census places, e.g. TN.')
    min_population: Union[Annotated[int, Field(ge=0, le=9007199254740991)], None] = Field(None, alias='minPopulation', description='Minimum Census place population for market selection.')
    population_year: Union[Annotated[int, Field(ge=2020, le=2025)], None] = Field(None, alias='populationYear', description='Census population estimate year (2020-2025 Population Estimates Program).')
    max_cities: Union[Annotated[int, Field(ge=1, le=100)], None] = Field(None, alias='maxCities', description='Maximum markets to process after sorting by population descending.')
    max_results_per_city: Union[Annotated[int, Field(ge=1, le=50)], None] = Field(None, alias='maxResultsPerCity', description='Google Maps candidates to collect per city.')
    concurrency: Union[Annotated[int, Field(ge=1, le=5)], None] = Field(None, alias='concurrency', description='City Maps searches to run in parallel.')
    include_zip_groups: Union[bool, None] = Field(None, alias='includeZipGroups', description='Attach ZIP and county groups from the active versioned hosted location dataset. Production never reads a server-local CSV.')
    save_csv: Union[bool, None] = Field(None, alias='saveCsv', description='Create a directory-ready CSV. Hosted runs return an owner-scoped artifact; local runs may also return a filesystem path.')
    background: Union[Literal[True], None] = Field(None, alias='background', description='Hosted MCP directory jobs always run durably in the background. Poll directory_workflow_status for progress, terminal billing, and the owner-scoped CSV artifact.')


DirectoryWorkflowOutputVariant1CsvArtifactVariant1 = TypedDict('DirectoryWorkflowOutputVariant1CsvArtifactVariant1', {
    'artifactId': Required[str],
    'filename': Required[str],
    'contentType': Required[str],
    'bytes': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'rowCount': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'sha256': Required[str],
    'expiresAt': Required[str],
    'downloadUrl': Required[Union[str, None]],
    'downloadUrlExpiresAt': Required[Union[str, None]],
})
DirectoryWorkflowOutputVariant1CsvArtifactVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


DirectoryWorkflowOutputVariant1Progress = TypedDict('DirectoryWorkflowOutputVariant1Progress', {
    'completedCities': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'totalCities': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'failedCities': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
})
DirectoryWorkflowOutputVariant1Progress.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


DirectoryWorkflowOutputVariant1Billing = TypedDict('DirectoryWorkflowOutputVariant1Billing', {
    'heldMc': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'finalMc': Required[Union[Annotated[int, Field(ge=0, le=9007199254740991)], None]],
    'refundMc': Required[Union[Annotated[int, Field(ge=0, le=9007199254740991)], None]],
})
DirectoryWorkflowOutputVariant1Billing.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


DirectoryWorkflowOutputVariant1CitiesItemResultsItem = TypedDict('DirectoryWorkflowOutputVariant1CitiesItemResultsItem', {
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
})
DirectoryWorkflowOutputVariant1CitiesItemResultsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


DirectoryWorkflowOutputVariant1CitiesItem = TypedDict('DirectoryWorkflowOutputVariant1CitiesItem', {
    'city': Required[str],
    'state': Required[str],
    'location': Required[str],
    'cityKey': Required[str],
    'censusName': Required[str],
    'population': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'populationYear': Required[Annotated[int, Field(ge=2020, le=2025)]],
    'zips': Required[list[str]],
    'counties': Required[list[str]],
    'status': Required[Literal['ok', 'empty', 'failed']],
    'error': Required[Union[str, None]],
    'errorCode': NotRequired[Union[str, None]],
    'retryable': NotRequired[bool],
    'resultCount': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'durationMs': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'results': Required[list[DirectoryWorkflowOutputVariant1CitiesItemResultsItem]],
})
DirectoryWorkflowOutputVariant1CitiesItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


DirectoryWorkflowOutputVariant1Artifact = TypedDict('DirectoryWorkflowOutputVariant1Artifact', {
    'artifactId': Required[str],
    'bytes': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'expiresAt': Required[str],
    'preview': Required[str],
})
DirectoryWorkflowOutputVariant1Artifact.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class DirectoryWorkflowOutputVariant1(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    job_id: Union[str, None] = Field(..., alias='jobId', description='')
    status: Literal['queued', 'running', 'complete', 'partial', 'empty', 'failed'] = Field(..., alias='status', description='')
    status_url: Union[str, None] = Field(..., alias='statusUrl', description='')
    query: str = Field(..., alias='query', description='')
    state: str = Field(..., alias='state', description='')
    min_population: Annotated[int, Field(ge=0, le=9007199254740991)] = Field(..., alias='minPopulation', description='')
    population_year: Annotated[int, Field(ge=2020, le=2025)] = Field(..., alias='populationYear', description='')
    max_results_per_city: Annotated[int, Field(ge=1, le=50)] = Field(..., alias='maxResultsPerCity', description='')
    concurrency: Annotated[int, Field(ge=1, le=5)] = Field(..., alias='concurrency', description='')
    census_source_url: str = Field(..., alias='censusSourceUrl', description='')
    us_zips_source_path: Union[str, None] = Field(..., alias='usZipsSourcePath', description='')
    warnings: list[str] = Field(..., alias='warnings', description='')
    extracted_at: str = Field(..., alias='extractedAt', description='')
    selected_city_count: Annotated[int, Field(ge=0, le=9007199254740991)] = Field(..., alias='selectedCityCount', description='')
    total_result_count: Annotated[int, Field(ge=0, le=9007199254740991)] = Field(..., alias='totalResultCount', description='')
    csv_path: Union[str, None] = Field(..., alias='csvPath', description='')
    csv_artifact: Union[DirectoryWorkflowOutputVariant1CsvArtifactVariant1, None] = Field(..., alias='csvArtifact', description='')
    progress: DirectoryWorkflowOutputVariant1Progress = Field(..., alias='progress', description='')
    billing: DirectoryWorkflowOutputVariant1Billing = Field(..., alias='billing', description='')
    error_code: Union[str, None] = Field(..., alias='errorCode', description='')
    error: Union[str, None] = Field(..., alias='error', description='')
    retryable: Union[bool, None] = Field(..., alias='retryable', description='')
    cities: list[DirectoryWorkflowOutputVariant1CitiesItem] = Field(..., alias='cities', description='')
    duration_ms: Annotated[int, Field(ge=0, le=9007199254740991)] = Field(..., alias='durationMs', description='')
    truncated_count: Union[Annotated[int, Field(ge=0, le=9007199254740991)], None] = Field(None, alias='truncatedCount', description='')
    artifact: Union[DirectoryWorkflowOutputVariant1Artifact, None] = Field(None, alias='artifact', description='')


DirectoryWorkflowOutputVariant2DeliveryArtifactsItem = TypedDict('DirectoryWorkflowOutputVariant2DeliveryArtifactsItem', {
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
DirectoryWorkflowOutputVariant2DeliveryArtifactsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


DirectoryWorkflowOutputVariant2DeliveryStorageFailureVariant1 = TypedDict('DirectoryWorkflowOutputVariant2DeliveryStorageFailureVariant1', {
    'artifactId': Required[Union[str, None]],
    'outcome': Required[Literal['unknown', 'bytes-stored-metadata-pending', 'failed']],
})
DirectoryWorkflowOutputVariant2DeliveryStorageFailureVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


DirectoryWorkflowOutputVariant2Delivery = TypedDict('DirectoryWorkflowOutputVariant2Delivery', {
    'mode': Required[Literal['artifact']],
    'status': Required[Literal['complete', 'partial', 'unavailable']],
    'retainedRepresentation': Required[Literal['formatted-tool-result']],
    'sourceIsError': Required[bool],
    'artifacts': Required[list[DirectoryWorkflowOutputVariant2DeliveryArtifactsItem]],
    'downloadLinksOmitted': Required[bool],
    'scopeOmittedFields': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'storageFailure': Required[Union[DirectoryWorkflowOutputVariant2DeliveryStorageFailureVariant1, None]],
    'nextAction': Required[str],
})
DirectoryWorkflowOutputVariant2Delivery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


DirectoryWorkflowOutputVariant2RecoveryOperation = TypedDict('DirectoryWorkflowOutputVariant2RecoveryOperation', {
    'runId': Required[Union[Annotated[str, Field(max_length=200)], None]],
    'idempotencyKey': Required[Annotated[str, Field(max_length=512)]],
    'state': Required[Annotated[str, Field(max_length=100)]],
})
DirectoryWorkflowOutputVariant2RecoveryOperation.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


DirectoryWorkflowOutputVariant2Recovery = TypedDict('DirectoryWorkflowOutputVariant2Recovery', {
    'idempotencyKey': NotRequired[Annotated[str, Field(max_length=512)]],
    'operationId': NotRequired[Annotated[str, Field(max_length=200)]],
    'runId': NotRequired[Annotated[str, Field(max_length=200)]],
    'jobId': NotRequired[Annotated[str, Field(max_length=200)]],
    'operation': NotRequired[DirectoryWorkflowOutputVariant2RecoveryOperation],
})
DirectoryWorkflowOutputVariant2Recovery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class DirectoryWorkflowOutputVariant2(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    delivery: DirectoryWorkflowOutputVariant2Delivery = Field(..., alias='delivery', description='')
    preview: str = Field(..., alias='preview', description='')
    scope: dict[str, Union[str, Union[float, int], bool, None]] = Field(..., alias='scope', description='')
    recovery: DirectoryWorkflowOutputVariant2Recovery = Field(..., alias='recovery', description='')


# Union schema: validate external payloads with TypeAdapter(DirectoryWorkflowOutput).
DirectoryWorkflowOutput = Union[DirectoryWorkflowOutputVariant1, DirectoryWorkflowOutputVariant2]

_DirectoryWorkflowInputAdapter = TypeAdapter(DirectoryWorkflowInput)
_DirectoryWorkflowOutputAdapter = TypeAdapter(DirectoryWorkflowOutput)