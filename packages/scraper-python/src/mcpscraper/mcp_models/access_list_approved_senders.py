from typing import Annotated, Any, Literal, Union
from typing_extensions import NotRequired, Required, TypedDict
from pydantic import BaseModel, ConfigDict, Field, TypeAdapter


class AccessListApprovedSendersInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=False)



class AccessListApprovedSendersOutputVariant1(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    ok: bool = Field(..., alias='ok', description='True on success; false on auth error.')
    approved_senders: Union[list[str], None] = Field(None, alias='approvedSenders', description='Identities approved to reach you.')
    allow_unapproved_senders: Union[bool, None] = Field(None, alias='allowUnapprovedSenders', description='True if your inbox is open to anyone regardless of this list.')
    error: Union[str, None] = Field(None, alias='error', description='Human-readable failure reason when ok is false.')


AccessListApprovedSendersOutputVariant2DeliveryArtifactsItem = TypedDict('AccessListApprovedSendersOutputVariant2DeliveryArtifactsItem', {
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
AccessListApprovedSendersOutputVariant2DeliveryArtifactsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


AccessListApprovedSendersOutputVariant2DeliveryStorageFailureVariant1 = TypedDict('AccessListApprovedSendersOutputVariant2DeliveryStorageFailureVariant1', {
    'artifactId': Required[Union[str, None]],
    'outcome': Required[Literal['unknown', 'bytes-stored-metadata-pending', 'failed']],
})
AccessListApprovedSendersOutputVariant2DeliveryStorageFailureVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


AccessListApprovedSendersOutputVariant2Delivery = TypedDict('AccessListApprovedSendersOutputVariant2Delivery', {
    'mode': Required[Literal['artifact']],
    'status': Required[Literal['complete', 'partial', 'unavailable']],
    'retainedRepresentation': Required[Literal['formatted-tool-result']],
    'sourceIsError': Required[bool],
    'artifacts': Required[list[AccessListApprovedSendersOutputVariant2DeliveryArtifactsItem]],
    'downloadLinksOmitted': Required[bool],
    'scopeOmittedFields': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'storageFailure': Required[Union[AccessListApprovedSendersOutputVariant2DeliveryStorageFailureVariant1, None]],
    'nextAction': Required[str],
})
AccessListApprovedSendersOutputVariant2Delivery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


AccessListApprovedSendersOutputVariant2RecoveryOperation = TypedDict('AccessListApprovedSendersOutputVariant2RecoveryOperation', {
    'runId': Required[Union[Annotated[str, Field(max_length=200)], None]],
    'idempotencyKey': Required[Annotated[str, Field(max_length=512)]],
    'state': Required[Annotated[str, Field(max_length=100)]],
})
AccessListApprovedSendersOutputVariant2RecoveryOperation.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


AccessListApprovedSendersOutputVariant2Recovery = TypedDict('AccessListApprovedSendersOutputVariant2Recovery', {
    'idempotencyKey': NotRequired[Annotated[str, Field(max_length=512)]],
    'operationId': NotRequired[Annotated[str, Field(max_length=200)]],
    'runId': NotRequired[Annotated[str, Field(max_length=200)]],
    'jobId': NotRequired[Annotated[str, Field(max_length=200)]],
    'operation': NotRequired[AccessListApprovedSendersOutputVariant2RecoveryOperation],
})
AccessListApprovedSendersOutputVariant2Recovery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class AccessListApprovedSendersOutputVariant2(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    delivery: AccessListApprovedSendersOutputVariant2Delivery = Field(..., alias='delivery', description='')
    preview: str = Field(..., alias='preview', description='')
    scope: dict[str, Union[str, Union[float, int], bool, None]] = Field(..., alias='scope', description='')
    recovery: AccessListApprovedSendersOutputVariant2Recovery = Field(..., alias='recovery', description='')


# Union schema: validate external payloads with TypeAdapter(AccessListApprovedSendersOutput).
AccessListApprovedSendersOutput = Union[AccessListApprovedSendersOutputVariant2, AccessListApprovedSendersOutputVariant1]

_AccessListApprovedSendersInputAdapter = TypeAdapter(AccessListApprovedSendersInput)
_AccessListApprovedSendersOutputAdapter = TypeAdapter(AccessListApprovedSendersOutput)