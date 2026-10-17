from typing import Annotated, Any, Literal, Union
from typing_extensions import NotRequired, Required, TypedDict
from pydantic import BaseModel, ConfigDict, Field, TypeAdapter


class ListSharedWithMeInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=False)



ListSharedWithMeOutputVariant1NotesItemPermissions = TypedDict('ListSharedWithMeOutputVariant1NotesItemPermissions', {
    'read': Required[bool],
    'edit': Required[bool],
    'delete': Required[bool],
    'reshare': Required[bool],
})
ListSharedWithMeOutputVariant1NotesItemPermissions.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


ListSharedWithMeOutputVariant1NotesItem = TypedDict('ListSharedWithMeOutputVariant1NotesItem', {
    'shareId': Required[str],
    'owner': Required[str],
    'title': Required[str],
    'permissions': Required[ListSharedWithMeOutputVariant1NotesItemPermissions],
    'revision': Required[Union[float, int]],
    'updatedAt': Required[str],
})
ListSharedWithMeOutputVariant1NotesItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class ListSharedWithMeOutputVariant1(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    ok: bool = Field(..., alias='ok', description='True on success; false on auth error.')
    notes: Union[list[ListSharedWithMeOutputVariant1NotesItem], None] = Field(None, alias='notes', description='Notes shared with you and accepted. Present when ok is true.')
    error: Union[str, None] = Field(None, alias='error', description='Human-readable failure reason when ok is false.')


ListSharedWithMeOutputVariant2DeliveryArtifactsItem = TypedDict('ListSharedWithMeOutputVariant2DeliveryArtifactsItem', {
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
ListSharedWithMeOutputVariant2DeliveryArtifactsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


ListSharedWithMeOutputVariant2DeliveryAvailableExportsItem = TypedDict('ListSharedWithMeOutputVariant2DeliveryAvailableExportsItem', {
    'artifactId': Required[str],
    'sourceArtifactId': Required[str],
    'filename': Required[Literal['result.md']],
    'contentType': Required[Literal['text/markdown; charset=utf-8']],
    'state': Required[Literal['on-demand']],
})
ListSharedWithMeOutputVariant2DeliveryAvailableExportsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


ListSharedWithMeOutputVariant2DeliveryStorageFailureVariant1 = TypedDict('ListSharedWithMeOutputVariant2DeliveryStorageFailureVariant1', {
    'artifactId': Required[Union[str, None]],
    'outcome': Required[Literal['unknown', 'bytes-stored-metadata-pending', 'failed']],
})
ListSharedWithMeOutputVariant2DeliveryStorageFailureVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


ListSharedWithMeOutputVariant2Delivery = TypedDict('ListSharedWithMeOutputVariant2Delivery', {
    'mode': Required[Literal['artifact']],
    'status': Required[Literal['complete', 'partial', 'unavailable']],
    'retainedRepresentation': Required[Literal['formatted-tool-result']],
    'sourceIsError': Required[bool],
    'artifacts': Required[list[ListSharedWithMeOutputVariant2DeliveryArtifactsItem]],
    'availableExports': NotRequired[list[ListSharedWithMeOutputVariant2DeliveryAvailableExportsItem]],
    'downloadLinksOmitted': Required[bool],
    'scopeOmittedFields': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'storageFailure': Required[Union[ListSharedWithMeOutputVariant2DeliveryStorageFailureVariant1, None]],
    'nextAction': Required[str],
})
ListSharedWithMeOutputVariant2Delivery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


ListSharedWithMeOutputVariant2RecoveryOperation = TypedDict('ListSharedWithMeOutputVariant2RecoveryOperation', {
    'runId': Required[Union[Annotated[str, Field(max_length=200)], None]],
    'idempotencyKey': Required[Annotated[str, Field(max_length=512)]],
    'state': Required[Annotated[str, Field(max_length=100)]],
})
ListSharedWithMeOutputVariant2RecoveryOperation.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


ListSharedWithMeOutputVariant2Recovery = TypedDict('ListSharedWithMeOutputVariant2Recovery', {
    'idempotencyKey': NotRequired[Annotated[str, Field(max_length=512)]],
    'operationId': NotRequired[Annotated[str, Field(max_length=200)]],
    'runId': NotRequired[Annotated[str, Field(max_length=200)]],
    'jobId': NotRequired[Annotated[str, Field(max_length=200)]],
    'operation': NotRequired[ListSharedWithMeOutputVariant2RecoveryOperation],
})
ListSharedWithMeOutputVariant2Recovery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class ListSharedWithMeOutputVariant2(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    delivery: ListSharedWithMeOutputVariant2Delivery = Field(..., alias='delivery', description='')
    preview: str = Field(..., alias='preview', description='')
    scope: dict[str, Union[str, Union[float, int], bool, None]] = Field(..., alias='scope', description='')
    recovery: ListSharedWithMeOutputVariant2Recovery = Field(..., alias='recovery', description='')


# Union schema: validate external payloads with TypeAdapter(ListSharedWithMeOutput).
ListSharedWithMeOutput = Union[ListSharedWithMeOutputVariant2, ListSharedWithMeOutputVariant1]

_ListSharedWithMeInputAdapter = TypeAdapter(ListSharedWithMeInput)
_ListSharedWithMeOutputAdapter = TypeAdapter(ListSharedWithMeOutput)