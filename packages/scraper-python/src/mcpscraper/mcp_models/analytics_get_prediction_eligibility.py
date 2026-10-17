from typing import Annotated, Any, Literal, Union
from typing_extensions import NotRequired, Required, TypedDict
from pydantic import BaseModel, ConfigDict, Field, TypeAdapter


class AnalyticsGetPredictionEligibilityInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=False)

    site_id: str = Field(..., alias='siteId', description='Analytics Site id returned by analytics_list_sites.')
    namespace_id: Annotated[str, Field(min_length=1, max_length=160)] = Field(..., alias='namespaceId', description='Identity Namespace belonging to this Site.')
    target_id: str = Field(..., alias='targetId', description='Prediction target id returned by analytics_list_prediction_targets.')


class AnalyticsGetPredictionEligibilityOutputVariant1(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    ok: bool = Field(..., alias='ok', description='')
    target: dict[str, Any] = Field(..., alias='target', description='')
    eligibility: dict[str, Any] = Field(..., alias='eligibility', description='')


AnalyticsGetPredictionEligibilityOutputVariant2DeliveryArtifactsItem = TypedDict('AnalyticsGetPredictionEligibilityOutputVariant2DeliveryArtifactsItem', {
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
AnalyticsGetPredictionEligibilityOutputVariant2DeliveryArtifactsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


AnalyticsGetPredictionEligibilityOutputVariant2DeliveryAvailableExportsItem = TypedDict('AnalyticsGetPredictionEligibilityOutputVariant2DeliveryAvailableExportsItem', {
    'artifactId': Required[str],
    'sourceArtifactId': Required[str],
    'filename': Required[Literal['result.md']],
    'contentType': Required[Literal['text/markdown; charset=utf-8']],
    'state': Required[Literal['on-demand']],
})
AnalyticsGetPredictionEligibilityOutputVariant2DeliveryAvailableExportsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


AnalyticsGetPredictionEligibilityOutputVariant2DeliveryStorageFailureVariant1 = TypedDict('AnalyticsGetPredictionEligibilityOutputVariant2DeliveryStorageFailureVariant1', {
    'artifactId': Required[Union[str, None]],
    'outcome': Required[Literal['unknown', 'bytes-stored-metadata-pending', 'failed']],
})
AnalyticsGetPredictionEligibilityOutputVariant2DeliveryStorageFailureVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


AnalyticsGetPredictionEligibilityOutputVariant2Delivery = TypedDict('AnalyticsGetPredictionEligibilityOutputVariant2Delivery', {
    'mode': Required[Literal['artifact']],
    'status': Required[Literal['complete', 'partial', 'unavailable']],
    'retainedRepresentation': Required[Literal['formatted-tool-result']],
    'sourceIsError': Required[bool],
    'artifacts': Required[list[AnalyticsGetPredictionEligibilityOutputVariant2DeliveryArtifactsItem]],
    'availableExports': NotRequired[list[AnalyticsGetPredictionEligibilityOutputVariant2DeliveryAvailableExportsItem]],
    'downloadLinksOmitted': Required[bool],
    'scopeOmittedFields': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'storageFailure': Required[Union[AnalyticsGetPredictionEligibilityOutputVariant2DeliveryStorageFailureVariant1, None]],
    'nextAction': Required[str],
})
AnalyticsGetPredictionEligibilityOutputVariant2Delivery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


AnalyticsGetPredictionEligibilityOutputVariant2RecoveryOperation = TypedDict('AnalyticsGetPredictionEligibilityOutputVariant2RecoveryOperation', {
    'runId': Required[Union[Annotated[str, Field(max_length=200)], None]],
    'idempotencyKey': Required[Annotated[str, Field(max_length=512)]],
    'state': Required[Annotated[str, Field(max_length=100)]],
})
AnalyticsGetPredictionEligibilityOutputVariant2RecoveryOperation.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


AnalyticsGetPredictionEligibilityOutputVariant2Recovery = TypedDict('AnalyticsGetPredictionEligibilityOutputVariant2Recovery', {
    'idempotencyKey': NotRequired[Annotated[str, Field(max_length=512)]],
    'operationId': NotRequired[Annotated[str, Field(max_length=200)]],
    'runId': NotRequired[Annotated[str, Field(max_length=200)]],
    'jobId': NotRequired[Annotated[str, Field(max_length=200)]],
    'operation': NotRequired[AnalyticsGetPredictionEligibilityOutputVariant2RecoveryOperation],
})
AnalyticsGetPredictionEligibilityOutputVariant2Recovery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class AnalyticsGetPredictionEligibilityOutputVariant2(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    delivery: AnalyticsGetPredictionEligibilityOutputVariant2Delivery = Field(..., alias='delivery', description='')
    preview: str = Field(..., alias='preview', description='')
    scope: dict[str, Union[str, Union[float, int], bool, None]] = Field(..., alias='scope', description='')
    recovery: AnalyticsGetPredictionEligibilityOutputVariant2Recovery = Field(..., alias='recovery', description='')


# Union schema: validate external payloads with TypeAdapter(AnalyticsGetPredictionEligibilityOutput).
AnalyticsGetPredictionEligibilityOutput = Union[AnalyticsGetPredictionEligibilityOutputVariant2, AnalyticsGetPredictionEligibilityOutputVariant1]

_AnalyticsGetPredictionEligibilityInputAdapter = TypeAdapter(AnalyticsGetPredictionEligibilityInput)
_AnalyticsGetPredictionEligibilityOutputAdapter = TypeAdapter(AnalyticsGetPredictionEligibilityOutput)