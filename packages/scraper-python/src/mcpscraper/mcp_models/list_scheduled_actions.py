from typing import Annotated, Any, Literal, Union
from typing_extensions import NotRequired, Required, TypedDict
from pydantic import BaseModel, ConfigDict, Field, TypeAdapter


class ListScheduledActionsInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=False)



ListScheduledActionsOutputVariant1ActionsItemArtifactSelectionVariant1 = TypedDict('ListScheduledActionsOutputVariant1ActionsItemArtifactSelectionVariant1', {
    'mode': Required[Literal['none']],
})
ListScheduledActionsOutputVariant1ActionsItemArtifactSelectionVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


ListScheduledActionsOutputVariant1ActionsItemArtifactSelectionVariant2 = TypedDict('ListScheduledActionsOutputVariant1ActionsItemArtifactSelectionVariant2', {
    'mode': Required[Literal['saved_template']],
    'templateId': Required[str],
    'templateVersionId': Required[str],
})
ListScheduledActionsOutputVariant1ActionsItemArtifactSelectionVariant2.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


ListScheduledActionsOutputVariant1ActionsItem = TypedDict('ListScheduledActionsOutputVariant1ActionsItem', {
    'id': Required[str],
    'description': Required[str],
    'vault': Required[str],
    'cadence': Required[Literal['once', 'daily', 'weekly', 'monthly']],
    'executionMode': Required[Literal['agent', 'connection_sync']],
    'artifactSelection': Required[Union[ListScheduledActionsOutputVariant1ActionsItemArtifactSelectionVariant1, ListScheduledActionsOutputVariant1ActionsItemArtifactSelectionVariant2]],
    'timeOfDay': Required[Union[str, None]],
    'timezone': Required[str],
    'status': Required[Literal['active', 'paused', 'completed']],
    'nextRunAt': Required[str],
    'lastRunAt': Required[Union[str, None]],
    'lastRunStatus': Required[Union[str, None]],
    'system': Required[bool],
})
ListScheduledActionsOutputVariant1ActionsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class ListScheduledActionsOutputVariant1(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    ok: bool = Field(..., alias='ok', description='')
    actions: Union[list[ListScheduledActionsOutputVariant1ActionsItem], None] = Field(None, alias='actions', description='')
    error: Union[str, None] = Field(None, alias='error', description='')


ListScheduledActionsOutputVariant2DeliveryArtifactsItem = TypedDict('ListScheduledActionsOutputVariant2DeliveryArtifactsItem', {
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
ListScheduledActionsOutputVariant2DeliveryArtifactsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


ListScheduledActionsOutputVariant2DeliveryStorageFailureVariant1 = TypedDict('ListScheduledActionsOutputVariant2DeliveryStorageFailureVariant1', {
    'artifactId': Required[Union[str, None]],
    'outcome': Required[Literal['unknown', 'bytes-stored-metadata-pending', 'failed']],
})
ListScheduledActionsOutputVariant2DeliveryStorageFailureVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


ListScheduledActionsOutputVariant2Delivery = TypedDict('ListScheduledActionsOutputVariant2Delivery', {
    'mode': Required[Literal['artifact']],
    'status': Required[Literal['complete', 'partial', 'unavailable']],
    'retainedRepresentation': Required[Literal['formatted-tool-result']],
    'sourceIsError': Required[bool],
    'artifacts': Required[list[ListScheduledActionsOutputVariant2DeliveryArtifactsItem]],
    'downloadLinksOmitted': Required[bool],
    'scopeOmittedFields': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'storageFailure': Required[Union[ListScheduledActionsOutputVariant2DeliveryStorageFailureVariant1, None]],
    'nextAction': Required[str],
})
ListScheduledActionsOutputVariant2Delivery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


ListScheduledActionsOutputVariant2RecoveryOperation = TypedDict('ListScheduledActionsOutputVariant2RecoveryOperation', {
    'runId': Required[Union[Annotated[str, Field(max_length=200)], None]],
    'idempotencyKey': Required[Annotated[str, Field(max_length=512)]],
    'state': Required[Annotated[str, Field(max_length=100)]],
})
ListScheduledActionsOutputVariant2RecoveryOperation.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


ListScheduledActionsOutputVariant2Recovery = TypedDict('ListScheduledActionsOutputVariant2Recovery', {
    'idempotencyKey': NotRequired[Annotated[str, Field(max_length=512)]],
    'operationId': NotRequired[Annotated[str, Field(max_length=200)]],
    'runId': NotRequired[Annotated[str, Field(max_length=200)]],
    'jobId': NotRequired[Annotated[str, Field(max_length=200)]],
    'operation': NotRequired[ListScheduledActionsOutputVariant2RecoveryOperation],
})
ListScheduledActionsOutputVariant2Recovery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class ListScheduledActionsOutputVariant2(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    delivery: ListScheduledActionsOutputVariant2Delivery = Field(..., alias='delivery', description='')
    preview: str = Field(..., alias='preview', description='')
    scope: dict[str, Union[str, Union[float, int], bool, None]] = Field(..., alias='scope', description='')
    recovery: ListScheduledActionsOutputVariant2Recovery = Field(..., alias='recovery', description='')


# Union schema: validate external payloads with TypeAdapter(ListScheduledActionsOutput).
ListScheduledActionsOutput = Union[ListScheduledActionsOutputVariant2, ListScheduledActionsOutputVariant1]

_ListScheduledActionsInputAdapter = TypeAdapter(ListScheduledActionsInput)
_ListScheduledActionsOutputAdapter = TypeAdapter(ListScheduledActionsOutput)