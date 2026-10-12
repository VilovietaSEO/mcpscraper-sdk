from typing import Annotated, Any, Literal, Union
from typing_extensions import NotRequired, Required, TypedDict
from pydantic import BaseModel, ConfigDict, Field, TypeAdapter


AnalyticsCreateLeadScoreInputGroupsItemPredicatesItemVariant1 = TypedDict('AnalyticsCreateLeadScoreInputGroupsItemPredicatesItemVariant1', {
    'kind': Required[Literal['event_completed']],
    'eventName': Required[Annotated[str, Field(min_length=1, max_length=160)]],
    'withinDays': NotRequired[Annotated[int, Field(ge=1, le=3650)]],
})
AnalyticsCreateLeadScoreInputGroupsItemPredicatesItemVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=False)


AnalyticsCreateLeadScoreInputGroupsItemPredicatesItemVariant2 = TypedDict('AnalyticsCreateLeadScoreInputGroupsItemPredicatesItemVariant2', {
    'kind': Required[Literal['event_frequency']],
    'eventName': Required[Annotated[str, Field(min_length=1, max_length=160)]],
    'minimum': Required[Annotated[int, Field(ge=1, le=1000)]],
    'withinDays': NotRequired[Annotated[int, Field(ge=1, le=3650)]],
})
AnalyticsCreateLeadScoreInputGroupsItemPredicatesItemVariant2.__pydantic_config__ = ConfigDict(extra="allow", strict=False)


AnalyticsCreateLeadScoreInputGroupsItemPredicatesItemVariant3 = TypedDict('AnalyticsCreateLeadScoreInputGroupsItemPredicatesItemVariant3', {
    'kind': Required[Literal['event_recency']],
    'eventName': Required[Annotated[str, Field(min_length=1, max_length=160)]],
    'withinDays': Required[Annotated[int, Field(ge=1, le=3650)]],
})
AnalyticsCreateLeadScoreInputGroupsItemPredicatesItemVariant3.__pydantic_config__ = ConfigDict(extra="allow", strict=False)


AnalyticsCreateLeadScoreInputGroupsItemPredicatesItemVariant4 = TypedDict('AnalyticsCreateLeadScoreInputGroupsItemPredicatesItemVariant4', {
    'kind': Required[Literal['page_visited']],
    'path': Required[Annotated[str, Field(max_length=2000)]],
    'withinDays': NotRequired[Annotated[int, Field(ge=1, le=3650)]],
})
AnalyticsCreateLeadScoreInputGroupsItemPredicatesItemVariant4.__pydantic_config__ = ConfigDict(extra="allow", strict=False)


AnalyticsCreateLeadScoreInputGroupsItemPredicatesItemVariant5 = TypedDict('AnalyticsCreateLeadScoreInputGroupsItemPredicatesItemVariant5', {
    'kind': Required[Literal['referrer_equals']],
    'value': Required[Annotated[str, Field(min_length=1, max_length=500)]],
})
AnalyticsCreateLeadScoreInputGroupsItemPredicatesItemVariant5.__pydantic_config__ = ConfigDict(extra="allow", strict=False)


AnalyticsCreateLeadScoreInputGroupsItemPredicatesItemVariant6 = TypedDict('AnalyticsCreateLeadScoreInputGroupsItemPredicatesItemVariant6', {
    'kind': Required[Literal['source_equals']],
    'value': Required[Annotated[str, Field(min_length=1, max_length=180)]],
})
AnalyticsCreateLeadScoreInputGroupsItemPredicatesItemVariant6.__pydantic_config__ = ConfigDict(extra="allow", strict=False)


AnalyticsCreateLeadScoreInputGroupsItemPredicatesItemVariant7 = TypedDict('AnalyticsCreateLeadScoreInputGroupsItemPredicatesItemVariant7', {
    'kind': Required[Literal['call_outcome']],
    'outcome': Required[Annotated[str, Field(min_length=1, max_length=160)]],
    'withinDays': NotRequired[Annotated[int, Field(ge=1, le=3650)]],
})
AnalyticsCreateLeadScoreInputGroupsItemPredicatesItemVariant7.__pydantic_config__ = ConfigDict(extra="allow", strict=False)


