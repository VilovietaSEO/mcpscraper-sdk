from typing import Annotated, Any, Literal, Union
from typing_extensions import NotRequired, Required, TypedDict
from pydantic import BaseModel, ConfigDict, Field, TypeAdapter


class AccessApproveSenderInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=False)

    sender_identity: Annotated[str, Field(min_length=1)] = Field(..., alias='senderIdentity', description='Identity (email or user id) to approve as a sender.')


class AccessApproveSenderOutputVariant1(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    ok: bool = Field(..., alias='ok', description='True on success; false on auth error.')
    sender: Union[str, None] = Field(None, alias='sender', description='The identity that was approved.')
    error: Union[str, None] = Field(None, alias='error', description='Human-readable failure reason when ok is false.')


AccessApproveSenderOutputVariant2DeliveryArtifactsItem = TypedDict('AccessApproveSenderOutputVariant2DeliveryArtifactsItem', {
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
AccessApproveSenderOutputVariant2DeliveryArtifactsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


AccessApproveSenderOutputVariant2DeliveryAvailableExportsItem = TypedDict('AccessApproveSenderOutputVariant2DeliveryAvailableExportsItem', {
    'artifactId': Required[str],
    'sourceArtifactId': Required[str],
    'filename': Required[Literal['result.md']],
    'contentType': Required[Literal['text/markdown; charset=utf-8']],
    'state': Required[Literal['on-demand']],
})
AccessApproveSenderOutputVariant2DeliveryAvailableExportsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


AccessApproveSenderOutputVariant2DeliveryStorageFailureVariant1 = TypedDict('AccessApproveSenderOutputVariant2DeliveryStorageFailureVariant1', {
    'artifactId': Required[Union[str, None]],
    'outcome': Required[Literal['unknown', 'bytes-stored-metadata-pending', 'failed']],
})
AccessApproveSenderOutputVariant2DeliveryStorageFailureVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


AccessApproveSenderOutputVariant2Delivery = TypedDict('AccessApproveSenderOutputVariant2Delivery', {
    'mode': Required[Literal['artifact']],
    'status': Required[Literal['complete', 'partial', 'unavailable']],
    'retainedRepresentation': Required[Literal['formatted-tool-result']],
    'sourceIsError': Required[bool],
    'artifacts': Required[list[AccessApproveSenderOutputVariant2DeliveryArtifactsItem]],
    'availableExports': NotRequired[list[AccessApproveSenderOutputVariant2DeliveryAvailableExportsItem]],
    'downloadLinksOmitted': Required[bool],
    'scopeOmittedFields': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'storageFailure': Required[Union[AccessApproveSenderOutputVariant2DeliveryStorageFailureVariant1, None]],
    'nextAction': Required[str],
})
AccessApproveSenderOutputVariant2Delivery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


AccessApproveSenderOutputVariant2RecoveryOperation = TypedDict('AccessApproveSenderOutputVariant2RecoveryOperation', {
    'runId': Required[Union[Annotated[str, Field(max_length=200)], None]],
    'idempotencyKey': Required[Annotated[str, Field(max_length=512)]],
    'state': Required[Annotated[str, Field(max_length=100)]],
})
AccessApproveSenderOutputVariant2RecoveryOperation.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


AccessApproveSenderOutputVariant2Recovery = TypedDict('AccessApproveSenderOutputVariant2Recovery', {
    'idempotencyKey': NotRequired[Annotated[str, Field(max_length=512)]],
    'operationId': NotRequired[Annotated[str, Field(max_length=200)]],
    'runId': NotRequired[Annotated[str, Field(max_length=200)]],
    'jobId': NotRequired[Annotated[str, Field(max_length=200)]],
    'operation': NotRequired[AccessApproveSenderOutputVariant2RecoveryOperation],
})
AccessApproveSenderOutputVariant2Recovery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class AccessApproveSenderOutputVariant2(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    delivery: AccessApproveSenderOutputVariant2Delivery = Field(..., alias='delivery', description='')
    preview: str = Field(..., alias='preview', description='')
    scope: dict[str, Union[str, Union[float, int], bool, None]] = Field(..., alias='scope', description='')
    recovery: AccessApproveSenderOutputVariant2Recovery = Field(..., alias='recovery', description='')


# Union schema: validate external payloads with TypeAdapter(AccessApproveSenderOutput).
AccessApproveSenderOutput = Union[AccessApproveSenderOutputVariant2, AccessApproveSenderOutputVariant1]

_AccessApproveSenderInputAdapter = TypeAdapter(AccessApproveSenderInput)
_AccessApproveSenderOutputAdapter = TypeAdapter(AccessApproveSenderOutput)