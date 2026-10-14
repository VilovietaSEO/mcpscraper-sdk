from typing import Annotated, Any, Literal, Union
from typing_extensions import NotRequired, Required, TypedDict
from pydantic import BaseModel, ConfigDict, Field, TypeAdapter


class DirectoryWorkflowStatusInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=False)

    job_id: Annotated[str, Field(min_length=1)] = Field(..., alias='jobId', description='The jobId returned by directory_workflow. Poll until status is complete, partial, empty, or failed.')


DirectoryWorkflowStatusOutputVariant1CsvArtifactVariant1 = TypedDict('DirectoryWorkflowStatusOutputVariant1CsvArtifactVariant1', {
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
DirectoryWorkflowStatusOutputVariant1CsvArtifactVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


DirectoryWorkflowStatusOutputVariant1Progress = TypedDict('DirectoryWorkflowStatusOutputVariant1Progress', {
    'completedCities': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'totalCities': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'failedCities': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
})
DirectoryWorkflowStatusOutputVariant1Progress.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


DirectoryWorkflowStatusOutputVariant1Billing = TypedDict('DirectoryWorkflowStatusOutputVariant1Billing', {
    'heldMc': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'finalMc': Required[Union[Annotated[int, Field(ge=0, le=9007199254740991)], None]],
    'refundMc': Required[Union[Annotated[int, Field(ge=0, le=9007199254740991)], None]],
})
DirectoryWorkflowStatusOutputVariant1Billing.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


DirectoryWorkflowStatusOutputVariant1CitiesItemResultsItem = TypedDict('DirectoryWorkflowStatusOutputVariant1CitiesItemResultsItem', {
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
DirectoryWorkflowStatusOutputVariant1CitiesItemResultsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


DirectoryWorkflowStatusOutputVariant1CitiesItem = TypedDict('DirectoryWorkflowStatusOutputVariant1CitiesItem', {
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
    'results': Required[list[DirectoryWorkflowStatusOutputVariant1CitiesItemResultsItem]],
})
DirectoryWorkflowStatusOutputVariant1CitiesItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


DirectoryWorkflowStatusOutputVariant1Artifact = TypedDict('DirectoryWorkflowStatusOutputVariant1Artifact', {
    'artifactId': Required[str],
    'bytes': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'expiresAt': Required[str],
    'preview': Required[str],
})
DirectoryWorkflowStatusOutputVariant1Artifact.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class DirectoryWorkflowStatusOutputVariant1(BaseModel):
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
    csv_artifact: Union[DirectoryWorkflowStatusOutputVariant1CsvArtifactVariant1, None] = Field(..., alias='csvArtifact', description='')
    progress: DirectoryWorkflowStatusOutputVariant1Progress = Field(..., alias='progress', description='')
    billing: DirectoryWorkflowStatusOutputVariant1Billing = Field(..., alias='billing', description='')
    error_code: Union[str, None] = Field(..., alias='errorCode', description='')
    error: Union[str, None] = Field(..., alias='error', description='')
    retryable: Union[bool, None] = Field(..., alias='retryable', description='')
    cities: list[DirectoryWorkflowStatusOutputVariant1CitiesItem] = Field(..., alias='cities', description='')
    duration_ms: Annotated[int, Field(ge=0, le=9007199254740991)] = Field(..., alias='durationMs', description='')
    truncated_count: Union[Annotated[int, Field(ge=0, le=9007199254740991)], None] = Field(None, alias='truncatedCount', description='')
    artifact: Union[DirectoryWorkflowStatusOutputVariant1Artifact, None] = Field(None, alias='artifact', description='')


DirectoryWorkflowStatusOutputVariant2DeliveryArtifactsItem = TypedDict('DirectoryWorkflowStatusOutputVariant2DeliveryArtifactsItem', {
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
DirectoryWorkflowStatusOutputVariant2DeliveryArtifactsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


DirectoryWorkflowStatusOutputVariant2DeliveryStorageFailureVariant1 = TypedDict('DirectoryWorkflowStatusOutputVariant2DeliveryStorageFailureVariant1', {
    'artifactId': Required[Union[str, None]],
    'outcome': Required[Literal['unknown', 'bytes-stored-metadata-pending', 'failed']],
})
DirectoryWorkflowStatusOutputVariant2DeliveryStorageFailureVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


DirectoryWorkflowStatusOutputVariant2Delivery = TypedDict('DirectoryWorkflowStatusOutputVariant2Delivery', {
    'mode': Required[Literal['artifact']],
    'status': Required[Literal['complete', 'partial', 'unavailable']],
    'retainedRepresentation': Required[Literal['formatted-tool-result']],
    'sourceIsError': Required[bool],
    'artifacts': Required[list[DirectoryWorkflowStatusOutputVariant2DeliveryArtifactsItem]],
    'downloadLinksOmitted': Required[bool],
    'scopeOmittedFields': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'storageFailure': Required[Union[DirectoryWorkflowStatusOutputVariant2DeliveryStorageFailureVariant1, None]],
    'nextAction': Required[str],
})
DirectoryWorkflowStatusOutputVariant2Delivery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


DirectoryWorkflowStatusOutputVariant2RecoveryOperation = TypedDict('DirectoryWorkflowStatusOutputVariant2RecoveryOperation', {
    'runId': Required[Union[Annotated[str, Field(max_length=200)], None]],
    'idempotencyKey': Required[Annotated[str, Field(max_length=512)]],
    'state': Required[Annotated[str, Field(max_length=100)]],
})
DirectoryWorkflowStatusOutputVariant2RecoveryOperation.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


DirectoryWorkflowStatusOutputVariant2Recovery = TypedDict('DirectoryWorkflowStatusOutputVariant2Recovery', {
    'idempotencyKey': NotRequired[Annotated[str, Field(max_length=512)]],
    'operationId': NotRequired[Annotated[str, Field(max_length=200)]],
    'runId': NotRequired[Annotated[str, Field(max_length=200)]],
    'jobId': NotRequired[Annotated[str, Field(max_length=200)]],
    'operation': NotRequired[DirectoryWorkflowStatusOutputVariant2RecoveryOperation],
})
DirectoryWorkflowStatusOutputVariant2Recovery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class DirectoryWorkflowStatusOutputVariant2(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    delivery: DirectoryWorkflowStatusOutputVariant2Delivery = Field(..., alias='delivery', description='')
    preview: str = Field(..., alias='preview', description='')
    scope: dict[str, Union[str, Union[float, int], bool, None]] = Field(..., alias='scope', description='')
    recovery: DirectoryWorkflowStatusOutputVariant2Recovery = Field(..., alias='recovery', description='')


# Union schema: validate external payloads with TypeAdapter(DirectoryWorkflowStatusOutput).
DirectoryWorkflowStatusOutput = Union[DirectoryWorkflowStatusOutputVariant1, DirectoryWorkflowStatusOutputVariant2]

_DirectoryWorkflowStatusInputAdapter = TypeAdapter(DirectoryWorkflowStatusInput)
_DirectoryWorkflowStatusOutputAdapter = TypeAdapter(DirectoryWorkflowStatusOutput)