from typing import Annotated, Any, Literal, Union
from typing_extensions import NotRequired, Required, TypedDict
from pydantic import BaseModel, ConfigDict, Field, TypeAdapter


AnalyticsTestFunnelInputDefinitionStagesItemRule = TypedDict('AnalyticsTestFunnelInputDefinitionStagesItemRule', {
    'eventNames': NotRequired[Annotated[list[str], Field(max_length=100)]],
    'conversionKinds': NotRequired[Annotated[list[str], Field(max_length=100)]],
    'externalEventNames': NotRequired[Annotated[list[str], Field(max_length=100)]],
})
AnalyticsTestFunnelInputDefinitionStagesItemRule.__pydantic_config__ = ConfigDict(extra="allow", strict=False)


AnalyticsTestFunnelInputDefinitionStagesItem = TypedDict('AnalyticsTestFunnelInputDefinitionStagesItem', {
    'key': Required[str],
    'label': Required[Annotated[str, Field(min_length=1, max_length=120)]],
    'rule': Required[AnalyticsTestFunnelInputDefinitionStagesItemRule],
})
AnalyticsTestFunnelInputDefinitionStagesItem.__pydantic_config__ = ConfigDict(extra="allow", strict=False)


AnalyticsTestFunnelInputDefinition = TypedDict('AnalyticsTestFunnelInputDefinition', {
    'name': Required[Annotated[str, Field(min_length=1, max_length=120)]],
    'stages': Required[Annotated[list[AnalyticsTestFunnelInputDefinitionStagesItem], Field(min_length=2, max_length=20)]],
    'isDefault': NotRequired[bool],
    'status': NotRequired[Literal['active', 'disabled']],
})
AnalyticsTestFunnelInputDefinition.__pydantic_config__ = ConfigDict(extra="allow", strict=False)


AnalyticsTestFunnelInputRecordsItem = TypedDict('AnalyticsTestFunnelInputRecordsItem', {
    'id': Required[Annotated[str, Field(min_length=1, max_length=240)]],
    'subjectRef': Required[Annotated[str, Field(min_length=8, max_length=240)]],
    'kind': Required[Literal['event', 'external', 'conversion']],
    'eventName': Required[str],
    'eventDefinitionId': NotRequired[Union[str, None]],
    'externalEventKind': NotRequired[Union[Annotated[str, Field(min_length=1, max_length=160)], None]],
    'occurredAt': Required[str],
    'source': NotRequired[Union[Annotated[str, Field(max_length=180)], None]],
    'campaign': NotRequired[Union[Annotated[str, Field(max_length=240)], None]],
    'adId': NotRequired[Union[Annotated[str, Field(max_length=240)], None]],
    'valueMinor': NotRequired[Union[Annotated[int, Field(ge=0, le=9007199254740991)], None]],
    'currency': NotRequired[Union[Annotated[str, Field(min_length=3, max_length=3)], None]],
})
AnalyticsTestFunnelInputRecordsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=False)


class AnalyticsTestFunnelInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=False)

    site_id: str = Field(..., alias='siteId', description='Analytics Site id returned by analytics_list_sites.')
    definition: AnalyticsTestFunnelInputDefinition = Field(..., alias='definition', description='Unsaved funnel definition to evaluate without persistence.')
    records: Annotated[list[AnalyticsTestFunnelInputRecordsItem], Field(max_length=10000)] = Field(..., alias='records', description='Bounded safe fixtures. personId, contact data, IP, click IDs, device identifiers, and provider bodies are schema-invalid.')
    start: str = Field(..., alias='start', description='Inclusive fixture window start.')
    end: str = Field(..., alias='end', description='Exclusive fixture window end.')


class AnalyticsTestFunnelOutputVariant1(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    ok: bool = Field(..., alias='ok', description='')
    result: dict[str, Any] = Field(..., alias='result', description='')


AnalyticsTestFunnelOutputVariant2DeliveryArtifactsItem = TypedDict('AnalyticsTestFunnelOutputVariant2DeliveryArtifactsItem', {
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
AnalyticsTestFunnelOutputVariant2DeliveryArtifactsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


AnalyticsTestFunnelOutputVariant2DeliveryStorageFailureVariant1 = TypedDict('AnalyticsTestFunnelOutputVariant2DeliveryStorageFailureVariant1', {
    'artifactId': Required[Union[str, None]],
    'outcome': Required[Literal['unknown', 'bytes-stored-metadata-pending', 'failed']],
})
AnalyticsTestFunnelOutputVariant2DeliveryStorageFailureVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


AnalyticsTestFunnelOutputVariant2Delivery = TypedDict('AnalyticsTestFunnelOutputVariant2Delivery', {
    'mode': Required[Literal['artifact']],
    'status': Required[Literal['complete', 'partial', 'unavailable']],
    'retainedRepresentation': Required[Literal['formatted-tool-result']],
    'sourceIsError': Required[bool],
    'artifacts': Required[list[AnalyticsTestFunnelOutputVariant2DeliveryArtifactsItem]],
    'downloadLinksOmitted': Required[bool],
    'scopeOmittedFields': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'storageFailure': Required[Union[AnalyticsTestFunnelOutputVariant2DeliveryStorageFailureVariant1, None]],
    'nextAction': Required[str],
})
AnalyticsTestFunnelOutputVariant2Delivery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


AnalyticsTestFunnelOutputVariant2RecoveryOperation = TypedDict('AnalyticsTestFunnelOutputVariant2RecoveryOperation', {
    'runId': Required[Union[Annotated[str, Field(max_length=200)], None]],
    'idempotencyKey': Required[Annotated[str, Field(max_length=512)]],
    'state': Required[Annotated[str, Field(max_length=100)]],
})
AnalyticsTestFunnelOutputVariant2RecoveryOperation.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


AnalyticsTestFunnelOutputVariant2Recovery = TypedDict('AnalyticsTestFunnelOutputVariant2Recovery', {
    'idempotencyKey': NotRequired[Annotated[str, Field(max_length=512)]],
    'operationId': NotRequired[Annotated[str, Field(max_length=200)]],
    'runId': NotRequired[Annotated[str, Field(max_length=200)]],
    'jobId': NotRequired[Annotated[str, Field(max_length=200)]],
    'operation': NotRequired[AnalyticsTestFunnelOutputVariant2RecoveryOperation],
})
AnalyticsTestFunnelOutputVariant2Recovery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class AnalyticsTestFunnelOutputVariant2(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    delivery: AnalyticsTestFunnelOutputVariant2Delivery = Field(..., alias='delivery', description='')
    preview: str = Field(..., alias='preview', description='')
    scope: dict[str, Union[str, Union[float, int], bool, None]] = Field(..., alias='scope', description='')
    recovery: AnalyticsTestFunnelOutputVariant2Recovery = Field(..., alias='recovery', description='')


# Union schema: validate external payloads with TypeAdapter(AnalyticsTestFunnelOutput).
AnalyticsTestFunnelOutput = Union[AnalyticsTestFunnelOutputVariant2, AnalyticsTestFunnelOutputVariant1]

_AnalyticsTestFunnelInputAdapter = TypeAdapter(AnalyticsTestFunnelInput)
_AnalyticsTestFunnelOutputAdapter = TypeAdapter(AnalyticsTestFunnelOutput)