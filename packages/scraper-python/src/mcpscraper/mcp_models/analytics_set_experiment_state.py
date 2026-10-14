from typing import Annotated, Any, Literal, Union
from typing_extensions import NotRequired, Required, TypedDict
from pydantic import BaseModel, ConfigDict, Field, TypeAdapter


class AnalyticsSetExperimentStateInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=False)

    site_id: str = Field(..., alias='siteId', description='Authorized Analytics Site id.')
    experiment_id: str = Field(..., alias='experimentId', description='Owner-bound experiment id returned by analytics_create_experiment.')
    revision: Annotated[int, Field(le=9007199254740991, gt=0)] = Field(..., alias='revision', description='Exact experiment revision being changed.')
    operation: Literal['approve', 'activate_canary', 'activate', 'pause', 'kill', 'archive'] = Field(..., alias='operation', description='Approval and activation are distinct operations. Pause and kill publish rollback immediately.')
    confirmed: Union[Literal[True], None] = Field(None, alias='confirmed', description='Required for approve, activate_canary, and activate. This confirms only the exact state transition.')
    idempotency_key: Annotated[str, Field(min_length=8, max_length=160)] = Field(..., alias='idempotencyKey', description='Retry key; reuse only for this exact mutation.')


AnalyticsSetExperimentStateOutputVariant1ExperimentPlanStoppingRule = TypedDict('AnalyticsSetExperimentStateOutputVariant1ExperimentPlanStoppingRule', {
    'method': Required[Literal['fixed_horizon']],
    'actionOnSampleRatioMismatch': Required[Literal['pause']],
    'actionOnGuardrailBreach': Required[Literal['pause']],
    'winnerRequiresSignificance': Required[Literal[True]],
})
AnalyticsSetExperimentStateOutputVariant1ExperimentPlanStoppingRule.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


AnalyticsSetExperimentStateOutputVariant1ExperimentPlanRollbackPlan = TypedDict('AnalyticsSetExperimentStateOutputVariant1ExperimentPlanRollbackPlan', {
    'action': Required[Literal['restore_control']],
    'triggers': Required[Annotated[list[Literal['pause', 'kill', 'expiry', 'manifest_error', 'selector_ambiguity', 'performance_guardrail']], Field(min_length=6, max_length=6)]],
})
AnalyticsSetExperimentStateOutputVariant1ExperimentPlanRollbackPlan.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


AnalyticsSetExperimentStateOutputVariant1ExperimentPlanAudience = TypedDict('AnalyticsSetExperimentStateOutputVariant1ExperimentPlanAudience', {
    'routePrefixes': Required[Annotated[list[Annotated[str, Field(max_length=2000)]], Field(min_length=1, max_length=25)]],
    'trafficClass': Required[Literal['internal', 'test', 'production']],
})
AnalyticsSetExperimentStateOutputVariant1ExperimentPlanAudience.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


AnalyticsSetExperimentStateOutputVariant1ExperimentPlanVariantsItemOperationsItemVariant1 = TypedDict('AnalyticsSetExperimentStateOutputVariant1ExperimentPlanVariantsItemOperationsItemVariant1', {
    'kind': Required[Literal['replace_text']],
    'selector': Required[Annotated[str, Field(min_length=1, max_length=500)]],
    'text': Required[Annotated[str, Field(max_length=240)]],
})
AnalyticsSetExperimentStateOutputVariant1ExperimentPlanVariantsItemOperationsItemVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


AnalyticsSetExperimentStateOutputVariant1ExperimentPlanVariantsItemOperationsItemVariant2 = TypedDict('AnalyticsSetExperimentStateOutputVariant1ExperimentPlanVariantsItemOperationsItemVariant2', {
    'kind': Required[Literal['set_style_token']],
    'selector': Required[Annotated[str, Field(min_length=1, max_length=500)]],
    'token': Required[Literal['cta_primary', 'cta_secondary', 'cta_contrast', 'muted', 'highlight']],
})
AnalyticsSetExperimentStateOutputVariant1ExperimentPlanVariantsItemOperationsItemVariant2.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


AnalyticsSetExperimentStateOutputVariant1ExperimentPlanVariantsItemOperationsItemVariant3 = TypedDict('AnalyticsSetExperimentStateOutputVariant1ExperimentPlanVariantsItemOperationsItemVariant3', {
    'kind': Required[Literal['swap_image']],
    'selector': Required[Annotated[str, Field(min_length=1, max_length=500)]],
    'src': Required[Annotated[str, Field(max_length=2000)]],
    'alt': Required[Annotated[str, Field(max_length=240)]],
})
AnalyticsSetExperimentStateOutputVariant1ExperimentPlanVariantsItemOperationsItemVariant3.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


