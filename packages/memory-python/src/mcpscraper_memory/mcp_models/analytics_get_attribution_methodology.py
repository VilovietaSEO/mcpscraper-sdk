from typing import Annotated, Any, Literal, Union
from typing_extensions import NotRequired, Required, TypedDict
from pydantic import BaseModel, ConfigDict, Field, TypeAdapter


class AnalyticsGetAttributionMethodologyInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=False)

    site_id: str = Field(..., alias='siteId', description='Authorized Analytics Site id.')


AnalyticsGetAttributionMethodologyOutputVariant1MethodologyObservedPlusReported = TypedDict('AnalyticsGetAttributionMethodologyOutputVariant1MethodologyObservedPlusReported', {
    'methodologyVersion': Required[Literal['xray_observed_plus_reported_equal_selected_v1']],
    'explicitWeightsRequired': Required[Literal[True]],
    'creditScaleMicros': Required[Literal[1000000]],
    'ledgersRemainSeparate': Required[Literal[True]],
})
AnalyticsGetAttributionMethodologyOutputVariant1MethodologyObservedPlusReported.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


AnalyticsGetAttributionMethodologyOutputVariant1Methodology = TypedDict('AnalyticsGetAttributionMethodologyOutputVariant1Methodology', {
    'observedModels': Required[list[Any]],
    'defaultModel': Required[Literal['position_based']],
    'defaultPositionWeights': Required[list[Any]],
    'observedPlusReported': Required[AnalyticsGetAttributionMethodologyOutputVariant1MethodologyObservedPlusReported],
    'viewEvidence': Required[Literal['provider_event_level_only']],
    'customerReportedIsDeterministicTouch': Required[Literal[False]],
})
AnalyticsGetAttributionMethodologyOutputVariant1Methodology.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class AnalyticsGetAttributionMethodologyOutputVariant1(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    ok: Literal[True] = Field(..., alias='ok', description='')
    methodology: AnalyticsGetAttributionMethodologyOutputVariant1Methodology = Field(..., alias='methodology', description='')


AnalyticsGetAttributionMethodologyOutputVariant2DeliveryArtifactsItem = TypedDict('AnalyticsGetAttributionMethodologyOutputVariant2DeliveryArtifactsItem', {
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
AnalyticsGetAttributionMethodologyOutputVariant2DeliveryArtifactsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


AnalyticsGetAttributionMethodologyOutputVariant2DeliveryStorageFailureVariant1 = TypedDict('AnalyticsGetAttributionMethodologyOutputVariant2DeliveryStorageFailureVariant1', {
    'artifactId': Required[Union[str, None]],
    'outcome': Required[Literal['unknown', 'bytes-stored-metadata-pending', 'failed']],
})
AnalyticsGetAttributionMethodologyOutputVariant2DeliveryStorageFailureVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


AnalyticsGetAttributionMethodologyOutputVariant2Delivery = TypedDict('AnalyticsGetAttributionMethodologyOutputVariant2Delivery', {
    'mode': Required[Literal['artifact']],
    'status': Required[Literal['complete', 'partial', 'unavailable']],
    'retainedRepresentation': Required[Literal['formatted-tool-result']],
    'sourceIsError': Required[bool],
    'artifacts': Required[list[AnalyticsGetAttributionMethodologyOutputVariant2DeliveryArtifactsItem]],
    'downloadLinksOmitted': Required[bool],
    'scopeOmittedFields': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'storageFailure': Required[Union[AnalyticsGetAttributionMethodologyOutputVariant2DeliveryStorageFailureVariant1, None]],
    'nextAction': Required[str],
})
AnalyticsGetAttributionMethodologyOutputVariant2Delivery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


AnalyticsGetAttributionMethodologyOutputVariant2RecoveryOperation = TypedDict('AnalyticsGetAttributionMethodologyOutputVariant2RecoveryOperation', {
    'runId': Required[Union[Annotated[str, Field(max_length=200)], None]],
    'idempotencyKey': Required[Annotated[str, Field(max_length=512)]],
    'state': Required[Annotated[str, Field(max_length=100)]],
})
AnalyticsGetAttributionMethodologyOutputVariant2RecoveryOperation.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


AnalyticsGetAttributionMethodologyOutputVariant2Recovery = TypedDict('AnalyticsGetAttributionMethodologyOutputVariant2Recovery', {
    'idempotencyKey': NotRequired[Annotated[str, Field(max_length=512)]],
    'operationId': NotRequired[Annotated[str, Field(max_length=200)]],
    'runId': NotRequired[Annotated[str, Field(max_length=200)]],
    'jobId': NotRequired[Annotated[str, Field(max_length=200)]],
    'operation': NotRequired[AnalyticsGetAttributionMethodologyOutputVariant2RecoveryOperation],
})
AnalyticsGetAttributionMethodologyOutputVariant2Recovery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class AnalyticsGetAttributionMethodologyOutputVariant2(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    delivery: AnalyticsGetAttributionMethodologyOutputVariant2Delivery = Field(..., alias='delivery', description='')
    preview: str = Field(..., alias='preview', description='')
    scope: dict[str, Union[str, Union[float, int], bool, None]] = Field(..., alias='scope', description='')
    recovery: AnalyticsGetAttributionMethodologyOutputVariant2Recovery = Field(..., alias='recovery', description='')


# Union schema: validate external payloads with TypeAdapter(AnalyticsGetAttributionMethodologyOutput).
AnalyticsGetAttributionMethodologyOutput = Union[AnalyticsGetAttributionMethodologyOutputVariant2, AnalyticsGetAttributionMethodologyOutputVariant1]

_AnalyticsGetAttributionMethodologyInputAdapter = TypeAdapter(AnalyticsGetAttributionMethodologyInput)
_AnalyticsGetAttributionMethodologyOutputAdapter = TypeAdapter(AnalyticsGetAttributionMethodologyOutput)