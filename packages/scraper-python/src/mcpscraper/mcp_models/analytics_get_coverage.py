from typing import Annotated, Any, Literal, Union
from typing_extensions import NotRequired, Required, TypedDict
from pydantic import BaseModel, ConfigDict, Field, TypeAdapter


class AnalyticsGetCoverageInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=False)

    site_id: str = Field(..., alias='siteId', description='Analytics Site id returned by analytics_list_sites.')
    limit: Union[Annotated[int, Field(ge=1, le=250)], None] = Field(None, alias='limit', description='Maximum rows or records to return on this page; use the returned cursor for more.')
    cursor: Union[Annotated[str, Field(max_length=1000)], None] = Field(None, alias='cursor', description='Opaque continuation cursor returned by the previous page; omit for the first page.')


class AnalyticsGetCoverageOutputVariant1(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    ok: bool = Field(..., alias='ok', description='')
    coverage: dict[str, Any] = Field(..., alias='coverage', description='')


AnalyticsGetCoverageOutputVariant2DeliveryArtifactsItem = TypedDict('AnalyticsGetCoverageOutputVariant2DeliveryArtifactsItem', {
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
AnalyticsGetCoverageOutputVariant2DeliveryArtifactsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


AnalyticsGetCoverageOutputVariant2DeliveryAvailableExportsItem = TypedDict('AnalyticsGetCoverageOutputVariant2DeliveryAvailableExportsItem', {
    'artifactId': Required[str],
    'sourceArtifactId': Required[str],
    'filename': Required[Literal['result.md']],
    'contentType': Required[Literal['text/markdown; charset=utf-8']],
    'state': Required[Literal['on-demand']],
})
AnalyticsGetCoverageOutputVariant2DeliveryAvailableExportsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


AnalyticsGetCoverageOutputVariant2DeliveryStorageFailureVariant1 = TypedDict('AnalyticsGetCoverageOutputVariant2DeliveryStorageFailureVariant1', {
    'artifactId': Required[Union[str, None]],
    'outcome': Required[Literal['unknown', 'bytes-stored-metadata-pending', 'failed']],
})
AnalyticsGetCoverageOutputVariant2DeliveryStorageFailureVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


AnalyticsGetCoverageOutputVariant2Delivery = TypedDict('AnalyticsGetCoverageOutputVariant2Delivery', {
    'mode': Required[Literal['artifact']],
    'status': Required[Literal['complete', 'partial', 'unavailable']],
    'retainedRepresentation': Required[Literal['formatted-tool-result']],
    'sourceIsError': Required[bool],
    'artifacts': Required[list[AnalyticsGetCoverageOutputVariant2DeliveryArtifactsItem]],
    'availableExports': NotRequired[list[AnalyticsGetCoverageOutputVariant2DeliveryAvailableExportsItem]],
    'downloadLinksOmitted': Required[bool],
    'scopeOmittedFields': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'storageFailure': Required[Union[AnalyticsGetCoverageOutputVariant2DeliveryStorageFailureVariant1, None]],
    'nextAction': Required[str],
})
AnalyticsGetCoverageOutputVariant2Delivery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


AnalyticsGetCoverageOutputVariant2RecoveryOperation = TypedDict('AnalyticsGetCoverageOutputVariant2RecoveryOperation', {
    'runId': Required[Union[Annotated[str, Field(max_length=200)], None]],
    'idempotencyKey': Required[Annotated[str, Field(max_length=512)]],
    'state': Required[Annotated[str, Field(max_length=100)]],
})
AnalyticsGetCoverageOutputVariant2RecoveryOperation.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


AnalyticsGetCoverageOutputVariant2Recovery = TypedDict('AnalyticsGetCoverageOutputVariant2Recovery', {
    'idempotencyKey': NotRequired[Annotated[str, Field(max_length=512)]],
    'operationId': NotRequired[Annotated[str, Field(max_length=200)]],
    'runId': NotRequired[Annotated[str, Field(max_length=200)]],
    'jobId': NotRequired[Annotated[str, Field(max_length=200)]],
    'operation': NotRequired[AnalyticsGetCoverageOutputVariant2RecoveryOperation],
})
AnalyticsGetCoverageOutputVariant2Recovery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class AnalyticsGetCoverageOutputVariant2(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    delivery: AnalyticsGetCoverageOutputVariant2Delivery = Field(..., alias='delivery', description='')
    preview: str = Field(..., alias='preview', description='')
    scope: dict[str, Union[str, Union[float, int], bool, None]] = Field(..., alias='scope', description='')
    recovery: AnalyticsGetCoverageOutputVariant2Recovery = Field(..., alias='recovery', description='')


# Union schema: validate external payloads with TypeAdapter(AnalyticsGetCoverageOutput).
AnalyticsGetCoverageOutput = Union[AnalyticsGetCoverageOutputVariant2, AnalyticsGetCoverageOutputVariant1]

_AnalyticsGetCoverageInputAdapter = TypeAdapter(AnalyticsGetCoverageInput)
_AnalyticsGetCoverageOutputAdapter = TypeAdapter(AnalyticsGetCoverageOutput)