from typing import Annotated, Any, Literal, Union
from typing_extensions import NotRequired, Required, TypedDict
from pydantic import BaseModel, ConfigDict, Field, TypeAdapter


GmailBulkManageMessagesInputOperationVariant1 = TypedDict('GmailBulkManageMessagesInputOperationVariant1', {
    'kind': Required[Literal['mark_read']],
})
GmailBulkManageMessagesInputOperationVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=False)


GmailBulkManageMessagesInputOperationVariant2 = TypedDict('GmailBulkManageMessagesInputOperationVariant2', {
    'kind': Required[Literal['mark_unread']],
})
GmailBulkManageMessagesInputOperationVariant2.__pydantic_config__ = ConfigDict(extra="allow", strict=False)


GmailBulkManageMessagesInputOperationVariant3 = TypedDict('GmailBulkManageMessagesInputOperationVariant3', {
    'kind': Required[Literal['archive']],
})
GmailBulkManageMessagesInputOperationVariant3.__pydantic_config__ = ConfigDict(extra="allow", strict=False)


GmailBulkManageMessagesInputOperationVariant4 = TypedDict('GmailBulkManageMessagesInputOperationVariant4', {
    'kind': Required[Literal['move_to_inbox']],
})
GmailBulkManageMessagesInputOperationVariant4.__pydantic_config__ = ConfigDict(extra="allow", strict=False)


GmailBulkManageMessagesInputOperationVariant5 = TypedDict('GmailBulkManageMessagesInputOperationVariant5', {
    'kind': Required[Literal['trash']],
})
GmailBulkManageMessagesInputOperationVariant5.__pydantic_config__ = ConfigDict(extra="allow", strict=False)


GmailBulkManageMessagesInputOperationVariant6 = TypedDict('GmailBulkManageMessagesInputOperationVariant6', {
    'kind': Required[Literal['restore']],
})
GmailBulkManageMessagesInputOperationVariant6.__pydantic_config__ = ConfigDict(extra="allow", strict=False)


GmailBulkManageMessagesInputOperationVariant7 = TypedDict('GmailBulkManageMessagesInputOperationVariant7', {
    'kind': Required[Literal['labels']],
    'addLabelIds': NotRequired[Annotated[list[Annotated[str, Field(min_length=1)]], Field(min_length=1, max_length=100)]],
    'removeLabelIds': NotRequired[Annotated[list[Annotated[str, Field(min_length=1)]], Field(min_length=1, max_length=100)]],
})
GmailBulkManageMessagesInputOperationVariant7.__pydantic_config__ = ConfigDict(extra="allow", strict=False)


class GmailBulkManageMessagesInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=False)

    confirmed: Union[bool, None] = Field(None, alias='confirmed', description='Set true only after the person explicitly approves this exact operation and frozen message count; otherwise a capable client may request confirmation.')
    idempotency_key: Annotated[str, Field(min_length=8, max_length=200)] = Field(..., alias='idempotencyKey', description='Stable retry key bound to this exact selection receipt and operation; a conflicting reuse fails before mutation.')
    connection_id: Annotated[str, Field(min_length=1, max_length=500)] = Field(..., alias='connectionId', description='The tenant-owned Gmail connectionId bound into this immutable selection.')
    selection_id: Annotated[str, Field(min_length=1, max_length=500)] = Field(..., alias='selectionId', description='Selection prepared with purpose mailbox_action.')
    selection_sha256: str = Field(..., alias='selectionSha256', description='Unchanged selection digest from gmail_prepare_selection.')
    expected_count: Annotated[int, Field(ge=1, le=5000)] = Field(..., alias='expectedCount', description='Exact reviewed selection count; the call fails if it no longer matches the receipt.')
    operation: Union[GmailBulkManageMessagesInputOperationVariant1, GmailBulkManageMessagesInputOperationVariant2, GmailBulkManageMessagesInputOperationVariant3, GmailBulkManageMessagesInputOperationVariant4, GmailBulkManageMessagesInputOperationVariant5, GmailBulkManageMessagesInputOperationVariant6, GmailBulkManageMessagesInputOperationVariant7] = Field(..., alias='operation', description='One reversible mailbox operation; permanent deletion requires gmail_bulk_delete_messages.')


