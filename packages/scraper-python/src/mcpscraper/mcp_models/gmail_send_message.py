from typing import Annotated, Any, Literal, Union
from typing_extensions import NotRequired, Required, TypedDict
from pydantic import BaseModel, ConfigDict, Field, TypeAdapter


class GmailSendMessageInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=False)

    confirmed: Union[bool, None] = Field(None, alias='confirmed', description='Set true only when the person explicitly authorized sending this exact email. If omitted, a 2026-capable client may ask for confirmation.')
    idempotency_key: Annotated[str, Field(min_length=8, max_length=200)] = Field(..., alias='idempotencyKey', description='Required stable key for this intended email. Reuse it only when retrying the same send after a lost response.')
    connection_id: Annotated[str, Field(min_length=1)] = Field(..., alias='connectionId', description='A Gmail connectionId from list_service_connections, with actionsEnabled true.')
    to: str = Field(..., alias='to', description='Recipient email address.')
    subject: Annotated[str, Field(min_length=1, max_length=500)] = Field(..., alias='subject', description='Email subject line.')
    body: Annotated[str, Field(min_length=1, max_length=50000)] = Field(..., alias='body', description='Plain-text email body.')


class GmailSendMessageOutputVariant1(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    ok: bool = Field(..., alias='ok', description='')
    result: Union[Any, None] = Field(None, alias='result', description='')
    error: Union[str, None] = Field(..., alias='error', description='')


GmailSendMessageOutputVariant2DeliveryArtifactsItem = TypedDict('GmailSendMessageOutputVariant2DeliveryArtifactsItem', {
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
GmailSendMessageOutputVariant2DeliveryArtifactsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


GmailSendMessageOutputVariant2DeliveryStorageFailureVariant1 = TypedDict('GmailSendMessageOutputVariant2DeliveryStorageFailureVariant1', {
    'artifactId': Required[Union[str, None]],
    'outcome': Required[Literal['unknown', 'bytes-stored-metadata-pending', 'failed']],
})
GmailSendMessageOutputVariant2DeliveryStorageFailureVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


GmailSendMessageOutputVariant2Delivery = TypedDict('GmailSendMessageOutputVariant2Delivery', {
    'mode': Required[Literal['artifact']],
    'status': Required[Literal['complete', 'partial', 'unavailable']],
    'retainedRepresentation': Required[Literal['formatted-tool-result']],
    'sourceIsError': Required[bool],
    'artifacts': Required[list[GmailSendMessageOutputVariant2DeliveryArtifactsItem]],
    'downloadLinksOmitted': Required[bool],
    'scopeOmittedFields': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'storageFailure': Required[Union[GmailSendMessageOutputVariant2DeliveryStorageFailureVariant1, None]],
    'nextAction': Required[str],
})
GmailSendMessageOutputVariant2Delivery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


GmailSendMessageOutputVariant2RecoveryOperation = TypedDict('GmailSendMessageOutputVariant2RecoveryOperation', {
    'runId': Required[Union[Annotated[str, Field(max_length=200)], None]],
    'idempotencyKey': Required[Annotated[str, Field(max_length=512)]],
    'state': Required[Annotated[str, Field(max_length=100)]],
})
GmailSendMessageOutputVariant2RecoveryOperation.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


GmailSendMessageOutputVariant2Recovery = TypedDict('GmailSendMessageOutputVariant2Recovery', {
    'idempotencyKey': NotRequired[Annotated[str, Field(max_length=512)]],
    'operationId': NotRequired[Annotated[str, Field(max_length=200)]],
    'runId': NotRequired[Annotated[str, Field(max_length=200)]],
    'jobId': NotRequired[Annotated[str, Field(max_length=200)]],
    'operation': NotRequired[GmailSendMessageOutputVariant2RecoveryOperation],
})
GmailSendMessageOutputVariant2Recovery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class GmailSendMessageOutputVariant2(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    delivery: GmailSendMessageOutputVariant2Delivery = Field(..., alias='delivery', description='')
    preview: str = Field(..., alias='preview', description='')
    scope: dict[str, Union[str, Union[float, int], bool, None]] = Field(..., alias='scope', description='')
    recovery: GmailSendMessageOutputVariant2Recovery = Field(..., alias='recovery', description='')


# Union schema: validate external payloads with TypeAdapter(GmailSendMessageOutput).
GmailSendMessageOutput = Union[GmailSendMessageOutputVariant2, GmailSendMessageOutputVariant1]

_GmailSendMessageInputAdapter = TypeAdapter(GmailSendMessageInput)
_GmailSendMessageOutputAdapter = TypeAdapter(GmailSendMessageOutput)