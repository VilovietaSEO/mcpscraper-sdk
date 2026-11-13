from typing import Annotated, Any, Literal, Union
from typing_extensions import NotRequired, Required, TypedDict
from pydantic import BaseModel, ConfigDict, Field, TypeAdapter


class CreateWebhookInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=False)

    vault: Union[str, None] = Field(None, alias='vault', description='Vault this webhook writes into. Optional; defaults to "Issues".')
    label: Union[str, None] = Field(None, alias='label', description='Optional human-readable label to help you remember what this webhook is for, e.g. "Website contact form".')


class CreateWebhookOutputVariant1(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    ok: bool = Field(..., alias='ok', description='')
    id: Union[str, None] = Field(None, alias='id', description='Webhook id, for listing/revoking later.')
    url: Union[str, None] = Field(None, alias='url', description='The full webhook URL — POST here to write a note.')
    vault: Union[str, None] = Field(None, alias='vault', description='')
    error: Union[str, None] = Field(None, alias='error', description='')


CreateWebhookOutputVariant2DeliveryArtifactsItem = TypedDict('CreateWebhookOutputVariant2DeliveryArtifactsItem', {
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
CreateWebhookOutputVariant2DeliveryArtifactsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


CreateWebhookOutputVariant2DeliveryAvailableExportsItem = TypedDict('CreateWebhookOutputVariant2DeliveryAvailableExportsItem', {
    'artifactId': Required[str],
    'sourceArtifactId': Required[str],
    'filename': Required[Literal['result.md']],
    'contentType': Required[Literal['text/markdown; charset=utf-8']],
    'state': Required[Literal['on-demand']],
})
CreateWebhookOutputVariant2DeliveryAvailableExportsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


CreateWebhookOutputVariant2DeliveryStorageFailureVariant1 = TypedDict('CreateWebhookOutputVariant2DeliveryStorageFailureVariant1', {
    'artifactId': Required[Union[str, None]],
    'outcome': Required[Literal['unknown', 'bytes-stored-metadata-pending', 'failed']],
})
CreateWebhookOutputVariant2DeliveryStorageFailureVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


CreateWebhookOutputVariant2Delivery = TypedDict('CreateWebhookOutputVariant2Delivery', {
    'mode': Required[Literal['artifact']],
    'status': Required[Literal['complete', 'partial', 'unavailable']],
    'retainedRepresentation': Required[Literal['formatted-tool-result']],
    'sourceIsError': Required[bool],
    'artifacts': Required[list[CreateWebhookOutputVariant2DeliveryArtifactsItem]],
    'availableExports': NotRequired[list[CreateWebhookOutputVariant2DeliveryAvailableExportsItem]],
    'downloadLinksOmitted': Required[bool],
    'scopeOmittedFields': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'storageFailure': Required[Union[CreateWebhookOutputVariant2DeliveryStorageFailureVariant1, None]],
    'nextAction': Required[str],
})
CreateWebhookOutputVariant2Delivery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


CreateWebhookOutputVariant2RecoveryOperation = TypedDict('CreateWebhookOutputVariant2RecoveryOperation', {
    'runId': Required[Union[Annotated[str, Field(max_length=200)], None]],
    'idempotencyKey': Required[Annotated[str, Field(max_length=512)]],
    'state': Required[Annotated[str, Field(max_length=100)]],
})
CreateWebhookOutputVariant2RecoveryOperation.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


CreateWebhookOutputVariant2Recovery = TypedDict('CreateWebhookOutputVariant2Recovery', {
    'idempotencyKey': NotRequired[Annotated[str, Field(max_length=512)]],
    'operationId': NotRequired[Annotated[str, Field(max_length=200)]],
    'runId': NotRequired[Annotated[str, Field(max_length=200)]],
    'jobId': NotRequired[Annotated[str, Field(max_length=200)]],
    'operation': NotRequired[CreateWebhookOutputVariant2RecoveryOperation],
})
CreateWebhookOutputVariant2Recovery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class CreateWebhookOutputVariant2(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    delivery: CreateWebhookOutputVariant2Delivery = Field(..., alias='delivery', description='')
    preview: str = Field(..., alias='preview', description='')
    scope: dict[str, Union[str, Union[float, int], bool, None]] = Field(..., alias='scope', description='')
    recovery: CreateWebhookOutputVariant2Recovery = Field(..., alias='recovery', description='')


# Union schema: validate external payloads with TypeAdapter(CreateWebhookOutput).
CreateWebhookOutput = Union[CreateWebhookOutputVariant2, CreateWebhookOutputVariant1]

_CreateWebhookInputAdapter = TypeAdapter(CreateWebhookInput)
_CreateWebhookOutputAdapter = TypeAdapter(CreateWebhookOutput)