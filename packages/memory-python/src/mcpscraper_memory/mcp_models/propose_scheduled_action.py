from typing import Annotated, Any, Literal, Union
from typing_extensions import NotRequired, Required, TypedDict
from pydantic import BaseModel, ConfigDict, Field, TypeAdapter


class ProposeScheduledActionInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=False)

    request: Annotated[str, Field(min_length=1)] = Field(..., alias='request', description='Freeform text describing what you want scheduled.')


class ProposeScheduledActionOutputVariant1(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    ok: bool = Field(..., alias='ok', description='')
    description: Union[str, None] = Field(None, alias='description', description='Proposed description — edit freely before confirming.')
    vault: Union[str, None] = Field(None, alias='vault', description='Proposed target vault.')
    cadence: Union[str, None] = Field(None, alias='cadence', description='Proposed cadence: once, daily, weekly, or monthly.')
    time_of_day: Union[str, None] = Field(None, alias='timeOfDay', description='Proposed 24-hour HH:MM run time, when the request named one.')
    timezone: Union[str, None] = Field(None, alias='timezone', description='Proposed IANA timezone — from the request, or the account default when the request named a time without a zone.')
    rationale: Union[str, None] = Field(None, alias='rationale', description='Why these choices were made — read this before confirming.')
    error: Union[str, None] = Field(None, alias='error', description='')


ProposeScheduledActionOutputVariant2DeliveryArtifactsItem = TypedDict('ProposeScheduledActionOutputVariant2DeliveryArtifactsItem', {
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
ProposeScheduledActionOutputVariant2DeliveryArtifactsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


ProposeScheduledActionOutputVariant2DeliveryStorageFailureVariant1 = TypedDict('ProposeScheduledActionOutputVariant2DeliveryStorageFailureVariant1', {
    'artifactId': Required[Union[str, None]],
    'outcome': Required[Literal['unknown', 'bytes-stored-metadata-pending', 'failed']],
})
ProposeScheduledActionOutputVariant2DeliveryStorageFailureVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


ProposeScheduledActionOutputVariant2Delivery = TypedDict('ProposeScheduledActionOutputVariant2Delivery', {
    'mode': Required[Literal['artifact']],
    'status': Required[Literal['complete', 'partial', 'unavailable']],
    'retainedRepresentation': Required[Literal['formatted-tool-result']],
    'sourceIsError': Required[bool],
    'artifacts': Required[list[ProposeScheduledActionOutputVariant2DeliveryArtifactsItem]],
    'downloadLinksOmitted': Required[bool],
    'scopeOmittedFields': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'storageFailure': Required[Union[ProposeScheduledActionOutputVariant2DeliveryStorageFailureVariant1, None]],
    'nextAction': Required[str],
})
ProposeScheduledActionOutputVariant2Delivery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


ProposeScheduledActionOutputVariant2RecoveryOperation = TypedDict('ProposeScheduledActionOutputVariant2RecoveryOperation', {
    'runId': Required[Union[Annotated[str, Field(max_length=200)], None]],
    'idempotencyKey': Required[Annotated[str, Field(max_length=512)]],
    'state': Required[Annotated[str, Field(max_length=100)]],
})
ProposeScheduledActionOutputVariant2RecoveryOperation.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


ProposeScheduledActionOutputVariant2Recovery = TypedDict('ProposeScheduledActionOutputVariant2Recovery', {
    'idempotencyKey': NotRequired[Annotated[str, Field(max_length=512)]],
    'operationId': NotRequired[Annotated[str, Field(max_length=200)]],
    'runId': NotRequired[Annotated[str, Field(max_length=200)]],
    'jobId': NotRequired[Annotated[str, Field(max_length=200)]],
    'operation': NotRequired[ProposeScheduledActionOutputVariant2RecoveryOperation],
})
ProposeScheduledActionOutputVariant2Recovery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class ProposeScheduledActionOutputVariant2(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    delivery: ProposeScheduledActionOutputVariant2Delivery = Field(..., alias='delivery', description='')
    preview: str = Field(..., alias='preview', description='')
    scope: dict[str, Union[str, Union[float, int], bool, None]] = Field(..., alias='scope', description='')
    recovery: ProposeScheduledActionOutputVariant2Recovery = Field(..., alias='recovery', description='')


# Union schema: validate external payloads with TypeAdapter(ProposeScheduledActionOutput).
ProposeScheduledActionOutput = Union[ProposeScheduledActionOutputVariant2, ProposeScheduledActionOutputVariant1]

_ProposeScheduledActionInputAdapter = TypeAdapter(ProposeScheduledActionInput)
_ProposeScheduledActionOutputAdapter = TypeAdapter(ProposeScheduledActionOutput)