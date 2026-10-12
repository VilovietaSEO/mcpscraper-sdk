from typing import Annotated, Any, Literal, Union
from typing_extensions import NotRequired, Required, TypedDict
from pydantic import BaseModel, ConfigDict, Field, TypeAdapter


class AnalyticsCreateCampaignLinkInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=False)

    site_id: str = Field(..., alias='siteId', description='Analytics Site id returned by analytics_list_sites.')
    pixel_id: Union[str, None] = Field(None, alias='pixelId', description='Analytics Pixel id belonging to the selected Site.')
    name: Annotated[str, Field(min_length=1, max_length=120)] = Field(..., alias='name', description='Human-readable name for the record being created or updated.')
    destination_url: Annotated[str, Field(max_length=3000)] = Field(..., alias='destinationUrl', description='Final public destination URL for the tracked campaign link.')
    source: Annotated[str, Field(min_length=1, max_length=180)] = Field(..., alias='source', description='Optional source or provenance constraint appropriate to this tool; omit when no source restriction is intended.')
    medium: Annotated[str, Field(min_length=1, max_length=180)] = Field(..., alias='medium', description='Exact normalized campaign medium used to filter or label analytics data.')
    campaign: Annotated[str, Field(min_length=1, max_length=240)] = Field(..., alias='campaign', description='Exact normalized campaign value used to filter or label analytics data.')
    term: Union[Annotated[str, Field(max_length=240)], None] = Field(None, alias='term', description='Optional paid-search term preserved on the tracked campaign link.')
    content: Union[Annotated[str, Field(max_length=240)], None] = Field(None, alias='content', description='Complete content to route, validate, or store; do not substitute a partial excerpt when full content is required.')
    ad_group: Union[Annotated[str, Field(max_length=240)], None] = Field(None, alias='adGroup', description='Optional advertising ad-group identifier preserved on the tracked campaign link.')
    ad_name: Union[Annotated[str, Field(max_length=240)], None] = Field(None, alias='adName', description='Optional advertising ad name preserved on the tracked campaign link.')
    creative_id: Union[Annotated[str, Field(max_length=240)], None] = Field(None, alias='creativeId', description='Optional advertising creative identifier preserved on the tracked campaign link.')
    idempotency_key: Annotated[str, Field(min_length=8, max_length=160)] = Field(..., alias='idempotencyKey', description='Retry key; reuse only for this exact mutation.')


class AnalyticsCreateCampaignLinkOutputVariant1(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    ok: bool = Field(..., alias='ok', description='')
    link: dict[str, Any] = Field(..., alias='link', description='')


AnalyticsCreateCampaignLinkOutputVariant2DeliveryArtifactsItem = TypedDict('AnalyticsCreateCampaignLinkOutputVariant2DeliveryArtifactsItem', {
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
AnalyticsCreateCampaignLinkOutputVariant2DeliveryArtifactsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


AnalyticsCreateCampaignLinkOutputVariant2DeliveryStorageFailureVariant1 = TypedDict('AnalyticsCreateCampaignLinkOutputVariant2DeliveryStorageFailureVariant1', {
    'artifactId': Required[Union[str, None]],
    'outcome': Required[Literal['unknown', 'bytes-stored-metadata-pending', 'failed']],
})
AnalyticsCreateCampaignLinkOutputVariant2DeliveryStorageFailureVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


AnalyticsCreateCampaignLinkOutputVariant2Delivery = TypedDict('AnalyticsCreateCampaignLinkOutputVariant2Delivery', {
    'mode': Required[Literal['artifact']],
    'status': Required[Literal['complete', 'partial', 'unavailable']],
    'retainedRepresentation': Required[Literal['formatted-tool-result']],
    'sourceIsError': Required[bool],
    'artifacts': Required[list[AnalyticsCreateCampaignLinkOutputVariant2DeliveryArtifactsItem]],
    'downloadLinksOmitted': Required[bool],
    'scopeOmittedFields': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'storageFailure': Required[Union[AnalyticsCreateCampaignLinkOutputVariant2DeliveryStorageFailureVariant1, None]],
    'nextAction': Required[str],
})
AnalyticsCreateCampaignLinkOutputVariant2Delivery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


AnalyticsCreateCampaignLinkOutputVariant2RecoveryOperation = TypedDict('AnalyticsCreateCampaignLinkOutputVariant2RecoveryOperation', {
    'runId': Required[Union[Annotated[str, Field(max_length=200)], None]],
    'idempotencyKey': Required[Annotated[str, Field(max_length=512)]],
    'state': Required[Annotated[str, Field(max_length=100)]],
})
AnalyticsCreateCampaignLinkOutputVariant2RecoveryOperation.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


AnalyticsCreateCampaignLinkOutputVariant2Recovery = TypedDict('AnalyticsCreateCampaignLinkOutputVariant2Recovery', {
    'idempotencyKey': NotRequired[Annotated[str, Field(max_length=512)]],
    'operationId': NotRequired[Annotated[str, Field(max_length=200)]],
    'runId': NotRequired[Annotated[str, Field(max_length=200)]],
    'jobId': NotRequired[Annotated[str, Field(max_length=200)]],
    'operation': NotRequired[AnalyticsCreateCampaignLinkOutputVariant2RecoveryOperation],
})
AnalyticsCreateCampaignLinkOutputVariant2Recovery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class AnalyticsCreateCampaignLinkOutputVariant2(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    delivery: AnalyticsCreateCampaignLinkOutputVariant2Delivery = Field(..., alias='delivery', description='')
    preview: str = Field(..., alias='preview', description='')
    scope: dict[str, Union[str, Union[float, int], bool, None]] = Field(..., alias='scope', description='')
    recovery: AnalyticsCreateCampaignLinkOutputVariant2Recovery = Field(..., alias='recovery', description='')


# Union schema: validate external payloads with TypeAdapter(AnalyticsCreateCampaignLinkOutput).
AnalyticsCreateCampaignLinkOutput = Union[AnalyticsCreateCampaignLinkOutputVariant2, AnalyticsCreateCampaignLinkOutputVariant1]

_AnalyticsCreateCampaignLinkInputAdapter = TypeAdapter(AnalyticsCreateCampaignLinkInput)
_AnalyticsCreateCampaignLinkOutputAdapter = TypeAdapter(AnalyticsCreateCampaignLinkOutput)