from typing import Annotated, Any, Literal, Union
from typing_extensions import NotRequired, Required, TypedDict
from pydantic import BaseModel, ConfigDict, Field, TypeAdapter


class GetScheduledRunInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=False)

    run_id: Annotated[str, Field(min_length=1, max_length=200)] = Field(..., alias='runId', description='Opaque scheduled-run identifier returned by a scheduled-results tool.')


GetScheduledRunOutputVariant1RunArtifactSelectionVariant1 = TypedDict('GetScheduledRunOutputVariant1RunArtifactSelectionVariant1', {
    'mode': Required[Literal['none']],
})
GetScheduledRunOutputVariant1RunArtifactSelectionVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


GetScheduledRunOutputVariant1RunArtifactSelectionVariant2 = TypedDict('GetScheduledRunOutputVariant1RunArtifactSelectionVariant2', {
    'mode': Required[Literal['saved_template']],
    'templateId': Required[str],
    'templateVersionId': Required[str],
})
GetScheduledRunOutputVariant1RunArtifactSelectionVariant2.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


GetScheduledRunOutputVariant1RunNoteOutputsItem = TypedDict('GetScheduledRunOutputVariant1RunNoteOutputsItem', {
    'vault': Required[Annotated[str, Field(min_length=1, max_length=120)]],
    'path': Required[Annotated[str, Field(min_length=1, max_length=1000)]],
    'title': NotRequired[Annotated[str, Field(max_length=300)]],
    'sourceRef': NotRequired[Annotated[str, Field(max_length=2000)]],
})
GetScheduledRunOutputVariant1RunNoteOutputsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


GetScheduledRunOutputVariant1RunArtifactOutputsItem = TypedDict('GetScheduledRunOutputVariant1RunArtifactOutputsItem', {
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
GetScheduledRunOutputVariant1RunArtifactOutputsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


GetScheduledRunOutputVariant1Run = TypedDict('GetScheduledRunOutputVariant1Run', {
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
    'artifactSelection': Required[Union[GetScheduledRunOutputVariant1RunArtifactSelectionVariant1, GetScheduledRunOutputVariant1RunArtifactSelectionVariant2]],
    'noteOutputs': Required[Annotated[list[GetScheduledRunOutputVariant1RunNoteOutputsItem], Field(max_length=100)]],
    'artifactOutputs': Required[Annotated[list[GetScheduledRunOutputVariant1RunArtifactOutputsItem], Field(max_length=10)]],
    'createdAt': Required[str],
    'updatedAt': Required[str],
})
GetScheduledRunOutputVariant1Run.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class GetScheduledRunOutputVariant1(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    ok: bool = Field(..., alias='ok', description='')
    run: Union[GetScheduledRunOutputVariant1Run, None] = Field(None, alias='run', description='')
    error: Union[Annotated[str, Field(min_length=1, max_length=500)], None] = Field(None, alias='error', description='')
    error_code: Union[Literal['invalid_request', 'not_found', 'conflict', 'template_archived', 'renderer_unavailable', 'artifact_unavailable', 'view_link_unavailable', 'internal_error'], None] = Field(None, alias='errorCode', description='')
    request_id: Union[Annotated[str, Field(max_length=200)], None] = Field(None, alias='requestId', description='')


GetScheduledRunOutputVariant2DeliveryArtifactsItem = TypedDict('GetScheduledRunOutputVariant2DeliveryArtifactsItem', {
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
GetScheduledRunOutputVariant2DeliveryArtifactsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


GetScheduledRunOutputVariant2DeliveryStorageFailureVariant1 = TypedDict('GetScheduledRunOutputVariant2DeliveryStorageFailureVariant1', {
    'artifactId': Required[Union[str, None]],
    'outcome': Required[Literal['unknown', 'bytes-stored-metadata-pending', 'failed']],
})
GetScheduledRunOutputVariant2DeliveryStorageFailureVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


GetScheduledRunOutputVariant2Delivery = TypedDict('GetScheduledRunOutputVariant2Delivery', {
    'mode': Required[Literal['artifact']],
    'status': Required[Literal['complete', 'partial', 'unavailable']],
    'retainedRepresentation': Required[Literal['formatted-tool-result']],
    'sourceIsError': Required[bool],
    'artifacts': Required[list[GetScheduledRunOutputVariant2DeliveryArtifactsItem]],
    'downloadLinksOmitted': Required[bool],
    'scopeOmittedFields': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'storageFailure': Required[Union[GetScheduledRunOutputVariant2DeliveryStorageFailureVariant1, None]],
    'nextAction': Required[str],
})
GetScheduledRunOutputVariant2Delivery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


GetScheduledRunOutputVariant2RecoveryOperation = TypedDict('GetScheduledRunOutputVariant2RecoveryOperation', {
    'runId': Required[Union[Annotated[str, Field(max_length=200)], None]],
    'idempotencyKey': Required[Annotated[str, Field(max_length=512)]],
    'state': Required[Annotated[str, Field(max_length=100)]],
})
GetScheduledRunOutputVariant2RecoveryOperation.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


GetScheduledRunOutputVariant2Recovery = TypedDict('GetScheduledRunOutputVariant2Recovery', {
    'idempotencyKey': NotRequired[Annotated[str, Field(max_length=512)]],
    'operationId': NotRequired[Annotated[str, Field(max_length=200)]],
    'runId': NotRequired[Annotated[str, Field(max_length=200)]],
    'jobId': NotRequired[Annotated[str, Field(max_length=200)]],
    'operation': NotRequired[GetScheduledRunOutputVariant2RecoveryOperation],
})
GetScheduledRunOutputVariant2Recovery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class GetScheduledRunOutputVariant2(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    delivery: GetScheduledRunOutputVariant2Delivery = Field(..., alias='delivery', description='')
    preview: str = Field(..., alias='preview', description='')
    scope: dict[str, Union[str, Union[float, int], bool, None]] = Field(..., alias='scope', description='')
    recovery: GetScheduledRunOutputVariant2Recovery = Field(..., alias='recovery', description='')


# Union schema: validate external payloads with TypeAdapter(GetScheduledRunOutput).
GetScheduledRunOutput = Union[GetScheduledRunOutputVariant2, GetScheduledRunOutputVariant1]

_GetScheduledRunInputAdapter = TypeAdapter(GetScheduledRunInput)
_GetScheduledRunOutputAdapter = TypeAdapter(GetScheduledRunOutput)