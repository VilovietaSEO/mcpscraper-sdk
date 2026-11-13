from typing import Annotated, Any, Literal, Union
from typing_extensions import NotRequired, Required, TypedDict
from pydantic import BaseModel, ConfigDict, Field, TypeAdapter


class AccessRemoveApprovedSenderInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=False)

    sender_identity: Annotated[str, Field(min_length=1)] = Field(..., alias='senderIdentity', description='Identity to remove from your approved-senders list.')


class AccessRemoveApprovedSenderOutputVariant1(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    ok: bool = Field(..., alias='ok', description='True on success; false on auth error.')
    sender: Union[str, None] = Field(None, alias='sender', description='The identity that was removed.')
    removed: Union[bool, None] = Field(None, alias='removed', description='True when an existing approval was found and removed.')
    error: Union[str, None] = Field(None, alias='error', description='Human-readable failure reason when ok is false.')


AccessRemoveApprovedSenderOutputVariant2DeliveryArtifactsItem = TypedDict('AccessRemoveApprovedSenderOutputVariant2DeliveryArtifactsItem', {
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
AccessRemoveApprovedSenderOutputVariant2DeliveryArtifactsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


AccessRemoveApprovedSenderOutputVariant2DeliveryAvailableExportsItem = TypedDict('AccessRemoveApprovedSenderOutputVariant2DeliveryAvailableExportsItem', {
    'artifactId': Required[str],
    'sourceArtifactId': Required[str],
    'filename': Required[Literal['result.md']],
    'contentType': Required[Literal['text/markdown; charset=utf-8']],
    'state': Required[Literal['on-demand']],
})
AccessRemoveApprovedSenderOutputVariant2DeliveryAvailableExportsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


AccessRemoveApprovedSenderOutputVariant2DeliveryStorageFailureVariant1 = TypedDict('AccessRemoveApprovedSenderOutputVariant2DeliveryStorageFailureVariant1', {
    'artifactId': Required[Union[str, None]],
    'outcome': Required[Literal['unknown', 'bytes-stored-metadata-pending', 'failed']],
})
AccessRemoveApprovedSenderOutputVariant2DeliveryStorageFailureVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


AccessRemoveApprovedSenderOutputVariant2Delivery = TypedDict('AccessRemoveApprovedSenderOutputVariant2Delivery', {
    'mode': Required[Literal['artifact']],
    'status': Required[Literal['complete', 'partial', 'unavailable']],
    'retainedRepresentation': Required[Literal['formatted-tool-result']],
    'sourceIsError': Required[bool],
    'artifacts': Required[list[AccessRemoveApprovedSenderOutputVariant2DeliveryArtifactsItem]],
    'availableExports': NotRequired[list[AccessRemoveApprovedSenderOutputVariant2DeliveryAvailableExportsItem]],
    'downloadLinksOmitted': Required[bool],
    'scopeOmittedFields': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'storageFailure': Required[Union[AccessRemoveApprovedSenderOutputVariant2DeliveryStorageFailureVariant1, None]],
    'nextAction': Required[str],
})
AccessRemoveApprovedSenderOutputVariant2Delivery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


AccessRemoveApprovedSenderOutputVariant2RecoveryOperation = TypedDict('AccessRemoveApprovedSenderOutputVariant2RecoveryOperation', {
    'runId': Required[Union[Annotated[str, Field(max_length=200)], None]],
    'idempotencyKey': Required[Annotated[str, Field(max_length=512)]],
    'state': Required[Annotated[str, Field(max_length=100)]],
})
AccessRemoveApprovedSenderOutputVariant2RecoveryOperation.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


AccessRemoveApprovedSenderOutputVariant2Recovery = TypedDict('AccessRemoveApprovedSenderOutputVariant2Recovery', {
    'idempotencyKey': NotRequired[Annotated[str, Field(max_length=512)]],
    'operationId': NotRequired[Annotated[str, Field(max_length=200)]],
    'runId': NotRequired[Annotated[str, Field(max_length=200)]],
    'jobId': NotRequired[Annotated[str, Field(max_length=200)]],
    'operation': NotRequired[AccessRemoveApprovedSenderOutputVariant2RecoveryOperation],
})
AccessRemoveApprovedSenderOutputVariant2Recovery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class AccessRemoveApprovedSenderOutputVariant2(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    delivery: AccessRemoveApprovedSenderOutputVariant2Delivery = Field(..., alias='delivery', description='')
    preview: str = Field(..., alias='preview', description='')
    scope: dict[str, Union[str, Union[float, int], bool, None]] = Field(..., alias='scope', description='')
    recovery: AccessRemoveApprovedSenderOutputVariant2Recovery = Field(..., alias='recovery', description='')


# Union schema: validate external payloads with TypeAdapter(AccessRemoveApprovedSenderOutput).
AccessRemoveApprovedSenderOutput = Union[AccessRemoveApprovedSenderOutputVariant2, AccessRemoveApprovedSenderOutputVariant1]

_AccessRemoveApprovedSenderInputAdapter = TypeAdapter(AccessRemoveApprovedSenderInput)
_AccessRemoveApprovedSenderOutputAdapter = TypeAdapter(AccessRemoveApprovedSenderOutput)