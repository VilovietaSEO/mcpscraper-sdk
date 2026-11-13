from typing import Annotated, Any, Literal, Union
from typing_extensions import NotRequired, Required, TypedDict
from pydantic import BaseModel, ConfigDict, Field, TypeAdapter


class TableDropInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=False)

    table_name: Annotated[str, Field(min_length=1)] = Field(..., alias='tableName', description='Table name to permanently delete, from table-list.')


class TableDropOutputVariant1(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    ok: bool = Field(..., alias='ok', description='True on success; false on auth/scope error.')
    dropped: Union[bool, None] = Field(None, alias='dropped', description='True if the table existed and was dropped; false if it did not exist.')
    error: Union[str, None] = Field(None, alias='error', description='Human-readable failure reason when ok is false.')


TableDropOutputVariant2DeliveryArtifactsItem = TypedDict('TableDropOutputVariant2DeliveryArtifactsItem', {
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
TableDropOutputVariant2DeliveryArtifactsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


TableDropOutputVariant2DeliveryAvailableExportsItem = TypedDict('TableDropOutputVariant2DeliveryAvailableExportsItem', {
    'artifactId': Required[str],
    'sourceArtifactId': Required[str],
    'filename': Required[Literal['result.md']],
    'contentType': Required[Literal['text/markdown; charset=utf-8']],
    'state': Required[Literal['on-demand']],
})
TableDropOutputVariant2DeliveryAvailableExportsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


TableDropOutputVariant2DeliveryStorageFailureVariant1 = TypedDict('TableDropOutputVariant2DeliveryStorageFailureVariant1', {
    'artifactId': Required[Union[str, None]],
    'outcome': Required[Literal['unknown', 'bytes-stored-metadata-pending', 'failed']],
})
TableDropOutputVariant2DeliveryStorageFailureVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


TableDropOutputVariant2Delivery = TypedDict('TableDropOutputVariant2Delivery', {
    'mode': Required[Literal['artifact']],
    'status': Required[Literal['complete', 'partial', 'unavailable']],
    'retainedRepresentation': Required[Literal['formatted-tool-result']],
    'sourceIsError': Required[bool],
    'artifacts': Required[list[TableDropOutputVariant2DeliveryArtifactsItem]],
    'availableExports': NotRequired[list[TableDropOutputVariant2DeliveryAvailableExportsItem]],
    'downloadLinksOmitted': Required[bool],
    'scopeOmittedFields': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'storageFailure': Required[Union[TableDropOutputVariant2DeliveryStorageFailureVariant1, None]],
    'nextAction': Required[str],
})
TableDropOutputVariant2Delivery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


TableDropOutputVariant2RecoveryOperation = TypedDict('TableDropOutputVariant2RecoveryOperation', {
    'runId': Required[Union[Annotated[str, Field(max_length=200)], None]],
    'idempotencyKey': Required[Annotated[str, Field(max_length=512)]],
    'state': Required[Annotated[str, Field(max_length=100)]],
})
TableDropOutputVariant2RecoveryOperation.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


TableDropOutputVariant2Recovery = TypedDict('TableDropOutputVariant2Recovery', {
    'idempotencyKey': NotRequired[Annotated[str, Field(max_length=512)]],
    'operationId': NotRequired[Annotated[str, Field(max_length=200)]],
    'runId': NotRequired[Annotated[str, Field(max_length=200)]],
    'jobId': NotRequired[Annotated[str, Field(max_length=200)]],
    'operation': NotRequired[TableDropOutputVariant2RecoveryOperation],
})
TableDropOutputVariant2Recovery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class TableDropOutputVariant2(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    delivery: TableDropOutputVariant2Delivery = Field(..., alias='delivery', description='')
    preview: str = Field(..., alias='preview', description='')
    scope: dict[str, Union[str, Union[float, int], bool, None]] = Field(..., alias='scope', description='')
    recovery: TableDropOutputVariant2Recovery = Field(..., alias='recovery', description='')


# Union schema: validate external payloads with TypeAdapter(TableDropOutput).
TableDropOutput = Union[TableDropOutputVariant2, TableDropOutputVariant1]

_TableDropInputAdapter = TypeAdapter(TableDropInput)
_TableDropOutputAdapter = TypeAdapter(TableDropOutput)