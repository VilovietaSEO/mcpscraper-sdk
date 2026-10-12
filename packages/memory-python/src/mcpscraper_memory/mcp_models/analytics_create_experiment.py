from typing import Annotated, Any, Literal, Union
from typing_extensions import NotRequired, Required, TypedDict
from pydantic import BaseModel, ConfigDict, Field, TypeAdapter


AnalyticsCreateExperimentInputPlanStoppingRule = TypedDict('AnalyticsCreateExperimentInputPlanStoppingRule', {
    'method': Required[Literal['fixed_horizon']],
    'actionOnSampleRatioMismatch': Required[Literal['pause']],
    'actionOnGuardrailBreach': Required[Literal['pause']],
    'winnerRequiresSignificance': Required[Literal[True]],
})
AnalyticsCreateExperimentInputPlanStoppingRule.__pydantic_config__ = ConfigDict(extra="allow", strict=False)


AnalyticsCreateExperimentInputPlanRollbackPlan = TypedDict('AnalyticsCreateExperimentInputPlanRollbackPlan', {
    'action': Required[Literal['restore_control']],
    'triggers': Required[Annotated[list[Literal['pause', 'kill', 'expiry', 'manifest_error', 'selector_ambiguity', 'performance_guardrail']], Field(min_length=6, max_length=6)]],
})
AnalyticsCreateExperimentInputPlanRollbackPlan.__pydantic_config__ = ConfigDict(extra="allow", strict=False)


AnalyticsCreateExperimentInputPlanAudience = TypedDict('AnalyticsCreateExperimentInputPlanAudience', {
    'routePrefixes': Required[Annotated[list[Annotated[str, Field(max_length=2000)]], Field(min_length=1, max_length=25)]],
    'trafficClass': NotRequired[Literal['internal', 'test', 'production']],
})
AnalyticsCreateExperimentInputPlanAudience.__pydantic_config__ = ConfigDict(extra="allow", strict=False)


AnalyticsCreateExperimentInputPlanVariantsItemOperationsItemVariant1 = TypedDict('AnalyticsCreateExperimentInputPlanVariantsItemOperationsItemVariant1', {
    'kind': Required[Literal['replace_text']],
    'selector': Required[Annotated[str, Field(min_length=1, max_length=500)]],
    'text': Required[Annotated[str, Field(max_length=240)]],
})
AnalyticsCreateExperimentInputPlanVariantsItemOperationsItemVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=False)


AnalyticsCreateExperimentInputPlanVariantsItemOperationsItemVariant2 = TypedDict('AnalyticsCreateExperimentInputPlanVariantsItemOperationsItemVariant2', {
    'kind': Required[Literal['set_style_token']],
    'selector': Required[Annotated[str, Field(min_length=1, max_length=500)]],
    'token': Required[Literal['cta_primary', 'cta_secondary', 'cta_contrast', 'muted', 'highlight']],
})
AnalyticsCreateExperimentInputPlanVariantsItemOperationsItemVariant2.__pydantic_config__ = ConfigDict(extra="allow", strict=False)


AnalyticsCreateExperimentInputPlanVariantsItemOperationsItemVariant3 = TypedDict('AnalyticsCreateExperimentInputPlanVariantsItemOperationsItemVariant3', {
    'kind': Required[Literal['swap_image']],
    'selector': Required[Annotated[str, Field(min_length=1, max_length=500)]],
    'src': Required[Annotated[str, Field(max_length=2000)]],
    'alt': Required[Annotated[str, Field(max_length=240)]],
})
AnalyticsCreateExperimentInputPlanVariantsItemOperationsItemVariant3.__pydantic_config__ = ConfigDict(extra="allow", strict=False)


AnalyticsCreateExperimentInputPlanVariantsItemOperationsItemVariant4 = TypedDict('AnalyticsCreateExperimentInputPlanVariantsItemOperationsItemVariant4', {
    'kind': Required[Literal['move_relative']],
    'selector': Required[Annotated[str, Field(min_length=1, max_length=500)]],
    'anchorSelector': Required[Annotated[str, Field(min_length=1, max_length=500)]],
    'position': Required[Literal['before', 'after']],
})
AnalyticsCreateExperimentInputPlanVariantsItemOperationsItemVariant4.__pydantic_config__ = ConfigDict(extra="allow", strict=False)


