from typing import Annotated, Any, Literal, Union
from typing_extensions import NotRequired, Required, TypedDict
from pydantic import BaseModel, ConfigDict, Field, TypeAdapter


CreateScheduledActionInputArtifactSelectionVariant1 = TypedDict('CreateScheduledActionInputArtifactSelectionVariant1', {
    'mode': Required[Literal['none']],
})
CreateScheduledActionInputArtifactSelectionVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=False)


CreateScheduledActionInputArtifactSelectionVariant2 = TypedDict('CreateScheduledActionInputArtifactSelectionVariant2', {
    'mode': Required[Literal['saved_template']],
    'templateId': Required[str],
    'templateVersionId': Required[str],
})
CreateScheduledActionInputArtifactSelectionVariant2.__pydantic_config__ = ConfigDict(extra="allow", strict=False)


class CreateScheduledActionInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=False)

    description: Annotated[str, Field(min_length=1)] = Field(..., alias='description', description='Free-text description of what this action should do each time it runs.')
    vault: Annotated[str, Field(min_length=1)] = Field(..., alias='vault', description='The vault this action writes its results into. You must already have write access to it.')
    cadence: Literal['once', 'daily', 'weekly', 'monthly'] = Field(..., alias='cadence', description='How often this action runs. "once" fires a single time and then completes.')
    execution_mode: Union[Literal['agent', 'connection_sync'], None] = Field(None, alias='executionMode', description='How to execute each run. "agent" (default) lets an agent follow the description. "connection_sync" deterministically ingests data from the schedule\'s bound connections using only their approved read-only tools; bind at least one connection before it runs.')
    time_of_day: Union[str, None] = Field(None, alias='timeOfDay', description='24-hour HH:MM clock time to run at, in the given timezone. Optional — omit to run at any time during the period (matches prior default behavior).')
    timezone: Union[str, None] = Field(None, alias='timezone', description='IANA timezone name, e.g. "America/Denver". Only meaningful together with timeOfDay or deployDate. Omit to use the account\'s default timezone (set via set-schedule-defaults), falling back to UTC.')
    deploy_date: Union[str, None] = Field(None, alias='deployDate', description='Calendar date (YYYY-MM-DD, in the given timezone) this action should first become eligible to run — its deployment/start date. For recurring cadences, the first occurrence lands on or after this date; every later occurrence still follows the normal cadence. For cadence "once", this (combined with timeOfDay if given) is exactly what day it fires. Omit to start immediately.')
    artifact_selection: Union[Union[CreateScheduledActionInputArtifactSelectionVariant1, CreateScheduledActionInputArtifactSelectionVariant2], None] = Field(None, alias='artifactSelection', description='Presentation artifact selection. "none" means no HTML artifact; it does not disable writing the scheduled result to Memory. A saved_template selection pins one exact immutable template version.')


CreateScheduledActionOutputVariant1ArtifactSelectionVariant1 = TypedDict('CreateScheduledActionOutputVariant1ArtifactSelectionVariant1', {
    'mode': Required[Literal['none']],
})
CreateScheduledActionOutputVariant1ArtifactSelectionVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


