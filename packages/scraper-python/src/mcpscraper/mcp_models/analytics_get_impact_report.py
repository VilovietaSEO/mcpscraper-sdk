from typing import Annotated, Any, Literal, Union
from typing_extensions import NotRequired, Required, TypedDict
from pydantic import BaseModel, ConfigDict, Field, TypeAdapter


class AnalyticsGetImpactReportInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=False)

    site_id: str = Field(..., alias='siteId', description='Authorized Analytics Site id.')
    survey_id: str = Field(..., alias='surveyId', description='Published or paused post-purchase survey whose immutable responses supply the reported ledger.')
    base_model: Literal['first_touch', 'last_touch', 'last_non_direct', 'linear', 'time_decay', 'position_based', 'custom_weighted'] = Field(..., alias='baseModel', description='Existing observed attribution model; observed_plus_reported is deliberately not an observed model.')
    observed_weight_micros: Annotated[int, Field(ge=0, le=1000000)] = Field(..., alias='observedWeightMicros', description='Observed share in micros. It must total exactly 1,000,000 with reportedWeightMicros.')
    reported_weight_micros: Annotated[int, Field(ge=0, le=1000000)] = Field(..., alias='reportedWeightMicros', description='Customer-reported share in micros. It must total exactly 1,000,000 with observedWeightMicros.')
    methodology_version: Literal['xray_observed_plus_reported_equal_selected_v1'] = Field(..., alias='methodologyVersion', description='Immutable methodology selected after reading analytics_get_attribution_methodology.')
    from_: Union[str, None] = Field(None, alias='from', description='Inclusive observed-evidence start. Omit with to for the last 30 days.')
    to: Union[str, None] = Field(None, alias='to', description='Exclusive observed-evidence end. Omit to use now.')
    click_window: Union[Union[Literal[7], Literal[14], Literal[30], Literal[60], Literal[90], Literal[180], Literal[365], Literal['lifetime']], None] = Field(None, alias='clickWindow', description='Independent observed click window.')
    view_window: Union[Union[Literal[7], Literal[14], Literal[30], Literal[60], Literal[90], Literal[180], Literal[365], Literal['lifetime']], None] = Field(None, alias='viewWindow', description='Independent view window; provider-unavailable state never manufactures view touches.')


AnalyticsGetImpactReportOutputVariant1ImpactWeights = TypedDict('AnalyticsGetImpactReportOutputVariant1ImpactWeights', {
    'observedWeightMicros': Required[Annotated[int, Field(ge=-9007199254740991, le=9007199254740991)]],
    'reportedWeightMicros': Required[Annotated[int, Field(ge=-9007199254740991, le=9007199254740991)]],
})
AnalyticsGetImpactReportOutputVariant1ImpactWeights.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


AnalyticsGetImpactReportOutputVariant1ImpactObservedCreditsItem = TypedDict('AnalyticsGetImpactReportOutputVariant1ImpactObservedCreditsItem', {
    'ledger': Required[Literal['observed', 'reported']],
    'conversionId': Required[str],
    'creditMicros': Required[Annotated[int, Field(ge=0, le=1000000)]],
    'creditedValueMinor': Required[str],
    'currency': Required[Union[Annotated[str, Field(min_length=3, max_length=3)], None]],
})
AnalyticsGetImpactReportOutputVariant1ImpactObservedCreditsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


AnalyticsGetImpactReportOutputVariant1ImpactObserved = TypedDict('AnalyticsGetImpactReportOutputVariant1ImpactObserved', {
    'credits': Required[list[AnalyticsGetImpactReportOutputVariant1ImpactObservedCreditsItem]],
    'totalsByCurrency': Required[dict[str, str]],
})
AnalyticsGetImpactReportOutputVariant1ImpactObserved.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


AnalyticsGetImpactReportOutputVariant1ImpactReportedCreditsItem = TypedDict('AnalyticsGetImpactReportOutputVariant1ImpactReportedCreditsItem', {
    'ledger': Required[Literal['observed', 'reported']],
    'conversionId': Required[str],
    'creditMicros': Required[Annotated[int, Field(ge=0, le=1000000)]],
    'creditedValueMinor': Required[str],
    'currency': Required[Union[Annotated[str, Field(min_length=3, max_length=3)], None]],
})
AnalyticsGetImpactReportOutputVariant1ImpactReportedCreditsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


AnalyticsGetImpactReportOutputVariant1ImpactReported = TypedDict('AnalyticsGetImpactReportOutputVariant1ImpactReported', {
    'credits': Required[list[AnalyticsGetImpactReportOutputVariant1ImpactReportedCreditsItem]],
    'totalsByCurrency': Required[dict[str, str]],
})
AnalyticsGetImpactReportOutputVariant1ImpactReported.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


AnalyticsGetImpactReportOutputVariant1ImpactCombinedCreditsItem = TypedDict('AnalyticsGetImpactReportOutputVariant1ImpactCombinedCreditsItem', {
    'ledger': Required[Literal['observed', 'reported']],
    'conversionId': Required[str],
    'creditMicros': Required[Annotated[int, Field(ge=0, le=1000000)]],
    'creditedValueMinor': Required[str],
    'currency': Required[Union[Annotated[str, Field(min_length=3, max_length=3)], None]],
})
AnalyticsGetImpactReportOutputVariant1ImpactCombinedCreditsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


AnalyticsGetImpactReportOutputVariant1ImpactCombined = TypedDict('AnalyticsGetImpactReportOutputVariant1ImpactCombined', {
    'credits': Required[list[AnalyticsGetImpactReportOutputVariant1ImpactCombinedCreditsItem]],
    'totalsByCurrency': Required[dict[str, str]],
    'crossCurrencyTotal': Required[None],
})
AnalyticsGetImpactReportOutputVariant1ImpactCombined.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


