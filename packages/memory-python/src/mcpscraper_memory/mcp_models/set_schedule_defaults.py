from typing import Annotated, Any, Literal, Union
from typing_extensions import NotRequired, Required, TypedDict
from pydantic import BaseModel, ConfigDict, Field, TypeAdapter


class SetScheduleDefaultsInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=False)

    default_timezone: Union[str, None] = Field(..., alias='defaultTimezone', description='IANA timezone name, e.g. "America/Denver". null clears the default (new schedules fall back to UTC).')


class SetScheduleDefaultsOutputVariant1(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    ok: bool = Field(..., alias='ok', description='')
    default_timezone: Union[Union[str, None], None] = Field(None, alias='defaultTimezone', description='The default timezone now in effect; null means UTC.')
    error: Union[str, None] = Field(None, alias='error', description='')


SetScheduleDefaultsOutputVariant2DeliveryArtifactsItem = TypedDict('SetScheduleDefaultsOutputVariant2DeliveryArtifactsItem', {
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
SetScheduleDefaultsOutputVariant2DeliveryArtifactsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


SetScheduleDefaultsOutputVariant2DeliveryStorageFailureVariant1 = TypedDict('SetScheduleDefaultsOutputVariant2DeliveryStorageFailureVariant1', {
    'artifactId': Required[Union[str, None]],
    'outcome': Required[Literal['unknown', 'bytes-stored-metadata-pending', 'failed']],
})
SetScheduleDefaultsOutputVariant2DeliveryStorageFailureVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


SetScheduleDefaultsOutputVariant2Delivery = TypedDict('SetScheduleDefaultsOutputVariant2Delivery', {
    'mode': Required[Literal['artifact']],
    'status': Required[Literal['complete', 'partial', 'unavailable']],
    'retainedRepresentation': Required[Literal['formatted-tool-result']],
    'sourceIsError': Required[bool],
    'artifacts': Required[list[SetScheduleDefaultsOutputVariant2DeliveryArtifactsItem]],
    'downloadLinksOmitted': Required[bool],
    'scopeOmittedFields': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'storageFailure': Required[Union[SetScheduleDefaultsOutputVariant2DeliveryStorageFailureVariant1, None]],
    'nextAction': Required[str],
})
SetScheduleDefaultsOutputVariant2Delivery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


SetScheduleDefaultsOutputVariant2RecoveryOperation = TypedDict('SetScheduleDefaultsOutputVariant2RecoveryOperation', {
    'runId': Required[Union[Annotated[str, Field(max_length=200)], None]],
    'idempotencyKey': Required[Annotated[str, Field(max_length=512)]],
    'state': Required[Annotated[str, Field(max_length=100)]],
})
SetScheduleDefaultsOutputVariant2RecoveryOperation.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


SetScheduleDefaultsOutputVariant2Recovery = TypedDict('SetScheduleDefaultsOutputVariant2Recovery', {
    'idempotencyKey': NotRequired[Annotated[str, Field(max_length=512)]],
    'operationId': NotRequired[Annotated[str, Field(max_length=200)]],
    'runId': NotRequired[Annotated[str, Field(max_length=200)]],
    'jobId': NotRequired[Annotated[str, Field(max_length=200)]],
    'operation': NotRequired[SetScheduleDefaultsOutputVariant2RecoveryOperation],
})
SetScheduleDefaultsOutputVariant2Recovery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class SetScheduleDefaultsOutputVariant2(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    delivery: SetScheduleDefaultsOutputVariant2Delivery = Field(..., alias='delivery', description='')
    preview: str = Field(..., alias='preview', description='')
    scope: dict[str, Union[str, Union[float, int], bool, None]] = Field(..., alias='scope', description='')
    recovery: SetScheduleDefaultsOutputVariant2Recovery = Field(..., alias='recovery', description='')


# Union schema: validate external payloads with TypeAdapter(SetScheduleDefaultsOutput).
SetScheduleDefaultsOutput = Union[SetScheduleDefaultsOutputVariant2, SetScheduleDefaultsOutputVariant1]

_SetScheduleDefaultsInputAdapter = TypeAdapter(SetScheduleDefaultsInput)
_SetScheduleDefaultsOutputAdapter = TypeAdapter(SetScheduleDefaultsOutput)