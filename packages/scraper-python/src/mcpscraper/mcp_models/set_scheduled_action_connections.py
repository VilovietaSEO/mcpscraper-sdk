from typing import Annotated, Any, Literal, Union
from typing_extensions import NotRequired, Required, TypedDict
from pydantic import BaseModel, ConfigDict, Field, TypeAdapter


SetScheduledActionConnectionsInputConnectionsItem = TypedDict('SetScheduledActionConnectionsInputConnectionsItem', {
    'connectionId': Required[Annotated[str, Field(min_length=1)]],
    'providerConfigKey': Required[Annotated[str, Field(min_length=1)]],
    'allowedTools': Required[Annotated[list[Annotated[str, Field(min_length=1)]], Field(min_length=1, max_length=100)]],
})
SetScheduledActionConnectionsInputConnectionsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=False)


class SetScheduledActionConnectionsInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=False)

    schedule_action_id: Annotated[str, Field(min_length=1)] = Field(..., alias='scheduleActionId', description='A scheduled action id returned by create-scheduled-action or list-scheduled-actions.')
    connections: Annotated[list[SetScheduledActionConnectionsInputConnectionsItem], Field(max_length=20)] = Field(..., alias='connections', description='Exact connection and tool grants for this schedule. Pass an empty array to remove every external-service grant.')


class SetScheduledActionConnectionsOutputVariant1(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    ok: bool = Field(..., alias='ok', description='')
    connections: Union[list[Any], None] = Field(None, alias='connections', description='')
    error: Union[str, None] = Field(..., alias='error', description='')


SetScheduledActionConnectionsOutputVariant2DeliveryArtifactsItem = TypedDict('SetScheduledActionConnectionsOutputVariant2DeliveryArtifactsItem', {
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
SetScheduledActionConnectionsOutputVariant2DeliveryArtifactsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


SetScheduledActionConnectionsOutputVariant2DeliveryStorageFailureVariant1 = TypedDict('SetScheduledActionConnectionsOutputVariant2DeliveryStorageFailureVariant1', {
    'artifactId': Required[Union[str, None]],
    'outcome': Required[Literal['unknown', 'bytes-stored-metadata-pending', 'failed']],
})
SetScheduledActionConnectionsOutputVariant2DeliveryStorageFailureVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


SetScheduledActionConnectionsOutputVariant2Delivery = TypedDict('SetScheduledActionConnectionsOutputVariant2Delivery', {
    'mode': Required[Literal['artifact']],
    'status': Required[Literal['complete', 'partial', 'unavailable']],
    'retainedRepresentation': Required[Literal['formatted-tool-result']],
    'sourceIsError': Required[bool],
    'artifacts': Required[list[SetScheduledActionConnectionsOutputVariant2DeliveryArtifactsItem]],
    'downloadLinksOmitted': Required[bool],
    'scopeOmittedFields': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'storageFailure': Required[Union[SetScheduledActionConnectionsOutputVariant2DeliveryStorageFailureVariant1, None]],
    'nextAction': Required[str],
})
SetScheduledActionConnectionsOutputVariant2Delivery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


SetScheduledActionConnectionsOutputVariant2RecoveryOperation = TypedDict('SetScheduledActionConnectionsOutputVariant2RecoveryOperation', {
    'runId': Required[Union[Annotated[str, Field(max_length=200)], None]],
    'idempotencyKey': Required[Annotated[str, Field(max_length=512)]],
    'state': Required[Annotated[str, Field(max_length=100)]],
})
SetScheduledActionConnectionsOutputVariant2RecoveryOperation.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


SetScheduledActionConnectionsOutputVariant2Recovery = TypedDict('SetScheduledActionConnectionsOutputVariant2Recovery', {
    'idempotencyKey': NotRequired[Annotated[str, Field(max_length=512)]],
    'operationId': NotRequired[Annotated[str, Field(max_length=200)]],
    'runId': NotRequired[Annotated[str, Field(max_length=200)]],
    'jobId': NotRequired[Annotated[str, Field(max_length=200)]],
    'operation': NotRequired[SetScheduledActionConnectionsOutputVariant2RecoveryOperation],
})
SetScheduledActionConnectionsOutputVariant2Recovery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class SetScheduledActionConnectionsOutputVariant2(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    delivery: SetScheduledActionConnectionsOutputVariant2Delivery = Field(..., alias='delivery', description='')
    preview: str = Field(..., alias='preview', description='')
    scope: dict[str, Union[str, Union[float, int], bool, None]] = Field(..., alias='scope', description='')
    recovery: SetScheduledActionConnectionsOutputVariant2Recovery = Field(..., alias='recovery', description='')


# Union schema: validate external payloads with TypeAdapter(SetScheduledActionConnectionsOutput).
SetScheduledActionConnectionsOutput = Union[SetScheduledActionConnectionsOutputVariant2, SetScheduledActionConnectionsOutputVariant1]

_SetScheduledActionConnectionsInputAdapter = TypeAdapter(SetScheduledActionConnectionsInput)
_SetScheduledActionConnectionsOutputAdapter = TypeAdapter(SetScheduledActionConnectionsOutput)