CreateScheduledActionOutputVariant1ArtifactSelectionVariant2 = TypedDict('CreateScheduledActionOutputVariant1ArtifactSelectionVariant2', {
    'mode': Required[Literal['saved_template']],
    'templateId': Required[str],
    'templateVersionId': Required[str],
})
CreateScheduledActionOutputVariant1ArtifactSelectionVariant2.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class CreateScheduledActionOutputVariant1(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    ok: bool = Field(..., alias='ok', description='True when the scheduled action was created.')
    id: Union[str, None] = Field(None, alias='id', description='The new scheduled action id.')
    next_run_at: Union[str, None] = Field(None, alias='nextRunAt', description='When it will first run.')
    execution_mode: Union[Literal['agent', 'connection_sync'], None] = Field(None, alias='executionMode', description='The stored execution mode. Defaults to agent when omitted from the request.')
    artifact_selection: Union[Union[CreateScheduledActionOutputVariant1ArtifactSelectionVariant1, CreateScheduledActionOutputVariant1ArtifactSelectionVariant2], None] = Field(None, alias='artifactSelection', description='The exact stored artifact selection.')
    error: Union[str, None] = Field(None, alias='error', description='Human-readable failure reason when ok is false.')
    code: Union[str, None] = Field(None, alias='code', description='Machine-readable denial code when creation is refused.')


CreateScheduledActionOutputVariant2DeliveryArtifactsItem = TypedDict('CreateScheduledActionOutputVariant2DeliveryArtifactsItem', {
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
CreateScheduledActionOutputVariant2DeliveryArtifactsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


CreateScheduledActionOutputVariant2DeliveryStorageFailureVariant1 = TypedDict('CreateScheduledActionOutputVariant2DeliveryStorageFailureVariant1', {
    'artifactId': Required[Union[str, None]],
    'outcome': Required[Literal['unknown', 'bytes-stored-metadata-pending', 'failed']],
})
CreateScheduledActionOutputVariant2DeliveryStorageFailureVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


CreateScheduledActionOutputVariant2Delivery = TypedDict('CreateScheduledActionOutputVariant2Delivery', {
    'mode': Required[Literal['artifact']],
    'status': Required[Literal['complete', 'partial', 'unavailable']],
    'retainedRepresentation': Required[Literal['formatted-tool-result']],
    'sourceIsError': Required[bool],
    'artifacts': Required[list[CreateScheduledActionOutputVariant2DeliveryArtifactsItem]],
    'downloadLinksOmitted': Required[bool],
    'scopeOmittedFields': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'storageFailure': Required[Union[CreateScheduledActionOutputVariant2DeliveryStorageFailureVariant1, None]],
    'nextAction': Required[str],
})
CreateScheduledActionOutputVariant2Delivery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


CreateScheduledActionOutputVariant2RecoveryOperation = TypedDict('CreateScheduledActionOutputVariant2RecoveryOperation', {
    'runId': Required[Union[Annotated[str, Field(max_length=200)], None]],
    'idempotencyKey': Required[Annotated[str, Field(max_length=512)]],
    'state': Required[Annotated[str, Field(max_length=100)]],
})
CreateScheduledActionOutputVariant2RecoveryOperation.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


CreateScheduledActionOutputVariant2Recovery = TypedDict('CreateScheduledActionOutputVariant2Recovery', {
    'idempotencyKey': NotRequired[Annotated[str, Field(max_length=512)]],
    'operationId': NotRequired[Annotated[str, Field(max_length=200)]],
    'runId': NotRequired[Annotated[str, Field(max_length=200)]],
    'jobId': NotRequired[Annotated[str, Field(max_length=200)]],
    'operation': NotRequired[CreateScheduledActionOutputVariant2RecoveryOperation],
})
CreateScheduledActionOutputVariant2Recovery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class CreateScheduledActionOutputVariant2(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    delivery: CreateScheduledActionOutputVariant2Delivery = Field(..., alias='delivery', description='')
    preview: str = Field(..., alias='preview', description='')
    scope: dict[str, Union[str, Union[float, int], bool, None]] = Field(..., alias='scope', description='')
    recovery: CreateScheduledActionOutputVariant2Recovery = Field(..., alias='recovery', description='')


# Union schema: validate external payloads with TypeAdapter(CreateScheduledActionOutput).
CreateScheduledActionOutput = Union[CreateScheduledActionOutputVariant2, CreateScheduledActionOutputVariant1]

_CreateScheduledActionInputAdapter = TypeAdapter(CreateScheduledActionInput)
_CreateScheduledActionOutputAdapter = TypeAdapter(CreateScheduledActionOutput)