AnalyticsCreateExperimentInputPlanVariantsItemOperationsItemVariant5 = TypedDict('AnalyticsCreateExperimentInputPlanVariantsItemOperationsItemVariant5', {
    'kind': Required[Literal['set_visibility']],
    'selector': Required[Annotated[str, Field(min_length=1, max_length=500)]],
    'visible': Required[bool],
})
AnalyticsCreateExperimentInputPlanVariantsItemOperationsItemVariant5.__pydantic_config__ = ConfigDict(extra="allow", strict=False)


AnalyticsCreateExperimentInputPlanVariantsItem = TypedDict('AnalyticsCreateExperimentInputPlanVariantsItem', {
    'variantId': Required[str],
    'label': Required[Annotated[str, Field(min_length=1, max_length=120)]],
    'allocation': Required[Annotated[Union[float, int], Field(le=1, gt=0)]],
    'operations': Required[Annotated[list[Union[AnalyticsCreateExperimentInputPlanVariantsItemOperationsItemVariant1, AnalyticsCreateExperimentInputPlanVariantsItemOperationsItemVariant2, AnalyticsCreateExperimentInputPlanVariantsItemOperationsItemVariant3, AnalyticsCreateExperimentInputPlanVariantsItemOperationsItemVariant4, AnalyticsCreateExperimentInputPlanVariantsItemOperationsItemVariant5]], Field(max_length=12)]],
})
AnalyticsCreateExperimentInputPlanVariantsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=False)


AnalyticsCreateExperimentInputPlan = TypedDict('AnalyticsCreateExperimentInputPlan', {
    'name': Required[Annotated[str, Field(min_length=1, max_length=120)]],
    'hypothesis': Required[Annotated[str, Field(min_length=10, max_length=500)]],
    'primaryMetricEvent': Required[str],
    'guardrailEvents': NotRequired[Annotated[list[str], Field(max_length=10)]],
    'guardrailMaximumAbsoluteIncrease': NotRequired[Annotated[Union[float, int], Field(le=1, gt=0)]],
    'stoppingRule': NotRequired[AnalyticsCreateExperimentInputPlanStoppingRule],
    'rollbackPlan': NotRequired[AnalyticsCreateExperimentInputPlanRollbackPlan],
    'performanceGuardrailMs': NotRequired[Annotated[int, Field(ge=1, le=50)]],
    'audience': Required[AnalyticsCreateExperimentInputPlanAudience],
    'assignmentUnit': NotRequired[Literal['visitor', 'session']],
    'minimumDurationHours': Required[Annotated[int, Field(ge=24, le=2160)]],
    'minimumExposures': Required[Annotated[int, Field(ge=100, le=10000000)]],
    'minimumDetectableEffect': Required[Annotated[Union[float, int], Field(le=1, gt=0)]],
    'alpha': NotRequired[Annotated[Union[float, int], Field(le=0.2, gt=0)]],
    'power': NotRequired[Annotated[Union[float, int], Field(ge=0.7, le=0.99)]],
    'variants': Required[Annotated[list[AnalyticsCreateExperimentInputPlanVariantsItem], Field(min_length=2, max_length=8)]],
    'expiresAt': Required[str],
})
AnalyticsCreateExperimentInputPlan.__pydantic_config__ = ConfigDict(extra="allow", strict=False)


class AnalyticsCreateExperimentInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=False)

    site_id: str = Field(..., alias='siteId', description='Authorized Analytics Site id.')
    plan: AnalyticsCreateExperimentInputPlan = Field(..., alias='plan', description='Preregistered hypothesis, metric, audience, sample requirements, expiry, allocations, and allowlisted visual operations. One control variant must have no operations.')
    idempotency_key: Annotated[str, Field(min_length=8, max_length=160)] = Field(..., alias='idempotencyKey', description='Retry key; reuse only for this exact mutation.')


