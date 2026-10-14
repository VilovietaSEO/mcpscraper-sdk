from typing import Annotated, Any, Literal, Union
from typing_extensions import NotRequired, Required, TypedDict
from pydantic import BaseModel, ConfigDict, Field, TypeAdapter


GoogleCalendarCreateEventInputAttendeesItem = TypedDict('GoogleCalendarCreateEventInputAttendeesItem', {
    'email': Required[str],
    'displayName': NotRequired[Annotated[str, Field(min_length=1, max_length=200)]],
})
GoogleCalendarCreateEventInputAttendeesItem.__pydantic_config__ = ConfigDict(extra="allow", strict=False)


class GoogleCalendarCreateEventInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=False)

    confirmed: Union[bool, None] = Field(None, alias='confirmed', description='Set true only when the person explicitly authorized creating this exact event and inviting these attendees. If omitted, a 2026-capable client may ask for confirmation.')
    idempotency_key: Annotated[str, Field(min_length=8, max_length=200)] = Field(..., alias='idempotencyKey', description='Required stable key for this intended event. Reuse it only when retrying the same creation after a lost response.')
    connection_id: Annotated[str, Field(min_length=1)] = Field(..., alias='connectionId', description='A Google Calendar connectionId from list_service_connections, with actionsEnabled true.')
    calendar_id: Union[Annotated[str, Field(min_length=1)], None] = Field(None, alias='calendarId', description='Calendar to create the event in. Default "primary".')
    summary: Annotated[str, Field(min_length=1, max_length=500)] = Field(..., alias='summary', description='Event title.')
    description: Annotated[str, Field(min_length=1, max_length=5000)] = Field(..., alias='description', description='Required event context. Include the purpose or agenda supplied by the user and the Zoom join link when one was created.')
    location: Union[Annotated[str, Field(max_length=500)], None] = Field(None, alias='location', description='Event location.')
    start_date_time: Annotated[str, Field(min_length=1)] = Field(..., alias='startDateTime', description='Start time, ISO 8601, e.g. "2026-07-15T09:00:00-06:00".')
    end_date_time: Annotated[str, Field(min_length=1)] = Field(..., alias='endDateTime', description='End time, ISO 8601, e.g. "2026-07-15T10:00:00-06:00".')
    time_zone: Union[Annotated[str, Field(max_length=100)], None] = Field(None, alias='timeZone', description='IANA timezone, e.g. "America/Denver". Applies to both start and end.')
    attendees: Annotated[list[GoogleCalendarCreateEventInputAttendeesItem], Field(max_length=100)] = Field(..., alias='attendees', description='Required attendee list. Include every person the user asked to invite; use an empty array only when no invitee was identified.')


class GoogleCalendarCreateEventOutputVariant1(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    ok: bool = Field(..., alias='ok', description='')
    result: Union[Any, None] = Field(None, alias='result', description='')
    error: Union[str, None] = Field(..., alias='error', description='')


GoogleCalendarCreateEventOutputVariant2DeliveryArtifactsItem = TypedDict('GoogleCalendarCreateEventOutputVariant2DeliveryArtifactsItem', {
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
GoogleCalendarCreateEventOutputVariant2DeliveryArtifactsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


GoogleCalendarCreateEventOutputVariant2DeliveryStorageFailureVariant1 = TypedDict('GoogleCalendarCreateEventOutputVariant2DeliveryStorageFailureVariant1', {
    'artifactId': Required[Union[str, None]],
    'outcome': Required[Literal['unknown', 'bytes-stored-metadata-pending', 'failed']],
})
GoogleCalendarCreateEventOutputVariant2DeliveryStorageFailureVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


GoogleCalendarCreateEventOutputVariant2Delivery = TypedDict('GoogleCalendarCreateEventOutputVariant2Delivery', {
    'mode': Required[Literal['artifact']],
    'status': Required[Literal['complete', 'partial', 'unavailable']],
    'retainedRepresentation': Required[Literal['formatted-tool-result']],
    'sourceIsError': Required[bool],
    'artifacts': Required[list[GoogleCalendarCreateEventOutputVariant2DeliveryArtifactsItem]],
    'downloadLinksOmitted': Required[bool],
    'scopeOmittedFields': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'storageFailure': Required[Union[GoogleCalendarCreateEventOutputVariant2DeliveryStorageFailureVariant1, None]],
    'nextAction': Required[str],
})
GoogleCalendarCreateEventOutputVariant2Delivery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


GoogleCalendarCreateEventOutputVariant2RecoveryOperation = TypedDict('GoogleCalendarCreateEventOutputVariant2RecoveryOperation', {
    'runId': Required[Union[Annotated[str, Field(max_length=200)], None]],
    'idempotencyKey': Required[Annotated[str, Field(max_length=512)]],
    'state': Required[Annotated[str, Field(max_length=100)]],
})
GoogleCalendarCreateEventOutputVariant2RecoveryOperation.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


GoogleCalendarCreateEventOutputVariant2Recovery = TypedDict('GoogleCalendarCreateEventOutputVariant2Recovery', {
    'idempotencyKey': NotRequired[Annotated[str, Field(max_length=512)]],
    'operationId': NotRequired[Annotated[str, Field(max_length=200)]],
    'runId': NotRequired[Annotated[str, Field(max_length=200)]],
    'jobId': NotRequired[Annotated[str, Field(max_length=200)]],
    'operation': NotRequired[GoogleCalendarCreateEventOutputVariant2RecoveryOperation],
})
GoogleCalendarCreateEventOutputVariant2Recovery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class GoogleCalendarCreateEventOutputVariant2(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    delivery: GoogleCalendarCreateEventOutputVariant2Delivery = Field(..., alias='delivery', description='')
    preview: str = Field(..., alias='preview', description='')
    scope: dict[str, Union[str, Union[float, int], bool, None]] = Field(..., alias='scope', description='')
    recovery: GoogleCalendarCreateEventOutputVariant2Recovery = Field(..., alias='recovery', description='')


# Union schema: validate external payloads with TypeAdapter(GoogleCalendarCreateEventOutput).
GoogleCalendarCreateEventOutput = Union[GoogleCalendarCreateEventOutputVariant2, GoogleCalendarCreateEventOutputVariant1]

_GoogleCalendarCreateEventInputAdapter = TypeAdapter(GoogleCalendarCreateEventInput)
_GoogleCalendarCreateEventOutputAdapter = TypeAdapter(GoogleCalendarCreateEventOutput)