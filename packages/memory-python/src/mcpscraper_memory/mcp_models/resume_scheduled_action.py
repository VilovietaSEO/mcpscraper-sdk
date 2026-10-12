from typing import Annotated, Any, Literal, Union
from typing_extensions import NotRequired, Required, TypedDict
from pydantic import BaseModel, ConfigDict, Field, TypeAdapter


class ResumeScheduledActionInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=False)

    id: Annotated[str, Field(min_length=1)] = Field(..., alias='id', description='The scheduled action id.')


class ResumeScheduledActionOutputVariant1(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    ok: bool = Field(..., alias='ok', description='')
    next_run_at: Union[str, None] = Field(None, alias='nextRunAt', description='')
    code: Union[str, None] = Field(None, alias='code', description='Machine-readable denial code when the action cannot be resumed.')
    error: Union[str, None] = Field(None, alias='error', description='')


ResumeScheduledActionOutputVariant2DeliveryArtifactsItem = TypedDict('ResumeScheduledActionOutputVariant2DeliveryArtifactsItem', {
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
ResumeScheduledActionOutputVariant2DeliveryArtifactsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


ResumeScheduledActionOutputVariant2DeliveryStorageFailureVariant1 = TypedDict('ResumeScheduledActionOutputVariant2DeliveryStorageFailureVariant1', {
    'artifactId': Required[Union[str, None]],
    'outcome': Required[Literal['unknown', 'bytes-stored-metadata-pending', 'failed']],
})
ResumeScheduledActionOutputVariant2DeliveryStorageFailureVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


ResumeScheduledActionOutputVariant2Delivery = TypedDict('ResumeScheduledActionOutputVariant2Delivery', {
    'mode': Required[Literal['artifact']],
    'status': Required[Literal['complete', 'partial', 'unavailable']],
    'retainedRepresentation': Required[Literal['formatted-tool-result']],
    'sourceIsError': Required[bool],
    'artifacts': Required[list[ResumeScheduledActionOutputVariant2DeliveryArtifactsItem]],
    'downloadLinksOmitted': Required[bool],
    'scopeOmittedFields': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'storageFailure': Required[Union[ResumeScheduledActionOutputVariant2DeliveryStorageFailureVariant1, None]],
    'nextAction': Required[str],
})
ResumeScheduledActionOutputVariant2Delivery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


ResumeScheduledActionOutputVariant2RecoveryOperation = TypedDict('ResumeScheduledActionOutputVariant2RecoveryOperation', {
    'runId': Required[Union[Annotated[str, Field(max_length=200)], None]],
    'idempotencyKey': Required[Annotated[str, Field(max_length=512)]],
    'state': Required[Annotated[str, Field(max_length=100)]],
})
ResumeScheduledActionOutputVariant2RecoveryOperation.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


ResumeScheduledActionOutputVariant2Recovery = TypedDict('ResumeScheduledActionOutputVariant2Recovery', {
    'idempotencyKey': NotRequired[Annotated[str, Field(max_length=512)]],
    'operationId': NotRequired[Annotated[str, Field(max_length=200)]],
    'runId': NotRequired[Annotated[str, Field(max_length=200)]],
    'jobId': NotRequired[Annotated[str, Field(max_length=200)]],
    'operation': NotRequired[ResumeScheduledActionOutputVariant2RecoveryOperation],
})
ResumeScheduledActionOutputVariant2Recovery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class ResumeScheduledActionOutputVariant2(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    delivery: ResumeScheduledActionOutputVariant2Delivery = Field(..., alias='delivery', description='')
    preview: str = Field(..., alias='preview', description='')
    scope: dict[str, Union[str, Union[float, int], bool, None]] = Field(..., alias='scope', description='')
    recovery: ResumeScheduledActionOutputVariant2Recovery = Field(..., alias='recovery', description='')


# Union schema: validate external payloads with TypeAdapter(ResumeScheduledActionOutput).
ResumeScheduledActionOutput = Union[ResumeScheduledActionOutputVariant2, ResumeScheduledActionOutputVariant1]

_ResumeScheduledActionInputAdapter = TypeAdapter(ResumeScheduledActionInput)
_ResumeScheduledActionOutputAdapter = TypeAdapter(ResumeScheduledActionOutput)