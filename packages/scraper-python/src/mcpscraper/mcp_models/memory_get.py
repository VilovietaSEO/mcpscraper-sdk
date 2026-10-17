from typing import Annotated, Any, Literal, Union
from typing_extensions import NotRequired, Required, TypedDict
from pydantic import BaseModel, ConfigDict, Field, TypeAdapter


class MemoryGetInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=False)

    vault: Union[str, None] = Field(None, alias='vault', description='Vault to read from. Optional; defaults to the session active vault, then the first vault the caller is entitled to. Ignored when shareId is given.')
    path: Union[str, None] = Field(None, alias='path', description='Exact vault-relative note path to read, e.g. projects/q3-plan (as returned by memory-list or recall). Required unless shareId is given.')
    share_id: Union[str, None] = Field(None, alias='shareId', description='Read a note shared with you and accepted, by its shareId (from note-inbox or list-shared-with-me), instead of vault+path.')


MemoryGetOutputVariant1NoteProps = TypedDict('MemoryGetOutputVariant1NoteProps', {
    'status': NotRequired[str],
    'summary': NotRequired[str],
    'tags': NotRequired[list[str]],
    'pinned': NotRequired[bool],
    'delete_after': NotRequired[str],
    'source_type': NotRequired[str],
    'source_ref': NotRequired[str],
    'related': NotRequired[list[str]],
    'related_vault_notes': NotRequired[list[str]],
    'embed': NotRequired[bool],
    'embed_priority': NotRequired[Literal['low', 'normal', 'high']],
    'embedding_summary': NotRequired[str],
    'type': NotRequired[str],
    'domain': NotRequired[str],
    'folder': NotRequired[str],
    'script_links': NotRequired[list[str]],
    'reference_links': NotRequired[list[str]],
    'template_links': NotRequired[list[str]],
    'parentMessageId': NotRequired[str],
})
MemoryGetOutputVariant1NoteProps.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


MemoryGetOutputVariant1Note = TypedDict('MemoryGetOutputVariant1Note', {
    'path': Required[str],
    'title': Required[str],
    'content': Required[str],
    'kind': Required[str],
    'source': Required[str],
    'updatedAt': Required[str],
    'capturedAt': Required[str],
    'revision': Required[Union[float, int]],
    'updatedBy': Required[Union[str, None]],
    'props': NotRequired[MemoryGetOutputVariant1NoteProps],
    'sharedBy': NotRequired[str],
    'othersEditing': NotRequired[list[str]],
})
MemoryGetOutputVariant1Note.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class MemoryGetOutputVariant1(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    ok: bool = Field(..., alias='ok', description='True when the note was found and returned; false on error or not-found.')
    note: Union[MemoryGetOutputVariant1Note, None] = Field(None, alias='note', description='The full note. Present when ok is true.')
    error: Union[str, None] = Field(None, alias='error', description='Human-readable failure reason when ok is false (e.g. "note not found").')


MemoryGetOutputVariant2DeliveryArtifactsItem = TypedDict('MemoryGetOutputVariant2DeliveryArtifactsItem', {
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
MemoryGetOutputVariant2DeliveryArtifactsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


MemoryGetOutputVariant2DeliveryAvailableExportsItem = TypedDict('MemoryGetOutputVariant2DeliveryAvailableExportsItem', {
    'artifactId': Required[str],
    'sourceArtifactId': Required[str],
    'filename': Required[Literal['result.md']],
    'contentType': Required[Literal['text/markdown; charset=utf-8']],
    'state': Required[Literal['on-demand']],
})
MemoryGetOutputVariant2DeliveryAvailableExportsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


MemoryGetOutputVariant2DeliveryStorageFailureVariant1 = TypedDict('MemoryGetOutputVariant2DeliveryStorageFailureVariant1', {
    'artifactId': Required[Union[str, None]],
    'outcome': Required[Literal['unknown', 'bytes-stored-metadata-pending', 'failed']],
})
MemoryGetOutputVariant2DeliveryStorageFailureVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


MemoryGetOutputVariant2Delivery = TypedDict('MemoryGetOutputVariant2Delivery', {
    'mode': Required[Literal['artifact']],
    'status': Required[Literal['complete', 'partial', 'unavailable']],
    'retainedRepresentation': Required[Literal['formatted-tool-result']],
    'sourceIsError': Required[bool],
    'artifacts': Required[list[MemoryGetOutputVariant2DeliveryArtifactsItem]],
    'availableExports': NotRequired[list[MemoryGetOutputVariant2DeliveryAvailableExportsItem]],
    'downloadLinksOmitted': Required[bool],
    'scopeOmittedFields': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'storageFailure': Required[Union[MemoryGetOutputVariant2DeliveryStorageFailureVariant1, None]],
    'nextAction': Required[str],
})
MemoryGetOutputVariant2Delivery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


MemoryGetOutputVariant2RecoveryOperation = TypedDict('MemoryGetOutputVariant2RecoveryOperation', {
    'runId': Required[Union[Annotated[str, Field(max_length=200)], None]],
    'idempotencyKey': Required[Annotated[str, Field(max_length=512)]],
    'state': Required[Annotated[str, Field(max_length=100)]],
})
MemoryGetOutputVariant2RecoveryOperation.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


MemoryGetOutputVariant2Recovery = TypedDict('MemoryGetOutputVariant2Recovery', {
    'idempotencyKey': NotRequired[Annotated[str, Field(max_length=512)]],
    'operationId': NotRequired[Annotated[str, Field(max_length=200)]],
    'runId': NotRequired[Annotated[str, Field(max_length=200)]],
    'jobId': NotRequired[Annotated[str, Field(max_length=200)]],
    'operation': NotRequired[MemoryGetOutputVariant2RecoveryOperation],
})
MemoryGetOutputVariant2Recovery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class MemoryGetOutputVariant2(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    delivery: MemoryGetOutputVariant2Delivery = Field(..., alias='delivery', description='')
    preview: str = Field(..., alias='preview', description='')
    scope: dict[str, Union[str, Union[float, int], bool, None]] = Field(..., alias='scope', description='')
    recovery: MemoryGetOutputVariant2Recovery = Field(..., alias='recovery', description='')


# Union schema: validate external payloads with TypeAdapter(MemoryGetOutput).
MemoryGetOutput = Union[MemoryGetOutputVariant2, MemoryGetOutputVariant1]

_MemoryGetInputAdapter = TypeAdapter(MemoryGetInput)
_MemoryGetOutputAdapter = TypeAdapter(MemoryGetOutput)