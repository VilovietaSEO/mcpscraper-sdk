from typing import Annotated, Any, Literal, Union
from typing_extensions import NotRequired, Required, TypedDict
from pydantic import BaseModel, ConfigDict, Field, TypeAdapter


ExportSearchConsoleTableDataInputFiltersItem = TypedDict('ExportSearchConsoleTableDataInputFiltersItem', {
    'column': Required[Literal['id', 'provider_record_id', 'connection_id', 'site_url', 'permission_level', 'date', 'query', 'page', 'country', 'device', 'clicks', 'impressions', 'ctr', 'position', 'captured_at', 'content_hash', 'created_at', 'updated_at']],
    'op': Required[Literal['eq', 'neq', 'gt', 'gte', 'lt', 'lte', 'like', 'in']],
    'value': Required[Any],
})
ExportSearchConsoleTableDataInputFiltersItem.__pydantic_config__ = ConfigDict(extra="allow", strict=False)


ExportSearchConsoleTableDataInputSort = TypedDict('ExportSearchConsoleTableDataInputSort', {
    'column': Required[Literal['id', 'provider_record_id', 'connection_id', 'site_url', 'permission_level', 'date', 'query', 'page', 'country', 'device', 'clicks', 'impressions', 'ctr', 'position', 'captured_at', 'content_hash', 'created_at', 'updated_at']],
    'direction': NotRequired[Literal['asc', 'desc']],
})
ExportSearchConsoleTableDataInputSort.__pydantic_config__ = ConfigDict(extra="allow", strict=False)


class ExportSearchConsoleTableDataInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=False)

    table_name: str = Field(..., alias='tableName', description='Existing tenant-owned Search Console tableName returned by list_service_connections; confirm its columns with table-describe.')
    filters: Union[Annotated[list[ExportSearchConsoleTableDataInputFiltersItem], Field(max_length=20)], None] = Field(None, alias='filters', description='Optional filters to AND together before download. Use table-describe or the documented typed columns.')
    sort: Union[ExportSearchConsoleTableDataInputSort, None] = Field(None, alias='sort', description='Optional row ordering for the JSONL download.')
    max_rows: Union[Annotated[int, Field(ge=1, le=50000)], None] = Field(None, alias='maxRows', description='Maximum matching persisted rows to place in this artifact. Use filters to bound large tables.')


ExportSearchConsoleTableDataOutputVariant1ArtifactReadbackArguments = TypedDict('ExportSearchConsoleTableDataOutputVariant1ArtifactReadbackArguments', {
    'artifactId': Required[str],
    'offset': Required[Literal[0]],
    'maxBytes': Required[Literal[20000]],
})
ExportSearchConsoleTableDataOutputVariant1ArtifactReadbackArguments.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


ExportSearchConsoleTableDataOutputVariant1ArtifactReadback = TypedDict('ExportSearchConsoleTableDataOutputVariant1ArtifactReadback', {
    'tool': Required[Literal['report_artifact_read']],
    'arguments': Required[ExportSearchConsoleTableDataOutputVariant1ArtifactReadbackArguments],
    'continuation': Required[str],
})
ExportSearchConsoleTableDataOutputVariant1ArtifactReadback.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


