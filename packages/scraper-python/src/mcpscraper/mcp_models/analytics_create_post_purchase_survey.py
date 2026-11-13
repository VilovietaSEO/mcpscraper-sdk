from typing import Annotated, Any, Literal, Union
from typing_extensions import NotRequired, Required, TypedDict
from pydantic import BaseModel, ConfigDict, Field, TypeAdapter


AnalyticsCreatePostPurchaseSurveyInputOptionsItem = TypedDict('AnalyticsCreatePostPurchaseSurveyInputOptionsItem', {
    'optionId': Required[Annotated[str, Field(min_length=1, max_length=80)]],
    'label': Required[Annotated[str, Field(min_length=1, max_length=160)]],
})
AnalyticsCreatePostPurchaseSurveyInputOptionsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=False)


class AnalyticsCreatePostPurchaseSurveyInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=False)

    site_id: str = Field(..., alias='siteId', description='Authorized Analytics Site id.')
    name: Annotated[str, Field(min_length=1, max_length=160)] = Field(..., alias='name', description='Owner-facing survey name.')
    question: Annotated[str, Field(min_length=1, max_length=500)] = Field(..., alias='question', description='Customer-visible structured influence question; do not request contact data or free text.')
    selection_mode: Literal['single', 'multiple'] = Field(..., alias='selectionMode', description='Whether a respondent may select one influence or several.')
    eligible_outcome_families: Annotated[list[Annotated[str, Field(min_length=1, max_length=80)]], Field(min_length=1, max_length=20)] = Field(..., alias='eligibleOutcomeFamilies', description='Authoritative outcome families eligible to receive an invitation.')
    exchange_ttl_seconds: Annotated[int, Field(ge=60, le=86400)] = Field(..., alias='exchangeTtlSeconds', description='Short-lived merchant exchange-code lifetime.')
    session_ttl_seconds: Annotated[int, Field(ge=60, le=86400)] = Field(..., alias='sessionTtlSeconds', description='Hosted survey session lifetime after one-time exchange.')
    approved_copy_id: Union[Union[Annotated[str, Field(min_length=1, max_length=200)], None], None] = Field(None, alias='approvedCopyId', description='Versioned privacy disclosure approval. A draft may omit it; production publication may not.')
    options: Annotated[list[AnalyticsCreatePostPurchaseSurveyInputOptionsItem], Field(min_length=2, max_length=20)] = Field(..., alias='options', description='Two to twenty stable structured influences.')
    idempotency_key: Annotated[str, Field(min_length=8, max_length=160)] = Field(..., alias='idempotencyKey', description='Retry key; reuse only for this exact mutation.')


AnalyticsCreatePostPurchaseSurveyOutputVariant1SurveyOptionsItem = TypedDict('AnalyticsCreatePostPurchaseSurveyOutputVariant1SurveyOptionsItem', {
    'optionId': Required[Annotated[str, Field(min_length=1)]],
    'label': Required[Annotated[str, Field(min_length=1)]],
    'position': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
})
AnalyticsCreatePostPurchaseSurveyOutputVariant1SurveyOptionsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