AnalyticsCreateLeadScoreInputGroupsItemPredicatesItemVariant8 = TypedDict('AnalyticsCreateLeadScoreInputGroupsItemPredicatesItemVariant8', {
    'kind': Required[Literal['crm_stage']],
    'stage': Required[Annotated[str, Field(min_length=1, max_length=160)]],
})
AnalyticsCreateLeadScoreInputGroupsItemPredicatesItemVariant8.__pydantic_config__ = ConfigDict(extra="allow", strict=False)


AnalyticsCreateLeadScoreInputGroupsItemPredicatesItemVariant9 = TypedDict('AnalyticsCreateLeadScoreInputGroupsItemPredicatesItemVariant9', {
    'kind': Required[Literal['property_equals']],
    'property': Required[Annotated[str, Field(min_length=1, max_length=160)]],
    'value': Required[Union[Annotated[str, Field(max_length=500)], Union[float, int], bool]],
})
AnalyticsCreateLeadScoreInputGroupsItemPredicatesItemVariant9.__pydantic_config__ = ConfigDict(extra="allow", strict=False)


AnalyticsCreateLeadScoreInputGroupsItemPredicatesItemVariant10 = TypedDict('AnalyticsCreateLeadScoreInputGroupsItemPredicatesItemVariant10', {
    'kind': Required[Literal['property_present']],
    'property': Required[Annotated[str, Field(min_length=1, max_length=160)]],
})
AnalyticsCreateLeadScoreInputGroupsItemPredicatesItemVariant10.__pydantic_config__ = ConfigDict(extra="allow", strict=False)


AnalyticsCreateLeadScoreInputGroupsItem = TypedDict('AnalyticsCreateLeadScoreInputGroupsItem', {
    'id': Required[Annotated[str, Field(min_length=1, max_length=160)]],
    'label': Required[Annotated[str, Field(min_length=1, max_length=160)]],
    'operation': Required[Literal['add', 'subtract']],
    'points': Required[Annotated[int, Field(ge=0, le=10000)]],
    'cap': NotRequired[Annotated[int, Field(ge=0, le=10000)]],
    'predicates': Required[Annotated[list[Union[AnalyticsCreateLeadScoreInputGroupsItemPredicatesItemVariant1, AnalyticsCreateLeadScoreInputGroupsItemPredicatesItemVariant2, AnalyticsCreateLeadScoreInputGroupsItemPredicatesItemVariant3, AnalyticsCreateLeadScoreInputGroupsItemPredicatesItemVariant4, AnalyticsCreateLeadScoreInputGroupsItemPredicatesItemVariant5, AnalyticsCreateLeadScoreInputGroupsItemPredicatesItemVariant6, AnalyticsCreateLeadScoreInputGroupsItemPredicatesItemVariant7, AnalyticsCreateLeadScoreInputGroupsItemPredicatesItemVariant8, AnalyticsCreateLeadScoreInputGroupsItemPredicatesItemVariant9, AnalyticsCreateLeadScoreInputGroupsItemPredicatesItemVariant10]], Field(min_length=1, max_length=20)]],
})
AnalyticsCreateLeadScoreInputGroupsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=False)


class AnalyticsCreateLeadScoreInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=False)

    site_id: str = Field(..., alias='siteId', description='Analytics Site id returned by analytics_list_sites.')
    namespace_id: Annotated[str, Field(min_length=1, max_length=160)] = Field(..., alias='namespaceId', description='Identity Namespace belonging to this Site.')
    name: Annotated[str, Field(min_length=1, max_length=120)] = Field(..., alias='name', description='Lead-score name.')
    kind: Literal['fit', 'engagement', 'combined'] = Field(..., alias='kind', description='Score purpose; a score is not a probability or currency value.')
    target_object: Literal['person', 'visitor'] = Field(..., alias='targetObject', description='Object the score evaluates.')
    minimum: Union[Annotated[int, Field(ge=-100000, le=100000)], None] = Field(None, alias='minimum', description='Overall lower bound.')
    maximum: Union[Annotated[int, Field(ge=-100000, le=100000)], None] = Field(None, alias='maximum', description='Overall upper bound.')
    groups: Annotated[list[AnalyticsCreateLeadScoreInputGroupsItem], Field(min_length=1, max_length=40)] = Field(..., alias='groups', description='Declarative score groups.')
    permitted_properties: Union[Annotated[list[Annotated[str, Field(min_length=1, max_length=160)]], Field(max_length=200)], None] = Field(None, alias='permittedProperties', description='Explicit property allowlist used by property predicates.')
    enabled: Union[bool, None] = Field(None, alias='enabled', description='Whether this version may evaluate.')
    idempotency_key: Annotated[str, Field(min_length=8, max_length=160)] = Field(..., alias='idempotencyKey', description='Caller-owned idempotency key. Reuse it only when retrying the same logical mutation.')