AnalyticsSetExperimentStateOutputVariant1ExperimentPlanVariantsItemOperationsItemVariant4 = TypedDict('AnalyticsSetExperimentStateOutputVariant1ExperimentPlanVariantsItemOperationsItemVariant4', {
    'kind': Required[Literal['move_relative']],
    'selector': Required[Annotated[str, Field(min_length=1, max_length=500)]],
    'anchorSelector': Required[Annotated[str, Field(min_length=1, max_length=500)]],
    'position': Required[Literal['before', 'after']],
})
AnalyticsSetExperimentStateOutputVariant1ExperimentPlanVariantsItemOperationsItemVariant4.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


AnalyticsSetExperimentStateOutputVariant1ExperimentPlanVariantsItemOperationsItemVariant5 = TypedDict('AnalyticsSetExperimentStateOutputVariant1ExperimentPlanVariantsItemOperationsItemVariant5', {
    'kind': Required[Literal['set_visibility']],
    'selector': Required[Annotated[str, Field(min_length=1, max_length=500)]],
    'visible': Required[bool],
})
AnalyticsSetExperimentStateOutputVariant1ExperimentPlanVariantsItemOperationsItemVariant5.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


AnalyticsSetExperimentStateOutputVariant1ExperimentPlanVariantsItem = TypedDict('AnalyticsSetExperimentStateOutputVariant1ExperimentPlanVariantsItem', {
    'variantId': Required[str],
    'label': Required[Annotated[str, Field(min_length=1, max_length=120)]],
    'allocation': Required[Annotated[Union[float, int], Field(le=1, gt=0)]],
    'operations': Required[Annotated[list[Union[AnalyticsSetExperimentStateOutputVariant1ExperimentPlanVariantsItemOperationsItemVariant1, AnalyticsSetExperimentStateOutputVariant1ExperimentPlanVariantsItemOperationsItemVariant2, AnalyticsSetExperimentStateOutputVariant1ExperimentPlanVariantsItemOperationsItemVariant3, AnalyticsSetExperimentStateOutputVariant1ExperimentPlanVariantsItemOperationsItemVariant4, AnalyticsSetExperimentStateOutputVariant1ExperimentPlanVariantsItemOperationsItemVariant5]], Field(max_length=12)]],
})
AnalyticsSetExperimentStateOutputVariant1ExperimentPlanVariantsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


AnalyticsSetExperimentStateOutputVariant1ExperimentPlan = TypedDict('AnalyticsSetExperimentStateOutputVariant1ExperimentPlan', {
    'name': Required[Annotated[str, Field(min_length=1, max_length=120)]],
    'hypothesis': Required[Annotated[str, Field(min_length=10, max_length=500)]],
    'primaryMetricEvent': Required[str],
    'guardrailEvents': Required[Annotated[list[str], Field(max_length=10)]],
    'guardrailMaximumAbsoluteIncrease': Required[Annotated[Union[float, int], Field(le=1, gt=0)]],
    'stoppingRule': Required[AnalyticsSetExperimentStateOutputVariant1ExperimentPlanStoppingRule],
    'rollbackPlan': Required[AnalyticsSetExperimentStateOutputVariant1ExperimentPlanRollbackPlan],
    'performanceGuardrailMs': Required[Annotated[int, Field(ge=1, le=50)]],
    'audience': Required[AnalyticsSetExperimentStateOutputVariant1ExperimentPlanAudience],
    'assignmentUnit': Required[Literal['visitor', 'session']],
    'minimumDurationHours': Required[Annotated[int, Field(ge=24, le=2160)]],
    'minimumExposures': Required[Annotated[int, Field(ge=100, le=10000000)]],
    'minimumDetectableEffect': Required[Annotated[Union[float, int], Field(le=1, gt=0)]],
    'alpha': Required[Annotated[Union[float, int], Field(le=0.2, gt=0)]],
    'power': Required[Annotated[Union[float, int], Field(ge=0.7, le=0.99)]],
    'variants': Required[Annotated[list[AnalyticsSetExperimentStateOutputVariant1ExperimentPlanVariantsItem], Field(min_length=2, max_length=8)]],
    'expiresAt': Required[str],
})
AnalyticsSetExperimentStateOutputVariant1ExperimentPlan.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