AnalyticsCreatePostPurchaseSurveyOutputVariant1Survey = TypedDict('AnalyticsCreatePostPurchaseSurveyOutputVariant1Survey', {
    'surveyId': Required[str],
    'siteId': Required[str],
    'revision': Required[Annotated[int, Field(le=9007199254740991, gt=0)]],
    'state': Required[Literal['draft', 'published', 'paused', 'archived']],
    'name': Required[Annotated[str, Field(min_length=1)]],
    'question': Required[Annotated[str, Field(min_length=1)]],
    'selectionMode': Required[Literal['single', 'multiple']],
    'eligibleOutcomeFamilies': Required[Annotated[list[Annotated[str, Field(min_length=1)]], Field(min_length=1)]],
    'exchangeTtlSeconds': Required[Annotated[int, Field(le=9007199254740991, gt=0)]],
    'sessionTtlSeconds': Required[Annotated[int, Field(le=9007199254740991, gt=0)]],
    'approvedCopyId': Required[Union[Annotated[str, Field(min_length=1)], None]],
    'options': Required[Annotated[list[AnalyticsCreatePostPurchaseSurveyOutputVariant1SurveyOptionsItem], Field(min_length=2)]],
})
AnalyticsCreatePostPurchaseSurveyOutputVariant1Survey.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class AnalyticsCreatePostPurchaseSurveyOutputVariant1(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    ok: Literal[True] = Field(..., alias='ok', description='')
    operation: Literal['create'] = Field(..., alias='operation', description='')
    survey: AnalyticsCreatePostPurchaseSurveyOutputVariant1Survey = Field(..., alias='survey', description='')
    created: Union[bool, None] = Field(None, alias='created', description='')


AnalyticsCreatePostPurchaseSurveyOutputVariant2DeliveryArtifactsItem = TypedDict('AnalyticsCreatePostPurchaseSurveyOutputVariant2DeliveryArtifactsItem', {
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
AnalyticsCreatePostPurchaseSurveyOutputVariant2DeliveryArtifactsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


AnalyticsCreatePostPurchaseSurveyOutputVariant2DeliveryAvailableExportsItem = TypedDict('AnalyticsCreatePostPurchaseSurveyOutputVariant2DeliveryAvailableExportsItem', {
    'artifactId': Required[str],
    'sourceArtifactId': Required[str],
    'filename': Required[Literal['result.md']],
    'contentType': Required[Literal['text/markdown; charset=utf-8']],
    'state': Required[Literal['on-demand']],
})
AnalyticsCreatePostPurchaseSurveyOutputVariant2DeliveryAvailableExportsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


AnalyticsCreatePostPurchaseSurveyOutputVariant2DeliveryStorageFailureVariant1 = TypedDict('AnalyticsCreatePostPurchaseSurveyOutputVariant2DeliveryStorageFailureVariant1', {
    'artifactId': Required[Union[str, None]],
    'outcome': Required[Literal['unknown', 'bytes-stored-metadata-pending', 'failed']],
})
AnalyticsCreatePostPurchaseSurveyOutputVariant2DeliveryStorageFailureVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


AnalyticsCreatePostPurchaseSurveyOutputVariant2Delivery = TypedDict('AnalyticsCreatePostPurchaseSurveyOutputVariant2Delivery', {
    'mode': Required[Literal['artifact']],
    'status': Required[Literal['complete', 'partial', 'unavailable']],
    'retainedRepresentation': Required[Literal['formatted-tool-result']],
    'sourceIsError': Required[bool],
    'artifacts': Required[list[AnalyticsCreatePostPurchaseSurveyOutputVariant2DeliveryArtifactsItem]],
    'availableExports': NotRequired[list[AnalyticsCreatePostPurchaseSurveyOutputVariant2DeliveryAvailableExportsItem]],
    'downloadLinksOmitted': Required[bool],
    'scopeOmittedFields': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'storageFailure': Required[Union[AnalyticsCreatePostPurchaseSurveyOutputVariant2DeliveryStorageFailureVariant1, None]],
    'nextAction': Required[str],
})
AnalyticsCreatePostPurchaseSurveyOutputVariant2Delivery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


AnalyticsCreatePostPurchaseSurveyOutputVariant2RecoveryOperation = TypedDict('AnalyticsCreatePostPurchaseSurveyOutputVariant2RecoveryOperation', {
    'runId': Required[Union[Annotated[str, Field(max_length=200)], None]],
    'idempotencyKey': Required[Annotated[str, Field(max_length=512)]],
    'state': Required[Annotated[str, Field(max_length=100)]],
})
AnalyticsCreatePostPurchaseSurveyOutputVariant2RecoveryOperation.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


AnalyticsCreatePostPurchaseSurveyOutputVariant2Recovery = TypedDict('AnalyticsCreatePostPurchaseSurveyOutputVariant2Recovery', {
    'idempotencyKey': NotRequired[Annotated[str, Field(max_length=512)]],
    'operationId': NotRequired[Annotated[str, Field(max_length=200)]],
    'runId': NotRequired[Annotated[str, Field(max_length=200)]],
    'jobId': NotRequired[Annotated[str, Field(max_length=200)]],
    'operation': NotRequired[AnalyticsCreatePostPurchaseSurveyOutputVariant2RecoveryOperation],
})
AnalyticsCreatePostPurchaseSurveyOutputVariant2Recovery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class AnalyticsCreatePostPurchaseSurveyOutputVariant2(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    delivery: AnalyticsCreatePostPurchaseSurveyOutputVariant2Delivery = Field(..., alias='delivery', description='')
    preview: str = Field(..., alias='preview', description='')
    scope: dict[str, Union[str, Union[float, int], bool, None]] = Field(..., alias='scope', description='')
    recovery: AnalyticsCreatePostPurchaseSurveyOutputVariant2Recovery = Field(..., alias='recovery', description='')


# Union schema: validate external payloads with TypeAdapter(AnalyticsCreatePostPurchaseSurveyOutput).
AnalyticsCreatePostPurchaseSurveyOutput = Union[AnalyticsCreatePostPurchaseSurveyOutputVariant2, AnalyticsCreatePostPurchaseSurveyOutputVariant1]

_AnalyticsCreatePostPurchaseSurveyInputAdapter = TypeAdapter(AnalyticsCreatePostPurchaseSurveyInput)
_AnalyticsCreatePostPurchaseSurveyOutputAdapter = TypeAdapter(AnalyticsCreatePostPurchaseSurveyOutput)