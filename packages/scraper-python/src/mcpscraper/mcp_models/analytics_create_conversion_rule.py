from typing import Annotated, Any, Literal, Union
from typing_extensions import NotRequired, Required, TypedDict
from pydantic import BaseModel, ConfigDict, Field, TypeAdapter


AnalyticsCreateConversionRuleInputCondition = TypedDict('AnalyticsCreateConversionRuleInputCondition', {
    'eventName': NotRequired[str],
    'eventKind': NotRequired[Literal['browser', 'form', 'call', 'crm', 'transaction', 'custom_server', 'conversion', 'delivery']],
    'source': NotRequired[Annotated[str, Field(min_length=1, max_length=80)]],
    'stageId': NotRequired[Annotated[str, Field(max_length=240)]],
    'status': NotRequired[Literal['open', 'won', 'lost', 'spam', 'unknown']],
    'answered': NotRequired[bool],
    'minimumCallDurationSeconds': NotRequired[Annotated[int, Field(ge=0, le=86400)]],
    'excludedTags': NotRequired[Annotated[list[Annotated[str, Field(max_length=80)]], Field(max_length=30)]],
    'requiredTags': NotRequired[Annotated[list[Annotated[str, Field(max_length=80)]], Field(max_length=30)]],
})
AnalyticsCreateConversionRuleInputCondition.__pydantic_config__ = ConfigDict(extra="allow", strict=False)


class AnalyticsCreateConversionRuleInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=False)

    site_id: str = Field(..., alias='siteId', description='Analytics Site id returned by analytics_list_sites.')
    name: Annotated[str, Field(min_length=1, max_length=120)] = Field(..., alias='name', description='Human-readable name for the record being created or updated.')
    conversion_kind: str = Field(..., alias='conversionKind', description='Optional normalized conversion event kind filter.')
    condition: AnalyticsCreateConversionRuleInputCondition = Field(..., alias='condition', description='Declarative event conditions that must match before X-Ray creates a conversion.')
    default_value_minor: Union[Annotated[int, Field(ge=0, le=9007199254740991)], None] = Field(None, alias='defaultValueMinor', description='Optional default conversion value in the currency minor unit.')
    default_currency: Union[Annotated[str, Field(min_length=3, max_length=3)], None] = Field(None, alias='defaultCurrency', description='Three-letter default currency code used when a matched event has no value currency.')
    enabled: Union[bool, None] = Field(None, alias='enabled', description='Whether the new rule should begin evaluating events immediately.')
    idempotency_key: Annotated[str, Field(min_length=8, max_length=160)] = Field(..., alias='idempotencyKey', description='Retry key; reuse only for this exact mutation.')


class AnalyticsCreateConversionRuleOutputVariant1(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    ok: bool = Field(..., alias='ok', description='')
    rule: dict[str, Any] = Field(..., alias='rule', description='')


AnalyticsCreateConversionRuleOutputVariant2DeliveryArtifactsItem = TypedDict('AnalyticsCreateConversionRuleOutputVariant2DeliveryArtifactsItem', {
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
AnalyticsCreateConversionRuleOutputVariant2DeliveryArtifactsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


AnalyticsCreateConversionRuleOutputVariant2DeliveryAvailableExportsItem = TypedDict('AnalyticsCreateConversionRuleOutputVariant2DeliveryAvailableExportsItem', {
    'artifactId': Required[str],
    'sourceArtifactId': Required[str],
    'filename': Required[Literal['result.md']],
    'contentType': Required[Literal['text/markdown; charset=utf-8']],
    'state': Required[Literal['on-demand']],
})
AnalyticsCreateConversionRuleOutputVariant2DeliveryAvailableExportsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


AnalyticsCreateConversionRuleOutputVariant2DeliveryStorageFailureVariant1 = TypedDict('AnalyticsCreateConversionRuleOutputVariant2DeliveryStorageFailureVariant1', {
    'artifactId': Required[Union[str, None]],
    'outcome': Required[Literal['unknown', 'bytes-stored-metadata-pending', 'failed']],
})
AnalyticsCreateConversionRuleOutputVariant2DeliveryStorageFailureVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


AnalyticsCreateConversionRuleOutputVariant2Delivery = TypedDict('AnalyticsCreateConversionRuleOutputVariant2Delivery', {
    'mode': Required[Literal['artifact']],
    'status': Required[Literal['complete', 'partial', 'unavailable']],
    'retainedRepresentation': Required[Literal['formatted-tool-result']],
    'sourceIsError': Required[bool],
    'artifacts': Required[list[AnalyticsCreateConversionRuleOutputVariant2DeliveryArtifactsItem]],
    'availableExports': NotRequired[list[AnalyticsCreateConversionRuleOutputVariant2DeliveryAvailableExportsItem]],
    'downloadLinksOmitted': Required[bool],
    'scopeOmittedFields': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'storageFailure': Required[Union[AnalyticsCreateConversionRuleOutputVariant2DeliveryStorageFailureVariant1, None]],
    'nextAction': Required[str],
})
AnalyticsCreateConversionRuleOutputVariant2Delivery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


AnalyticsCreateConversionRuleOutputVariant2RecoveryOperation = TypedDict('AnalyticsCreateConversionRuleOutputVariant2RecoveryOperation', {
    'runId': Required[Union[Annotated[str, Field(max_length=200)], None]],
    'idempotencyKey': Required[Annotated[str, Field(max_length=512)]],
    'state': Required[Annotated[str, Field(max_length=100)]],
})
AnalyticsCreateConversionRuleOutputVariant2RecoveryOperation.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


AnalyticsCreateConversionRuleOutputVariant2Recovery = TypedDict('AnalyticsCreateConversionRuleOutputVariant2Recovery', {
    'idempotencyKey': NotRequired[Annotated[str, Field(max_length=512)]],
    'operationId': NotRequired[Annotated[str, Field(max_length=200)]],
    'runId': NotRequired[Annotated[str, Field(max_length=200)]],
    'jobId': NotRequired[Annotated[str, Field(max_length=200)]],
    'operation': NotRequired[AnalyticsCreateConversionRuleOutputVariant2RecoveryOperation],
})
AnalyticsCreateConversionRuleOutputVariant2Recovery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class AnalyticsCreateConversionRuleOutputVariant2(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    delivery: AnalyticsCreateConversionRuleOutputVariant2Delivery = Field(..., alias='delivery', description='')
    preview: str = Field(..., alias='preview', description='')
    scope: dict[str, Union[str, Union[float, int], bool, None]] = Field(..., alias='scope', description='')
    recovery: AnalyticsCreateConversionRuleOutputVariant2Recovery = Field(..., alias='recovery', description='')


# Union schema: validate external payloads with TypeAdapter(AnalyticsCreateConversionRuleOutput).
AnalyticsCreateConversionRuleOutput = Union[AnalyticsCreateConversionRuleOutputVariant2, AnalyticsCreateConversionRuleOutputVariant1]

_AnalyticsCreateConversionRuleInputAdapter = TypeAdapter(AnalyticsCreateConversionRuleInput)
_AnalyticsCreateConversionRuleOutputAdapter = TypeAdapter(AnalyticsCreateConversionRuleOutput)