from typing import Annotated, Any, Literal, Union
from typing_extensions import NotRequired, Required, TypedDict
from pydantic import BaseModel, ConfigDict, Field, TypeAdapter


class TableListInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=False)



class TableListOutputVariant1(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    ok: bool = Field(..., alias='ok', description='True on success; false on auth error.')
    tables: Union[list[str], None] = Field(None, alias='tables', description='Table names owned by the caller. Present when ok is true; may be empty.')
    error: Union[str, None] = Field(None, alias='error', description='Human-readable failure reason when ok is false.')


TableListOutputVariant2DeliveryArtifactsItem = TypedDict('TableListOutputVariant2DeliveryArtifactsItem', {
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
TableListOutputVariant2DeliveryArtifactsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


TableListOutputVariant2DeliveryAvailableExportsItem = TypedDict('TableListOutputVariant2DeliveryAvailableExportsItem', {
    'artifactId': Required[str],
    'sourceArtifactId': Required[str],
    'filename': Required[Literal['result.md']],
    'contentType': Required[Literal['text/markdown; charset=utf-8']],
    'state': Required[Literal['on-demand']],
})
TableListOutputVariant2DeliveryAvailableExportsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


TableListOutputVariant2DeliveryStorageFailureVariant1 = TypedDict('TableListOutputVariant2DeliveryStorageFailureVariant1', {
    'artifactId': Required[Union[str, None]],
    'outcome': Required[Literal['unknown', 'bytes-stored-metadata-pending', 'failed']],
})
TableListOutputVariant2DeliveryStorageFailureVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


TableListOutputVariant2Delivery = TypedDict('TableListOutputVariant2Delivery', {
    'mode': Required[Literal['artifact']],
    'status': Required[Literal['complete', 'partial', 'unavailable']],
    'retainedRepresentation': Required[Literal['formatted-tool-result']],
    'sourceIsError': Required[bool],
    'artifacts': Required[list[TableListOutputVariant2DeliveryArtifactsItem]],
    'availableExports': NotRequired[list[TableListOutputVariant2DeliveryAvailableExportsItem]],
    'downloadLinksOmitted': Required[bool],
    'scopeOmittedFields': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'storageFailure': Required[Union[TableListOutputVariant2DeliveryStorageFailureVariant1, None]],
    'nextAction': Required[str],
})
TableListOutputVariant2Delivery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


TableListOutputVariant2RecoveryOperation = TypedDict('TableListOutputVariant2RecoveryOperation', {
    'runId': Required[Union[Annotated[str, Field(max_length=200)], None]],
    'idempotencyKey': Required[Annotated[str, Field(max_length=512)]],
    'state': Required[Annotated[str, Field(max_length=100)]],
})
TableListOutputVariant2RecoveryOperation.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


TableListOutputVariant2Recovery = TypedDict('TableListOutputVariant2Recovery', {
    'idempotencyKey': NotRequired[Annotated[str, Field(max_length=512)]],
    'operationId': NotRequired[Annotated[str, Field(max_length=200)]],
    'runId': NotRequired[Annotated[str, Field(max_length=200)]],
    'jobId': NotRequired[Annotated[str, Field(max_length=200)]],
    'operation': NotRequired[TableListOutputVariant2RecoveryOperation],
})
TableListOutputVariant2Recovery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class TableListOutputVariant2(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    delivery: TableListOutputVariant2Delivery = Field(..., alias='delivery', description='')
    preview: str = Field(..., alias='preview', description='')
    scope: dict[str, Union[str, Union[float, int], bool, None]] = Field(..., alias='scope', description='')
    recovery: TableListOutputVariant2Recovery = Field(..., alias='recovery', description='')


# Union schema: validate external payloads with TypeAdapter(TableListOutput).
TableListOutput = Union[TableListOutputVariant2, TableListOutputVariant1]

_TableListInputAdapter = TypeAdapter(TableListInput)
_TableListOutputAdapter = TypeAdapter(TableListOutput)