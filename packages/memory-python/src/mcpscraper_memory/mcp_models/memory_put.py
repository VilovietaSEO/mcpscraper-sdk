from typing import Annotated, Any, Literal, Union
from typing_extensions import NotRequired, Required, TypedDict
from pydantic import BaseModel, ConfigDict, Field, TypeAdapter


MemoryPutInputProps = TypedDict('MemoryPutInputProps', {
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
MemoryPutInputProps.__pydantic_config__ = ConfigDict(extra="allow", strict=False)


class MemoryPutInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=False)

    vault: Union[str, None] = Field(None, alias='vault', description='Vault to write to. Optional; defaults to the session active vault, then the first vault the caller is entitled to. Pick the vault whose job matches the content; use prepare-memory-write for the live vault contract or list-vaults for vault inventory rather than defaulting blindly — e.g. a lesson learned goes in Knowledge, the raw source it came from goes in Library, a broken feature goes in Issues, a named real-world initiative goes in Projects. Research People/Organizations and CRM People/Organizations require their specialized tools and are always rejected here. For Deals, Projects, Tasks, or Communication records, first use prepare-memory-write then memory-capture so relationships and approval state are validated.')
    path: Union[str, None] = Field(None, alias='path', description='Vault-relative note path to create or overwrite, e.g. projects/q3-plan. Writing an existing path replaces it. Required unless shareId is given.')
    share_id: Union[str, None] = Field(None, alias='shareId', description='Edit a note someone individually shared with you and you accepted (accept-share), by its shareId, instead of vault+path. Requires the share to grant edit permission, and baseRevision is mandatory (get the current revision first) since you are editing alongside the owner and possibly others.')
    title: Union[str, None] = Field(None, alias='title', description='Optional human-readable title; defaults are derived from the path when omitted.')
    content: Annotated[str, Field(min_length=1)] = Field(..., alias='content', description='The complete note body to store and index. Content is replace-all: for an edit, first read the current note, merge the requested change into its full body, and never pass only the changed fragment. Must be non-empty.')
    props: Union[MemoryPutInputProps, None] = Field(None, alias='props', description='Obsidian note primitives plus vault-specific template fields. On edits, supplied fields patch the stored props instead of replacing the whole object; pass an empty array to deliberately clear a link list. Type/domain/folder also steer routing when no vault is given.')
    base_revision: Union[Union[float, int], None] = Field(None, alias='baseRevision', description='Revision from the current note read or prior successful write. Pass it with the complete merged body when editing: a mismatch rejects the write and returns the current note for reconciliation. Never replay the stale body unchanged. Required for edits through shareId; omission on owned notes permits last-write-wins.')
    tag_descriptions: Union[dict[str, str], None] = Field(None, alias='tagDescriptions', description="One-line meaning for any tag in props.tags that is new to the account, keyed by tag. Tags resolve against the account's existing vocabulary; new tags require a one-line description.")


MemoryPutOutputVariant1Note = TypedDict('MemoryPutOutputVariant1Note', {
    'path': Required[str],
    'title': Required[str],
    'updatedAt': Required[str],
    'revision': Required[Union[float, int]],
})
MemoryPutOutputVariant1Note.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


MemoryPutOutputVariant1Current = TypedDict('MemoryPutOutputVariant1Current', {
    'content': Required[str],
    'revision': Required[Union[float, int]],
    'updatedBy': Required[Union[str, None]],
    'updatedAt': Required[str],
})
MemoryPutOutputVariant1Current.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class MemoryPutOutputVariant1(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    ok: bool = Field(..., alias='ok', description='True when the note was stored; false on auth/scope error, empty content, or a revision conflict.')
    note: Union[MemoryPutOutputVariant1Note, None] = Field(None, alias='note', description='The stored note metadata. Present when ok is true.')
    indexed: Union[Union[float, int], None] = Field(None, alias='indexed', description='Number of search chunks indexed for the content (0 if embedding failed but the note still saved).')
    conflict: Union[bool, None] = Field(None, alias='conflict', description='True when baseRevision did not match the current revision: someone else changed the note first. No write happened.')
    current: Union[MemoryPutOutputVariant1Current, None] = Field(None, alias='current', description='Present only when conflict is true: the note as it stands now, so the caller can reconcile and retry without another round trip.')
    code: Union[str, None] = Field(None, alias='code', description='Machine-readable denial code when ok is false: quota_exceeded, free_cost_cap, or revision_conflict.')
    error: Union[str, None] = Field(None, alias='error', description='Human-readable failure reason when ok is false.')


MemoryPutOutputVariant2DeliveryArtifactsItem = TypedDict('MemoryPutOutputVariant2DeliveryArtifactsItem', {
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
MemoryPutOutputVariant2DeliveryArtifactsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


MemoryPutOutputVariant2DeliveryStorageFailureVariant1 = TypedDict('MemoryPutOutputVariant2DeliveryStorageFailureVariant1', {
    'artifactId': Required[Union[str, None]],
    'outcome': Required[Literal['unknown', 'bytes-stored-metadata-pending', 'failed']],
})
MemoryPutOutputVariant2DeliveryStorageFailureVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


MemoryPutOutputVariant2Delivery = TypedDict('MemoryPutOutputVariant2Delivery', {
    'mode': Required[Literal['artifact']],
    'status': Required[Literal['complete', 'partial', 'unavailable']],
    'retainedRepresentation': Required[Literal['formatted-tool-result']],
    'sourceIsError': Required[bool],
    'artifacts': Required[list[MemoryPutOutputVariant2DeliveryArtifactsItem]],
    'downloadLinksOmitted': Required[bool],
    'scopeOmittedFields': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'storageFailure': Required[Union[MemoryPutOutputVariant2DeliveryStorageFailureVariant1, None]],
    'nextAction': Required[str],
})
MemoryPutOutputVariant2Delivery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


MemoryPutOutputVariant2RecoveryOperation = TypedDict('MemoryPutOutputVariant2RecoveryOperation', {
    'runId': Required[Union[Annotated[str, Field(max_length=200)], None]],
    'idempotencyKey': Required[Annotated[str, Field(max_length=512)]],
    'state': Required[Annotated[str, Field(max_length=100)]],
})
MemoryPutOutputVariant2RecoveryOperation.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


MemoryPutOutputVariant2Recovery = TypedDict('MemoryPutOutputVariant2Recovery', {
    'idempotencyKey': NotRequired[Annotated[str, Field(max_length=512)]],
    'operationId': NotRequired[Annotated[str, Field(max_length=200)]],
    'runId': NotRequired[Annotated[str, Field(max_length=200)]],
    'jobId': NotRequired[Annotated[str, Field(max_length=200)]],
    'operation': NotRequired[MemoryPutOutputVariant2RecoveryOperation],
})
MemoryPutOutputVariant2Recovery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class MemoryPutOutputVariant2(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    delivery: MemoryPutOutputVariant2Delivery = Field(..., alias='delivery', description='')
    preview: str = Field(..., alias='preview', description='')
    scope: dict[str, Union[str, Union[float, int], bool, None]] = Field(..., alias='scope', description='')
    recovery: MemoryPutOutputVariant2Recovery = Field(..., alias='recovery', description='')


# Union schema: validate external payloads with TypeAdapter(MemoryPutOutput).
MemoryPutOutput = Union[MemoryPutOutputVariant2, MemoryPutOutputVariant1]

_MemoryPutInputAdapter = TypeAdapter(MemoryPutInput)
_MemoryPutOutputAdapter = TypeAdapter(MemoryPutOutput)