ExportSearchConsoleTableDataOutputVariant1Artifact = TypedDict('ExportSearchConsoleTableDataOutputVariant1Artifact', {
    'artifactId': Required[str],
    'filename': Required[str],
    'contentType': Required[Literal['application/x-ndjson']],
    'bytes': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'sha256': Required[str],
    'expiresAt': Required[str],
    'downloadUrl': Required[Union[str, None]],
    'downloadUrlExpiresAt': Required[Union[str, None]],
    'readback': Required[ExportSearchConsoleTableDataOutputVariant1ArtifactReadback],
})
ExportSearchConsoleTableDataOutputVariant1Artifact.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class ExportSearchConsoleTableDataOutputVariant1(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    ok: bool = Field(..., alias='ok', description='')
    table_name: Union[str, None] = Field(None, alias='tableName', description='')
    rows_exported: Union[Annotated[int, Field(ge=0, le=9007199254740991)], None] = Field(None, alias='rowsExported', description='')
    matched_rows: Union[Annotated[int, Field(ge=0, le=9007199254740991)], None] = Field(None, alias='matchedRows', description='')
    complete: Union[bool, None] = Field(None, alias='complete', description='')
    artifact: Union[ExportSearchConsoleTableDataOutputVariant1Artifact, None] = Field(None, alias='artifact', description='')
    warnings: Union[list[str], None] = Field(None, alias='warnings', description='')
    error: Union[str, None] = Field(..., alias='error', description='')


ExportSearchConsoleTableDataOutputVariant2DeliveryArtifactsItem = TypedDict('ExportSearchConsoleTableDataOutputVariant2DeliveryArtifactsItem', {
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
ExportSearchConsoleTableDataOutputVariant2DeliveryArtifactsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


ExportSearchConsoleTableDataOutputVariant2DeliveryAvailableExportsItem = TypedDict('ExportSearchConsoleTableDataOutputVariant2DeliveryAvailableExportsItem', {
    'artifactId': Required[str],
    'sourceArtifactId': Required[str],
    'filename': Required[Literal['result.md']],
    'contentType': Required[Literal['text/markdown; charset=utf-8']],
    'state': Required[Literal['on-demand']],
})
ExportSearchConsoleTableDataOutputVariant2DeliveryAvailableExportsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


ExportSearchConsoleTableDataOutputVariant2DeliveryStorageFailureVariant1 = TypedDict('ExportSearchConsoleTableDataOutputVariant2DeliveryStorageFailureVariant1', {
    'artifactId': Required[Union[str, None]],
    'outcome': Required[Literal['unknown', 'bytes-stored-metadata-pending', 'failed']],
})
ExportSearchConsoleTableDataOutputVariant2DeliveryStorageFailureVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


ExportSearchConsoleTableDataOutputVariant2Delivery = TypedDict('ExportSearchConsoleTableDataOutputVariant2Delivery', {
    'mode': Required[Literal['artifact']],
    'status': Required[Literal['complete', 'partial', 'unavailable']],
    'retainedRepresentation': Required[Literal['formatted-tool-result']],
    'sourceIsError': Required[bool],
    'artifacts': Required[list[ExportSearchConsoleTableDataOutputVariant2DeliveryArtifactsItem]],
    'availableExports': NotRequired[list[ExportSearchConsoleTableDataOutputVariant2DeliveryAvailableExportsItem]],
    'downloadLinksOmitted': Required[bool],
    'scopeOmittedFields': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'storageFailure': Required[Union[ExportSearchConsoleTableDataOutputVariant2DeliveryStorageFailureVariant1, None]],
    'nextAction': Required[str],
})
ExportSearchConsoleTableDataOutputVariant2Delivery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


ExportSearchConsoleTableDataOutputVariant2RecoveryOperation = TypedDict('ExportSearchConsoleTableDataOutputVariant2RecoveryOperation', {
    'runId': Required[Union[Annotated[str, Field(max_length=200)], None]],
    'idempotencyKey': Required[Annotated[str, Field(max_length=512)]],
    'state': Required[Annotated[str, Field(max_length=100)]],
})
ExportSearchConsoleTableDataOutputVariant2RecoveryOperation.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


ExportSearchConsoleTableDataOutputVariant2Recovery = TypedDict('ExportSearchConsoleTableDataOutputVariant2Recovery', {
    'idempotencyKey': NotRequired[Annotated[str, Field(max_length=512)]],
    'operationId': NotRequired[Annotated[str, Field(max_length=200)]],
    'runId': NotRequired[Annotated[str, Field(max_length=200)]],
    'jobId': NotRequired[Annotated[str, Field(max_length=200)]],
    'operation': NotRequired[ExportSearchConsoleTableDataOutputVariant2RecoveryOperation],
})
ExportSearchConsoleTableDataOutputVariant2Recovery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class ExportSearchConsoleTableDataOutputVariant2(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    delivery: ExportSearchConsoleTableDataOutputVariant2Delivery = Field(..., alias='delivery', description='')
    preview: str = Field(..., alias='preview', description='')
    scope: dict[str, Union[str, Union[float, int], bool, None]] = Field(..., alias='scope', description='')
    recovery: ExportSearchConsoleTableDataOutputVariant2Recovery = Field(..., alias='recovery', description='')


# Union schema: validate external payloads with TypeAdapter(ExportSearchConsoleTableDataOutput).
ExportSearchConsoleTableDataOutput = Union[ExportSearchConsoleTableDataOutputVariant2, ExportSearchConsoleTableDataOutputVariant1]

_ExportSearchConsoleTableDataInputAdapter = TypeAdapter(ExportSearchConsoleTableDataInput)
_ExportSearchConsoleTableDataOutputAdapter = TypeAdapter(ExportSearchConsoleTableDataOutput)