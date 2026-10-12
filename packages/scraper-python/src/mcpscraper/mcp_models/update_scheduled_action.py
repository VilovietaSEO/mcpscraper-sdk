from typing import Annotated, Any, Literal, Union
from typing_extensions import NotRequired, Required, TypedDict
from pydantic import BaseModel, ConfigDict, Field, TypeAdapter


UpdateScheduledActionInputArtifactSelectionVariant1 = TypedDict('UpdateScheduledActionInputArtifactSelectionVariant1', {
    'mode': Required[Literal['none']],
})
UpdateScheduledActionInputArtifactSelectionVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=False)


UpdateScheduledActionInputArtifactSelectionVariant2 = TypedDict('UpdateScheduledActionInputArtifactSelectionVariant2', {
    'mode': Required[Literal['saved_template']],
    'templateId': Required[str],
    'templateVersionId': Required[str],
})
UpdateScheduledActionInputArtifactSelectionVariant2.__pydantic_config__ = ConfigDict(extra="allow", strict=False)


class UpdateScheduledActionInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=False)

    id: Annotated[str, Field(min_length=1)] = Field(..., alias='id', description='The scheduled action id.')
    description: Union[Annotated[str, Field(min_length=1)], None] = Field(None, alias='description', description='Human-readable summary that distinguishes this record from similarly named records.')
    vault: Union[Annotated[str, Field(min_length=1)], None] = Field(None, alias='vault', description='Exact accessible Memory vault name; omit only when this tool documents a safe active-vault default.')
    cadence: Union[Literal['once', 'daily', 'weekly', 'monthly'], None] = Field(None, alias='cadence', description='New execution cadence; omit to preserve the scheduled action cadence.')
    time_of_day: Union[Union[str, None], None] = Field(None, alias='timeOfDay', description='Local execution time in 24-hour HH:MM form; null clears the stored time.')
    timezone: Union[str, None] = Field(None, alias='timezone', description='IANA timezone for schedule evaluation; omit to preserve the current timezone.')
    artifact_selection: Union[Union[UpdateScheduledActionInputArtifactSelectionVariant1, UpdateScheduledActionInputArtifactSelectionVariant2], None] = Field(None, alias='artifactSelection', description='Explicit HTML artifact choice; omit to preserve the current selection.')


UpdateScheduledActionOutputVariant1ArtifactSelectionVariant1 = TypedDict('UpdateScheduledActionOutputVariant1ArtifactSelectionVariant1', {
    'mode': Required[Literal['none']],
})
UpdateScheduledActionOutputVariant1ArtifactSelectionVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


UpdateScheduledActionOutputVariant1ArtifactSelectionVariant2 = TypedDict('UpdateScheduledActionOutputVariant1ArtifactSelectionVariant2', {
    'mode': Required[Literal['saved_template']],
    'templateId': Required[str],
    'templateVersionId': Required[str],
})
UpdateScheduledActionOutputVariant1ArtifactSelectionVariant2.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class UpdateScheduledActionOutputVariant1(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    ok: bool = Field(..., alias='ok', description='')
    artifact_selection: Union[Union[UpdateScheduledActionOutputVariant1ArtifactSelectionVariant1, UpdateScheduledActionOutputVariant1ArtifactSelectionVariant2], None] = Field(None, alias='artifactSelection', description='')
    error: Union[str, None] = Field(None, alias='error', description='')
    error_code: Union[str, None] = Field(None, alias='errorCode', description='')


UpdateScheduledActionOutputVariant2DeliveryArtifactsItem = TypedDict('UpdateScheduledActionOutputVariant2DeliveryArtifactsItem', {
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
UpdateScheduledActionOutputVariant2DeliveryArtifactsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


UpdateScheduledActionOutputVariant2DeliveryStorageFailureVariant1 = TypedDict('UpdateScheduledActionOutputVariant2DeliveryStorageFailureVariant1', {
    'artifactId': Required[Union[str, None]],
    'outcome': Required[Literal['unknown', 'bytes-stored-metadata-pending', 'failed']],
})
UpdateScheduledActionOutputVariant2DeliveryStorageFailureVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


UpdateScheduledActionOutputVariant2Delivery = TypedDict('UpdateScheduledActionOutputVariant2Delivery', {
    'mode': Required[Literal['artifact']],
    'status': Required[Literal['complete', 'partial', 'unavailable']],
    'retainedRepresentation': Required[Literal['formatted-tool-result']],
    'sourceIsError': Required[bool],
    'artifacts': Required[list[UpdateScheduledActionOutputVariant2DeliveryArtifactsItem]],
    'downloadLinksOmitted': Required[bool],
    'scopeOmittedFields': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'storageFailure': Required[Union[UpdateScheduledActionOutputVariant2DeliveryStorageFailureVariant1, None]],
    'nextAction': Required[str],
})
UpdateScheduledActionOutputVariant2Delivery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


UpdateScheduledActionOutputVariant2RecoveryOperation = TypedDict('UpdateScheduledActionOutputVariant2RecoveryOperation', {
    'runId': Required[Union[Annotated[str, Field(max_length=200)], None]],
    'idempotencyKey': Required[Annotated[str, Field(max_length=512)]],
    'state': Required[Annotated[str, Field(max_length=100)]],
})
UpdateScheduledActionOutputVariant2RecoveryOperation.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


UpdateScheduledActionOutputVariant2Recovery = TypedDict('UpdateScheduledActionOutputVariant2Recovery', {
    'idempotencyKey': NotRequired[Annotated[str, Field(max_length=512)]],
    'operationId': NotRequired[Annotated[str, Field(max_length=200)]],
    'runId': NotRequired[Annotated[str, Field(max_length=200)]],
    'jobId': NotRequired[Annotated[str, Field(max_length=200)]],
    'operation': NotRequired[UpdateScheduledActionOutputVariant2RecoveryOperation],
})
UpdateScheduledActionOutputVariant2Recovery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class UpdateScheduledActionOutputVariant2(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    delivery: UpdateScheduledActionOutputVariant2Delivery = Field(..., alias='delivery', description='')
    preview: str = Field(..., alias='preview', description='')
    scope: dict[str, Union[str, Union[float, int], bool, None]] = Field(..., alias='scope', description='')
    recovery: UpdateScheduledActionOutputVariant2Recovery = Field(..., alias='recovery', description='')


# Union schema: validate external payloads with TypeAdapter(UpdateScheduledActionOutput).
UpdateScheduledActionOutput = Union[UpdateScheduledActionOutputVariant2, UpdateScheduledActionOutputVariant1]

_UpdateScheduledActionInputAdapter = TypeAdapter(UpdateScheduledActionInput)
_UpdateScheduledActionOutputAdapter = TypeAdapter(UpdateScheduledActionOutput)