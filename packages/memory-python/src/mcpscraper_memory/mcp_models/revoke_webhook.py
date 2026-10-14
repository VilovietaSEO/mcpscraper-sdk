from typing import Annotated, Any, Literal, Union
from typing_extensions import NotRequired, Required, TypedDict
from pydantic import BaseModel, ConfigDict, Field, TypeAdapter


class RevokeWebhookInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=False)

    id: Annotated[str, Field(min_length=1)] = Field(..., alias='id', description='Webhook id, from list-webhooks.')


class RevokeWebhookOutputVariant1(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    ok: bool = Field(..., alias='ok', description='')
    revoked: Union[bool, None] = Field(None, alias='revoked', description='')
    error: Union[str, None] = Field(None, alias='error', description='')


RevokeWebhookOutputVariant2DeliveryArtifactsItem = TypedDict('RevokeWebhookOutputVariant2DeliveryArtifactsItem', {
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
RevokeWebhookOutputVariant2DeliveryArtifactsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


RevokeWebhookOutputVariant2DeliveryStorageFailureVariant1 = TypedDict('RevokeWebhookOutputVariant2DeliveryStorageFailureVariant1', {
    'artifactId': Required[Union[str, None]],
    'outcome': Required[Literal['unknown', 'bytes-stored-metadata-pending', 'failed']],
})
RevokeWebhookOutputVariant2DeliveryStorageFailureVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


RevokeWebhookOutputVariant2Delivery = TypedDict('RevokeWebhookOutputVariant2Delivery', {
    'mode': Required[Literal['artifact']],
    'status': Required[Literal['complete', 'partial', 'unavailable']],
    'retainedRepresentation': Required[Literal['formatted-tool-result']],
    'sourceIsError': Required[bool],
    'artifacts': Required[list[RevokeWebhookOutputVariant2DeliveryArtifactsItem]],
    'downloadLinksOmitted': Required[bool],
    'scopeOmittedFields': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'storageFailure': Required[Union[RevokeWebhookOutputVariant2DeliveryStorageFailureVariant1, None]],
    'nextAction': Required[str],
})
RevokeWebhookOutputVariant2Delivery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


RevokeWebhookOutputVariant2RecoveryOperation = TypedDict('RevokeWebhookOutputVariant2RecoveryOperation', {
    'runId': Required[Union[Annotated[str, Field(max_length=200)], None]],
    'idempotencyKey': Required[Annotated[str, Field(max_length=512)]],
    'state': Required[Annotated[str, Field(max_length=100)]],
})
RevokeWebhookOutputVariant2RecoveryOperation.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


RevokeWebhookOutputVariant2Recovery = TypedDict('RevokeWebhookOutputVariant2Recovery', {
    'idempotencyKey': NotRequired[Annotated[str, Field(max_length=512)]],
    'operationId': NotRequired[Annotated[str, Field(max_length=200)]],
    'runId': NotRequired[Annotated[str, Field(max_length=200)]],
    'jobId': NotRequired[Annotated[str, Field(max_length=200)]],
    'operation': NotRequired[RevokeWebhookOutputVariant2RecoveryOperation],
})
RevokeWebhookOutputVariant2Recovery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class RevokeWebhookOutputVariant2(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    delivery: RevokeWebhookOutputVariant2Delivery = Field(..., alias='delivery', description='')
    preview: str = Field(..., alias='preview', description='')
    scope: dict[str, Union[str, Union[float, int], bool, None]] = Field(..., alias='scope', description='')
    recovery: RevokeWebhookOutputVariant2Recovery = Field(..., alias='recovery', description='')


# Union schema: validate external payloads with TypeAdapter(RevokeWebhookOutput).
RevokeWebhookOutput = Union[RevokeWebhookOutputVariant2, RevokeWebhookOutputVariant1]

_RevokeWebhookInputAdapter = TypeAdapter(RevokeWebhookInput)
_RevokeWebhookOutputAdapter = TypeAdapter(RevokeWebhookOutput)