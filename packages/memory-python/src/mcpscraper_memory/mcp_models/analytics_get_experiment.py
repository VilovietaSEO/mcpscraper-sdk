from typing import Annotated, Any, Literal, Union
from typing_extensions import NotRequired, Required, TypedDict
from pydantic import BaseModel, ConfigDict, Field, TypeAdapter


class AnalyticsGetExperimentInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=False)

    site_id: str = Field(..., alias='siteId', description='Authorized Analytics Site id.')
    experiment_id: str = Field(..., alias='experimentId', description='Owner-bound experiment id returned by analytics_create_experiment.')


AnalyticsGetExperimentOutputVariant1ExperimentPlanStoppingRule = TypedDict('AnalyticsGetExperimentOutputVariant1ExperimentPlanStoppingRule', {
    'method': Required[Literal['fixed_horizon']],
    'actionOnSampleRatioMismatch': Required[Literal['pause']],
    'actionOnGuardrailBreach': Required[Literal['pause']],
    'winnerRequiresSignificance': Required[Literal[True]],
})
AnalyticsGetExperimentOutputVariant1ExperimentPlanStoppingRule.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


AnalyticsGetExperimentOutputVariant1ExperimentPlanRollbackPlan = TypedDict('AnalyticsGetExperimentOutputVariant1ExperimentPlanRollbackPlan', {
    'action': Required[Literal['restore_control']],
    'triggers': Required[Annotated[list[Literal['pause', 'kill', 'expiry', 'manifest_error', 'selector_ambiguity', 'performance_guardrail']], Field(min_length=6, max_length=6)]],
})
AnalyticsGetExperimentOutputVariant1ExperimentPlanRollbackPlan.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


AnalyticsGetExperimentOutputVariant1ExperimentPlanAudience = TypedDict('AnalyticsGetExperimentOutputVariant1ExperimentPlanAudience', {
    'routePrefixes': Required[Annotated[list[Annotated[str, Field(max_length=2000)]], Field(min_length=1, max_length=25)]],
    'trafficClass': Required[Literal['internal', 'test', 'production']],
})
AnalyticsGetExperimentOutputVariant1ExperimentPlanAudience.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


AnalyticsGetExperimentOutputVariant1ExperimentPlanVariantsItemOperationsItemVariant1 = TypedDict('AnalyticsGetExperimentOutputVariant1ExperimentPlanVariantsItemOperationsItemVariant1', {
    'kind': Required[Literal['replace_text']],
    'selector': Required[Annotated[str, Field(min_length=1, max_length=500)]],
    'text': Required[Annotated[str, Field(max_length=240)]],
})
AnalyticsGetExperimentOutputVariant1ExperimentPlanVariantsItemOperationsItemVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


AnalyticsGetExperimentOutputVariant1ExperimentPlanVariantsItemOperationsItemVariant2 = TypedDict('AnalyticsGetExperimentOutputVariant1ExperimentPlanVariantsItemOperationsItemVariant2', {
    'kind': Required[Literal['set_style_token']],
    'selector': Required[Annotated[str, Field(min_length=1, max_length=500)]],
    'token': Required[Literal['cta_primary', 'cta_secondary', 'cta_contrast', 'muted', 'highlight']],
})
AnalyticsGetExperimentOutputVariant1ExperimentPlanVariantsItemOperationsItemVariant2.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


AnalyticsGetExperimentOutputVariant1ExperimentPlanVariantsItemOperationsItemVariant3 = TypedDict('AnalyticsGetExperimentOutputVariant1ExperimentPlanVariantsItemOperationsItemVariant3', {
    'kind': Required[Literal['swap_image']],
    'selector': Required[Annotated[str, Field(min_length=1, max_length=500)]],
    'src': Required[Annotated[str, Field(max_length=2000)]],
    'alt': Required[Annotated[str, Field(max_length=240)]],
})
AnalyticsGetExperimentOutputVariant1ExperimentPlanVariantsItemOperationsItemVariant3.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


