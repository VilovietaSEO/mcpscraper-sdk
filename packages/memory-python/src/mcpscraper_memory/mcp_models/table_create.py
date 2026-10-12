from typing import Annotated, Any, Literal, Union
from typing_extensions import NotRequired, Required, TypedDict
from pydantic import BaseModel, ConfigDict, Field, TypeAdapter


TableCreateInputColumnsItem = TypedDict('TableCreateInputColumnsItem', {
    'name': Required[str],
    'type': Required[Literal['text', 'number', 'integer', 'boolean', 'date', 'timestamp', 'json']],
})
TableCreateInputColumnsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=False)


class TableCreateInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=False)

    table_name: Annotated[str, Field(min_length=1)] = Field(..., alias='tableName', description='Table name: lowercase letters, numbers, underscores, starting with a letter (e.g. rank_tracker).')
    columns: Annotated[list[TableCreateInputColumnsItem], Field(min_length=1)] = Field(..., alias='columns', description='Columns to create, in addition to the automatic id/created_at/updated_at.')


TableCreateOutputVariant1ColumnsItem = TypedDict('TableCreateOutputVariant1ColumnsItem', {
    'name': Required[str],
    'type': Required[str],
})
TableCreateOutputVariant1ColumnsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class TableCreateOutputVariant1(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    ok: bool = Field(..., alias='ok', description='True on success; false on auth/scope/validation error.')
    table_name: Union[str, None] = Field(None, alias='tableName', description='The table name.')
    created: Union[bool, None] = Field(None, alias='created', description='True if the table was newly created; false if it already existed.')
    columns: Union[list[TableCreateOutputVariant1ColumnsItem], None] = Field(None, alias='columns', description='The columns requested (existing tables are not altered to match).')
    error: Union[str, None] = Field(None, alias='error', description='Human-readable failure reason when ok is false.')


TableCreateOutputVariant2DeliveryArtifactsItem = TypedDict('TableCreateOutputVariant2DeliveryArtifactsItem', {
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
TableCreateOutputVariant2DeliveryArtifactsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


TableCreateOutputVariant2DeliveryStorageFailureVariant1 = TypedDict('TableCreateOutputVariant2DeliveryStorageFailureVariant1', {
    'artifactId': Required[Union[str, None]],
    'outcome': Required[Literal['unknown', 'bytes-stored-metadata-pending', 'failed']],
})
TableCreateOutputVariant2DeliveryStorageFailureVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


TableCreateOutputVariant2Delivery = TypedDict('TableCreateOutputVariant2Delivery', {
    'mode': Required[Literal['artifact']],
    'status': Required[Literal['complete', 'partial', 'unavailable']],
    'retainedRepresentation': Required[Literal['formatted-tool-result']],
    'sourceIsError': Required[bool],
    'artifacts': Required[list[TableCreateOutputVariant2DeliveryArtifactsItem]],
    'downloadLinksOmitted': Required[bool],
    'scopeOmittedFields': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'storageFailure': Required[Union[TableCreateOutputVariant2DeliveryStorageFailureVariant1, None]],
    'nextAction': Required[str],
})
TableCreateOutputVariant2Delivery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


TableCreateOutputVariant2RecoveryOperation = TypedDict('TableCreateOutputVariant2RecoveryOperation', {
    'runId': Required[Union[Annotated[str, Field(max_length=200)], None]],
    'idempotencyKey': Required[Annotated[str, Field(max_length=512)]],
    'state': Required[Annotated[str, Field(max_length=100)]],
})
TableCreateOutputVariant2RecoveryOperation.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


TableCreateOutputVariant2Recovery = TypedDict('TableCreateOutputVariant2Recovery', {
    'idempotencyKey': NotRequired[Annotated[str, Field(max_length=512)]],
    'operationId': NotRequired[Annotated[str, Field(max_length=200)]],
    'runId': NotRequired[Annotated[str, Field(max_length=200)]],
    'jobId': NotRequired[Annotated[str, Field(max_length=200)]],
    'operation': NotRequired[TableCreateOutputVariant2RecoveryOperation],
})
TableCreateOutputVariant2Recovery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class TableCreateOutputVariant2(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    delivery: TableCreateOutputVariant2Delivery = Field(..., alias='delivery', description='')
    preview: str = Field(..., alias='preview', description='')
    scope: dict[str, Union[str, Union[float, int], bool, None]] = Field(..., alias='scope', description='')
    recovery: TableCreateOutputVariant2Recovery = Field(..., alias='recovery', description='')


# Union schema: validate external payloads with TypeAdapter(TableCreateOutput).
TableCreateOutput = Union[TableCreateOutputVariant2, TableCreateOutputVariant1]

_TableCreateInputAdapter = TypeAdapter(TableCreateInput)
_TableCreateOutputAdapter = TypeAdapter(TableCreateOutput)