from typing import Annotated, Any, Literal, Union
from typing_extensions import NotRequired, Required, TypedDict
from pydantic import BaseModel, ConfigDict, Field, TypeAdapter


class CreateScheduledRunViewLinkInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=False)

    run_id: Annotated[str, Field(min_length=1, max_length=200)] = Field(..., alias='runId', description='Opaque scheduled-run identifier returned by a scheduled-results tool.')
    artifact_id: Annotated[str, Field(min_length=1, max_length=1000)] = Field(..., alias='artifactId', description='Opaque artifact identifier returned by the creating or listing tool.')
    expires_in_days: Union[Annotated[int, Field(ge=1, le=30)], None] = Field(None, alias='expiresInDays', description='Requested view-link lifetime in days; the server enforces its maximum.')


class CreateScheduledRunViewLinkOutputVariant1(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    ok: bool = Field(..., alias='ok', description='')
    share_id: Union[str, None] = Field(None, alias='shareId', description='')
    run_id: Union[Annotated[str, Field(min_length=1, max_length=200)], None] = Field(None, alias='runId', description='Opaque scheduled-run identifier returned by a scheduled-results tool.')
    artifact_id: Union[Annotated[str, Field(min_length=1, max_length=1000)], None] = Field(None, alias='artifactId', description='')
    url: Union[str, None] = Field(None, alias='url', description='')
    expires_at: Union[str, None] = Field(None, alias='expiresAt', description='')
    created_at: Union[str, None] = Field(None, alias='createdAt', description='')
    error: Union[Annotated[str, Field(min_length=1, max_length=500)], None] = Field(None, alias='error', description='')
    error_code: Union[Literal['invalid_request', 'not_found', 'conflict', 'template_archived', 'renderer_unavailable', 'artifact_unavailable', 'view_link_unavailable', 'internal_error'], None] = Field(None, alias='errorCode', description='')
    request_id: Union[Annotated[str, Field(max_length=200)], None] = Field(None, alias='requestId', description='')


CreateScheduledRunViewLinkOutputVariant2DeliveryArtifactsItem = TypedDict('CreateScheduledRunViewLinkOutputVariant2DeliveryArtifactsItem', {
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
CreateScheduledRunViewLinkOutputVariant2DeliveryArtifactsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


CreateScheduledRunViewLinkOutputVariant2DeliveryStorageFailureVariant1 = TypedDict('CreateScheduledRunViewLinkOutputVariant2DeliveryStorageFailureVariant1', {
    'artifactId': Required[Union[str, None]],
    'outcome': Required[Literal['unknown', 'bytes-stored-metadata-pending', 'failed']],
})
CreateScheduledRunViewLinkOutputVariant2DeliveryStorageFailureVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


CreateScheduledRunViewLinkOutputVariant2Delivery = TypedDict('CreateScheduledRunViewLinkOutputVariant2Delivery', {
    'mode': Required[Literal['artifact']],
    'status': Required[Literal['complete', 'partial', 'unavailable']],
    'retainedRepresentation': Required[Literal['formatted-tool-result']],
    'sourceIsError': Required[bool],
    'artifacts': Required[list[CreateScheduledRunViewLinkOutputVariant2DeliveryArtifactsItem]],
    'downloadLinksOmitted': Required[bool],
    'scopeOmittedFields': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'storageFailure': Required[Union[CreateScheduledRunViewLinkOutputVariant2DeliveryStorageFailureVariant1, None]],
    'nextAction': Required[str],
})
CreateScheduledRunViewLinkOutputVariant2Delivery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


CreateScheduledRunViewLinkOutputVariant2RecoveryOperation = TypedDict('CreateScheduledRunViewLinkOutputVariant2RecoveryOperation', {
    'runId': Required[Union[Annotated[str, Field(max_length=200)], None]],
    'idempotencyKey': Required[Annotated[str, Field(max_length=512)]],
    'state': Required[Annotated[str, Field(max_length=100)]],
})
CreateScheduledRunViewLinkOutputVariant2RecoveryOperation.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


CreateScheduledRunViewLinkOutputVariant2Recovery = TypedDict('CreateScheduledRunViewLinkOutputVariant2Recovery', {
    'idempotencyKey': NotRequired[Annotated[str, Field(max_length=512)]],
    'operationId': NotRequired[Annotated[str, Field(max_length=200)]],
    'runId': NotRequired[Annotated[str, Field(max_length=200)]],
    'jobId': NotRequired[Annotated[str, Field(max_length=200)]],
    'operation': NotRequired[CreateScheduledRunViewLinkOutputVariant2RecoveryOperation],
})
CreateScheduledRunViewLinkOutputVariant2Recovery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class CreateScheduledRunViewLinkOutputVariant2(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    delivery: CreateScheduledRunViewLinkOutputVariant2Delivery = Field(..., alias='delivery', description='')
    preview: str = Field(..., alias='preview', description='')
    scope: dict[str, Union[str, Union[float, int], bool, None]] = Field(..., alias='scope', description='')
    recovery: CreateScheduledRunViewLinkOutputVariant2Recovery = Field(..., alias='recovery', description='')


# Union schema: validate external payloads with TypeAdapter(CreateScheduledRunViewLinkOutput).
CreateScheduledRunViewLinkOutput = Union[CreateScheduledRunViewLinkOutputVariant2, CreateScheduledRunViewLinkOutputVariant1]

_CreateScheduledRunViewLinkInputAdapter = TypeAdapter(CreateScheduledRunViewLinkInput)
_CreateScheduledRunViewLinkOutputAdapter = TypeAdapter(CreateScheduledRunViewLinkOutput)