AnalyticsSetExperimentStateOutputVariant1Experiment = TypedDict('AnalyticsSetExperimentStateOutputVariant1Experiment', {
    'experimentId': Required[str],
    'siteId': Required[str],
    'revision': Required[Annotated[int, Field(le=9007199254740991, gt=0)]],
    'state': Required[Literal['draft', 'approved', 'canary', 'active', 'paused', 'killed', 'archived']],
    'plan': Required[AnalyticsSetExperimentStateOutputVariant1ExperimentPlan],
})
AnalyticsSetExperimentStateOutputVariant1Experiment.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class AnalyticsSetExperimentStateOutputVariant1(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    ok: Literal[True] = Field(..., alias='ok', description='')
    experiment: AnalyticsSetExperimentStateOutputVariant1Experiment = Field(..., alias='experiment', description='')


AnalyticsSetExperimentStateOutputVariant2DeliveryArtifactsItem = TypedDict('AnalyticsSetExperimentStateOutputVariant2DeliveryArtifactsItem', {
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
AnalyticsSetExperimentStateOutputVariant2DeliveryArtifactsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


AnalyticsSetExperimentStateOutputVariant2DeliveryStorageFailureVariant1 = TypedDict('AnalyticsSetExperimentStateOutputVariant2DeliveryStorageFailureVariant1', {
    'artifactId': Required[Union[str, None]],
    'outcome': Required[Literal['unknown', 'bytes-stored-metadata-pending', 'failed']],
})
AnalyticsSetExperimentStateOutputVariant2DeliveryStorageFailureVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


AnalyticsSetExperimentStateOutputVariant2Delivery = TypedDict('AnalyticsSetExperimentStateOutputVariant2Delivery', {
    'mode': Required[Literal['artifact']],
    'status': Required[Literal['complete', 'partial', 'unavailable']],
    'retainedRepresentation': Required[Literal['formatted-tool-result']],
    'sourceIsError': Required[bool],
    'artifacts': Required[list[AnalyticsSetExperimentStateOutputVariant2DeliveryArtifactsItem]],
    'downloadLinksOmitted': Required[bool],
    'scopeOmittedFields': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'storageFailure': Required[Union[AnalyticsSetExperimentStateOutputVariant2DeliveryStorageFailureVariant1, None]],
    'nextAction': Required[str],
})
AnalyticsSetExperimentStateOutputVariant2Delivery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


AnalyticsSetExperimentStateOutputVariant2RecoveryOperation = TypedDict('AnalyticsSetExperimentStateOutputVariant2RecoveryOperation', {
    'runId': Required[Union[Annotated[str, Field(max_length=200)], None]],
    'idempotencyKey': Required[Annotated[str, Field(max_length=512)]],
    'state': Required[Annotated[str, Field(max_length=100)]],
})
AnalyticsSetExperimentStateOutputVariant2RecoveryOperation.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


AnalyticsSetExperimentStateOutputVariant2Recovery = TypedDict('AnalyticsSetExperimentStateOutputVariant2Recovery', {
    'idempotencyKey': NotRequired[Annotated[str, Field(max_length=512)]],
    'operationId': NotRequired[Annotated[str, Field(max_length=200)]],
    'runId': NotRequired[Annotated[str, Field(max_length=200)]],
    'jobId': NotRequired[Annotated[str, Field(max_length=200)]],
    'operation': NotRequired[AnalyticsSetExperimentStateOutputVariant2RecoveryOperation],
})
AnalyticsSetExperimentStateOutputVariant2Recovery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class AnalyticsSetExperimentStateOutputVariant2(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    delivery: AnalyticsSetExperimentStateOutputVariant2Delivery = Field(..., alias='delivery', description='')
    preview: str = Field(..., alias='preview', description='')
    scope: dict[str, Union[str, Union[float, int], bool, None]] = Field(..., alias='scope', description='')
    recovery: AnalyticsSetExperimentStateOutputVariant2Recovery = Field(..., alias='recovery', description='')


# Union schema: validate external payloads with TypeAdapter(AnalyticsSetExperimentStateOutput).
AnalyticsSetExperimentStateOutput = Union[AnalyticsSetExperimentStateOutputVariant2, AnalyticsSetExperimentStateOutputVariant1]

_AnalyticsSetExperimentStateInputAdapter = TypeAdapter(AnalyticsSetExperimentStateInput)
_AnalyticsSetExperimentStateOutputAdapter = TypeAdapter(AnalyticsSetExperimentStateOutput)