from typing import Annotated, Any, Literal, Union
from typing_extensions import NotRequired, Required, TypedDict
from pydantic import BaseModel, ConfigDict, Field, TypeAdapter


AnalyticsUpdateEventDefinitionInputMetadataVariant1 = TypedDict('AnalyticsUpdateEventDefinitionInputMetadataVariant1', {
    'value': NotRequired[Annotated[Union[float, int], Field(ge=0, le=1000000000000)]],
    'currency': NotRequired[str],
    'orderId': NotRequired[Annotated[str, Field(min_length=1, max_length=200)]],
    'contentId': NotRequired[Annotated[str, Field(min_length=1, max_length=200)]],
    'contentType': NotRequired[Annotated[str, Field(min_length=1, max_length=80)]],
})
AnalyticsUpdateEventDefinitionInputMetadataVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=False)


class AnalyticsUpdateEventDefinitionInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=False)

    site_id: str = Field(..., alias='siteId', description='Analytics Site id returned by analytics_list_sites.')
    definition_id: str = Field(..., alias='definitionId', description='Event definition id returned by analytics_list_event_definitions.')
    name: Union[Annotated[str, Field(min_length=1, max_length=120)], None] = Field(None, alias='name', description='Human-readable definition name unique within the Site.')
    event_name: Union[str, None] = Field(None, alias='eventName', description='Canonical event name emitted when this definition matches.')
    trigger_kind: Union[Literal['page', 'click', 'form', 'semantic'], None] = Field(None, alias='triggerKind', description='Declarative browser trigger. Semantic uses a data-xray-event tag.')
    path: Union[Union[Annotated[str, Field(max_length=2000)], None], None] = Field(None, alias='path', description='Replacement page path; null clears it.')
    path_match: Union[Literal['exact', 'prefix'], None] = Field(None, alias='pathMatch', description='Replacement page path match mode.')
    selector: Union[Union[Annotated[str, Field(min_length=1, max_length=500)], None], None] = Field(None, alias='selector', description='Replacement browser-only selector; null clears it.')
    hostnames: Union[Annotated[list[Annotated[str, Field(min_length=1, max_length=253)]], Field(max_length=25)], None] = Field(None, alias='hostnames', description='Replacement approved bare-hostname scope.')
    metadata: Union[Union[AnalyticsUpdateEventDefinitionInputMetadataVariant1, None], None] = Field(None, alias='metadata', description='Replacement safe metadata; null clears it.')
    once_per_session: Union[bool, None] = Field(None, alias='oncePerSession', description='Replacement once-per-browser-session behavior.')
    enabled: Union[bool, None] = Field(None, alias='enabled', description='Replacement enabled state.')
    idempotency_key: Annotated[str, Field(min_length=8, max_length=160)] = Field(..., alias='idempotencyKey', description='Retry key; reuse only for this exact mutation.')


class AnalyticsUpdateEventDefinitionOutputVariant1(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    ok: bool = Field(..., alias='ok', description='')
    definition: dict[str, Any] = Field(..., alias='definition', description='')


AnalyticsUpdateEventDefinitionOutputVariant2DeliveryArtifactsItem = TypedDict('AnalyticsUpdateEventDefinitionOutputVariant2DeliveryArtifactsItem', {
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
AnalyticsUpdateEventDefinitionOutputVariant2DeliveryArtifactsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


AnalyticsUpdateEventDefinitionOutputVariant2DeliveryAvailableExportsItem = TypedDict('AnalyticsUpdateEventDefinitionOutputVariant2DeliveryAvailableExportsItem', {
    'artifactId': Required[str],
    'sourceArtifactId': Required[str],
    'filename': Required[Literal['result.md']],
    'contentType': Required[Literal['text/markdown; charset=utf-8']],
    'state': Required[Literal['on-demand']],
})
AnalyticsUpdateEventDefinitionOutputVariant2DeliveryAvailableExportsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


AnalyticsUpdateEventDefinitionOutputVariant2DeliveryStorageFailureVariant1 = TypedDict('AnalyticsUpdateEventDefinitionOutputVariant2DeliveryStorageFailureVariant1', {
    'artifactId': Required[Union[str, None]],
    'outcome': Required[Literal['unknown', 'bytes-stored-metadata-pending', 'failed']],
})
AnalyticsUpdateEventDefinitionOutputVariant2DeliveryStorageFailureVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


AnalyticsUpdateEventDefinitionOutputVariant2Delivery = TypedDict('AnalyticsUpdateEventDefinitionOutputVariant2Delivery', {
    'mode': Required[Literal['artifact']],
    'status': Required[Literal['complete', 'partial', 'unavailable']],
    'retainedRepresentation': Required[Literal['formatted-tool-result']],
    'sourceIsError': Required[bool],
    'artifacts': Required[list[AnalyticsUpdateEventDefinitionOutputVariant2DeliveryArtifactsItem]],
    'availableExports': NotRequired[list[AnalyticsUpdateEventDefinitionOutputVariant2DeliveryAvailableExportsItem]],
    'downloadLinksOmitted': Required[bool],
    'scopeOmittedFields': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'storageFailure': Required[Union[AnalyticsUpdateEventDefinitionOutputVariant2DeliveryStorageFailureVariant1, None]],
    'nextAction': Required[str],
})
AnalyticsUpdateEventDefinitionOutputVariant2Delivery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


AnalyticsUpdateEventDefinitionOutputVariant2RecoveryOperation = TypedDict('AnalyticsUpdateEventDefinitionOutputVariant2RecoveryOperation', {
    'runId': Required[Union[Annotated[str, Field(max_length=200)], None]],
    'idempotencyKey': Required[Annotated[str, Field(max_length=512)]],
    'state': Required[Annotated[str, Field(max_length=100)]],
})
AnalyticsUpdateEventDefinitionOutputVariant2RecoveryOperation.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


AnalyticsUpdateEventDefinitionOutputVariant2Recovery = TypedDict('AnalyticsUpdateEventDefinitionOutputVariant2Recovery', {
    'idempotencyKey': NotRequired[Annotated[str, Field(max_length=512)]],
    'operationId': NotRequired[Annotated[str, Field(max_length=200)]],
    'runId': NotRequired[Annotated[str, Field(max_length=200)]],
    'jobId': NotRequired[Annotated[str, Field(max_length=200)]],
    'operation': NotRequired[AnalyticsUpdateEventDefinitionOutputVariant2RecoveryOperation],
})
AnalyticsUpdateEventDefinitionOutputVariant2Recovery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class AnalyticsUpdateEventDefinitionOutputVariant2(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    delivery: AnalyticsUpdateEventDefinitionOutputVariant2Delivery = Field(..., alias='delivery', description='')
    preview: str = Field(..., alias='preview', description='')
    scope: dict[str, Union[str, Union[float, int], bool, None]] = Field(..., alias='scope', description='')
    recovery: AnalyticsUpdateEventDefinitionOutputVariant2Recovery = Field(..., alias='recovery', description='')


# Union schema: validate external payloads with TypeAdapter(AnalyticsUpdateEventDefinitionOutput).
AnalyticsUpdateEventDefinitionOutput = Union[AnalyticsUpdateEventDefinitionOutputVariant2, AnalyticsUpdateEventDefinitionOutputVariant1]

_AnalyticsUpdateEventDefinitionInputAdapter = TypeAdapter(AnalyticsUpdateEventDefinitionInput)
_AnalyticsUpdateEventDefinitionOutputAdapter = TypeAdapter(AnalyticsUpdateEventDefinitionOutput)