AnalyticsCreateExperimentOutputVariant1ExperimentPlanStoppingRule = TypedDict('AnalyticsCreateExperimentOutputVariant1ExperimentPlanStoppingRule', {
    'method': Required[Literal['fixed_horizon']],
    'actionOnSampleRatioMismatch': Required[Literal['pause']],
    'actionOnGuardrailBreach': Required[Literal['pause']],
    'winnerRequiresSignificance': Required[Literal[True]],
})
AnalyticsCreateExperimentOutputVariant1ExperimentPlanStoppingRule.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


AnalyticsCreateExperimentOutputVariant1ExperimentPlanRollbackPlan = TypedDict('AnalyticsCreateExperimentOutputVariant1ExperimentPlanRollbackPlan', {
    'action': Required[Literal['restore_control']],
    'triggers': Required[Annotated[list[Literal['pause', 'kill', 'expiry', 'manifest_error', 'selector_ambiguity', 'performance_guardrail']], Field(min_length=6, max_length=6)]],
})
AnalyticsCreateExperimentOutputVariant1ExperimentPlanRollbackPlan.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


AnalyticsCreateExperimentOutputVariant1ExperimentPlanAudience = TypedDict('AnalyticsCreateExperimentOutputVariant1ExperimentPlanAudience', {
    'routePrefixes': Required[Annotated[list[Annotated[str, Field(max_length=2000)]], Field(min_length=1, max_length=25)]],
    'trafficClass': Required[Literal['internal', 'test', 'production']],
})
AnalyticsCreateExperimentOutputVariant1ExperimentPlanAudience.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


AnalyticsCreateExperimentOutputVariant1ExperimentPlanVariantsItemOperationsItemVariant1 = TypedDict('AnalyticsCreateExperimentOutputVariant1ExperimentPlanVariantsItemOperationsItemVariant1', {
    'kind': Required[Literal['replace_text']],
    'selector': Required[Annotated[str, Field(min_length=1, max_length=500)]],
    'text': Required[Annotated[str, Field(max_length=240)]],
})
AnalyticsCreateExperimentOutputVariant1ExperimentPlanVariantsItemOperationsItemVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


AnalyticsCreateExperimentOutputVariant1ExperimentPlanVariantsItemOperationsItemVariant2 = TypedDict('AnalyticsCreateExperimentOutputVariant1ExperimentPlanVariantsItemOperationsItemVariant2', {
    'kind': Required[Literal['set_style_token']],
    'selector': Required[Annotated[str, Field(min_length=1, max_length=500)]],
    'token': Required[Literal['cta_primary', 'cta_secondary', 'cta_contrast', 'muted', 'highlight']],
})
AnalyticsCreateExperimentOutputVariant1ExperimentPlanVariantsItemOperationsItemVariant2.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


AnalyticsCreateExperimentOutputVariant1ExperimentPlanVariantsItemOperationsItemVariant3 = TypedDict('AnalyticsCreateExperimentOutputVariant1ExperimentPlanVariantsItemOperationsItemVariant3', {
    'kind': Required[Literal['swap_image']],
    'selector': Required[Annotated[str, Field(min_length=1, max_length=500)]],
    'src': Required[Annotated[str, Field(max_length=2000)]],
    'alt': Required[Annotated[str, Field(max_length=240)]],
})
AnalyticsCreateExperimentOutputVariant1ExperimentPlanVariantsItemOperationsItemVariant3.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


AnalyticsCreateExperimentOutputVariant1ExperimentPlanVariantsItemOperationsItemVariant4 = TypedDict('AnalyticsCreateExperimentOutputVariant1ExperimentPlanVariantsItemOperationsItemVariant4', {
    'kind': Required[Literal['move_relative']],
    'selector': Required[Annotated[str, Field(min_length=1, max_length=500)]],
    'anchorSelector': Required[Annotated[str, Field(min_length=1, max_length=500)]],
    'position': Required[Literal['before', 'after']],
})
AnalyticsCreateExperimentOutputVariant1ExperimentPlanVariantsItemOperationsItemVariant4.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


