from typing import Annotated, Any, Literal, Union
from typing_extensions import NotRequired, Required, TypedDict
from pydantic import BaseModel, ConfigDict, Field, TypeAdapter


class ZoomCreateMeetingInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=False)

    confirmed: Union[bool, None] = Field(None, alias='confirmed', description='Set true only when the person explicitly authorized creating this exact meeting. If omitted, a 2026-capable client may ask for confirmation.')
    idempotency_key: Annotated[str, Field(min_length=8, max_length=200)] = Field(..., alias='idempotencyKey', description='Required stable key for this intended meeting. Reuse it only when retrying the same creation after a lost response.')
    connection_id: Annotated[str, Field(min_length=1)] = Field(..., alias='connectionId', description='A Zoom connectionId from list_service_connections, with actionsEnabled true.')
    topic: Annotated[str, Field(min_length=1, max_length=200)] = Field(..., alias='topic', description='Meeting topic/title.')
    start_date_time: Annotated[str, Field(min_length=1)] = Field(..., alias='startDateTime', description='Start time, ISO 8601, e.g. "2026-07-15T09:00:00-06:00".')
    duration_minutes: Union[Annotated[int, Field(ge=1, le=1440)], None] = Field(None, alias='durationMinutes', description='Meeting duration in minutes. Default 30.')
    timezone: Union[Annotated[str, Field(max_length=100)], None] = Field(None, alias='timezone', description='IANA timezone, e.g. "America/Denver".')
    agenda: Annotated[str, Field(min_length=1, max_length=2000)] = Field(..., alias='agenda', description='Required meeting description or agenda. Preserve the purpose and context supplied by the user.')


class ZoomCreateMeetingOutputVariant1(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    ok: bool = Field(..., alias='ok', description='')
    result: Union[Any, None] = Field(None, alias='result', description='')
    error: Union[str, None] = Field(..., alias='error', description='')


ZoomCreateMeetingOutputVariant2DeliveryArtifactsItem = TypedDict('ZoomCreateMeetingOutputVariant2DeliveryArtifactsItem', {
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
ZoomCreateMeetingOutputVariant2DeliveryArtifactsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


ZoomCreateMeetingOutputVariant2DeliveryStorageFailureVariant1 = TypedDict('ZoomCreateMeetingOutputVariant2DeliveryStorageFailureVariant1', {
    'artifactId': Required[Union[str, None]],
    'outcome': Required[Literal['unknown', 'bytes-stored-metadata-pending', 'failed']],
})
ZoomCreateMeetingOutputVariant2DeliveryStorageFailureVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


ZoomCreateMeetingOutputVariant2Delivery = TypedDict('ZoomCreateMeetingOutputVariant2Delivery', {
    'mode': Required[Literal['artifact']],
    'status': Required[Literal['complete', 'partial', 'unavailable']],
    'retainedRepresentation': Required[Literal['formatted-tool-result']],
    'sourceIsError': Required[bool],
    'artifacts': Required[list[ZoomCreateMeetingOutputVariant2DeliveryArtifactsItem]],
    'downloadLinksOmitted': Required[bool],
    'scopeOmittedFields': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'storageFailure': Required[Union[ZoomCreateMeetingOutputVariant2DeliveryStorageFailureVariant1, None]],
    'nextAction': Required[str],
})
ZoomCreateMeetingOutputVariant2Delivery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


ZoomCreateMeetingOutputVariant2RecoveryOperation = TypedDict('ZoomCreateMeetingOutputVariant2RecoveryOperation', {
    'runId': Required[Union[Annotated[str, Field(max_length=200)], None]],
    'idempotencyKey': Required[Annotated[str, Field(max_length=512)]],
    'state': Required[Annotated[str, Field(max_length=100)]],
})
ZoomCreateMeetingOutputVariant2RecoveryOperation.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


ZoomCreateMeetingOutputVariant2Recovery = TypedDict('ZoomCreateMeetingOutputVariant2Recovery', {
    'idempotencyKey': NotRequired[Annotated[str, Field(max_length=512)]],
    'operationId': NotRequired[Annotated[str, Field(max_length=200)]],
    'runId': NotRequired[Annotated[str, Field(max_length=200)]],
    'jobId': NotRequired[Annotated[str, Field(max_length=200)]],
    'operation': NotRequired[ZoomCreateMeetingOutputVariant2RecoveryOperation],
})
ZoomCreateMeetingOutputVariant2Recovery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class ZoomCreateMeetingOutputVariant2(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    delivery: ZoomCreateMeetingOutputVariant2Delivery = Field(..., alias='delivery', description='')
    preview: str = Field(..., alias='preview', description='')
    scope: dict[str, Union[str, Union[float, int], bool, None]] = Field(..., alias='scope', description='')
    recovery: ZoomCreateMeetingOutputVariant2Recovery = Field(..., alias='recovery', description='')


# Union schema: validate external payloads with TypeAdapter(ZoomCreateMeetingOutput).
ZoomCreateMeetingOutput = Union[ZoomCreateMeetingOutputVariant2, ZoomCreateMeetingOutputVariant1]

_ZoomCreateMeetingInputAdapter = TypeAdapter(ZoomCreateMeetingInput)
_ZoomCreateMeetingOutputAdapter = TypeAdapter(ZoomCreateMeetingOutput)