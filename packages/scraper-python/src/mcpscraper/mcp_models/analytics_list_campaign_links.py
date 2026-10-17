from typing import Annotated, Any, Literal, Union
from typing_extensions import NotRequired, Required, TypedDict
from pydantic import BaseModel, ConfigDict, Field, TypeAdapter


class AnalyticsListCampaignLinksInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=False)

    site_id: str = Field(..., alias='siteId', description='Analytics Site id returned by analytics_list_sites.')
    limit: Union[Annotated[int, Field(ge=1, le=250)], None] = Field(None, alias='limit', description='Maximum rows or records to return on this page; use the returned cursor for more.')
    cursor: Union[Annotated[str, Field(max_length=1000)], None] = Field(None, alias='cursor', description='Opaque continuation cursor returned by the previous page; omit for the first page.')


class AnalyticsListCampaignLinksOutputVariant1(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    ok: bool = Field(..., alias='ok', description='')
    data: dict[str, Any] = Field(..., alias='data', description='')


AnalyticsListCampaignLinksOutputVariant2DeliveryArtifactsItem = TypedDict('AnalyticsListCampaignLinksOutputVariant2DeliveryArtifactsItem', {
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
AnalyticsListCampaignLinksOutputVariant2DeliveryArtifactsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


AnalyticsListCampaignLinksOutputVariant2DeliveryAvailableExportsItem = TypedDict('AnalyticsListCampaignLinksOutputVariant2DeliveryAvailableExportsItem', {
    'artifactId': Required[str],
    'sourceArtifactId': Required[str],
    'filename': Required[Literal['result.md']],
    'contentType': Required[Literal['text/markdown; charset=utf-8']],
    'state': Required[Literal['on-demand']],
})
AnalyticsListCampaignLinksOutputVariant2DeliveryAvailableExportsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


AnalyticsListCampaignLinksOutputVariant2DeliveryStorageFailureVariant1 = TypedDict('AnalyticsListCampaignLinksOutputVariant2DeliveryStorageFailureVariant1', {
    'artifactId': Required[Union[str, None]],
    'outcome': Required[Literal['unknown', 'bytes-stored-metadata-pending', 'failed']],
})
AnalyticsListCampaignLinksOutputVariant2DeliveryStorageFailureVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


AnalyticsListCampaignLinksOutputVariant2Delivery = TypedDict('AnalyticsListCampaignLinksOutputVariant2Delivery', {
    'mode': Required[Literal['artifact']],
    'status': Required[Literal['complete', 'partial', 'unavailable']],
    'retainedRepresentation': Required[Literal['formatted-tool-result']],
    'sourceIsError': Required[bool],
    'artifacts': Required[list[AnalyticsListCampaignLinksOutputVariant2DeliveryArtifactsItem]],
    'availableExports': NotRequired[list[AnalyticsListCampaignLinksOutputVariant2DeliveryAvailableExportsItem]],
    'downloadLinksOmitted': Required[bool],
    'scopeOmittedFields': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'storageFailure': Required[Union[AnalyticsListCampaignLinksOutputVariant2DeliveryStorageFailureVariant1, None]],
    'nextAction': Required[str],
})
AnalyticsListCampaignLinksOutputVariant2Delivery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


AnalyticsListCampaignLinksOutputVariant2RecoveryOperation = TypedDict('AnalyticsListCampaignLinksOutputVariant2RecoveryOperation', {
    'runId': Required[Union[Annotated[str, Field(max_length=200)], None]],
    'idempotencyKey': Required[Annotated[str, Field(max_length=512)]],
    'state': Required[Annotated[str, Field(max_length=100)]],
})
AnalyticsListCampaignLinksOutputVariant2RecoveryOperation.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


AnalyticsListCampaignLinksOutputVariant2Recovery = TypedDict('AnalyticsListCampaignLinksOutputVariant2Recovery', {
    'idempotencyKey': NotRequired[Annotated[str, Field(max_length=512)]],
    'operationId': NotRequired[Annotated[str, Field(max_length=200)]],
    'runId': NotRequired[Annotated[str, Field(max_length=200)]],
    'jobId': NotRequired[Annotated[str, Field(max_length=200)]],
    'operation': NotRequired[AnalyticsListCampaignLinksOutputVariant2RecoveryOperation],
})
AnalyticsListCampaignLinksOutputVariant2Recovery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class AnalyticsListCampaignLinksOutputVariant2(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    delivery: AnalyticsListCampaignLinksOutputVariant2Delivery = Field(..., alias='delivery', description='')
    preview: str = Field(..., alias='preview', description='')
    scope: dict[str, Union[str, Union[float, int], bool, None]] = Field(..., alias='scope', description='')
    recovery: AnalyticsListCampaignLinksOutputVariant2Recovery = Field(..., alias='recovery', description='')


# Union schema: validate external payloads with TypeAdapter(AnalyticsListCampaignLinksOutput).
AnalyticsListCampaignLinksOutput = Union[AnalyticsListCampaignLinksOutputVariant2, AnalyticsListCampaignLinksOutputVariant1]

_AnalyticsListCampaignLinksInputAdapter = TypeAdapter(AnalyticsListCampaignLinksInput)
_AnalyticsListCampaignLinksOutputAdapter = TypeAdapter(AnalyticsListCampaignLinksOutput)