AnalyticsGetExperimentOutputVariant1ExperimentPlanVariantsItemOperationsItemVariant4 = TypedDict('AnalyticsGetExperimentOutputVariant1ExperimentPlanVariantsItemOperationsItemVariant4', {
    'kind': Required[Literal['move_relative']],
    'selector': Required[Annotated[str, Field(min_length=1, max_length=500)]],
    'anchorSelector': Required[Annotated[str, Field(min_length=1, max_length=500)]],
    'position': Required[Literal['before', 'after']],
})
AnalyticsGetExperimentOutputVariant1ExperimentPlanVariantsItemOperationsItemVariant4.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


AnalyticsGetExperimentOutputVariant1ExperimentPlanVariantsItemOperationsItemVariant5 = TypedDict('AnalyticsGetExperimentOutputVariant1ExperimentPlanVariantsItemOperationsItemVariant5', {
    'kind': Required[Literal['set_visibility']],
    'selector': Required[Annotated[str, Field(min_length=1, max_length=500)]],
    'visible': Required[bool],
})
AnalyticsGetExperimentOutputVariant1ExperimentPlanVariantsItemOperationsItemVariant5.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


AnalyticsGetExperimentOutputVariant1ExperimentPlanVariantsItem = TypedDict('AnalyticsGetExperimentOutputVariant1ExperimentPlanVariantsItem', {
    'variantId': Required[str],
    'label': Required[Annotated[str, Field(min_length=1, max_length=120)]],
    'allocation': Required[Annotated[Union[float, int], Field(le=1, gt=0)]],
    'operations': Required[Annotated[list[Union[AnalyticsGetExperimentOutputVariant1ExperimentPlanVariantsItemOperationsItemVariant1, AnalyticsGetExperimentOutputVariant1ExperimentPlanVariantsItemOperationsItemVariant2, AnalyticsGetExperimentOutputVariant1ExperimentPlanVariantsItemOperationsItemVariant3, AnalyticsGetExperimentOutputVariant1ExperimentPlanVariantsItemOperationsItemVariant4, AnalyticsGetExperimentOutputVariant1ExperimentPlanVariantsItemOperationsItemVariant5]], Field(max_length=12)]],
})
AnalyticsGetExperimentOutputVariant1ExperimentPlanVariantsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


AnalyticsGetExperimentOutputVariant1ExperimentPlan = TypedDict('AnalyticsGetExperimentOutputVariant1ExperimentPlan', {
    'name': Required[Annotated[str, Field(min_length=1, max_length=120)]],
    'hypothesis': Required[Annotated[str, Field(min_length=10, max_length=500)]],
    'primaryMetricEvent': Required[str],
    'guardrailEvents': Required[Annotated[list[str], Field(max_length=10)]],
    'guardrailMaximumAbsoluteIncrease': Required[Annotated[Union[float, int], Field(le=1, gt=0)]],
    'stoppingRule': Required[AnalyticsGetExperimentOutputVariant1ExperimentPlanStoppingRule],
    'rollbackPlan': Required[AnalyticsGetExperimentOutputVariant1ExperimentPlanRollbackPlan],
    'performanceGuardrailMs': Required[Annotated[int, Field(ge=1, le=50)]],
    'audience': Required[AnalyticsGetExperimentOutputVariant1ExperimentPlanAudience],
    'assignmentUnit': Required[Literal['visitor', 'session']],
    'minimumDurationHours': Required[Annotated[int, Field(ge=24, le=2160)]],
    'minimumExposures': Required[Annotated[int, Field(ge=100, le=10000000)]],
    'minimumDetectableEffect': Required[Annotated[Union[float, int], Field(le=1, gt=0)]],
    'alpha': Required[Annotated[Union[float, int], Field(le=0.2, gt=0)]],
    'power': Required[Annotated[Union[float, int], Field(ge=0.7, le=0.99)]],
    'variants': Required[Annotated[list[AnalyticsGetExperimentOutputVariant1ExperimentPlanVariantsItem], Field(min_length=2, max_length=8)]],
    'expiresAt': Required[str],
})
AnalyticsGetExperimentOutputVariant1ExperimentPlan.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


