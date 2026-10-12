from typing import Annotated, Any, Literal, Union
from typing_extensions import NotRequired, Required, TypedDict
from pydantic import BaseModel, ConfigDict, Field, TypeAdapter


class ReadServiceConnectionInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=False)

    connection_id: Annotated[str, Field(min_length=1)] = Field(..., alias='connectionId', description='A connectionId from list_service_connections.')
    tool: Annotated[str, Field(min_length=1)] = Field(..., alias='tool', description="One of that connection's readTools (from list_service_connections). An unlisted tool name is rejected with the allowed list.")
    args: Union[dict[str, Any], None] = Field(None, alias='args', description='Arguments for the tool, if it needs any (e.g. a channel id, a date filter).')


class ReadServiceConnectionOutputVariant1(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    ok: bool = Field(..., alias='ok', description='')
    result: Union[Any, None] = Field(None, alias='result', description='')
    error: Union[str, None] = Field(..., alias='error', description='')


ReadServiceConnectionOutputVariant2DeliveryArtifactsItem = TypedDict('ReadServiceConnectionOutputVariant2DeliveryArtifactsItem', {
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
ReadServiceConnectionOutputVariant2DeliveryArtifactsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


ReadServiceConnectionOutputVariant2DeliveryStorageFailureVariant1 = TypedDict('ReadServiceConnectionOutputVariant2DeliveryStorageFailureVariant1', {
    'artifactId': Required[Union[str, None]],
    'outcome': Required[Literal['unknown', 'bytes-stored-metadata-pending', 'failed']],
})
ReadServiceConnectionOutputVariant2DeliveryStorageFailureVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


ReadServiceConnectionOutputVariant2Delivery = TypedDict('ReadServiceConnectionOutputVariant2Delivery', {
    'mode': Required[Literal['artifact']],
    'status': Required[Literal['complete', 'partial', 'unavailable']],
    'retainedRepresentation': Required[Literal['formatted-tool-result']],
    'sourceIsError': Required[bool],
    'artifacts': Required[list[ReadServiceConnectionOutputVariant2DeliveryArtifactsItem]],
    'downloadLinksOmitted': Required[bool],
    'scopeOmittedFields': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'storageFailure': Required[Union[ReadServiceConnectionOutputVariant2DeliveryStorageFailureVariant1, None]],
    'nextAction': Required[str],
})
ReadServiceConnectionOutputVariant2Delivery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


ReadServiceConnectionOutputVariant2RecoveryOperation = TypedDict('ReadServiceConnectionOutputVariant2RecoveryOperation', {
    'runId': Required[Union[Annotated[str, Field(max_length=200)], None]],
    'idempotencyKey': Required[Annotated[str, Field(max_length=512)]],
    'state': Required[Annotated[str, Field(max_length=100)]],
})
ReadServiceConnectionOutputVariant2RecoveryOperation.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


ReadServiceConnectionOutputVariant2Recovery = TypedDict('ReadServiceConnectionOutputVariant2Recovery', {
    'idempotencyKey': NotRequired[Annotated[str, Field(max_length=512)]],
    'operationId': NotRequired[Annotated[str, Field(max_length=200)]],
    'runId': NotRequired[Annotated[str, Field(max_length=200)]],
    'jobId': NotRequired[Annotated[str, Field(max_length=200)]],
    'operation': NotRequired[ReadServiceConnectionOutputVariant2RecoveryOperation],
})
ReadServiceConnectionOutputVariant2Recovery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class ReadServiceConnectionOutputVariant2(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    delivery: ReadServiceConnectionOutputVariant2Delivery = Field(..., alias='delivery', description='')
    preview: str = Field(..., alias='preview', description='')
    scope: dict[str, Union[str, Union[float, int], bool, None]] = Field(..., alias='scope', description='')
    recovery: ReadServiceConnectionOutputVariant2Recovery = Field(..., alias='recovery', description='')


# Union schema: validate external payloads with TypeAdapter(ReadServiceConnectionOutput).
ReadServiceConnectionOutput = Union[ReadServiceConnectionOutputVariant2, ReadServiceConnectionOutputVariant1]

_ReadServiceConnectionInputAdapter = TypeAdapter(ReadServiceConnectionInput)
_ReadServiceConnectionOutputAdapter = TypeAdapter(ReadServiceConnectionOutput)