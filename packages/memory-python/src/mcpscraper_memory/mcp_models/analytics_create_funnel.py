from typing import Annotated, Any, Literal, Union
from typing_extensions import NotRequired, Required, TypedDict
from pydantic import BaseModel, ConfigDict, Field, TypeAdapter


AnalyticsCreateFunnelInputStagesItemRule = TypedDict('AnalyticsCreateFunnelInputStagesItemRule', {
    'eventNames': NotRequired[Annotated[list[str], Field(max_length=100)]],
    'conversionKinds': NotRequired[Annotated[list[str], Field(max_length=100)]],
    'externalEventNames': NotRequired[Annotated[list[str], Field(max_length=100)]],
})
AnalyticsCreateFunnelInputStagesItemRule.__pydantic_config__ = ConfigDict(extra="allow", strict=False)


AnalyticsCreateFunnelInputStagesItem = TypedDict('AnalyticsCreateFunnelInputStagesItem', {
    'key': Required[str],
    'label': Required[Annotated[str, Field(min_length=1, max_length=120)]],
    'rule': Required[AnalyticsCreateFunnelInputStagesItemRule],
})
AnalyticsCreateFunnelInputStagesItem.__pydantic_config__ = ConfigDict(extra="allow", strict=False)


class AnalyticsCreateFunnelInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=False)

    site_id: str = Field(..., alias='siteId', description='Analytics Site id returned by analytics_list_sites.')
    name: Annotated[str, Field(min_length=1, max_length=120)] = Field(..., alias='name', description='Human-readable funnel name.')
    stages: Annotated[list[AnalyticsCreateFunnelInputStagesItem], Field(min_length=2, max_length=20)] = Field(..., alias='stages', description='Ordered stage definitions.')
    is_default: Union[bool, None] = Field(None, alias='isDefault', description='Make this version the Site default.')
    status: Union[Literal['active', 'disabled'], None] = Field(None, alias='status', description='Initial funnel status.')
    idempotency_key: Annotated[str, Field(min_length=8, max_length=160)] = Field(..., alias='idempotencyKey', description='Caller-owned idempotency key. Reuse it only when retrying the same logical mutation.')


class AnalyticsCreateFunnelOutputVariant1(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    ok: bool = Field(..., alias='ok', description='')
    definition: dict[str, Any] = Field(..., alias='definition', description='')


AnalyticsCreateFunnelOutputVariant2DeliveryArtifactsItem = TypedDict('AnalyticsCreateFunnelOutputVariant2DeliveryArtifactsItem', {
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
AnalyticsCreateFunnelOutputVariant2DeliveryArtifactsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


AnalyticsCreateFunnelOutputVariant2DeliveryStorageFailureVariant1 = TypedDict('AnalyticsCreateFunnelOutputVariant2DeliveryStorageFailureVariant1', {
    'artifactId': Required[Union[str, None]],
    'outcome': Required[Literal['unknown', 'bytes-stored-metadata-pending', 'failed']],
})
AnalyticsCreateFunnelOutputVariant2DeliveryStorageFailureVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


AnalyticsCreateFunnelOutputVariant2Delivery = TypedDict('AnalyticsCreateFunnelOutputVariant2Delivery', {
    'mode': Required[Literal['artifact']],
    'status': Required[Literal['complete', 'partial', 'unavailable']],
    'retainedRepresentation': Required[Literal['formatted-tool-result']],
    'sourceIsError': Required[bool],
    'artifacts': Required[list[AnalyticsCreateFunnelOutputVariant2DeliveryArtifactsItem]],
    'downloadLinksOmitted': Required[bool],
    'scopeOmittedFields': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'storageFailure': Required[Union[AnalyticsCreateFunnelOutputVariant2DeliveryStorageFailureVariant1, None]],
    'nextAction': Required[str],
})
AnalyticsCreateFunnelOutputVariant2Delivery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


AnalyticsCreateFunnelOutputVariant2RecoveryOperation = TypedDict('AnalyticsCreateFunnelOutputVariant2RecoveryOperation', {
    'runId': Required[Union[Annotated[str, Field(max_length=200)], None]],
    'idempotencyKey': Required[Annotated[str, Field(max_length=512)]],
    'state': Required[Annotated[str, Field(max_length=100)]],
})
AnalyticsCreateFunnelOutputVariant2RecoveryOperation.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


AnalyticsCreateFunnelOutputVariant2Recovery = TypedDict('AnalyticsCreateFunnelOutputVariant2Recovery', {
    'idempotencyKey': NotRequired[Annotated[str, Field(max_length=512)]],
    'operationId': NotRequired[Annotated[str, Field(max_length=200)]],
    'runId': NotRequired[Annotated[str, Field(max_length=200)]],
    'jobId': NotRequired[Annotated[str, Field(max_length=200)]],
    'operation': NotRequired[AnalyticsCreateFunnelOutputVariant2RecoveryOperation],
})
AnalyticsCreateFunnelOutputVariant2Recovery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class AnalyticsCreateFunnelOutputVariant2(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    delivery: AnalyticsCreateFunnelOutputVariant2Delivery = Field(..., alias='delivery', description='')
    preview: str = Field(..., alias='preview', description='')
    scope: dict[str, Union[str, Union[float, int], bool, None]] = Field(..., alias='scope', description='')
    recovery: AnalyticsCreateFunnelOutputVariant2Recovery = Field(..., alias='recovery', description='')


# Union schema: validate external payloads with TypeAdapter(AnalyticsCreateFunnelOutput).
AnalyticsCreateFunnelOutput = Union[AnalyticsCreateFunnelOutputVariant2, AnalyticsCreateFunnelOutputVariant1]

_AnalyticsCreateFunnelInputAdapter = TypeAdapter(AnalyticsCreateFunnelInput)
_AnalyticsCreateFunnelOutputAdapter = TypeAdapter(AnalyticsCreateFunnelOutput)