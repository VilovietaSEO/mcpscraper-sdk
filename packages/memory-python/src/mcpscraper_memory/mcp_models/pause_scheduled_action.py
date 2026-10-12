from typing import Annotated, Any, Literal, Union
from typing_extensions import NotRequired, Required, TypedDict
from pydantic import BaseModel, ConfigDict, Field, TypeAdapter


class PauseScheduledActionInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=False)

    id: Annotated[str, Field(min_length=1)] = Field(..., alias='id', description='The scheduled action id, from create-scheduled-action or list-scheduled-actions.')


class PauseScheduledActionOutputVariant1(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    ok: bool = Field(..., alias='ok', description='')
    error: Union[str, None] = Field(None, alias='error', description='')


PauseScheduledActionOutputVariant2DeliveryArtifactsItem = TypedDict('PauseScheduledActionOutputVariant2DeliveryArtifactsItem', {
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
PauseScheduledActionOutputVariant2DeliveryArtifactsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


PauseScheduledActionOutputVariant2DeliveryStorageFailureVariant1 = TypedDict('PauseScheduledActionOutputVariant2DeliveryStorageFailureVariant1', {
    'artifactId': Required[Union[str, None]],
    'outcome': Required[Literal['unknown', 'bytes-stored-metadata-pending', 'failed']],
})
PauseScheduledActionOutputVariant2DeliveryStorageFailureVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


PauseScheduledActionOutputVariant2Delivery = TypedDict('PauseScheduledActionOutputVariant2Delivery', {
    'mode': Required[Literal['artifact']],
    'status': Required[Literal['complete', 'partial', 'unavailable']],
    'retainedRepresentation': Required[Literal['formatted-tool-result']],
    'sourceIsError': Required[bool],
    'artifacts': Required[list[PauseScheduledActionOutputVariant2DeliveryArtifactsItem]],
    'downloadLinksOmitted': Required[bool],
    'scopeOmittedFields': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'storageFailure': Required[Union[PauseScheduledActionOutputVariant2DeliveryStorageFailureVariant1, None]],
    'nextAction': Required[str],
})
PauseScheduledActionOutputVariant2Delivery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


PauseScheduledActionOutputVariant2RecoveryOperation = TypedDict('PauseScheduledActionOutputVariant2RecoveryOperation', {
    'runId': Required[Union[Annotated[str, Field(max_length=200)], None]],
    'idempotencyKey': Required[Annotated[str, Field(max_length=512)]],
    'state': Required[Annotated[str, Field(max_length=100)]],
})
PauseScheduledActionOutputVariant2RecoveryOperation.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


PauseScheduledActionOutputVariant2Recovery = TypedDict('PauseScheduledActionOutputVariant2Recovery', {
    'idempotencyKey': NotRequired[Annotated[str, Field(max_length=512)]],
    'operationId': NotRequired[Annotated[str, Field(max_length=200)]],
    'runId': NotRequired[Annotated[str, Field(max_length=200)]],
    'jobId': NotRequired[Annotated[str, Field(max_length=200)]],
    'operation': NotRequired[PauseScheduledActionOutputVariant2RecoveryOperation],
})
PauseScheduledActionOutputVariant2Recovery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class PauseScheduledActionOutputVariant2(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    delivery: PauseScheduledActionOutputVariant2Delivery = Field(..., alias='delivery', description='')
    preview: str = Field(..., alias='preview', description='')
    scope: dict[str, Union[str, Union[float, int], bool, None]] = Field(..., alias='scope', description='')
    recovery: PauseScheduledActionOutputVariant2Recovery = Field(..., alias='recovery', description='')


# Union schema: validate external payloads with TypeAdapter(PauseScheduledActionOutput).
PauseScheduledActionOutput = Union[PauseScheduledActionOutputVariant2, PauseScheduledActionOutputVariant1]

_PauseScheduledActionInputAdapter = TypeAdapter(PauseScheduledActionInput)
_PauseScheduledActionOutputAdapter = TypeAdapter(PauseScheduledActionOutput)