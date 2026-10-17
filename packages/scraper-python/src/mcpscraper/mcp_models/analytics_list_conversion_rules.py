from typing import Annotated, Any, Literal, Union
from typing_extensions import NotRequired, Required, TypedDict
from pydantic import BaseModel, ConfigDict, Field, TypeAdapter


class AnalyticsListConversionRulesInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=False)

    site_id: str = Field(..., alias='siteId', description='Analytics Site id returned by analytics_list_sites.')
    limit: Union[Annotated[int, Field(ge=1, le=250)], None] = Field(None, alias='limit', description='Maximum rows or records to return on this page; use the returned cursor for more.')
    cursor: Union[Annotated[str, Field(max_length=1000)], None] = Field(None, alias='cursor', description='Opaque continuation cursor returned by the previous page; omit for the first page.')


class AnalyticsListConversionRulesOutputVariant1(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    ok: bool = Field(..., alias='ok', description='')
    rules: Annotated[list[dict[str, Any]], Field(max_length=500)] = Field(..., alias='rules', description='')


AnalyticsListConversionRulesOutputVariant2DeliveryArtifactsItem = TypedDict('AnalyticsListConversionRulesOutputVariant2DeliveryArtifactsItem', {
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
AnalyticsListConversionRulesOutputVariant2DeliveryArtifactsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


AnalyticsListConversionRulesOutputVariant2DeliveryAvailableExportsItem = TypedDict('AnalyticsListConversionRulesOutputVariant2DeliveryAvailableExportsItem', {
    'artifactId': Required[str],
    'sourceArtifactId': Required[str],
    'filename': Required[Literal['result.md']],
    'contentType': Required[Literal['text/markdown; charset=utf-8']],
    'state': Required[Literal['on-demand']],
})
AnalyticsListConversionRulesOutputVariant2DeliveryAvailableExportsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


AnalyticsListConversionRulesOutputVariant2DeliveryStorageFailureVariant1 = TypedDict('AnalyticsListConversionRulesOutputVariant2DeliveryStorageFailureVariant1', {
    'artifactId': Required[Union[str, None]],
    'outcome': Required[Literal['unknown', 'bytes-stored-metadata-pending', 'failed']],
})
AnalyticsListConversionRulesOutputVariant2DeliveryStorageFailureVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


AnalyticsListConversionRulesOutputVariant2Delivery = TypedDict('AnalyticsListConversionRulesOutputVariant2Delivery', {
    'mode': Required[Literal['artifact']],
    'status': Required[Literal['complete', 'partial', 'unavailable']],
    'retainedRepresentation': Required[Literal['formatted-tool-result']],
    'sourceIsError': Required[bool],
    'artifacts': Required[list[AnalyticsListConversionRulesOutputVariant2DeliveryArtifactsItem]],
    'availableExports': NotRequired[list[AnalyticsListConversionRulesOutputVariant2DeliveryAvailableExportsItem]],
    'downloadLinksOmitted': Required[bool],
    'scopeOmittedFields': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'storageFailure': Required[Union[AnalyticsListConversionRulesOutputVariant2DeliveryStorageFailureVariant1, None]],
    'nextAction': Required[str],
})
AnalyticsListConversionRulesOutputVariant2Delivery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


AnalyticsListConversionRulesOutputVariant2RecoveryOperation = TypedDict('AnalyticsListConversionRulesOutputVariant2RecoveryOperation', {
    'runId': Required[Union[Annotated[str, Field(max_length=200)], None]],
    'idempotencyKey': Required[Annotated[str, Field(max_length=512)]],
    'state': Required[Annotated[str, Field(max_length=100)]],
})
AnalyticsListConversionRulesOutputVariant2RecoveryOperation.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


AnalyticsListConversionRulesOutputVariant2Recovery = TypedDict('AnalyticsListConversionRulesOutputVariant2Recovery', {
    'idempotencyKey': NotRequired[Annotated[str, Field(max_length=512)]],
    'operationId': NotRequired[Annotated[str, Field(max_length=200)]],
    'runId': NotRequired[Annotated[str, Field(max_length=200)]],
    'jobId': NotRequired[Annotated[str, Field(max_length=200)]],
    'operation': NotRequired[AnalyticsListConversionRulesOutputVariant2RecoveryOperation],
})
AnalyticsListConversionRulesOutputVariant2Recovery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class AnalyticsListConversionRulesOutputVariant2(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    delivery: AnalyticsListConversionRulesOutputVariant2Delivery = Field(..., alias='delivery', description='')
    preview: str = Field(..., alias='preview', description='')
    scope: dict[str, Union[str, Union[float, int], bool, None]] = Field(..., alias='scope', description='')
    recovery: AnalyticsListConversionRulesOutputVariant2Recovery = Field(..., alias='recovery', description='')


# Union schema: validate external payloads with TypeAdapter(AnalyticsListConversionRulesOutput).
AnalyticsListConversionRulesOutput = Union[AnalyticsListConversionRulesOutputVariant2, AnalyticsListConversionRulesOutputVariant1]

_AnalyticsListConversionRulesInputAdapter = TypeAdapter(AnalyticsListConversionRulesInput)
_AnalyticsListConversionRulesOutputAdapter = TypeAdapter(AnalyticsListConversionRulesOutput)