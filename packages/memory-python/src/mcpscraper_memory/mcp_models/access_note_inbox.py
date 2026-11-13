from typing import Annotated, Any, Literal, Union
from typing_extensions import NotRequired, Required, TypedDict
from pydantic import BaseModel, ConfigDict, Field, TypeAdapter


class AccessNoteInboxInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=False)



AccessNoteInboxOutputVariant1PendingItemPermissions = TypedDict('AccessNoteInboxOutputVariant1PendingItemPermissions', {
    'read': Required[bool],
    'edit': Required[bool],
    'delete': Required[bool],
    'reshare': Required[bool],
})
AccessNoteInboxOutputVariant1PendingItemPermissions.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


AccessNoteInboxOutputVariant1PendingItem = TypedDict('AccessNoteInboxOutputVariant1PendingItem', {
    'shareId': Required[str],
    'owner': Required[str],
    'title': Required[str],
    'permissions': Required[AccessNoteInboxOutputVariant1PendingItemPermissions],
    'offeredAt': Required[str],
    'content': Required[str],
})
AccessNoteInboxOutputVariant1PendingItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class AccessNoteInboxOutputVariant1(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    ok: bool = Field(..., alias='ok', description='True on success; false on auth error.')
    pending: Union[list[AccessNoteInboxOutputVariant1PendingItem], None] = Field(None, alias='pending', description='Pending offers, oldest first. Present when ok is true.')
    error: Union[str, None] = Field(None, alias='error', description='Human-readable failure reason when ok is false.')


AccessNoteInboxOutputVariant2DeliveryArtifactsItem = TypedDict('AccessNoteInboxOutputVariant2DeliveryArtifactsItem', {
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
AccessNoteInboxOutputVariant2DeliveryArtifactsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


AccessNoteInboxOutputVariant2DeliveryAvailableExportsItem = TypedDict('AccessNoteInboxOutputVariant2DeliveryAvailableExportsItem', {
    'artifactId': Required[str],
    'sourceArtifactId': Required[str],
    'filename': Required[Literal['result.md']],
    'contentType': Required[Literal['text/markdown; charset=utf-8']],
    'state': Required[Literal['on-demand']],
})
AccessNoteInboxOutputVariant2DeliveryAvailableExportsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


AccessNoteInboxOutputVariant2DeliveryStorageFailureVariant1 = TypedDict('AccessNoteInboxOutputVariant2DeliveryStorageFailureVariant1', {
    'artifactId': Required[Union[str, None]],
    'outcome': Required[Literal['unknown', 'bytes-stored-metadata-pending', 'failed']],
})
AccessNoteInboxOutputVariant2DeliveryStorageFailureVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


AccessNoteInboxOutputVariant2Delivery = TypedDict('AccessNoteInboxOutputVariant2Delivery', {
    'mode': Required[Literal['artifact']],
    'status': Required[Literal['complete', 'partial', 'unavailable']],
    'retainedRepresentation': Required[Literal['formatted-tool-result']],
    'sourceIsError': Required[bool],
    'artifacts': Required[list[AccessNoteInboxOutputVariant2DeliveryArtifactsItem]],
    'availableExports': NotRequired[list[AccessNoteInboxOutputVariant2DeliveryAvailableExportsItem]],
    'downloadLinksOmitted': Required[bool],
    'scopeOmittedFields': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'storageFailure': Required[Union[AccessNoteInboxOutputVariant2DeliveryStorageFailureVariant1, None]],
    'nextAction': Required[str],
})
AccessNoteInboxOutputVariant2Delivery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


AccessNoteInboxOutputVariant2RecoveryOperation = TypedDict('AccessNoteInboxOutputVariant2RecoveryOperation', {
    'runId': Required[Union[Annotated[str, Field(max_length=200)], None]],
    'idempotencyKey': Required[Annotated[str, Field(max_length=512)]],
    'state': Required[Annotated[str, Field(max_length=100)]],
})
AccessNoteInboxOutputVariant2RecoveryOperation.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


AccessNoteInboxOutputVariant2Recovery = TypedDict('AccessNoteInboxOutputVariant2Recovery', {
    'idempotencyKey': NotRequired[Annotated[str, Field(max_length=512)]],
    'operationId': NotRequired[Annotated[str, Field(max_length=200)]],
    'runId': NotRequired[Annotated[str, Field(max_length=200)]],
    'jobId': NotRequired[Annotated[str, Field(max_length=200)]],
    'operation': NotRequired[AccessNoteInboxOutputVariant2RecoveryOperation],
})
AccessNoteInboxOutputVariant2Recovery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class AccessNoteInboxOutputVariant2(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    delivery: AccessNoteInboxOutputVariant2Delivery = Field(..., alias='delivery', description='')
    preview: str = Field(..., alias='preview', description='')
    scope: dict[str, Union[str, Union[float, int], bool, None]] = Field(..., alias='scope', description='')
    recovery: AccessNoteInboxOutputVariant2Recovery = Field(..., alias='recovery', description='')


# Union schema: validate external payloads with TypeAdapter(AccessNoteInboxOutput).
AccessNoteInboxOutput = Union[AccessNoteInboxOutputVariant2, AccessNoteInboxOutputVariant1]

_AccessNoteInboxInputAdapter = TypeAdapter(AccessNoteInboxInput)
_AccessNoteInboxOutputAdapter = TypeAdapter(AccessNoteInboxOutput)