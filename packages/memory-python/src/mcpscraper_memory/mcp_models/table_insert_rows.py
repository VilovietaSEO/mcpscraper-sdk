from typing import Annotated, Any, Literal, Union
from typing_extensions import NotRequired, Required, TypedDict
from pydantic import BaseModel, ConfigDict, Field, TypeAdapter


class TableInsertRowsInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=False)

    table_name: Annotated[str, Field(min_length=1)] = Field(..., alias='tableName', description='Table name, from table-list.')
    rows: Annotated[list[dict[str, Any]], Field(min_length=1, max_length=500)] = Field(..., alias='rows', description='Rows to insert, each an object of column name to value.')


class TableInsertRowsOutputVariant1(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    ok: bool = Field(..., alias='ok', description='True on success; false on auth/scope/validation error.')
    inserted: Union[Union[float, int], None] = Field(None, alias='inserted', description='Number of rows inserted.')
    error: Union[str, None] = Field(None, alias='error', description='Human-readable failure reason when ok is false.')


TableInsertRowsOutputVariant2DeliveryArtifactsItem = TypedDict('TableInsertRowsOutputVariant2DeliveryArtifactsItem', {
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
TableInsertRowsOutputVariant2DeliveryArtifactsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


TableInsertRowsOutputVariant2DeliveryStorageFailureVariant1 = TypedDict('TableInsertRowsOutputVariant2DeliveryStorageFailureVariant1', {
    'artifactId': Required[Union[str, None]],
    'outcome': Required[Literal['unknown', 'bytes-stored-metadata-pending', 'failed']],
})
TableInsertRowsOutputVariant2DeliveryStorageFailureVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


TableInsertRowsOutputVariant2Delivery = TypedDict('TableInsertRowsOutputVariant2Delivery', {
    'mode': Required[Literal['artifact']],
    'status': Required[Literal['complete', 'partial', 'unavailable']],
    'retainedRepresentation': Required[Literal['formatted-tool-result']],
    'sourceIsError': Required[bool],
    'artifacts': Required[list[TableInsertRowsOutputVariant2DeliveryArtifactsItem]],
    'downloadLinksOmitted': Required[bool],
    'scopeOmittedFields': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'storageFailure': Required[Union[TableInsertRowsOutputVariant2DeliveryStorageFailureVariant1, None]],
    'nextAction': Required[str],
})
TableInsertRowsOutputVariant2Delivery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


TableInsertRowsOutputVariant2RecoveryOperation = TypedDict('TableInsertRowsOutputVariant2RecoveryOperation', {
    'runId': Required[Union[Annotated[str, Field(max_length=200)], None]],
    'idempotencyKey': Required[Annotated[str, Field(max_length=512)]],
    'state': Required[Annotated[str, Field(max_length=100)]],
})
TableInsertRowsOutputVariant2RecoveryOperation.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


TableInsertRowsOutputVariant2Recovery = TypedDict('TableInsertRowsOutputVariant2Recovery', {
    'idempotencyKey': NotRequired[Annotated[str, Field(max_length=512)]],
    'operationId': NotRequired[Annotated[str, Field(max_length=200)]],
    'runId': NotRequired[Annotated[str, Field(max_length=200)]],
    'jobId': NotRequired[Annotated[str, Field(max_length=200)]],
    'operation': NotRequired[TableInsertRowsOutputVariant2RecoveryOperation],
})
TableInsertRowsOutputVariant2Recovery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class TableInsertRowsOutputVariant2(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    delivery: TableInsertRowsOutputVariant2Delivery = Field(..., alias='delivery', description='')
    preview: str = Field(..., alias='preview', description='')
    scope: dict[str, Union[str, Union[float, int], bool, None]] = Field(..., alias='scope', description='')
    recovery: TableInsertRowsOutputVariant2Recovery = Field(..., alias='recovery', description='')


# Union schema: validate external payloads with TypeAdapter(TableInsertRowsOutput).
TableInsertRowsOutput = Union[TableInsertRowsOutputVariant2, TableInsertRowsOutputVariant1]

_TableInsertRowsInputAdapter = TypeAdapter(TableInsertRowsInput)
_TableInsertRowsOutputAdapter = TypeAdapter(TableInsertRowsOutput)