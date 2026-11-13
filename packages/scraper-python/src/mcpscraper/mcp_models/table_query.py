from typing import Annotated, Any, Literal, Union
from typing_extensions import NotRequired, Required, TypedDict
from pydantic import BaseModel, ConfigDict, Field, TypeAdapter


TableQueryInputFiltersItem = TypedDict('TableQueryInputFiltersItem', {
    'column': Required[str],
    'op': Required[Literal['eq', 'neq', 'gt', 'gte', 'lt', 'lte', 'like', 'in']],
    'value': Required[Any],
})
TableQueryInputFiltersItem.__pydantic_config__ = ConfigDict(extra="allow", strict=False)


TableQueryInputSort = TypedDict('TableQueryInputSort', {
    'column': Required[str],
    'direction': NotRequired[Literal['asc', 'desc']],
})
TableQueryInputSort.__pydantic_config__ = ConfigDict(extra="allow", strict=False)


class TableQueryInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=False)

    table_name: Annotated[str, Field(min_length=1)] = Field(..., alias='tableName', description='Table name, from table-list.')
    filters: Union[list[TableQueryInputFiltersItem], None] = Field(None, alias='filters', description='Filters to AND together. Optional; omit to match every row.')
    sort: Union[TableQueryInputSort, None] = Field(None, alias='sort', description='Column to sort by. Optional; defaults to id ascending (insertion order).')
    limit: Union[Annotated[int, Field(ge=1, le=2000)], None] = Field(None, alias='limit', description='Max rows to return. Optional; default 100, max 2000.')
    offset: Union[Annotated[int, Field(ge=0, le=9007199254740991)], None] = Field(None, alias='offset', description='Rows to skip, for pagination. Optional; default 0.')


class TableQueryOutputVariant1(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    ok: bool = Field(..., alias='ok', description='True on success; false on auth/validation error.')
    table_name: Union[str, None] = Field(None, alias='tableName', description='The table name.')
    rows: Union[list[dict[str, Any]], None] = Field(None, alias='rows', description='Matching rows, each an object of column name to value.')
    count: Union[Union[float, int], None] = Field(None, alias='count', description='Total rows matching the filters, before limit/offset — use for pagination.')
    error: Union[str, None] = Field(None, alias='error', description='Human-readable failure reason when ok is false.')


TableQueryOutputVariant2DeliveryArtifactsItem = TypedDict('TableQueryOutputVariant2DeliveryArtifactsItem', {
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
TableQueryOutputVariant2DeliveryArtifactsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


TableQueryOutputVariant2DeliveryAvailableExportsItem = TypedDict('TableQueryOutputVariant2DeliveryAvailableExportsItem', {
    'artifactId': Required[str],
    'sourceArtifactId': Required[str],
    'filename': Required[Literal['result.md']],
    'contentType': Required[Literal['text/markdown; charset=utf-8']],
    'state': Required[Literal['on-demand']],
})
TableQueryOutputVariant2DeliveryAvailableExportsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


TableQueryOutputVariant2DeliveryStorageFailureVariant1 = TypedDict('TableQueryOutputVariant2DeliveryStorageFailureVariant1', {
    'artifactId': Required[Union[str, None]],
    'outcome': Required[Literal['unknown', 'bytes-stored-metadata-pending', 'failed']],
})
TableQueryOutputVariant2DeliveryStorageFailureVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


TableQueryOutputVariant2Delivery = TypedDict('TableQueryOutputVariant2Delivery', {
    'mode': Required[Literal['artifact']],
    'status': Required[Literal['complete', 'partial', 'unavailable']],
    'retainedRepresentation': Required[Literal['formatted-tool-result']],
    'sourceIsError': Required[bool],
    'artifacts': Required[list[TableQueryOutputVariant2DeliveryArtifactsItem]],
    'availableExports': NotRequired[list[TableQueryOutputVariant2DeliveryAvailableExportsItem]],
    'downloadLinksOmitted': Required[bool],
    'scopeOmittedFields': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'storageFailure': Required[Union[TableQueryOutputVariant2DeliveryStorageFailureVariant1, None]],
    'nextAction': Required[str],
})
TableQueryOutputVariant2Delivery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


TableQueryOutputVariant2RecoveryOperation = TypedDict('TableQueryOutputVariant2RecoveryOperation', {
    'runId': Required[Union[Annotated[str, Field(max_length=200)], None]],
    'idempotencyKey': Required[Annotated[str, Field(max_length=512)]],
    'state': Required[Annotated[str, Field(max_length=100)]],
})
TableQueryOutputVariant2RecoveryOperation.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


TableQueryOutputVariant2Recovery = TypedDict('TableQueryOutputVariant2Recovery', {
    'idempotencyKey': NotRequired[Annotated[str, Field(max_length=512)]],
    'operationId': NotRequired[Annotated[str, Field(max_length=200)]],
    'runId': NotRequired[Annotated[str, Field(max_length=200)]],
    'jobId': NotRequired[Annotated[str, Field(max_length=200)]],
    'operation': NotRequired[TableQueryOutputVariant2RecoveryOperation],
})
TableQueryOutputVariant2Recovery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class TableQueryOutputVariant2(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    delivery: TableQueryOutputVariant2Delivery = Field(..., alias='delivery', description='')
    preview: str = Field(..., alias='preview', description='')
    scope: dict[str, Union[str, Union[float, int], bool, None]] = Field(..., alias='scope', description='')
    recovery: TableQueryOutputVariant2Recovery = Field(..., alias='recovery', description='')


# Union schema: validate external payloads with TypeAdapter(TableQueryOutput).
TableQueryOutput = Union[TableQueryOutputVariant2, TableQueryOutputVariant1]

_TableQueryInputAdapter = TypeAdapter(TableQueryInput)
_TableQueryOutputAdapter = TypeAdapter(TableQueryOutput)