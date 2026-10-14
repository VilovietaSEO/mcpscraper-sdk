from typing import Annotated, Any, Literal, Union
from typing_extensions import NotRequired, Required, TypedDict
from pydantic import BaseModel, ConfigDict, Field, TypeAdapter


AnalyticsCreateEventDefinitionInputMetadata = TypedDict('AnalyticsCreateEventDefinitionInputMetadata', {
    'value': NotRequired[Annotated[Union[float, int], Field(ge=0, le=1000000000000)]],
    'currency': NotRequired[str],
    'orderId': NotRequired[Annotated[str, Field(min_length=1, max_length=200)]],
    'contentId': NotRequired[Annotated[str, Field(min_length=1, max_length=200)]],
    'contentType': NotRequired[Annotated[str, Field(min_length=1, max_length=80)]],
})
AnalyticsCreateEventDefinitionInputMetadata.__pydantic_config__ = ConfigDict(extra="allow", strict=False)


class AnalyticsCreateEventDefinitionInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=False)

    site_id: str = Field(..., alias='siteId', description='Analytics Site id returned by analytics_list_sites.')
    name: Annotated[str, Field(min_length=1, max_length=120)] = Field(..., alias='name', description='Human-readable definition name unique within the Site.')
    event_name: str = Field(..., alias='eventName', description='Canonical event name emitted when this definition matches.')
    trigger_kind: Literal['page', 'click', 'form', 'semantic'] = Field(..., alias='triggerKind', description='Declarative browser trigger. Semantic uses a data-xray-event tag.')
    path: Union[Annotated[str, Field(max_length=2000)], None] = Field(None, alias='path', description='URL path required for page triggers.')
    path_match: Union[Literal['exact', 'prefix'], None] = Field(None, alias='pathMatch', description='Whether the page path must equal or begin with path.')
    selector: Union[Annotated[str, Field(min_length=1, max_length=500)], None] = Field(None, alias='selector', description='CSS selector evaluated only by the first-party Pixel for click or form triggers.')
    hostnames: Union[Annotated[list[Annotated[str, Field(min_length=1, max_length=253)]], Field(max_length=25)], None] = Field(None, alias='hostnames', description='Optional approved bare hostnames. Empty applies across the Site Pixel hosts.')
    metadata: Union[AnalyticsCreateEventDefinitionInputMetadata, None] = Field(None, alias='metadata', description='Safe fixed event metadata; never form field values or arbitrary code.')
    once_per_session: Union[bool, None] = Field(None, alias='oncePerSession', description='Emit at most once per browser session when true.')
    enabled: Union[bool, None] = Field(None, alias='enabled', description='Whether the Pixel may emit this definition.')
    idempotency_key: Annotated[str, Field(min_length=8, max_length=160)] = Field(..., alias='idempotencyKey', description='Retry key; reuse only for this exact mutation.')


class AnalyticsCreateEventDefinitionOutputVariant1(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    ok: bool = Field(..., alias='ok', description='')
    definition: dict[str, Any] = Field(..., alias='definition', description='')


AnalyticsCreateEventDefinitionOutputVariant2DeliveryArtifactsItem = TypedDict('AnalyticsCreateEventDefinitionOutputVariant2DeliveryArtifactsItem', {
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
AnalyticsCreateEventDefinitionOutputVariant2DeliveryArtifactsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


AnalyticsCreateEventDefinitionOutputVariant2DeliveryStorageFailureVariant1 = TypedDict('AnalyticsCreateEventDefinitionOutputVariant2DeliveryStorageFailureVariant1', {
    'artifactId': Required[Union[str, None]],
    'outcome': Required[Literal['unknown', 'bytes-stored-metadata-pending', 'failed']],
})
AnalyticsCreateEventDefinitionOutputVariant2DeliveryStorageFailureVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


AnalyticsCreateEventDefinitionOutputVariant2Delivery = TypedDict('AnalyticsCreateEventDefinitionOutputVariant2Delivery', {
    'mode': Required[Literal['artifact']],
    'status': Required[Literal['complete', 'partial', 'unavailable']],
    'retainedRepresentation': Required[Literal['formatted-tool-result']],
    'sourceIsError': Required[bool],
    'artifacts': Required[list[AnalyticsCreateEventDefinitionOutputVariant2DeliveryArtifactsItem]],
    'downloadLinksOmitted': Required[bool],
    'scopeOmittedFields': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'storageFailure': Required[Union[AnalyticsCreateEventDefinitionOutputVariant2DeliveryStorageFailureVariant1, None]],
    'nextAction': Required[str],
})
AnalyticsCreateEventDefinitionOutputVariant2Delivery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


AnalyticsCreateEventDefinitionOutputVariant2RecoveryOperation = TypedDict('AnalyticsCreateEventDefinitionOutputVariant2RecoveryOperation', {
    'runId': Required[Union[Annotated[str, Field(max_length=200)], None]],
    'idempotencyKey': Required[Annotated[str, Field(max_length=512)]],
    'state': Required[Annotated[str, Field(max_length=100)]],
})
AnalyticsCreateEventDefinitionOutputVariant2RecoveryOperation.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


AnalyticsCreateEventDefinitionOutputVariant2Recovery = TypedDict('AnalyticsCreateEventDefinitionOutputVariant2Recovery', {
    'idempotencyKey': NotRequired[Annotated[str, Field(max_length=512)]],
    'operationId': NotRequired[Annotated[str, Field(max_length=200)]],
    'runId': NotRequired[Annotated[str, Field(max_length=200)]],
    'jobId': NotRequired[Annotated[str, Field(max_length=200)]],
    'operation': NotRequired[AnalyticsCreateEventDefinitionOutputVariant2RecoveryOperation],
})
AnalyticsCreateEventDefinitionOutputVariant2Recovery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class AnalyticsCreateEventDefinitionOutputVariant2(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    delivery: AnalyticsCreateEventDefinitionOutputVariant2Delivery = Field(..., alias='delivery', description='')
    preview: str = Field(..., alias='preview', description='')
    scope: dict[str, Union[str, Union[float, int], bool, None]] = Field(..., alias='scope', description='')
    recovery: AnalyticsCreateEventDefinitionOutputVariant2Recovery = Field(..., alias='recovery', description='')


# Union schema: validate external payloads with TypeAdapter(AnalyticsCreateEventDefinitionOutput).
AnalyticsCreateEventDefinitionOutput = Union[AnalyticsCreateEventDefinitionOutputVariant2, AnalyticsCreateEventDefinitionOutputVariant1]

_AnalyticsCreateEventDefinitionInputAdapter = TypeAdapter(AnalyticsCreateEventDefinitionInput)
_AnalyticsCreateEventDefinitionOutputAdapter = TypeAdapter(AnalyticsCreateEventDefinitionOutput)