AnalyticsCreateExperimentOutputVariant1ExperimentPlanVariantsItemOperationsItemVariant5 = TypedDict('AnalyticsCreateExperimentOutputVariant1ExperimentPlanVariantsItemOperationsItemVariant5', {
    'kind': Required[Literal['set_visibility']],
    'selector': Required[Annotated[str, Field(min_length=1, max_length=500)]],
    'visible': Required[bool],
})
AnalyticsCreateExperimentOutputVariant1ExperimentPlanVariantsItemOperationsItemVariant5.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


AnalyticsCreateExperimentOutputVariant1ExperimentPlanVariantsItem = TypedDict('AnalyticsCreateExperimentOutputVariant1ExperimentPlanVariantsItem', {
    'variantId': Required[str],
    'label': Required[Annotated[str, Field(min_length=1, max_length=120)]],
    'allocation': Required[Annotated[Union[float, int], Field(le=1, gt=0)]],
    'operations': Required[Annotated[list[Union[AnalyticsCreateExperimentOutputVariant1ExperimentPlanVariantsItemOperationsItemVariant1, AnalyticsCreateExperimentOutputVariant1ExperimentPlanVariantsItemOperationsItemVariant2, AnalyticsCreateExperimentOutputVariant1ExperimentPlanVariantsItemOperationsItemVariant3, AnalyticsCreateExperimentOutputVariant1ExperimentPlanVariantsItemOperationsItemVariant4, AnalyticsCreateExperimentOutputVariant1ExperimentPlanVariantsItemOperationsItemVariant5]], Field(max_length=12)]],
})
AnalyticsCreateExperimentOutputVariant1ExperimentPlanVariantsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


AnalyticsCreateExperimentOutputVariant1ExperimentPlan = TypedDict('AnalyticsCreateExperimentOutputVariant1ExperimentPlan', {
    'name': Required[Annotated[str, Field(min_length=1, max_length=120)]],
    'hypothesis': Required[Annotated[str, Field(min_length=10, max_length=500)]],
    'primaryMetricEvent': Required[str],
    'guardrailEvents': Required[Annotated[list[str], Field(max_length=10)]],
    'guardrailMaximumAbsoluteIncrease': Required[Annotated[Union[float, int], Field(le=1, gt=0)]],
    'stoppingRule': Required[AnalyticsCreateExperimentOutputVariant1ExperimentPlanStoppingRule],
    'rollbackPlan': Required[AnalyticsCreateExperimentOutputVariant1ExperimentPlanRollbackPlan],
    'performanceGuardrailMs': Required[Annotated[int, Field(ge=1, le=50)]],
    'audience': Required[AnalyticsCreateExperimentOutputVariant1ExperimentPlanAudience],
    'assignmentUnit': Required[Literal['visitor', 'session']],
    'minimumDurationHours': Required[Annotated[int, Field(ge=24, le=2160)]],
    'minimumExposures': Required[Annotated[int, Field(ge=100, le=10000000)]],
    'minimumDetectableEffect': Required[Annotated[Union[float, int], Field(le=1, gt=0)]],
    'alpha': Required[Annotated[Union[float, int], Field(le=0.2, gt=0)]],
    'power': Required[Annotated[Union[float, int], Field(ge=0.7, le=0.99)]],
    'variants': Required[Annotated[list[AnalyticsCreateExperimentOutputVariant1ExperimentPlanVariantsItem], Field(min_length=2, max_length=8)]],
    'expiresAt': Required[str],
})
AnalyticsCreateExperimentOutputVariant1ExperimentPlan.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


