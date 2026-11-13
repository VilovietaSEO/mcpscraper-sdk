from typing import Annotated, Any, Literal, Union
from typing_extensions import NotRequired, Required, TypedDict
from pydantic import BaseModel, ConfigDict, Field, TypeAdapter


class AnalyticsTestEventDefinitionInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=False)

    site_id: str = Field(..., alias='siteId', description='Analytics Site id returned by analytics_list_sites.')
    definition_id: str = Field(..., alias='definitionId', description='Event definition id returned by analytics_list_event_definitions.')
    hostname: Annotated[str, Field(min_length=1, max_length=253)] = Field(..., alias='hostname', description='Bare hostname observed by the browser.')
    path: Annotated[str, Field(max_length=2000)] = Field(..., alias='path', description='URL path observed by the browser.')
    trigger_kind: Literal['page', 'click', 'form', 'semantic'] = Field(..., alias='triggerKind', description='Trigger interaction being previewed.')
    tag_event_name: Union[str, None] = Field(None, alias='tagEventName', description='Validated data-xray-event name observed by the browser.')
    selector_matched: Union[bool, None] = Field(None, alias='selectorMatched', description='The browser-reported match result. The server never receives HTML or evaluates a selector.')


class AnalyticsTestEventDefinitionOutputVariant1(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    ok: bool = Field(..., alias='ok', description='')
    test: dict[str, Any] = Field(..., alias='test', description='')


AnalyticsTestEventDefinitionOutputVariant2DeliveryArtifactsItem = TypedDict('AnalyticsTestEventDefinitionOutputVariant2DeliveryArtifactsItem', {
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
AnalyticsTestEventDefinitionOutputVariant2DeliveryArtifactsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


AnalyticsTestEventDefinitionOutputVariant2DeliveryAvailableExportsItem = TypedDict('AnalyticsTestEventDefinitionOutputVariant2DeliveryAvailableExportsItem', {
    'artifactId': Required[str],
    'sourceArtifactId': Required[str],
    'filename': Required[Literal['result.md']],
    'contentType': Required[Literal['text/markdown; charset=utf-8']],
    'state': Required[Literal['on-demand']],
})
AnalyticsTestEventDefinitionOutputVariant2DeliveryAvailableExportsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


AnalyticsTestEventDefinitionOutputVariant2DeliveryStorageFailureVariant1 = TypedDict('AnalyticsTestEventDefinitionOutputVariant2DeliveryStorageFailureVariant1', {
    'artifactId': Required[Union[str, None]],
    'outcome': Required[Literal['unknown', 'bytes-stored-metadata-pending', 'failed']],
})
AnalyticsTestEventDefinitionOutputVariant2DeliveryStorageFailureVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


AnalyticsTestEventDefinitionOutputVariant2Delivery = TypedDict('AnalyticsTestEventDefinitionOutputVariant2Delivery', {
    'mode': Required[Literal['artifact']],
    'status': Required[Literal['complete', 'partial', 'unavailable']],
    'retainedRepresentation': Required[Literal['formatted-tool-result']],
    'sourceIsError': Required[bool],
    'artifacts': Required[list[AnalyticsTestEventDefinitionOutputVariant2DeliveryArtifactsItem]],
    'availableExports': NotRequired[list[AnalyticsTestEventDefinitionOutputVariant2DeliveryAvailableExportsItem]],
    'downloadLinksOmitted': Required[bool],
    'scopeOmittedFields': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'storageFailure': Required[Union[AnalyticsTestEventDefinitionOutputVariant2DeliveryStorageFailureVariant1, None]],
    'nextAction': Required[str],
})
AnalyticsTestEventDefinitionOutputVariant2Delivery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


AnalyticsTestEventDefinitionOutputVariant2RecoveryOperation = TypedDict('AnalyticsTestEventDefinitionOutputVariant2RecoveryOperation', {
    'runId': Required[Union[Annotated[str, Field(max_length=200)], None]],
    'idempotencyKey': Required[Annotated[str, Field(max_length=512)]],
    'state': Required[Annotated[str, Field(max_length=100)]],
})
AnalyticsTestEventDefinitionOutputVariant2RecoveryOperation.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


AnalyticsTestEventDefinitionOutputVariant2Recovery = TypedDict('AnalyticsTestEventDefinitionOutputVariant2Recovery', {
    'idempotencyKey': NotRequired[Annotated[str, Field(max_length=512)]],
    'operationId': NotRequired[Annotated[str, Field(max_length=200)]],
    'runId': NotRequired[Annotated[str, Field(max_length=200)]],
    'jobId': NotRequired[Annotated[str, Field(max_length=200)]],
    'operation': NotRequired[AnalyticsTestEventDefinitionOutputVariant2RecoveryOperation],
})
AnalyticsTestEventDefinitionOutputVariant2Recovery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class AnalyticsTestEventDefinitionOutputVariant2(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    delivery: AnalyticsTestEventDefinitionOutputVariant2Delivery = Field(..., alias='delivery', description='')
    preview: str = Field(..., alias='preview', description='')
    scope: dict[str, Union[str, Union[float, int], bool, None]] = Field(..., alias='scope', description='')
    recovery: AnalyticsTestEventDefinitionOutputVariant2Recovery = Field(..., alias='recovery', description='')


# Union schema: validate external payloads with TypeAdapter(AnalyticsTestEventDefinitionOutput).
AnalyticsTestEventDefinitionOutput = Union[AnalyticsTestEventDefinitionOutputVariant2, AnalyticsTestEventDefinitionOutputVariant1]

_AnalyticsTestEventDefinitionInputAdapter = TypeAdapter(AnalyticsTestEventDefinitionInput)
_AnalyticsTestEventDefinitionOutputAdapter = TypeAdapter(AnalyticsTestEventDefinitionOutput)