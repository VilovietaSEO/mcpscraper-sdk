from typing import Annotated, Any, Literal, Union
from typing_extensions import NotRequired, Required, TypedDict
from pydantic import BaseModel, ConfigDict, Field, TypeAdapter


class ListScheduledRunsInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=False)

    view: Union[Literal['inbox', 'all', 'archived'], None] = Field(None, alias='view', description='Scheduled-results view to return, such as inbox, all unarchived, or archived.')
    status: Union[Literal['running', 'succeeded', 'no_output', 'partial', 'billing_stopped', 'failed'], None] = Field(None, alias='status', description='Optional scheduled-run execution status filter.')
    schedule_id: Union[str, None] = Field(None, alias='scheduleId', description='Optional scheduled-action identifier used to restrict results to one schedule.')
    template_id: Union[str, None] = Field(None, alias='templateId', description='Opaque saved-template identifier returned by an artifact-template tool.')
    from_: Union[str, None] = Field(None, alias='from', description='Inclusive ISO 8601 lower bound for scheduled-run creation time.')
    to: Union[str, None] = Field(None, alias='to', description='Exclusive ISO 8601 upper bound for scheduled-run creation time.')
    query: Union[Annotated[str, Field(max_length=200)], None] = Field(None, alias='query', description='Text matched against scheduled-run titles and searchable metadata.')
    cursor: Union[Annotated[str, Field(max_length=2000)], None] = Field(None, alias='cursor', description='Opaque continuation cursor returned by the previous page; omit for the first page.')
    limit: Union[Annotated[int, Field(ge=1, le=100)], None] = Field(None, alias='limit', description='Maximum rows or records to return on this page; use the returned cursor for more.')


ListScheduledRunsOutputVariant1ItemsItemArtifactSelectionVariant1 = TypedDict('ListScheduledRunsOutputVariant1ItemsItemArtifactSelectionVariant1', {
    'mode': Required[Literal['none']],
})
ListScheduledRunsOutputVariant1ItemsItemArtifactSelectionVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


ListScheduledRunsOutputVariant1ItemsItemArtifactSelectionVariant2 = TypedDict('ListScheduledRunsOutputVariant1ItemsItemArtifactSelectionVariant2', {
    'mode': Required[Literal['saved_template']],
    'templateId': Required[str],
    'templateVersionId': Required[str],
})
ListScheduledRunsOutputVariant1ItemsItemArtifactSelectionVariant2.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


ListScheduledRunsOutputVariant1ItemsItemNoteOutputsItem = TypedDict('ListScheduledRunsOutputVariant1ItemsItemNoteOutputsItem', {
    'vault': Required[Annotated[str, Field(min_length=1, max_length=120)]],
    'path': Required[Annotated[str, Field(min_length=1, max_length=1000)]],
    'title': NotRequired[Annotated[str, Field(max_length=300)]],
    'sourceRef': NotRequired[Annotated[str, Field(max_length=2000)]],
})
ListScheduledRunsOutputVariant1ItemsItemNoteOutputsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


ListScheduledRunsOutputVariant1ItemsItemArtifactOutputsItem = TypedDict('ListScheduledRunsOutputVariant1ItemsItemArtifactOutputsItem', {
    'artifactId': Required[Annotated[str, Field(min_length=1, max_length=1000)]],
    'templateId': Required[str],
    'templateVersionId': Required[str],
    'rendererKey': Required[Literal['editorial_reading_room_v1', 'personal_authority_v1', 'personal_authority_v2', 'newsroom_publisher_v1', 'blog_article_v1']],
    'rendererVersion': Required[Literal[1]],
    'mimeType': Required[Literal['text/html']],
    'title': Required[Annotated[str, Field(min_length=1, max_length=300)]],
    'bytes': Required[Annotated[int, Field(ge=0, le=2000000)]],
    'sha256': Required[str],
    'createdAt': Required[str],
    'viewerPath': Required[str],
})
ListScheduledRunsOutputVariant1ItemsItemArtifactOutputsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