GmailBulkManageMessagesOutputVariant1FailedChunksItem = TypedDict('GmailBulkManageMessagesOutputVariant1FailedChunksItem', {
    'chunk': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'code': Required[str],
    'retryable': NotRequired[bool],
})
GmailBulkManageMessagesOutputVariant1FailedChunksItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class GmailBulkManageMessagesOutputVariant1(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    ok: bool = Field(..., alias='ok', description='')
    action_id: Annotated[str, Field(min_length=1, max_length=500)] = Field(..., alias='actionId', description='')
    selection_id: Annotated[str, Field(min_length=1, max_length=500)] = Field(..., alias='selectionId', description='')
    expected_count: Annotated[int, Field(ge=1, le=5000)] = Field(..., alias='expectedCount', description='')
    changed_count: Annotated[int, Field(ge=0, le=9007199254740991)] = Field(..., alias='changedCount', description='')
    failed_count: Annotated[int, Field(ge=0, le=9007199254740991)] = Field(..., alias='failedCount', description='')
    status: Literal['running', 'complete', 'partial', 'failed'] = Field(..., alias='status', description='')
    replay: Union[bool, None] = Field(None, alias='replay', description='')
    failed_chunks: Union[Annotated[list[GmailBulkManageMessagesOutputVariant1FailedChunksItem], Field(max_length=20)], None] = Field(None, alias='failedChunks', description='')
    error: Union[str, None] = Field(..., alias='error', description='')


GmailBulkManageMessagesOutputVariant2DeliveryArtifactsItem = TypedDict('GmailBulkManageMessagesOutputVariant2DeliveryArtifactsItem', {
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
GmailBulkManageMessagesOutputVariant2DeliveryArtifactsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


GmailBulkManageMessagesOutputVariant2DeliveryStorageFailureVariant1 = TypedDict('GmailBulkManageMessagesOutputVariant2DeliveryStorageFailureVariant1', {
    'artifactId': Required[Union[str, None]],
    'outcome': Required[Literal['unknown', 'bytes-stored-metadata-pending', 'failed']],
})
GmailBulkManageMessagesOutputVariant2DeliveryStorageFailureVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


GmailBulkManageMessagesOutputVariant2Delivery = TypedDict('GmailBulkManageMessagesOutputVariant2Delivery', {
    'mode': Required[Literal['artifact']],
    'status': Required[Literal['complete', 'partial', 'unavailable']],
    'retainedRepresentation': Required[Literal['formatted-tool-result']],
    'sourceIsError': Required[bool],
    'artifacts': Required[list[GmailBulkManageMessagesOutputVariant2DeliveryArtifactsItem]],
    'downloadLinksOmitted': Required[bool],
    'scopeOmittedFields': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'storageFailure': Required[Union[GmailBulkManageMessagesOutputVariant2DeliveryStorageFailureVariant1, None]],
    'nextAction': Required[str],
})
GmailBulkManageMessagesOutputVariant2Delivery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


GmailBulkManageMessagesOutputVariant2RecoveryOperation = TypedDict('GmailBulkManageMessagesOutputVariant2RecoveryOperation', {
    'runId': Required[Union[Annotated[str, Field(max_length=200)], None]],
    'idempotencyKey': Required[Annotated[str, Field(max_length=512)]],
    'state': Required[Annotated[str, Field(max_length=100)]],
})
GmailBulkManageMessagesOutputVariant2RecoveryOperation.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


GmailBulkManageMessagesOutputVariant2Recovery = TypedDict('GmailBulkManageMessagesOutputVariant2Recovery', {
    'idempotencyKey': NotRequired[Annotated[str, Field(max_length=512)]],
    'operationId': NotRequired[Annotated[str, Field(max_length=200)]],
    'runId': NotRequired[Annotated[str, Field(max_length=200)]],
    'jobId': NotRequired[Annotated[str, Field(max_length=200)]],
    'operation': NotRequired[GmailBulkManageMessagesOutputVariant2RecoveryOperation],
})
GmailBulkManageMessagesOutputVariant2Recovery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class GmailBulkManageMessagesOutputVariant2(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    delivery: GmailBulkManageMessagesOutputVariant2Delivery = Field(..., alias='delivery', description='')
    preview: str = Field(..., alias='preview', description='')
    scope: dict[str, Union[str, Union[float, int], bool, None]] = Field(..., alias='scope', description='')
    recovery: GmailBulkManageMessagesOutputVariant2Recovery = Field(..., alias='recovery', description='')


# Union schema: validate external payloads with TypeAdapter(GmailBulkManageMessagesOutput).
GmailBulkManageMessagesOutput = Union[GmailBulkManageMessagesOutputVariant1, GmailBulkManageMessagesOutputVariant2]

_GmailBulkManageMessagesInputAdapter = TypeAdapter(GmailBulkManageMessagesInput)
_GmailBulkManageMessagesOutputAdapter = TypeAdapter(GmailBulkManageMessagesOutput)