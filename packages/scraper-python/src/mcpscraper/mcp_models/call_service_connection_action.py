from typing import Annotated, Any, Literal, Union
from typing_extensions import NotRequired, Required, TypedDict
from pydantic import BaseModel, ConfigDict, Field, TypeAdapter


class CallServiceConnectionActionInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=False)

    confirmed: Union[bool, None] = Field(None, alias='confirmed', description='Set true only when the person explicitly authorized this exact external action. If omitted, a 2026-capable client may ask for confirmation through MCP multi-round input.')
    idempotency_key: Annotated[str, Field(min_length=8, max_length=200)] = Field(..., alias='idempotencyKey', description='Required stable key for this intended external action. Reuse it only to retry the same action after a lost response; use a new key for a new action.')
    connection_id: Annotated[str, Field(min_length=1)] = Field(..., alias='connectionId', description='A connectionId from list_service_connections with actionsEnabled true.')
    tool: Annotated[str, Field(min_length=1)] = Field(..., alias='tool', description="One exact tool name from that connection's actionTools. Arbitrary provider action names and adminBlockedTools are rejected server-side.")
    args: dict[str, Any] = Field(..., alias='args', description='Arguments required by the selected action. The provider action validates its own typed input before execution.')


class CallServiceConnectionActionOutputVariant1(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    ok: bool = Field(..., alias='ok', description='')
    result: Union[Any, None] = Field(None, alias='result', description='')
    error: Union[str, None] = Field(..., alias='error', description='')


CallServiceConnectionActionOutputVariant2DeliveryArtifactsItem = TypedDict('CallServiceConnectionActionOutputVariant2DeliveryArtifactsItem', {
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
CallServiceConnectionActionOutputVariant2DeliveryArtifactsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


CallServiceConnectionActionOutputVariant2DeliveryAvailableExportsItem = TypedDict('CallServiceConnectionActionOutputVariant2DeliveryAvailableExportsItem', {
    'artifactId': Required[str],
    'sourceArtifactId': Required[str],
    'filename': Required[Literal['result.md']],
    'contentType': Required[Literal['text/markdown; charset=utf-8']],
    'state': Required[Literal['on-demand']],
})
CallServiceConnectionActionOutputVariant2DeliveryAvailableExportsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


CallServiceConnectionActionOutputVariant2DeliveryStorageFailureVariant1 = TypedDict('CallServiceConnectionActionOutputVariant2DeliveryStorageFailureVariant1', {
    'artifactId': Required[Union[str, None]],
    'outcome': Required[Literal['unknown', 'bytes-stored-metadata-pending', 'failed']],
})
CallServiceConnectionActionOutputVariant2DeliveryStorageFailureVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


CallServiceConnectionActionOutputVariant2Delivery = TypedDict('CallServiceConnectionActionOutputVariant2Delivery', {
    'mode': Required[Literal['artifact']],
    'status': Required[Literal['complete', 'partial', 'unavailable']],
    'retainedRepresentation': Required[Literal['formatted-tool-result']],
    'sourceIsError': Required[bool],
    'artifacts': Required[list[CallServiceConnectionActionOutputVariant2DeliveryArtifactsItem]],
    'availableExports': NotRequired[list[CallServiceConnectionActionOutputVariant2DeliveryAvailableExportsItem]],
    'downloadLinksOmitted': Required[bool],
    'scopeOmittedFields': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'storageFailure': Required[Union[CallServiceConnectionActionOutputVariant2DeliveryStorageFailureVariant1, None]],
    'nextAction': Required[str],
})
CallServiceConnectionActionOutputVariant2Delivery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


CallServiceConnectionActionOutputVariant2RecoveryOperation = TypedDict('CallServiceConnectionActionOutputVariant2RecoveryOperation', {
    'runId': Required[Union[Annotated[str, Field(max_length=200)], None]],
    'idempotencyKey': Required[Annotated[str, Field(max_length=512)]],
    'state': Required[Annotated[str, Field(max_length=100)]],
})
CallServiceConnectionActionOutputVariant2RecoveryOperation.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


CallServiceConnectionActionOutputVariant2Recovery = TypedDict('CallServiceConnectionActionOutputVariant2Recovery', {
    'idempotencyKey': NotRequired[Annotated[str, Field(max_length=512)]],
    'operationId': NotRequired[Annotated[str, Field(max_length=200)]],
    'runId': NotRequired[Annotated[str, Field(max_length=200)]],
    'jobId': NotRequired[Annotated[str, Field(max_length=200)]],
    'operation': NotRequired[CallServiceConnectionActionOutputVariant2RecoveryOperation],
})
CallServiceConnectionActionOutputVariant2Recovery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class CallServiceConnectionActionOutputVariant2(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    delivery: CallServiceConnectionActionOutputVariant2Delivery = Field(..., alias='delivery', description='')
    preview: str = Field(..., alias='preview', description='')
    scope: dict[str, Union[str, Union[float, int], bool, None]] = Field(..., alias='scope', description='')
    recovery: CallServiceConnectionActionOutputVariant2Recovery = Field(..., alias='recovery', description='')


# Union schema: validate external payloads with TypeAdapter(CallServiceConnectionActionOutput).
CallServiceConnectionActionOutput = Union[CallServiceConnectionActionOutputVariant2, CallServiceConnectionActionOutputVariant1]

_CallServiceConnectionActionInputAdapter = TypeAdapter(CallServiceConnectionActionInput)
_CallServiceConnectionActionOutputAdapter = TypeAdapter(CallServiceConnectionActionOutput)