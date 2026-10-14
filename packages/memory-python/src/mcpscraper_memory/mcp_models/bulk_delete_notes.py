from typing import Annotated, Any, Literal, Union
from typing_extensions import NotRequired, Required, TypedDict
from pydantic import BaseModel, ConfigDict, Field, TypeAdapter


BulkDeleteNotesInputFiltersItem = TypedDict('BulkDeleteNotesInputFiltersItem', {
    'column': Required[Literal['path', 'title', 'kind', 'source', 'captured_at', 'created_at', 'updated_at', 'revision']],
    'op': Required[Literal['eq', 'neq', 'gt', 'gte', 'lt', 'lte', 'like', 'prefix', 'in']],
    'value': Required[Any],
})
BulkDeleteNotesInputFiltersItem.__pydantic_config__ = ConfigDict(extra="allow", strict=False)


class BulkDeleteNotesInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=False)

    vault: Union[str, None] = Field(None, alias='vault', description='Vault to delete from. Optional; defaults to the session active vault, then the first vault the caller is entitled to.')
    filters: Union[list[BulkDeleteNotesInputFiltersItem], None] = Field(None, alias='filters', description='Filters to AND together. At least one of filters/tags is required.')
    tags: Union[list[str], None] = Field(None, alias='tags', description='Match notes carrying ANY of these tags (ORed among themselves, ANDed with filters). At least one of filters/tags is required.')
    dry_run: Union[bool, None] = Field(None, alias='dryRun', description='When true (default), previews matches without deleting anything. Pass false to actually delete.')


BulkDeleteNotesOutputVariant1SampleItem = TypedDict('BulkDeleteNotesOutputVariant1SampleItem', {
    'path': Required[str],
    'title': Required[str],
    'updatedAt': Required[str],
})
BulkDeleteNotesOutputVariant1SampleItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class BulkDeleteNotesOutputVariant1(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    ok: bool = Field(..., alias='ok', description='True on success; false on auth/scope/validation error.')
    vault: Union[str, None] = Field(None, alias='vault', description='The vault operated on (after defaulting). Present when ok is true.')
    dry_run: Union[bool, None] = Field(None, alias='dryRun', description='Echoes whether this call was a preview or a real delete.')
    match_count: Union[Union[float, int], None] = Field(None, alias='matchCount', description='Number of notes matching the filters. Present on a dry run.')
    sample: Union[list[BulkDeleteNotesOutputVariant1SampleItem], None] = Field(None, alias='sample', description='Up to 20 matching notes, most-recently-updated first. Present on a dry run.')
    deleted: Union[Union[float, int], None] = Field(None, alias='deleted', description='Number of notes actually deleted. Present when dryRun is false.')
    deleted_paths: Union[list[str], None] = Field(None, alias='deletedPaths', description='Paths of the deleted notes. Present when dryRun is false.')
    error: Union[str, None] = Field(None, alias='error', description='Human-readable failure reason when ok is false.')


BulkDeleteNotesOutputVariant2DeliveryArtifactsItem = TypedDict('BulkDeleteNotesOutputVariant2DeliveryArtifactsItem', {
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
BulkDeleteNotesOutputVariant2DeliveryArtifactsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


BulkDeleteNotesOutputVariant2DeliveryStorageFailureVariant1 = TypedDict('BulkDeleteNotesOutputVariant2DeliveryStorageFailureVariant1', {
    'artifactId': Required[Union[str, None]],
    'outcome': Required[Literal['unknown', 'bytes-stored-metadata-pending', 'failed']],
})
BulkDeleteNotesOutputVariant2DeliveryStorageFailureVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


BulkDeleteNotesOutputVariant2Delivery = TypedDict('BulkDeleteNotesOutputVariant2Delivery', {
    'mode': Required[Literal['artifact']],
    'status': Required[Literal['complete', 'partial', 'unavailable']],
    'retainedRepresentation': Required[Literal['formatted-tool-result']],
    'sourceIsError': Required[bool],
    'artifacts': Required[list[BulkDeleteNotesOutputVariant2DeliveryArtifactsItem]],
    'downloadLinksOmitted': Required[bool],
    'scopeOmittedFields': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'storageFailure': Required[Union[BulkDeleteNotesOutputVariant2DeliveryStorageFailureVariant1, None]],
    'nextAction': Required[str],
})
BulkDeleteNotesOutputVariant2Delivery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


BulkDeleteNotesOutputVariant2RecoveryOperation = TypedDict('BulkDeleteNotesOutputVariant2RecoveryOperation', {
    'runId': Required[Union[Annotated[str, Field(max_length=200)], None]],
    'idempotencyKey': Required[Annotated[str, Field(max_length=512)]],
    'state': Required[Annotated[str, Field(max_length=100)]],
})
BulkDeleteNotesOutputVariant2RecoveryOperation.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


BulkDeleteNotesOutputVariant2Recovery = TypedDict('BulkDeleteNotesOutputVariant2Recovery', {
    'idempotencyKey': NotRequired[Annotated[str, Field(max_length=512)]],
    'operationId': NotRequired[Annotated[str, Field(max_length=200)]],
    'runId': NotRequired[Annotated[str, Field(max_length=200)]],
    'jobId': NotRequired[Annotated[str, Field(max_length=200)]],
    'operation': NotRequired[BulkDeleteNotesOutputVariant2RecoveryOperation],
})
BulkDeleteNotesOutputVariant2Recovery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class BulkDeleteNotesOutputVariant2(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    delivery: BulkDeleteNotesOutputVariant2Delivery = Field(..., alias='delivery', description='')
    preview: str = Field(..., alias='preview', description='')
    scope: dict[str, Union[str, Union[float, int], bool, None]] = Field(..., alias='scope', description='')
    recovery: BulkDeleteNotesOutputVariant2Recovery = Field(..., alias='recovery', description='')


# Union schema: validate external payloads with TypeAdapter(BulkDeleteNotesOutput).
BulkDeleteNotesOutput = Union[BulkDeleteNotesOutputVariant2, BulkDeleteNotesOutputVariant1]

_BulkDeleteNotesInputAdapter = TypeAdapter(BulkDeleteNotesInput)
_BulkDeleteNotesOutputAdapter = TypeAdapter(BulkDeleteNotesOutput)