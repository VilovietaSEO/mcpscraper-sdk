from typing import Annotated, Any, Literal, Union
from typing_extensions import NotRequired, Required, TypedDict
from pydantic import BaseModel, ConfigDict, Field, TypeAdapter


class LibraryIngestInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=False)

    vault: Union[str, None] = Field(None, alias='vault', description='Vault to deposit into. Optional and normally omitted: raw scrapes always default to Library. Override only for a deliberate nonstandard migration.')
    title: Annotated[str, Field(min_length=1)] = Field(..., alias='title', description='Short human-readable title for the item; used to build the stored path. Must be non-empty.')
    content: Annotated[str, Field(min_length=1)] = Field(..., alias='content', description='The full captured text (scrape/transcript/output) to store and index. Must be non-empty.')
    source: Annotated[str, Field(min_length=1)] = Field(..., alias='source', description='Provenance of the content, e.g. a URL or tool name. Must be non-empty.')
    captured_at: Union[str, None] = Field(None, alias='capturedAt', description='ISO-8601 capture timestamp. Defaults to now and seeds the storage path with title. Preserve this timestamp and title on retries; omitting it can create another note.')
    summary: Union[str, None] = Field(None, alias='summary', description='Retrieval-ready source summary. Optional; a provenance summary is generated when omitted.')
    tags: Union[Annotated[list[str], Field(max_length=8)], None] = Field(None, alias='tags', description="Reviewed canonical tags. Tags resolve against the account's existing vocabulary; new tags require a one-line description. When omitted, only deterministic source-provenance tags are recorded.")
    tag_descriptions: Union[dict[str, str], None] = Field(None, alias='tagDescriptions', description='One-line meaning for any supplied tag that is new to the account, keyed by tag.')
    related: Union[list[str], None] = Field(None, alias='related', description='Reviewed same-vault Library note paths.')
    related_vault_notes: Union[list[str], None] = Field(None, alias='relatedVaultNotes', description='Reviewed cross-vault references in Vault::path.md form.')


class LibraryIngestOutputVariant1(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    ok: bool = Field(..., alias='ok', description='True when the item was stored; false on auth/scope error.')
    vault: Union[str, None] = Field(None, alias='vault', description='The vault the item was stored in (after defaulting).')
    note_id: Union[str, None] = Field(None, alias='noteId', description='Internal id of the created note.')
    path: Union[str, None] = Field(None, alias='path', description='Vault-relative path the item was stored at (under library/...).')
    indexed: Union[Union[float, int], None] = Field(None, alias='indexed', description='Number of search chunks indexed (0 if embedding failed but the note still saved).')
    next_step: Union[str, None] = Field(None, alias='nextStep', description='Recommended extraction action after the raw Library source is safe.')
    code: Union[str, None] = Field(None, alias='code', description='Machine-readable denial code when ok is false: quota_exceeded or free_cost_cap.')
    error: Union[str, None] = Field(None, alias='error', description='Human-readable failure reason when ok is false.')


LibraryIngestOutputVariant2DeliveryArtifactsItem = TypedDict('LibraryIngestOutputVariant2DeliveryArtifactsItem', {
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
LibraryIngestOutputVariant2DeliveryArtifactsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


LibraryIngestOutputVariant2DeliveryStorageFailureVariant1 = TypedDict('LibraryIngestOutputVariant2DeliveryStorageFailureVariant1', {
    'artifactId': Required[Union[str, None]],
    'outcome': Required[Literal['unknown', 'bytes-stored-metadata-pending', 'failed']],
})
LibraryIngestOutputVariant2DeliveryStorageFailureVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


LibraryIngestOutputVariant2Delivery = TypedDict('LibraryIngestOutputVariant2Delivery', {
    'mode': Required[Literal['artifact']],
    'status': Required[Literal['complete', 'partial', 'unavailable']],
    'retainedRepresentation': Required[Literal['formatted-tool-result']],
    'sourceIsError': Required[bool],
    'artifacts': Required[list[LibraryIngestOutputVariant2DeliveryArtifactsItem]],
    'downloadLinksOmitted': Required[bool],
    'scopeOmittedFields': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'storageFailure': Required[Union[LibraryIngestOutputVariant2DeliveryStorageFailureVariant1, None]],
    'nextAction': Required[str],
})
LibraryIngestOutputVariant2Delivery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


LibraryIngestOutputVariant2RecoveryOperation = TypedDict('LibraryIngestOutputVariant2RecoveryOperation', {
    'runId': Required[Union[Annotated[str, Field(max_length=200)], None]],
    'idempotencyKey': Required[Annotated[str, Field(max_length=512)]],
    'state': Required[Annotated[str, Field(max_length=100)]],
})
LibraryIngestOutputVariant2RecoveryOperation.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


LibraryIngestOutputVariant2Recovery = TypedDict('LibraryIngestOutputVariant2Recovery', {
    'idempotencyKey': NotRequired[Annotated[str, Field(max_length=512)]],
    'operationId': NotRequired[Annotated[str, Field(max_length=200)]],
    'runId': NotRequired[Annotated[str, Field(max_length=200)]],
    'jobId': NotRequired[Annotated[str, Field(max_length=200)]],
    'operation': NotRequired[LibraryIngestOutputVariant2RecoveryOperation],
})
LibraryIngestOutputVariant2Recovery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class LibraryIngestOutputVariant2(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    delivery: LibraryIngestOutputVariant2Delivery = Field(..., alias='delivery', description='')
    preview: str = Field(..., alias='preview', description='')
    scope: dict[str, Union[str, Union[float, int], bool, None]] = Field(..., alias='scope', description='')
    recovery: LibraryIngestOutputVariant2Recovery = Field(..., alias='recovery', description='')


# Union schema: validate external payloads with TypeAdapter(LibraryIngestOutput).
LibraryIngestOutput = Union[LibraryIngestOutputVariant2, LibraryIngestOutputVariant1]

_LibraryIngestInputAdapter = TypeAdapter(LibraryIngestInput)
_LibraryIngestOutputAdapter = TypeAdapter(LibraryIngestOutput)