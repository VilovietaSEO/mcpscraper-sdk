from typing import Annotated, Any, Literal, Union
from typing_extensions import NotRequired, Required, TypedDict
from pydantic import BaseModel, ConfigDict, Field, TypeAdapter


class MemoryListInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=False)

    vault: Union[str, None] = Field(None, alias='vault', description='Vault to list. Optional; defaults to the session active vault, then the first vault the caller is entitled to.')
    all_vaults: Union[bool, None] = Field(None, alias='allVaults', description='Set true for one complete account-wide inventory across every entitled vault. Omit or set false for one vault. When true, vault is ignored and reads run sequentially to avoid backend contention.')
    kind: Union[Literal['note', 'library', 'capture', 'decision'], None] = Field(None, alias='kind', description='Filter to a single note kind. Optional; omit to list every kind in the vault.')
    tags: Union[list[str], None] = Field(None, alias='tags', description="Filter to notes tagged with any of these tags (matches the note's tags primitive). Optional; omit to not filter by tag.")


MemoryListOutputVariant1NotesItem = TypedDict('MemoryListOutputVariant1NotesItem', {
    'path': Required[str],
    'title': Required[str],
    'kind': Required[str],
    'tags': Required[list[str]],
    'updatedAt': Required[str],
})
MemoryListOutputVariant1NotesItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


MemoryListOutputVariant1VaultInventoriesItemNotesItem = TypedDict('MemoryListOutputVariant1VaultInventoriesItemNotesItem', {
    'path': Required[str],
    'title': Required[str],
    'kind': Required[str],
    'tags': Required[list[str]],
    'updatedAt': Required[str],
})
MemoryListOutputVariant1VaultInventoriesItemNotesItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


MemoryListOutputVariant1VaultInventoriesItem = TypedDict('MemoryListOutputVariant1VaultInventoriesItem', {
    'vault': Required[str],
    'noteCount': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'folderCount': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'notes': Required[list[MemoryListOutputVariant1VaultInventoriesItemNotesItem]],
    'folders': Required[list[str]],
})
MemoryListOutputVariant1VaultInventoriesItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class MemoryListOutputVariant1(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    ok: bool = Field(..., alias='ok', description='True when the listing succeeded; false on an auth/scope/lookup error.')
    scope: Union[Literal['vault', 'account'], None] = Field(None, alias='scope', description='Whether the result covers one logical vault or the whole entitled account.')
    partial: Union[bool, None] = Field(None, alias='partial', description='Account-wide mode only: true if one vault failed and vaultInventories contains only the completed prefix.')
    vault: Union[str, None] = Field(None, alias='vault', description='The vault that was actually listed (after defaulting).')
    notes: Union[list[MemoryListOutputVariant1NotesItem], None] = Field(None, alias='notes', description='The notes in the vault (metadata only, no content). Present when ok is true.')
    folders: Union[list[str], None] = Field(None, alias='folders', description='Sorted complete folder inventory derived from note paths, including represented nested parent folders. Present when ok is true.')
    vaults: Union[list[str], None] = Field(None, alias='vaults', description='All vaults the caller is entitled to, for choosing a different vault to list.')
    total_notes: Union[Annotated[int, Field(ge=0, le=9007199254740991)], None] = Field(None, alias='totalNotes', description='Account-wide mode only: total notes across every completed vault inventory.')
    total_folders: Union[Annotated[int, Field(ge=0, le=9007199254740991)], None] = Field(None, alias='totalFolders', description='Account-wide mode only: total represented folder instances across vaults.')
    vault_inventories: Union[list[MemoryListOutputVariant1VaultInventoriesItem], None] = Field(None, alias='vaultInventories', description='Account-wide mode only: complete note and folder inventories grouped by vault so paths remain unambiguous.')
    error: Union[str, None] = Field(None, alias='error', description='Human-readable failure reason when ok is false.')


MemoryListOutputVariant2DeliveryArtifactsItem = TypedDict('MemoryListOutputVariant2DeliveryArtifactsItem', {
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
MemoryListOutputVariant2DeliveryArtifactsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


MemoryListOutputVariant2DeliveryAvailableExportsItem = TypedDict('MemoryListOutputVariant2DeliveryAvailableExportsItem', {
    'artifactId': Required[str],
    'sourceArtifactId': Required[str],
    'filename': Required[Literal['result.md']],
    'contentType': Required[Literal['text/markdown; charset=utf-8']],
    'state': Required[Literal['on-demand']],
})
MemoryListOutputVariant2DeliveryAvailableExportsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


MemoryListOutputVariant2DeliveryStorageFailureVariant1 = TypedDict('MemoryListOutputVariant2DeliveryStorageFailureVariant1', {
    'artifactId': Required[Union[str, None]],
    'outcome': Required[Literal['unknown', 'bytes-stored-metadata-pending', 'failed']],
})
MemoryListOutputVariant2DeliveryStorageFailureVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


MemoryListOutputVariant2Delivery = TypedDict('MemoryListOutputVariant2Delivery', {
    'mode': Required[Literal['artifact']],
    'status': Required[Literal['complete', 'partial', 'unavailable']],
    'retainedRepresentation': Required[Literal['formatted-tool-result']],
    'sourceIsError': Required[bool],
    'artifacts': Required[list[MemoryListOutputVariant2DeliveryArtifactsItem]],
    'availableExports': NotRequired[list[MemoryListOutputVariant2DeliveryAvailableExportsItem]],
    'downloadLinksOmitted': Required[bool],
    'scopeOmittedFields': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'storageFailure': Required[Union[MemoryListOutputVariant2DeliveryStorageFailureVariant1, None]],
    'nextAction': Required[str],
})
MemoryListOutputVariant2Delivery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


MemoryListOutputVariant2RecoveryOperation = TypedDict('MemoryListOutputVariant2RecoveryOperation', {
    'runId': Required[Union[Annotated[str, Field(max_length=200)], None]],
    'idempotencyKey': Required[Annotated[str, Field(max_length=512)]],
    'state': Required[Annotated[str, Field(max_length=100)]],
})
MemoryListOutputVariant2RecoveryOperation.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


MemoryListOutputVariant2Recovery = TypedDict('MemoryListOutputVariant2Recovery', {
    'idempotencyKey': NotRequired[Annotated[str, Field(max_length=512)]],
    'operationId': NotRequired[Annotated[str, Field(max_length=200)]],
    'runId': NotRequired[Annotated[str, Field(max_length=200)]],
    'jobId': NotRequired[Annotated[str, Field(max_length=200)]],
    'operation': NotRequired[MemoryListOutputVariant2RecoveryOperation],
})
MemoryListOutputVariant2Recovery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class MemoryListOutputVariant2(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    delivery: MemoryListOutputVariant2Delivery = Field(..., alias='delivery', description='')
    preview: str = Field(..., alias='preview', description='')
    scope: dict[str, Union[str, Union[float, int], bool, None]] = Field(..., alias='scope', description='')
    recovery: MemoryListOutputVariant2Recovery = Field(..., alias='recovery', description='')


# Union schema: validate external payloads with TypeAdapter(MemoryListOutput).
MemoryListOutput = Union[MemoryListOutputVariant2, MemoryListOutputVariant1]

_MemoryListInputAdapter = TypeAdapter(MemoryListInput)
_MemoryListOutputAdapter = TypeAdapter(MemoryListOutput)