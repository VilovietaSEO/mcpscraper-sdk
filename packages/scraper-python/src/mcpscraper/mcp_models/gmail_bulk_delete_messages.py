from typing import Annotated, Any, Literal, Union
from typing_extensions import NotRequired, Required, TypedDict
from pydantic import BaseModel, ConfigDict, Field, TypeAdapter


class GmailBulkDeleteMessagesInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=False)

    confirmed: Union[bool, None] = Field(None, alias='confirmed', description='Set true only after the person explicitly approves permanent deletion of this exact frozen message count; otherwise a capable client may request confirmation.')
    confirm_permanent_delete: Literal[True] = Field(..., alias='confirmPermanentDelete', description='Required literal boolean proving the caller selected irreversible deletion rather than reversible trash.')
    idempotency_key: Annotated[str, Field(min_length=8, max_length=200)] = Field(..., alias='idempotencyKey', description='Stable retry key bound to this exact deletion receipt; a conflicting reuse fails before mutation.')
    connection_id: Annotated[str, Field(min_length=1, max_length=500)] = Field(..., alias='connectionId', description='The tenant-owned Gmail connectionId bound into this immutable selection.')
    selection_id: Annotated[str, Field(min_length=1, max_length=500)] = Field(..., alias='selectionId', description='Selection prepared with purpose mailbox_action.')
    selection_sha256: str = Field(..., alias='selectionSha256', description='Unchanged selection digest from gmail_prepare_selection.')
    expected_count: Annotated[int, Field(ge=1, le=5000)] = Field(..., alias='expectedCount', description='Exact reviewed selection count; the call fails if it no longer matches the receipt.')


GmailBulkDeleteMessagesOutputVariant1FailedChunksItem = TypedDict('GmailBulkDeleteMessagesOutputVariant1FailedChunksItem', {
    'chunk': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'code': Required[str],
    'retryable': NotRequired[bool],
})
GmailBulkDeleteMessagesOutputVariant1FailedChunksItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class GmailBulkDeleteMessagesOutputVariant1(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    ok: bool = Field(..., alias='ok', description='')
    action_id: Annotated[str, Field(min_length=1, max_length=500)] = Field(..., alias='actionId', description='')
    selection_id: Annotated[str, Field(min_length=1, max_length=500)] = Field(..., alias='selectionId', description='')
    expected_count: Annotated[int, Field(ge=1, le=5000)] = Field(..., alias='expectedCount', description='')
    changed_count: Annotated[int, Field(ge=0, le=9007199254740991)] = Field(..., alias='changedCount', description='')
    failed_count: Annotated[int, Field(ge=0, le=9007199254740991)] = Field(..., alias='failedCount', description='')
    status: Literal['running', 'complete', 'partial', 'failed'] = Field(..., alias='status', description='')
    replay: Union[bool, None] = Field(None, alias='replay', description='')
    failed_chunks: Union[Annotated[list[GmailBulkDeleteMessagesOutputVariant1FailedChunksItem], Field(max_length=20)], None] = Field(None, alias='failedChunks', description='')
    irreversible: Literal[True] = Field(..., alias='irreversible', description='')
    provider_guarantee: str = Field(..., alias='providerGuarantee', description='')
    error: Union[str, None] = Field(..., alias='error', description='')


GmailBulkDeleteMessagesOutputVariant2DeliveryArtifactsItem = TypedDict('GmailBulkDeleteMessagesOutputVariant2DeliveryArtifactsItem', {
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
GmailBulkDeleteMessagesOutputVariant2DeliveryArtifactsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


GmailBulkDeleteMessagesOutputVariant2DeliveryAvailableExportsItem = TypedDict('GmailBulkDeleteMessagesOutputVariant2DeliveryAvailableExportsItem', {
    'artifactId': Required[str],
    'sourceArtifactId': Required[str],
    'filename': Required[Literal['result.md']],
    'contentType': Required[Literal['text/markdown; charset=utf-8']],
    'state': Required[Literal['on-demand']],
})
GmailBulkDeleteMessagesOutputVariant2DeliveryAvailableExportsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


GmailBulkDeleteMessagesOutputVariant2DeliveryStorageFailureVariant1 = TypedDict('GmailBulkDeleteMessagesOutputVariant2DeliveryStorageFailureVariant1', {
    'artifactId': Required[Union[str, None]],
    'outcome': Required[Literal['unknown', 'bytes-stored-metadata-pending', 'failed']],
})
GmailBulkDeleteMessagesOutputVariant2DeliveryStorageFailureVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


GmailBulkDeleteMessagesOutputVariant2Delivery = TypedDict('GmailBulkDeleteMessagesOutputVariant2Delivery', {
    'mode': Required[Literal['artifact']],
    'status': Required[Literal['complete', 'partial', 'unavailable']],
    'retainedRepresentation': Required[Literal['formatted-tool-result']],
    'sourceIsError': Required[bool],
    'artifacts': Required[list[GmailBulkDeleteMessagesOutputVariant2DeliveryArtifactsItem]],
    'availableExports': NotRequired[list[GmailBulkDeleteMessagesOutputVariant2DeliveryAvailableExportsItem]],
    'downloadLinksOmitted': Required[bool],
    'scopeOmittedFields': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'storageFailure': Required[Union[GmailBulkDeleteMessagesOutputVariant2DeliveryStorageFailureVariant1, None]],
    'nextAction': Required[str],
})
GmailBulkDeleteMessagesOutputVariant2Delivery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


GmailBulkDeleteMessagesOutputVariant2RecoveryOperation = TypedDict('GmailBulkDeleteMessagesOutputVariant2RecoveryOperation', {
    'runId': Required[Union[Annotated[str, Field(max_length=200)], None]],
    'idempotencyKey': Required[Annotated[str, Field(max_length=512)]],
    'state': Required[Annotated[str, Field(max_length=100)]],
})
GmailBulkDeleteMessagesOutputVariant2RecoveryOperation.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


GmailBulkDeleteMessagesOutputVariant2Recovery = TypedDict('GmailBulkDeleteMessagesOutputVariant2Recovery', {
    'idempotencyKey': NotRequired[Annotated[str, Field(max_length=512)]],
    'operationId': NotRequired[Annotated[str, Field(max_length=200)]],
    'runId': NotRequired[Annotated[str, Field(max_length=200)]],
    'jobId': NotRequired[Annotated[str, Field(max_length=200)]],
    'operation': NotRequired[GmailBulkDeleteMessagesOutputVariant2RecoveryOperation],
})
GmailBulkDeleteMessagesOutputVariant2Recovery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class GmailBulkDeleteMessagesOutputVariant2(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    delivery: GmailBulkDeleteMessagesOutputVariant2Delivery = Field(..., alias='delivery', description='')
    preview: str = Field(..., alias='preview', description='')
    scope: dict[str, Union[str, Union[float, int], bool, None]] = Field(..., alias='scope', description='')
    recovery: GmailBulkDeleteMessagesOutputVariant2Recovery = Field(..., alias='recovery', description='')


# Union schema: validate external payloads with TypeAdapter(GmailBulkDeleteMessagesOutput).
GmailBulkDeleteMessagesOutput = Union[GmailBulkDeleteMessagesOutputVariant1, GmailBulkDeleteMessagesOutputVariant2]

_GmailBulkDeleteMessagesInputAdapter = TypeAdapter(GmailBulkDeleteMessagesInput)
_GmailBulkDeleteMessagesOutputAdapter = TypeAdapter(GmailBulkDeleteMessagesOutput)