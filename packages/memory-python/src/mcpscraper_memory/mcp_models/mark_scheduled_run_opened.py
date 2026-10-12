from typing import Annotated, Any, Literal, Union
from typing_extensions import NotRequired, Required, TypedDict
from pydantic import BaseModel, ConfigDict, Field, TypeAdapter


class MarkScheduledRunOpenedInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=False)

    run_id: Annotated[str, Field(min_length=1, max_length=200)] = Field(..., alias='runId', description='Opaque scheduled-run identifier returned by a scheduled-results tool.')


MarkScheduledRunOpenedOutputVariant1RunArtifactSelectionVariant1 = TypedDict('MarkScheduledRunOpenedOutputVariant1RunArtifactSelectionVariant1', {
    'mode': Required[Literal['none']],
})
MarkScheduledRunOpenedOutputVariant1RunArtifactSelectionVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


MarkScheduledRunOpenedOutputVariant1RunArtifactSelectionVariant2 = TypedDict('MarkScheduledRunOpenedOutputVariant1RunArtifactSelectionVariant2', {
    'mode': Required[Literal['saved_template']],
    'templateId': Required[str],
    'templateVersionId': Required[str],
})
MarkScheduledRunOpenedOutputVariant1RunArtifactSelectionVariant2.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


MarkScheduledRunOpenedOutputVariant1RunNoteOutputsItem = TypedDict('MarkScheduledRunOpenedOutputVariant1RunNoteOutputsItem', {
    'vault': Required[Annotated[str, Field(min_length=1, max_length=120)]],
    'path': Required[Annotated[str, Field(min_length=1, max_length=1000)]],
    'title': NotRequired[Annotated[str, Field(max_length=300)]],
    'sourceRef': NotRequired[Annotated[str, Field(max_length=2000)]],
})
MarkScheduledRunOpenedOutputVariant1RunNoteOutputsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


MarkScheduledRunOpenedOutputVariant1RunArtifactOutputsItem = TypedDict('MarkScheduledRunOpenedOutputVariant1RunArtifactOutputsItem', {
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
MarkScheduledRunOpenedOutputVariant1RunArtifactOutputsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


MarkScheduledRunOpenedOutputVariant1Run = TypedDict('MarkScheduledRunOpenedOutputVariant1Run', {
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
    'artifactSelection': Required[Union[MarkScheduledRunOpenedOutputVariant1RunArtifactSelectionVariant1, MarkScheduledRunOpenedOutputVariant1RunArtifactSelectionVariant2]],
    'noteOutputs': Required[Annotated[list[MarkScheduledRunOpenedOutputVariant1RunNoteOutputsItem], Field(max_length=100)]],
    'artifactOutputs': Required[Annotated[list[MarkScheduledRunOpenedOutputVariant1RunArtifactOutputsItem], Field(max_length=10)]],
    'createdAt': Required[str],
    'updatedAt': Required[str],
})
MarkScheduledRunOpenedOutputVariant1Run.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class MarkScheduledRunOpenedOutputVariant1(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    ok: bool = Field(..., alias='ok', description='')
    run: Union[MarkScheduledRunOpenedOutputVariant1Run, None] = Field(None, alias='run', description='')
    error: Union[Annotated[str, Field(min_length=1, max_length=500)], None] = Field(None, alias='error', description='')
    error_code: Union[Literal['invalid_request', 'not_found', 'conflict', 'template_archived', 'renderer_unavailable', 'artifact_unavailable', 'view_link_unavailable', 'internal_error'], None] = Field(None, alias='errorCode', description='')
    request_id: Union[Annotated[str, Field(max_length=200)], None] = Field(None, alias='requestId', description='')


MarkScheduledRunOpenedOutputVariant2DeliveryArtifactsItem = TypedDict('MarkScheduledRunOpenedOutputVariant2DeliveryArtifactsItem', {
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
MarkScheduledRunOpenedOutputVariant2DeliveryArtifactsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


MarkScheduledRunOpenedOutputVariant2DeliveryStorageFailureVariant1 = TypedDict('MarkScheduledRunOpenedOutputVariant2DeliveryStorageFailureVariant1', {
    'artifactId': Required[Union[str, None]],
    'outcome': Required[Literal['unknown', 'bytes-stored-metadata-pending', 'failed']],
})
MarkScheduledRunOpenedOutputVariant2DeliveryStorageFailureVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


MarkScheduledRunOpenedOutputVariant2Delivery = TypedDict('MarkScheduledRunOpenedOutputVariant2Delivery', {
    'mode': Required[Literal['artifact']],
    'status': Required[Literal['complete', 'partial', 'unavailable']],
    'retainedRepresentation': Required[Literal['formatted-tool-result']],
    'sourceIsError': Required[bool],
    'artifacts': Required[list[MarkScheduledRunOpenedOutputVariant2DeliveryArtifactsItem]],
    'downloadLinksOmitted': Required[bool],
    'scopeOmittedFields': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'storageFailure': Required[Union[MarkScheduledRunOpenedOutputVariant2DeliveryStorageFailureVariant1, None]],
    'nextAction': Required[str],
})
MarkScheduledRunOpenedOutputVariant2Delivery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


MarkScheduledRunOpenedOutputVariant2RecoveryOperation = TypedDict('MarkScheduledRunOpenedOutputVariant2RecoveryOperation', {
    'runId': Required[Union[Annotated[str, Field(max_length=200)], None]],
    'idempotencyKey': Required[Annotated[str, Field(max_length=512)]],
    'state': Required[Annotated[str, Field(max_length=100)]],
})
MarkScheduledRunOpenedOutputVariant2RecoveryOperation.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


MarkScheduledRunOpenedOutputVariant2Recovery = TypedDict('MarkScheduledRunOpenedOutputVariant2Recovery', {
    'idempotencyKey': NotRequired[Annotated[str, Field(max_length=512)]],
    'operationId': NotRequired[Annotated[str, Field(max_length=200)]],
    'runId': NotRequired[Annotated[str, Field(max_length=200)]],
    'jobId': NotRequired[Annotated[str, Field(max_length=200)]],
    'operation': NotRequired[MarkScheduledRunOpenedOutputVariant2RecoveryOperation],
})
MarkScheduledRunOpenedOutputVariant2Recovery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class MarkScheduledRunOpenedOutputVariant2(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    delivery: MarkScheduledRunOpenedOutputVariant2Delivery = Field(..., alias='delivery', description='')
    preview: str = Field(..., alias='preview', description='')
    scope: dict[str, Union[str, Union[float, int], bool, None]] = Field(..., alias='scope', description='')
    recovery: MarkScheduledRunOpenedOutputVariant2Recovery = Field(..., alias='recovery', description='')


# Union schema: validate external payloads with TypeAdapter(MarkScheduledRunOpenedOutput).
MarkScheduledRunOpenedOutput = Union[MarkScheduledRunOpenedOutputVariant2, MarkScheduledRunOpenedOutputVariant1]

_MarkScheduledRunOpenedInputAdapter = TypeAdapter(MarkScheduledRunOpenedInput)
_MarkScheduledRunOpenedOutputAdapter = TypeAdapter(MarkScheduledRunOpenedOutput)