from typing import Annotated, Any, Literal, Union
from typing_extensions import NotRequired, Required, TypedDict
from pydantic import BaseModel, ConfigDict, Field, TypeAdapter


class AnalyticsCreatePredictionTargetInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=False)

    site_id: str = Field(..., alias='siteId', description='Analytics Site id returned by analytics_list_sites.')
    namespace_id: Annotated[str, Field(min_length=1, max_length=160)] = Field(..., alias='namespaceId', description='Identity Namespace belonging to this Site.')
    name: Annotated[str, Field(min_length=1, max_length=160)] = Field(..., alias='name', description='Human-readable prediction target.')
    outcome_event: str = Field(..., alias='outcomeEvent', description='Confirmed outcome event to predict.')
    horizon_days: Annotated[int, Field(ge=1, le=3650)] = Field(..., alias='horizonDays', description='Prediction horizon in days.')
    outcome_value_minor: Union[Annotated[int, Field(ge=0, le=9007199254740991)], None] = Field(None, alias='outcomeValueMinor', description='Optional outcome value in minor units; this is not predicted revenue.')
    currency: Union[Annotated[str, Field(min_length=3, max_length=3)], None] = Field(None, alias='currency', description='ISO 4217 currency, required with outcomeValueMinor.')
    enabled: Union[bool, None] = Field(None, alias='enabled', description='Whether to collect eligibility evidence for this target.')
    idempotency_key: Annotated[str, Field(min_length=8, max_length=160)] = Field(..., alias='idempotencyKey', description='Caller-owned idempotency key. Reuse it only when retrying the same logical mutation.')


class AnalyticsCreatePredictionTargetOutputVariant1(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    ok: bool = Field(..., alias='ok', description='')
    target: dict[str, Any] = Field(..., alias='target', description='')


AnalyticsCreatePredictionTargetOutputVariant2DeliveryArtifactsItem = TypedDict('AnalyticsCreatePredictionTargetOutputVariant2DeliveryArtifactsItem', {
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
AnalyticsCreatePredictionTargetOutputVariant2DeliveryArtifactsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


AnalyticsCreatePredictionTargetOutputVariant2DeliveryAvailableExportsItem = TypedDict('AnalyticsCreatePredictionTargetOutputVariant2DeliveryAvailableExportsItem', {
    'artifactId': Required[str],
    'sourceArtifactId': Required[str],
    'filename': Required[Literal['result.md']],
    'contentType': Required[Literal['text/markdown; charset=utf-8']],
    'state': Required[Literal['on-demand']],
})
AnalyticsCreatePredictionTargetOutputVariant2DeliveryAvailableExportsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


AnalyticsCreatePredictionTargetOutputVariant2DeliveryStorageFailureVariant1 = TypedDict('AnalyticsCreatePredictionTargetOutputVariant2DeliveryStorageFailureVariant1', {
    'artifactId': Required[Union[str, None]],
    'outcome': Required[Literal['unknown', 'bytes-stored-metadata-pending', 'failed']],
})
AnalyticsCreatePredictionTargetOutputVariant2DeliveryStorageFailureVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


AnalyticsCreatePredictionTargetOutputVariant2Delivery = TypedDict('AnalyticsCreatePredictionTargetOutputVariant2Delivery', {
    'mode': Required[Literal['artifact']],
    'status': Required[Literal['complete', 'partial', 'unavailable']],
    'retainedRepresentation': Required[Literal['formatted-tool-result']],
    'sourceIsError': Required[bool],
    'artifacts': Required[list[AnalyticsCreatePredictionTargetOutputVariant2DeliveryArtifactsItem]],
    'availableExports': NotRequired[list[AnalyticsCreatePredictionTargetOutputVariant2DeliveryAvailableExportsItem]],
    'downloadLinksOmitted': Required[bool],
    'scopeOmittedFields': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'storageFailure': Required[Union[AnalyticsCreatePredictionTargetOutputVariant2DeliveryStorageFailureVariant1, None]],
    'nextAction': Required[str],
})
AnalyticsCreatePredictionTargetOutputVariant2Delivery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


AnalyticsCreatePredictionTargetOutputVariant2RecoveryOperation = TypedDict('AnalyticsCreatePredictionTargetOutputVariant2RecoveryOperation', {
    'runId': Required[Union[Annotated[str, Field(max_length=200)], None]],
    'idempotencyKey': Required[Annotated[str, Field(max_length=512)]],
    'state': Required[Annotated[str, Field(max_length=100)]],
})
AnalyticsCreatePredictionTargetOutputVariant2RecoveryOperation.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


AnalyticsCreatePredictionTargetOutputVariant2Recovery = TypedDict('AnalyticsCreatePredictionTargetOutputVariant2Recovery', {
    'idempotencyKey': NotRequired[Annotated[str, Field(max_length=512)]],
    'operationId': NotRequired[Annotated[str, Field(max_length=200)]],
    'runId': NotRequired[Annotated[str, Field(max_length=200)]],
    'jobId': NotRequired[Annotated[str, Field(max_length=200)]],
    'operation': NotRequired[AnalyticsCreatePredictionTargetOutputVariant2RecoveryOperation],
})
AnalyticsCreatePredictionTargetOutputVariant2Recovery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class AnalyticsCreatePredictionTargetOutputVariant2(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    delivery: AnalyticsCreatePredictionTargetOutputVariant2Delivery = Field(..., alias='delivery', description='')
    preview: str = Field(..., alias='preview', description='')
    scope: dict[str, Union[str, Union[float, int], bool, None]] = Field(..., alias='scope', description='')
    recovery: AnalyticsCreatePredictionTargetOutputVariant2Recovery = Field(..., alias='recovery', description='')


# Union schema: validate external payloads with TypeAdapter(AnalyticsCreatePredictionTargetOutput).
AnalyticsCreatePredictionTargetOutput = Union[AnalyticsCreatePredictionTargetOutputVariant2, AnalyticsCreatePredictionTargetOutputVariant1]

_AnalyticsCreatePredictionTargetInputAdapter = TypeAdapter(AnalyticsCreatePredictionTargetInput)
_AnalyticsCreatePredictionTargetOutputAdapter = TypeAdapter(AnalyticsCreatePredictionTargetOutput)