ListScheduledRunsOutputVariant1ItemsItem = TypedDict('ListScheduledRunsOutputVariant1ItemsItem', {
    'runId': Required[Annotated[str, Field(min_length=1, max_length=200)]],
    'scheduleId': Required[str],
    'scheduleDescription': Required[Annotated[str, Field(min_length=1, max_length=20000)]],
    'executionMode': Required[Literal['agent', 'connection_sync']],
    'status': Required[Literal['running', 'succeeded', 'no_output', 'partial', 'billing_stopped', 'failed']],
    'summary': Required[Annotated[str, Field(max_length=2000)]],
    'errorCode': Required[Union[Annotated[str, Field(max_length=120)], None]],
    'errorMessage': Required[Union[Annotated[str, Field(max_length=2000)], None]],
    'scheduledFor': Required[str],
    'startedAt': Required[str],
    'completedAt': Required[Union[str, None]],
    'openedAt': Required[Union[str, None]],
    'archivedAt': Required[Union[str, None]],
    'artifactSelection': Required[Union[ListScheduledRunsOutputVariant1ItemsItemArtifactSelectionVariant1, ListScheduledRunsOutputVariant1ItemsItemArtifactSelectionVariant2]],
    'noteOutputs': Required[Annotated[list[ListScheduledRunsOutputVariant1ItemsItemNoteOutputsItem], Field(max_length=100)]],
    'artifactOutputs': Required[Annotated[list[ListScheduledRunsOutputVariant1ItemsItemArtifactOutputsItem], Field(max_length=10)]],
    'createdAt': Required[str],
    'updatedAt': Required[str],
})
ListScheduledRunsOutputVariant1ItemsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class ListScheduledRunsOutputVariant1(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    ok: bool = Field(..., alias='ok', description='')
    items: Union[list[ListScheduledRunsOutputVariant1ItemsItem], None] = Field(None, alias='items', description='')
    next_cursor: Union[Union[Annotated[str, Field(max_length=2000)], None], None] = Field(None, alias='nextCursor', description='')
    error: Union[Annotated[str, Field(min_length=1, max_length=500)], None] = Field(None, alias='error', description='')
    error_code: Union[Literal['invalid_request', 'not_found', 'conflict', 'template_archived', 'renderer_unavailable', 'artifact_unavailable', 'view_link_unavailable', 'internal_error'], None] = Field(None, alias='errorCode', description='')
    request_id: Union[Annotated[str, Field(max_length=200)], None] = Field(None, alias='requestId', description='')


ListScheduledRunsOutputVariant2DeliveryArtifactsItem = TypedDict('ListScheduledRunsOutputVariant2DeliveryArtifactsItem', {
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
ListScheduledRunsOutputVariant2DeliveryArtifactsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


ListScheduledRunsOutputVariant2DeliveryStorageFailureVariant1 = TypedDict('ListScheduledRunsOutputVariant2DeliveryStorageFailureVariant1', {
    'artifactId': Required[Union[str, None]],
    'outcome': Required[Literal['unknown', 'bytes-stored-metadata-pending', 'failed']],
})
ListScheduledRunsOutputVariant2DeliveryStorageFailureVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


ListScheduledRunsOutputVariant2Delivery = TypedDict('ListScheduledRunsOutputVariant2Delivery', {
    'mode': Required[Literal['artifact']],
    'status': Required[Literal['complete', 'partial', 'unavailable']],
    'retainedRepresentation': Required[Literal['formatted-tool-result']],
    'sourceIsError': Required[bool],
    'artifacts': Required[list[ListScheduledRunsOutputVariant2DeliveryArtifactsItem]],
    'downloadLinksOmitted': Required[bool],
    'scopeOmittedFields': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'storageFailure': Required[Union[ListScheduledRunsOutputVariant2DeliveryStorageFailureVariant1, None]],
    'nextAction': Required[str],
})
ListScheduledRunsOutputVariant2Delivery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


ListScheduledRunsOutputVariant2RecoveryOperation = TypedDict('ListScheduledRunsOutputVariant2RecoveryOperation', {
    'runId': Required[Union[Annotated[str, Field(max_length=200)], None]],
    'idempotencyKey': Required[Annotated[str, Field(max_length=512)]],
    'state': Required[Annotated[str, Field(max_length=100)]],
})
ListScheduledRunsOutputVariant2RecoveryOperation.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


ListScheduledRunsOutputVariant2Recovery = TypedDict('ListScheduledRunsOutputVariant2Recovery', {
    'idempotencyKey': NotRequired[Annotated[str, Field(max_length=512)]],
    'operationId': NotRequired[Annotated[str, Field(max_length=200)]],
    'runId': NotRequired[Annotated[str, Field(max_length=200)]],
    'jobId': NotRequired[Annotated[str, Field(max_length=200)]],
    'operation': NotRequired[ListScheduledRunsOutputVariant2RecoveryOperation],
})
ListScheduledRunsOutputVariant2Recovery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class ListScheduledRunsOutputVariant2(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    delivery: ListScheduledRunsOutputVariant2Delivery = Field(..., alias='delivery', description='')
    preview: str = Field(..., alias='preview', description='')
    scope: dict[str, Union[str, Union[float, int], bool, None]] = Field(..., alias='scope', description='')
    recovery: ListScheduledRunsOutputVariant2Recovery = Field(..., alias='recovery', description='')


# Union schema: validate external payloads with TypeAdapter(ListScheduledRunsOutput).
ListScheduledRunsOutput = Union[ListScheduledRunsOutputVariant2, ListScheduledRunsOutputVariant1]

_ListScheduledRunsInputAdapter = TypeAdapter(ListScheduledRunsInput)
_ListScheduledRunsOutputAdapter = TypeAdapter(ListScheduledRunsOutput)