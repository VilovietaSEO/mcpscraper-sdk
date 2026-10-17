from typing import Annotated, Any, Literal, Union
from typing_extensions import NotRequired, Required, TypedDict
from pydantic import BaseModel, ConfigDict, Field, TypeAdapter


class DeleteNoteInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=False)

    vault: Union[str, None] = Field(None, alias='vault', description='Vault to delete from. Optional; defaults to the session active vault, then the first vault the caller is entitled to.')
    path: Union[str, None] = Field(None, alias='path', description='Exact vault-relative note path to delete, e.g. projects/q3-plan (as returned by memory-list or recall). Required unless shareId is given.')
    share_id: Union[str, None] = Field(None, alias='shareId', description='Destroy a note shared with you and you accepted, by its shareId, instead of vault+path. Requires the share to grant delete permission and baseRevision (mandatory for shared notes).')
    base_revision: Union[Union[float, int], None] = Field(None, alias='baseRevision', description='Revision the delete is based on (from a prior get). When provided, the delete only applies if the note is still at this revision; otherwise it is rejected as a conflict instead of destroying a concurrent edit. Mandatory when shareId is given; optional otherwise (omit to delete unconditionally).')


DeleteNoteOutputVariant1Current = TypedDict('DeleteNoteOutputVariant1Current', {
    'content': Required[str],
    'revision': Required[Union[float, int]],
    'updatedBy': Required[Union[str, None]],
    'updatedAt': Required[str],
})
DeleteNoteOutputVariant1Current.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class DeleteNoteOutputVariant1(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    ok: bool = Field(..., alias='ok', description='True when the delete request was processed; false on an auth/scope/lookup error or a revision conflict.')
    vault: Union[str, None] = Field(None, alias='vault', description='The vault the delete was applied to (after defaulting). Present when ok is true.')
    deleted: Union[bool, None] = Field(None, alias='deleted', description='True if a note was removed; false if no matching note existed (idempotent). Present when ok is true.')
    conflict: Union[bool, None] = Field(None, alias='conflict', description='True when baseRevision did not match the current revision: someone else changed the note first. Nothing was deleted.')
    current: Union[DeleteNoteOutputVariant1Current, None] = Field(None, alias='current', description='Present only when conflict is true: the note as it stands now, so the caller can re-read before deciding whether to still delete.')
    code: Union[str, None] = Field(None, alias='code', description='Machine-readable denial code when ok is false: revision_conflict.')
    error: Union[str, None] = Field(None, alias='error', description='Human-readable failure reason when ok is false.')


DeleteNoteOutputVariant2DeliveryArtifactsItem = TypedDict('DeleteNoteOutputVariant2DeliveryArtifactsItem', {
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
DeleteNoteOutputVariant2DeliveryArtifactsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


DeleteNoteOutputVariant2DeliveryAvailableExportsItem = TypedDict('DeleteNoteOutputVariant2DeliveryAvailableExportsItem', {
    'artifactId': Required[str],
    'sourceArtifactId': Required[str],
    'filename': Required[Literal['result.md']],
    'contentType': Required[Literal['text/markdown; charset=utf-8']],
    'state': Required[Literal['on-demand']],
})
DeleteNoteOutputVariant2DeliveryAvailableExportsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


DeleteNoteOutputVariant2DeliveryStorageFailureVariant1 = TypedDict('DeleteNoteOutputVariant2DeliveryStorageFailureVariant1', {
    'artifactId': Required[Union[str, None]],
    'outcome': Required[Literal['unknown', 'bytes-stored-metadata-pending', 'failed']],
})
DeleteNoteOutputVariant2DeliveryStorageFailureVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


DeleteNoteOutputVariant2Delivery = TypedDict('DeleteNoteOutputVariant2Delivery', {
    'mode': Required[Literal['artifact']],
    'status': Required[Literal['complete', 'partial', 'unavailable']],
    'retainedRepresentation': Required[Literal['formatted-tool-result']],
    'sourceIsError': Required[bool],
    'artifacts': Required[list[DeleteNoteOutputVariant2DeliveryArtifactsItem]],
    'availableExports': NotRequired[list[DeleteNoteOutputVariant2DeliveryAvailableExportsItem]],
    'downloadLinksOmitted': Required[bool],
    'scopeOmittedFields': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'storageFailure': Required[Union[DeleteNoteOutputVariant2DeliveryStorageFailureVariant1, None]],
    'nextAction': Required[str],
})
DeleteNoteOutputVariant2Delivery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


DeleteNoteOutputVariant2RecoveryOperation = TypedDict('DeleteNoteOutputVariant2RecoveryOperation', {
    'runId': Required[Union[Annotated[str, Field(max_length=200)], None]],
    'idempotencyKey': Required[Annotated[str, Field(max_length=512)]],
    'state': Required[Annotated[str, Field(max_length=100)]],
})
DeleteNoteOutputVariant2RecoveryOperation.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


DeleteNoteOutputVariant2Recovery = TypedDict('DeleteNoteOutputVariant2Recovery', {
    'idempotencyKey': NotRequired[Annotated[str, Field(max_length=512)]],
    'operationId': NotRequired[Annotated[str, Field(max_length=200)]],
    'runId': NotRequired[Annotated[str, Field(max_length=200)]],
    'jobId': NotRequired[Annotated[str, Field(max_length=200)]],
    'operation': NotRequired[DeleteNoteOutputVariant2RecoveryOperation],
})
DeleteNoteOutputVariant2Recovery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class DeleteNoteOutputVariant2(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    delivery: DeleteNoteOutputVariant2Delivery = Field(..., alias='delivery', description='')
    preview: str = Field(..., alias='preview', description='')
    scope: dict[str, Union[str, Union[float, int], bool, None]] = Field(..., alias='scope', description='')
    recovery: DeleteNoteOutputVariant2Recovery = Field(..., alias='recovery', description='')


# Union schema: validate external payloads with TypeAdapter(DeleteNoteOutput).
DeleteNoteOutput = Union[DeleteNoteOutputVariant2, DeleteNoteOutputVariant1]

_DeleteNoteInputAdapter = TypeAdapter(DeleteNoteInput)
_DeleteNoteOutputAdapter = TypeAdapter(DeleteNoteOutput)