AnalyticsCreateExperimentOutputVariant1Experiment = TypedDict('AnalyticsCreateExperimentOutputVariant1Experiment', {
    'experimentId': Required[str],
    'siteId': Required[str],
    'revision': Required[Annotated[int, Field(le=9007199254740991, gt=0)]],
    'state': Required[Literal['draft', 'approved', 'canary', 'active', 'paused', 'killed', 'archived']],
    'plan': Required[AnalyticsCreateExperimentOutputVariant1ExperimentPlan],
})
AnalyticsCreateExperimentOutputVariant1Experiment.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class AnalyticsCreateExperimentOutputVariant1(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    ok: Literal[True] = Field(..., alias='ok', description='')
    experiment: AnalyticsCreateExperimentOutputVariant1Experiment = Field(..., alias='experiment', description='')


AnalyticsCreateExperimentOutputVariant2DeliveryArtifactsItem = TypedDict('AnalyticsCreateExperimentOutputVariant2DeliveryArtifactsItem', {
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
AnalyticsCreateExperimentOutputVariant2DeliveryArtifactsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


AnalyticsCreateExperimentOutputVariant2DeliveryStorageFailureVariant1 = TypedDict('AnalyticsCreateExperimentOutputVariant2DeliveryStorageFailureVariant1', {
    'artifactId': Required[Union[str, None]],
    'outcome': Required[Literal['unknown', 'bytes-stored-metadata-pending', 'failed']],
})
AnalyticsCreateExperimentOutputVariant2DeliveryStorageFailureVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


AnalyticsCreateExperimentOutputVariant2Delivery = TypedDict('AnalyticsCreateExperimentOutputVariant2Delivery', {
    'mode': Required[Literal['artifact']],
    'status': Required[Literal['complete', 'partial', 'unavailable']],
    'retainedRepresentation': Required[Literal['formatted-tool-result']],
    'sourceIsError': Required[bool],
    'artifacts': Required[list[AnalyticsCreateExperimentOutputVariant2DeliveryArtifactsItem]],
    'downloadLinksOmitted': Required[bool],
    'scopeOmittedFields': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'storageFailure': Required[Union[AnalyticsCreateExperimentOutputVariant2DeliveryStorageFailureVariant1, None]],
    'nextAction': Required[str],
})
AnalyticsCreateExperimentOutputVariant2Delivery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


AnalyticsCreateExperimentOutputVariant2RecoveryOperation = TypedDict('AnalyticsCreateExperimentOutputVariant2RecoveryOperation', {
    'runId': Required[Union[Annotated[str, Field(max_length=200)], None]],
    'idempotencyKey': Required[Annotated[str, Field(max_length=512)]],
    'state': Required[Annotated[str, Field(max_length=100)]],
})
AnalyticsCreateExperimentOutputVariant2RecoveryOperation.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


AnalyticsCreateExperimentOutputVariant2Recovery = TypedDict('AnalyticsCreateExperimentOutputVariant2Recovery', {
    'idempotencyKey': NotRequired[Annotated[str, Field(max_length=512)]],
    'operationId': NotRequired[Annotated[str, Field(max_length=200)]],
    'runId': NotRequired[Annotated[str, Field(max_length=200)]],
    'jobId': NotRequired[Annotated[str, Field(max_length=200)]],
    'operation': NotRequired[AnalyticsCreateExperimentOutputVariant2RecoveryOperation],
})
AnalyticsCreateExperimentOutputVariant2Recovery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class AnalyticsCreateExperimentOutputVariant2(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    delivery: AnalyticsCreateExperimentOutputVariant2Delivery = Field(..., alias='delivery', description='')
    preview: str = Field(..., alias='preview', description='')
    scope: dict[str, Union[str, Union[float, int], bool, None]] = Field(..., alias='scope', description='')
    recovery: AnalyticsCreateExperimentOutputVariant2Recovery = Field(..., alias='recovery', description='')


# Union schema: validate external payloads with TypeAdapter(AnalyticsCreateExperimentOutput).
AnalyticsCreateExperimentOutput = Union[AnalyticsCreateExperimentOutputVariant2, AnalyticsCreateExperimentOutputVariant1]

_AnalyticsCreateExperimentInputAdapter = TypeAdapter(AnalyticsCreateExperimentInput)
_AnalyticsCreateExperimentOutputAdapter = TypeAdapter(AnalyticsCreateExperimentOutput)