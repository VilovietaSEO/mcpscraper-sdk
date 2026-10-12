from typing import Annotated, Any, Literal, Union
from typing_extensions import NotRequired, Required, TypedDict
from pydantic import BaseModel, ConfigDict, Field, TypeAdapter


class TableDescribeInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=False)

    table_name: Annotated[str, Field(min_length=1)] = Field(..., alias='tableName', description='Table name, from table-list.')


TableDescribeOutputVariant1ColumnsItem = TypedDict('TableDescribeOutputVariant1ColumnsItem', {
    'name': Required[str],
    'type': Required[str],
})
TableDescribeOutputVariant1ColumnsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class TableDescribeOutputVariant1(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    ok: bool = Field(..., alias='ok', description='True on success; false on auth or not-found error.')
    table_name: Union[str, None] = Field(None, alias='tableName', description='The table name.')
    columns: Union[list[TableDescribeOutputVariant1ColumnsItem], None] = Field(None, alias='columns', description='Column names and their Postgres types, in table order.')
    error: Union[str, None] = Field(None, alias='error', description='Human-readable failure reason when ok is false.')


TableDescribeOutputVariant2DeliveryArtifactsItem = TypedDict('TableDescribeOutputVariant2DeliveryArtifactsItem', {
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
TableDescribeOutputVariant2DeliveryArtifactsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


TableDescribeOutputVariant2DeliveryStorageFailureVariant1 = TypedDict('TableDescribeOutputVariant2DeliveryStorageFailureVariant1', {
    'artifactId': Required[Union[str, None]],
    'outcome': Required[Literal['unknown', 'bytes-stored-metadata-pending', 'failed']],
})
TableDescribeOutputVariant2DeliveryStorageFailureVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


TableDescribeOutputVariant2Delivery = TypedDict('TableDescribeOutputVariant2Delivery', {
    'mode': Required[Literal['artifact']],
    'status': Required[Literal['complete', 'partial', 'unavailable']],
    'retainedRepresentation': Required[Literal['formatted-tool-result']],
    'sourceIsError': Required[bool],
    'artifacts': Required[list[TableDescribeOutputVariant2DeliveryArtifactsItem]],
    'downloadLinksOmitted': Required[bool],
    'scopeOmittedFields': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'storageFailure': Required[Union[TableDescribeOutputVariant2DeliveryStorageFailureVariant1, None]],
    'nextAction': Required[str],
})
TableDescribeOutputVariant2Delivery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


TableDescribeOutputVariant2RecoveryOperation = TypedDict('TableDescribeOutputVariant2RecoveryOperation', {
    'runId': Required[Union[Annotated[str, Field(max_length=200)], None]],
    'idempotencyKey': Required[Annotated[str, Field(max_length=512)]],
    'state': Required[Annotated[str, Field(max_length=100)]],
})
TableDescribeOutputVariant2RecoveryOperation.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


TableDescribeOutputVariant2Recovery = TypedDict('TableDescribeOutputVariant2Recovery', {
    'idempotencyKey': NotRequired[Annotated[str, Field(max_length=512)]],
    'operationId': NotRequired[Annotated[str, Field(max_length=200)]],
    'runId': NotRequired[Annotated[str, Field(max_length=200)]],
    'jobId': NotRequired[Annotated[str, Field(max_length=200)]],
    'operation': NotRequired[TableDescribeOutputVariant2RecoveryOperation],
})
TableDescribeOutputVariant2Recovery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class TableDescribeOutputVariant2(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    delivery: TableDescribeOutputVariant2Delivery = Field(..., alias='delivery', description='')
    preview: str = Field(..., alias='preview', description='')
    scope: dict[str, Union[str, Union[float, int], bool, None]] = Field(..., alias='scope', description='')
    recovery: TableDescribeOutputVariant2Recovery = Field(..., alias='recovery', description='')


# Union schema: validate external payloads with TypeAdapter(TableDescribeOutput).
TableDescribeOutput = Union[TableDescribeOutputVariant2, TableDescribeOutputVariant1]

_TableDescribeInputAdapter = TypeAdapter(TableDescribeInput)
_TableDescribeOutputAdapter = TypeAdapter(TableDescribeOutput)