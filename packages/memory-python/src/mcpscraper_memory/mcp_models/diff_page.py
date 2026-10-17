from typing import Annotated, Any, Literal, Union
from typing_extensions import NotRequired, Required, TypedDict
from pydantic import BaseModel, ConfigDict, Field, TypeAdapter


class DiffPageInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=False)

    url: str = Field(..., alias='url', description='Public http/https URL to check for changes since the last diff_page call.')
    reset_baseline: Union[bool, None] = Field(None, alias='resetBaseline', description='Discard any previously stored snapshot for this URL and capture the current content as a fresh baseline instead of diffing against history. Use when you deliberately want to restart change tracking.')


DiffPageOutputVariant1Summary = TypedDict('DiffPageOutputVariant1Summary', {
    'linesAdded': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'linesRemoved': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'percentChanged': Required[Union[Annotated[Union[float, int], Field(ge=0, le=100)], None]],
})
DiffPageOutputVariant1Summary.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


DiffPageOutputVariant1HunksItem = TypedDict('DiffPageOutputVariant1HunksItem', {
    'type': Required[Literal['added', 'removed']],
    'lines': Required[list[str]],
})
DiffPageOutputVariant1HunksItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class DiffPageOutputVariant1(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    url: str = Field(..., alias='url', description='')
    title: Union[str, None] = Field(..., alias='title', description='')
    status: Literal['baseline', 'unchanged', 'changed'] = Field(..., alias='status', description='"baseline" = first-ever check for this URL, or resetBaseline was used — nothing to compare against. "unchanged" = content hash matched the stored snapshot. "changed" = a diff was computed.')
    is_reset: bool = Field(..., alias='isReset', description="True only when resetBaseline discarded a real prior snapshot — distinguishes an explicit reset from a URL's true first-ever check.")
    previous_checked_at: Union[str, None] = Field(..., alias='previousCheckedAt', description='ISO timestamp of the snapshot this was compared against, or null if there was none.')
    current_checked_at: str = Field(..., alias='currentCheckedAt', description='ISO timestamp of this check, now stored as the new snapshot.')
    content_hash: str = Field(..., alias='contentHash', description='sha256 of the full (untruncated) page content just captured.')
    previous_content_hash: Union[str, None] = Field(..., alias='previousContentHash', description='')
    summary: DiffPageOutputVariant1Summary = Field(..., alias='summary', description='')
    hunks: list[DiffPageOutputVariant1HunksItem] = Field(..., alias='hunks', description='Ordered added/removed line hunks, capped for response size — see hunksTruncated.')
    content_truncated: bool = Field(..., alias='contentTruncated', description='True if the scraped page exceeded the 250,000-character storable cap and was truncated before hashing/diffing/storing — changes past that point are invisible to this comparison.')
    hunks_truncated: bool = Field(..., alias='hunksTruncated', description='True if the hunks list above was capped for response size — see hunksTruncatedReason.')
    hunks_truncated_reason: Union[str, None] = Field(..., alias='hunksTruncatedReason', description='')
    total_changed_line_count: Annotated[int, Field(ge=0, le=9007199254740991)] = Field(..., alias='totalChangedLineCount', description='Total changed lines found before any hunksTruncated capping was applied.')


DiffPageOutputVariant2DeliveryArtifactsItem = TypedDict('DiffPageOutputVariant2DeliveryArtifactsItem', {
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
DiffPageOutputVariant2DeliveryArtifactsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


DiffPageOutputVariant2DeliveryAvailableExportsItem = TypedDict('DiffPageOutputVariant2DeliveryAvailableExportsItem', {
    'artifactId': Required[str],
    'sourceArtifactId': Required[str],
    'filename': Required[Literal['result.md']],
    'contentType': Required[Literal['text/markdown; charset=utf-8']],
    'state': Required[Literal['on-demand']],
})
DiffPageOutputVariant2DeliveryAvailableExportsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


DiffPageOutputVariant2DeliveryStorageFailureVariant1 = TypedDict('DiffPageOutputVariant2DeliveryStorageFailureVariant1', {
    'artifactId': Required[Union[str, None]],
    'outcome': Required[Literal['unknown', 'bytes-stored-metadata-pending', 'failed']],
})
DiffPageOutputVariant2DeliveryStorageFailureVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


DiffPageOutputVariant2Delivery = TypedDict('DiffPageOutputVariant2Delivery', {
    'mode': Required[Literal['artifact']],
    'status': Required[Literal['complete', 'partial', 'unavailable']],
    'retainedRepresentation': Required[Literal['formatted-tool-result']],
    'sourceIsError': Required[bool],
    'artifacts': Required[list[DiffPageOutputVariant2DeliveryArtifactsItem]],
    'availableExports': NotRequired[list[DiffPageOutputVariant2DeliveryAvailableExportsItem]],
    'downloadLinksOmitted': Required[bool],
    'scopeOmittedFields': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'storageFailure': Required[Union[DiffPageOutputVariant2DeliveryStorageFailureVariant1, None]],
    'nextAction': Required[str],
})
DiffPageOutputVariant2Delivery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


DiffPageOutputVariant2RecoveryOperation = TypedDict('DiffPageOutputVariant2RecoveryOperation', {
    'runId': Required[Union[Annotated[str, Field(max_length=200)], None]],
    'idempotencyKey': Required[Annotated[str, Field(max_length=512)]],
    'state': Required[Annotated[str, Field(max_length=100)]],
})
DiffPageOutputVariant2RecoveryOperation.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


DiffPageOutputVariant2Recovery = TypedDict('DiffPageOutputVariant2Recovery', {
    'idempotencyKey': NotRequired[Annotated[str, Field(max_length=512)]],
    'operationId': NotRequired[Annotated[str, Field(max_length=200)]],
    'runId': NotRequired[Annotated[str, Field(max_length=200)]],
    'jobId': NotRequired[Annotated[str, Field(max_length=200)]],
    'operation': NotRequired[DiffPageOutputVariant2RecoveryOperation],
})
DiffPageOutputVariant2Recovery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class DiffPageOutputVariant2(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    delivery: DiffPageOutputVariant2Delivery = Field(..., alias='delivery', description='')
    preview: str = Field(..., alias='preview', description='')
    scope: dict[str, Union[str, Union[float, int], bool, None]] = Field(..., alias='scope', description='')
    recovery: DiffPageOutputVariant2Recovery = Field(..., alias='recovery', description='')


# Union schema: validate external payloads with TypeAdapter(DiffPageOutput).
DiffPageOutput = Union[DiffPageOutputVariant1, DiffPageOutputVariant2]

_DiffPageInputAdapter = TypeAdapter(DiffPageInput)
_DiffPageOutputAdapter = TypeAdapter(DiffPageOutput)