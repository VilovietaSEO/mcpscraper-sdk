from typing import Annotated, Any, Literal, Union
from typing_extensions import NotRequired, Required, TypedDict
from pydantic import BaseModel, ConfigDict, Field, TypeAdapter


class SlackSendMessageInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=False)

    confirmed: Union[bool, None] = Field(None, alias='confirmed', description='Set true only when the person explicitly authorized sending this exact message. If omitted, a 2026-capable client may ask for confirmation.')
    idempotency_key: Annotated[str, Field(min_length=8, max_length=200)] = Field(..., alias='idempotencyKey', description='Required stable key for this intended message. Reuse it only when retrying the same send after a lost response.')
    connection_id: Annotated[str, Field(min_length=1)] = Field(..., alias='connectionId', description='A Slack connectionId from list_service_connections, with actionsEnabled true.')
    channel: Annotated[str, Field(min_length=1)] = Field(..., alias='channel', description='Slack channel ID to send to, e.g. "C1234567890". Get this from the connection\'s own read tools, not guessed.')
    text: Annotated[str, Field(min_length=1, max_length=4000)] = Field(..., alias='text', description='Message text to send.')


class SlackSendMessageOutputVariant1(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    ok: bool = Field(..., alias='ok', description='')
    result: Union[Any, None] = Field(None, alias='result', description='')
    error: Union[str, None] = Field(..., alias='error', description='')


SlackSendMessageOutputVariant2DeliveryArtifactsItem = TypedDict('SlackSendMessageOutputVariant2DeliveryArtifactsItem', {
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
SlackSendMessageOutputVariant2DeliveryArtifactsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


SlackSendMessageOutputVariant2DeliveryAvailableExportsItem = TypedDict('SlackSendMessageOutputVariant2DeliveryAvailableExportsItem', {
    'artifactId': Required[str],
    'sourceArtifactId': Required[str],
    'filename': Required[Literal['result.md']],
    'contentType': Required[Literal['text/markdown; charset=utf-8']],
    'state': Required[Literal['on-demand']],
})
SlackSendMessageOutputVariant2DeliveryAvailableExportsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


SlackSendMessageOutputVariant2DeliveryStorageFailureVariant1 = TypedDict('SlackSendMessageOutputVariant2DeliveryStorageFailureVariant1', {
    'artifactId': Required[Union[str, None]],
    'outcome': Required[Literal['unknown', 'bytes-stored-metadata-pending', 'failed']],
})
SlackSendMessageOutputVariant2DeliveryStorageFailureVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


SlackSendMessageOutputVariant2Delivery = TypedDict('SlackSendMessageOutputVariant2Delivery', {
    'mode': Required[Literal['artifact']],
    'status': Required[Literal['complete', 'partial', 'unavailable']],
    'retainedRepresentation': Required[Literal['formatted-tool-result']],
    'sourceIsError': Required[bool],
    'artifacts': Required[list[SlackSendMessageOutputVariant2DeliveryArtifactsItem]],
    'availableExports': NotRequired[list[SlackSendMessageOutputVariant2DeliveryAvailableExportsItem]],
    'downloadLinksOmitted': Required[bool],
    'scopeOmittedFields': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'storageFailure': Required[Union[SlackSendMessageOutputVariant2DeliveryStorageFailureVariant1, None]],
    'nextAction': Required[str],
})
SlackSendMessageOutputVariant2Delivery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


SlackSendMessageOutputVariant2RecoveryOperation = TypedDict('SlackSendMessageOutputVariant2RecoveryOperation', {
    'runId': Required[Union[Annotated[str, Field(max_length=200)], None]],
    'idempotencyKey': Required[Annotated[str, Field(max_length=512)]],
    'state': Required[Annotated[str, Field(max_length=100)]],
})
SlackSendMessageOutputVariant2RecoveryOperation.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


SlackSendMessageOutputVariant2Recovery = TypedDict('SlackSendMessageOutputVariant2Recovery', {
    'idempotencyKey': NotRequired[Annotated[str, Field(max_length=512)]],
    'operationId': NotRequired[Annotated[str, Field(max_length=200)]],
    'runId': NotRequired[Annotated[str, Field(max_length=200)]],
    'jobId': NotRequired[Annotated[str, Field(max_length=200)]],
    'operation': NotRequired[SlackSendMessageOutputVariant2RecoveryOperation],
})
SlackSendMessageOutputVariant2Recovery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class SlackSendMessageOutputVariant2(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    delivery: SlackSendMessageOutputVariant2Delivery = Field(..., alias='delivery', description='')
    preview: str = Field(..., alias='preview', description='')
    scope: dict[str, Union[str, Union[float, int], bool, None]] = Field(..., alias='scope', description='')
    recovery: SlackSendMessageOutputVariant2Recovery = Field(..., alias='recovery', description='')


# Union schema: validate external payloads with TypeAdapter(SlackSendMessageOutput).
SlackSendMessageOutput = Union[SlackSendMessageOutputVariant2, SlackSendMessageOutputVariant1]

_SlackSendMessageInputAdapter = TypeAdapter(SlackSendMessageInput)
_SlackSendMessageOutputAdapter = TypeAdapter(SlackSendMessageOutput)