AnalyticsGetExperimentOutputVariant1Experiment = TypedDict('AnalyticsGetExperimentOutputVariant1Experiment', {
    'experimentId': Required[str],
    'siteId': Required[str],
    'revision': Required[Annotated[int, Field(le=9007199254740991, gt=0)]],
    'state': Required[Literal['draft', 'approved', 'canary', 'active', 'paused', 'killed', 'archived']],
    'plan': Required[AnalyticsGetExperimentOutputVariant1ExperimentPlan],
})
AnalyticsGetExperimentOutputVariant1Experiment.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class AnalyticsGetExperimentOutputVariant1(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    ok: Literal[True] = Field(..., alias='ok', description='')
    experiment: AnalyticsGetExperimentOutputVariant1Experiment = Field(..., alias='experiment', description='')


AnalyticsGetExperimentOutputVariant2DeliveryArtifactsItem = TypedDict('AnalyticsGetExperimentOutputVariant2DeliveryArtifactsItem', {
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
AnalyticsGetExperimentOutputVariant2DeliveryArtifactsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


AnalyticsGetExperimentOutputVariant2DeliveryStorageFailureVariant1 = TypedDict('AnalyticsGetExperimentOutputVariant2DeliveryStorageFailureVariant1', {
    'artifactId': Required[Union[str, None]],
    'outcome': Required[Literal['unknown', 'bytes-stored-metadata-pending', 'failed']],
})
AnalyticsGetExperimentOutputVariant2DeliveryStorageFailureVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


AnalyticsGetExperimentOutputVariant2Delivery = TypedDict('AnalyticsGetExperimentOutputVariant2Delivery', {
    'mode': Required[Literal['artifact']],
    'status': Required[Literal['complete', 'partial', 'unavailable']],
    'retainedRepresentation': Required[Literal['formatted-tool-result']],
    'sourceIsError': Required[bool],
    'artifacts': Required[list[AnalyticsGetExperimentOutputVariant2DeliveryArtifactsItem]],
    'downloadLinksOmitted': Required[bool],
    'scopeOmittedFields': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'storageFailure': Required[Union[AnalyticsGetExperimentOutputVariant2DeliveryStorageFailureVariant1, None]],
    'nextAction': Required[str],
})
AnalyticsGetExperimentOutputVariant2Delivery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


AnalyticsGetExperimentOutputVariant2RecoveryOperation = TypedDict('AnalyticsGetExperimentOutputVariant2RecoveryOperation', {
    'runId': Required[Union[Annotated[str, Field(max_length=200)], None]],
    'idempotencyKey': Required[Annotated[str, Field(max_length=512)]],
    'state': Required[Annotated[str, Field(max_length=100)]],
})
AnalyticsGetExperimentOutputVariant2RecoveryOperation.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


AnalyticsGetExperimentOutputVariant2Recovery = TypedDict('AnalyticsGetExperimentOutputVariant2Recovery', {
    'idempotencyKey': NotRequired[Annotated[str, Field(max_length=512)]],
    'operationId': NotRequired[Annotated[str, Field(max_length=200)]],
    'runId': NotRequired[Annotated[str, Field(max_length=200)]],
    'jobId': NotRequired[Annotated[str, Field(max_length=200)]],
    'operation': NotRequired[AnalyticsGetExperimentOutputVariant2RecoveryOperation],
})
AnalyticsGetExperimentOutputVariant2Recovery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class AnalyticsGetExperimentOutputVariant2(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    delivery: AnalyticsGetExperimentOutputVariant2Delivery = Field(..., alias='delivery', description='')
    preview: str = Field(..., alias='preview', description='')
    scope: dict[str, Union[str, Union[float, int], bool, None]] = Field(..., alias='scope', description='')
    recovery: AnalyticsGetExperimentOutputVariant2Recovery = Field(..., alias='recovery', description='')


# Union schema: validate external payloads with TypeAdapter(AnalyticsGetExperimentOutput).
AnalyticsGetExperimentOutput = Union[AnalyticsGetExperimentOutputVariant2, AnalyticsGetExperimentOutputVariant1]

_AnalyticsGetExperimentInputAdapter = TypeAdapter(AnalyticsGetExperimentInput)
_AnalyticsGetExperimentOutputAdapter = TypeAdapter(AnalyticsGetExperimentOutput)