class AnalyticsCreateLeadScoreOutputVariant1(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    ok: bool = Field(..., alias='ok', description='')
    score: dict[str, Any] = Field(..., alias='score', description='')


AnalyticsCreateLeadScoreOutputVariant2DeliveryArtifactsItem = TypedDict('AnalyticsCreateLeadScoreOutputVariant2DeliveryArtifactsItem', {
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
AnalyticsCreateLeadScoreOutputVariant2DeliveryArtifactsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


AnalyticsCreateLeadScoreOutputVariant2DeliveryStorageFailureVariant1 = TypedDict('AnalyticsCreateLeadScoreOutputVariant2DeliveryStorageFailureVariant1', {
    'artifactId': Required[Union[str, None]],
    'outcome': Required[Literal['unknown', 'bytes-stored-metadata-pending', 'failed']],
})
AnalyticsCreateLeadScoreOutputVariant2DeliveryStorageFailureVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


AnalyticsCreateLeadScoreOutputVariant2Delivery = TypedDict('AnalyticsCreateLeadScoreOutputVariant2Delivery', {
    'mode': Required[Literal['artifact']],
    'status': Required[Literal['complete', 'partial', 'unavailable']],
    'retainedRepresentation': Required[Literal['formatted-tool-result']],
    'sourceIsError': Required[bool],
    'artifacts': Required[list[AnalyticsCreateLeadScoreOutputVariant2DeliveryArtifactsItem]],
    'downloadLinksOmitted': Required[bool],
    'scopeOmittedFields': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'storageFailure': Required[Union[AnalyticsCreateLeadScoreOutputVariant2DeliveryStorageFailureVariant1, None]],
    'nextAction': Required[str],
})
AnalyticsCreateLeadScoreOutputVariant2Delivery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


AnalyticsCreateLeadScoreOutputVariant2RecoveryOperation = TypedDict('AnalyticsCreateLeadScoreOutputVariant2RecoveryOperation', {
    'runId': Required[Union[Annotated[str, Field(max_length=200)], None]],
    'idempotencyKey': Required[Annotated[str, Field(max_length=512)]],
    'state': Required[Annotated[str, Field(max_length=100)]],
})
AnalyticsCreateLeadScoreOutputVariant2RecoveryOperation.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


AnalyticsCreateLeadScoreOutputVariant2Recovery = TypedDict('AnalyticsCreateLeadScoreOutputVariant2Recovery', {
    'idempotencyKey': NotRequired[Annotated[str, Field(max_length=512)]],
    'operationId': NotRequired[Annotated[str, Field(max_length=200)]],
    'runId': NotRequired[Annotated[str, Field(max_length=200)]],
    'jobId': NotRequired[Annotated[str, Field(max_length=200)]],
    'operation': NotRequired[AnalyticsCreateLeadScoreOutputVariant2RecoveryOperation],
})
AnalyticsCreateLeadScoreOutputVariant2Recovery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class AnalyticsCreateLeadScoreOutputVariant2(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    delivery: AnalyticsCreateLeadScoreOutputVariant2Delivery = Field(..., alias='delivery', description='')
    preview: str = Field(..., alias='preview', description='')
    scope: dict[str, Union[str, Union[float, int], bool, None]] = Field(..., alias='scope', description='')
    recovery: AnalyticsCreateLeadScoreOutputVariant2Recovery = Field(..., alias='recovery', description='')


# Union schema: validate external payloads with TypeAdapter(AnalyticsCreateLeadScoreOutput).
AnalyticsCreateLeadScoreOutput = Union[AnalyticsCreateLeadScoreOutputVariant2, AnalyticsCreateLeadScoreOutputVariant1]

_AnalyticsCreateLeadScoreInputAdapter = TypeAdapter(AnalyticsCreateLeadScoreInput)
_AnalyticsCreateLeadScoreOutputAdapter = TypeAdapter(AnalyticsCreateLeadScoreOutput)