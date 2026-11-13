from typing import Annotated, Any, Literal, Union
from typing_extensions import NotRequired, Required, TypedDict
from pydantic import BaseModel, ConfigDict, Field, TypeAdapter


class ListWebhooksInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=False)



ListWebhooksOutputVariant1WebhooksItem = TypedDict('ListWebhooksOutputVariant1WebhooksItem', {
    'id': Required[str],
    'vault': Required[str],
    'label': Required[Union[str, None]],
    'createdAt': Required[str],
})
ListWebhooksOutputVariant1WebhooksItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class ListWebhooksOutputVariant1(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    ok: bool = Field(..., alias='ok', description='')
    webhooks: Union[list[ListWebhooksOutputVariant1WebhooksItem], None] = Field(None, alias='webhooks', description='')
    error: Union[str, None] = Field(None, alias='error', description='')


ListWebhooksOutputVariant2DeliveryArtifactsItem = TypedDict('ListWebhooksOutputVariant2DeliveryArtifactsItem', {
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
ListWebhooksOutputVariant2DeliveryArtifactsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


ListWebhooksOutputVariant2DeliveryAvailableExportsItem = TypedDict('ListWebhooksOutputVariant2DeliveryAvailableExportsItem', {
    'artifactId': Required[str],
    'sourceArtifactId': Required[str],
    'filename': Required[Literal['result.md']],
    'contentType': Required[Literal['text/markdown; charset=utf-8']],
    'state': Required[Literal['on-demand']],
})
ListWebhooksOutputVariant2DeliveryAvailableExportsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


ListWebhooksOutputVariant2DeliveryStorageFailureVariant1 = TypedDict('ListWebhooksOutputVariant2DeliveryStorageFailureVariant1', {
    'artifactId': Required[Union[str, None]],
    'outcome': Required[Literal['unknown', 'bytes-stored-metadata-pending', 'failed']],
})
ListWebhooksOutputVariant2DeliveryStorageFailureVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


ListWebhooksOutputVariant2Delivery = TypedDict('ListWebhooksOutputVariant2Delivery', {
    'mode': Required[Literal['artifact']],
    'status': Required[Literal['complete', 'partial', 'unavailable']],
    'retainedRepresentation': Required[Literal['formatted-tool-result']],
    'sourceIsError': Required[bool],
    'artifacts': Required[list[ListWebhooksOutputVariant2DeliveryArtifactsItem]],
    'availableExports': NotRequired[list[ListWebhooksOutputVariant2DeliveryAvailableExportsItem]],
    'downloadLinksOmitted': Required[bool],
    'scopeOmittedFields': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'storageFailure': Required[Union[ListWebhooksOutputVariant2DeliveryStorageFailureVariant1, None]],
    'nextAction': Required[str],
})
ListWebhooksOutputVariant2Delivery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


ListWebhooksOutputVariant2RecoveryOperation = TypedDict('ListWebhooksOutputVariant2RecoveryOperation', {
    'runId': Required[Union[Annotated[str, Field(max_length=200)], None]],
    'idempotencyKey': Required[Annotated[str, Field(max_length=512)]],
    'state': Required[Annotated[str, Field(max_length=100)]],
})
ListWebhooksOutputVariant2RecoveryOperation.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


ListWebhooksOutputVariant2Recovery = TypedDict('ListWebhooksOutputVariant2Recovery', {
    'idempotencyKey': NotRequired[Annotated[str, Field(max_length=512)]],
    'operationId': NotRequired[Annotated[str, Field(max_length=200)]],
    'runId': NotRequired[Annotated[str, Field(max_length=200)]],
    'jobId': NotRequired[Annotated[str, Field(max_length=200)]],
    'operation': NotRequired[ListWebhooksOutputVariant2RecoveryOperation],
})
ListWebhooksOutputVariant2Recovery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class ListWebhooksOutputVariant2(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    delivery: ListWebhooksOutputVariant2Delivery = Field(..., alias='delivery', description='')
    preview: str = Field(..., alias='preview', description='')
    scope: dict[str, Union[str, Union[float, int], bool, None]] = Field(..., alias='scope', description='')
    recovery: ListWebhooksOutputVariant2Recovery = Field(..., alias='recovery', description='')


# Union schema: validate external payloads with TypeAdapter(ListWebhooksOutput).
ListWebhooksOutput = Union[ListWebhooksOutputVariant2, ListWebhooksOutputVariant1]

_ListWebhooksInputAdapter = TypeAdapter(ListWebhooksInput)
_ListWebhooksOutputAdapter = TypeAdapter(ListWebhooksOutput)