AnalyticsGetImpactReportOutputVariant1Impact = TypedDict('AnalyticsGetImpactReportOutputVariant1Impact', {
    'methodologyVersion': Required[Literal['xray_observed_plus_reported_equal_selected_v1']],
    'baseModel': Required[Literal['first_touch', 'last_touch', 'last_non_direct', 'linear', 'time_decay', 'position_based', 'custom_weighted']],
    'weights': Required[AnalyticsGetImpactReportOutputVariant1ImpactWeights],
    'observed': Required[AnalyticsGetImpactReportOutputVariant1ImpactObserved],
    'reported': Required[AnalyticsGetImpactReportOutputVariant1ImpactReported],
    'combined': Required[AnalyticsGetImpactReportOutputVariant1ImpactCombined],
    'eligibleInvitationCount': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'responseCount': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'coverage': Required[Union[Annotated[Union[float, int], Field(ge=0, le=1)], None]],
    'missingReasons': Required[list[str]],
})
AnalyticsGetImpactReportOutputVariant1Impact.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class AnalyticsGetImpactReportOutputVariant1(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    ok: Literal[True] = Field(..., alias='ok', description='')
    impact: AnalyticsGetImpactReportOutputVariant1Impact = Field(..., alias='impact', description='')


AnalyticsGetImpactReportOutputVariant2DeliveryArtifactsItem = TypedDict('AnalyticsGetImpactReportOutputVariant2DeliveryArtifactsItem', {
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
AnalyticsGetImpactReportOutputVariant2DeliveryArtifactsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


AnalyticsGetImpactReportOutputVariant2DeliveryAvailableExportsItem = TypedDict('AnalyticsGetImpactReportOutputVariant2DeliveryAvailableExportsItem', {
    'artifactId': Required[str],
    'sourceArtifactId': Required[str],
    'filename': Required[Literal['result.md']],
    'contentType': Required[Literal['text/markdown; charset=utf-8']],
    'state': Required[Literal['on-demand']],
})
AnalyticsGetImpactReportOutputVariant2DeliveryAvailableExportsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


AnalyticsGetImpactReportOutputVariant2DeliveryStorageFailureVariant1 = TypedDict('AnalyticsGetImpactReportOutputVariant2DeliveryStorageFailureVariant1', {
    'artifactId': Required[Union[str, None]],
    'outcome': Required[Literal['unknown', 'bytes-stored-metadata-pending', 'failed']],
})
AnalyticsGetImpactReportOutputVariant2DeliveryStorageFailureVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


AnalyticsGetImpactReportOutputVariant2Delivery = TypedDict('AnalyticsGetImpactReportOutputVariant2Delivery', {
    'mode': Required[Literal['artifact']],
    'status': Required[Literal['complete', 'partial', 'unavailable']],
    'retainedRepresentation': Required[Literal['formatted-tool-result']],
    'sourceIsError': Required[bool],
    'artifacts': Required[list[AnalyticsGetImpactReportOutputVariant2DeliveryArtifactsItem]],
    'availableExports': NotRequired[list[AnalyticsGetImpactReportOutputVariant2DeliveryAvailableExportsItem]],
    'downloadLinksOmitted': Required[bool],
    'scopeOmittedFields': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'storageFailure': Required[Union[AnalyticsGetImpactReportOutputVariant2DeliveryStorageFailureVariant1, None]],
    'nextAction': Required[str],
})
AnalyticsGetImpactReportOutputVariant2Delivery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


AnalyticsGetImpactReportOutputVariant2RecoveryOperation = TypedDict('AnalyticsGetImpactReportOutputVariant2RecoveryOperation', {
    'runId': Required[Union[Annotated[str, Field(max_length=200)], None]],
    'idempotencyKey': Required[Annotated[str, Field(max_length=512)]],
    'state': Required[Annotated[str, Field(max_length=100)]],
})
AnalyticsGetImpactReportOutputVariant2RecoveryOperation.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


AnalyticsGetImpactReportOutputVariant2Recovery = TypedDict('AnalyticsGetImpactReportOutputVariant2Recovery', {
    'idempotencyKey': NotRequired[Annotated[str, Field(max_length=512)]],
    'operationId': NotRequired[Annotated[str, Field(max_length=200)]],
    'runId': NotRequired[Annotated[str, Field(max_length=200)]],
    'jobId': NotRequired[Annotated[str, Field(max_length=200)]],
    'operation': NotRequired[AnalyticsGetImpactReportOutputVariant2RecoveryOperation],
})
AnalyticsGetImpactReportOutputVariant2Recovery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class AnalyticsGetImpactReportOutputVariant2(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    delivery: AnalyticsGetImpactReportOutputVariant2Delivery = Field(..., alias='delivery', description='')
    preview: str = Field(..., alias='preview', description='')
    scope: dict[str, Union[str, Union[float, int], bool, None]] = Field(..., alias='scope', description='')
    recovery: AnalyticsGetImpactReportOutputVariant2Recovery = Field(..., alias='recovery', description='')


# Union schema: validate external payloads with TypeAdapter(AnalyticsGetImpactReportOutput).
AnalyticsGetImpactReportOutput = Union[AnalyticsGetImpactReportOutputVariant2, AnalyticsGetImpactReportOutputVariant1]

_AnalyticsGetImpactReportInputAdapter = TypeAdapter(AnalyticsGetImpactReportInput)
_AnalyticsGetImpactReportOutputAdapter = TypeAdapter(AnalyticsGetImpactReportOutput)