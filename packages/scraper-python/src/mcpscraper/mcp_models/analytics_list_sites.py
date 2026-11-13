from typing import Annotated, Any, Literal, Union
from typing_extensions import NotRequired, Required, TypedDict
from pydantic import BaseModel, ConfigDict, Field, TypeAdapter


class AnalyticsListSitesInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=False)



AnalyticsListSitesOutputVariant1SitesItem = TypedDict('AnalyticsListSitesOutputVariant1SitesItem', {
    'id': Required[str],
    'slug': Required[str],
    'name': Required[str],
    'timezone': Required[str],
    'status': Required[str],
    'role': Required[Literal['viewer', 'editor', 'owner']],
    'pixel_count': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'last_event_at': Required[Union[str, None]],
})
AnalyticsListSitesOutputVariant1SitesItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class AnalyticsListSitesOutputVariant1(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    ok: bool = Field(..., alias='ok', description='')
    sites: list[AnalyticsListSitesOutputVariant1SitesItem] = Field(..., alias='sites', description='')


AnalyticsListSitesOutputVariant2DeliveryArtifactsItem = TypedDict('AnalyticsListSitesOutputVariant2DeliveryArtifactsItem', {
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
AnalyticsListSitesOutputVariant2DeliveryArtifactsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


AnalyticsListSitesOutputVariant2DeliveryAvailableExportsItem = TypedDict('AnalyticsListSitesOutputVariant2DeliveryAvailableExportsItem', {
    'artifactId': Required[str],
    'sourceArtifactId': Required[str],
    'filename': Required[Literal['result.md']],
    'contentType': Required[Literal['text/markdown; charset=utf-8']],
    'state': Required[Literal['on-demand']],
})
AnalyticsListSitesOutputVariant2DeliveryAvailableExportsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


AnalyticsListSitesOutputVariant2DeliveryStorageFailureVariant1 = TypedDict('AnalyticsListSitesOutputVariant2DeliveryStorageFailureVariant1', {
    'artifactId': Required[Union[str, None]],
    'outcome': Required[Literal['unknown', 'bytes-stored-metadata-pending', 'failed']],
})
AnalyticsListSitesOutputVariant2DeliveryStorageFailureVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


AnalyticsListSitesOutputVariant2Delivery = TypedDict('AnalyticsListSitesOutputVariant2Delivery', {
    'mode': Required[Literal['artifact']],
    'status': Required[Literal['complete', 'partial', 'unavailable']],
    'retainedRepresentation': Required[Literal['formatted-tool-result']],
    'sourceIsError': Required[bool],
    'artifacts': Required[list[AnalyticsListSitesOutputVariant2DeliveryArtifactsItem]],
    'availableExports': NotRequired[list[AnalyticsListSitesOutputVariant2DeliveryAvailableExportsItem]],
    'downloadLinksOmitted': Required[bool],
    'scopeOmittedFields': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'storageFailure': Required[Union[AnalyticsListSitesOutputVariant2DeliveryStorageFailureVariant1, None]],
    'nextAction': Required[str],
})
AnalyticsListSitesOutputVariant2Delivery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


AnalyticsListSitesOutputVariant2RecoveryOperation = TypedDict('AnalyticsListSitesOutputVariant2RecoveryOperation', {
    'runId': Required[Union[Annotated[str, Field(max_length=200)], None]],
    'idempotencyKey': Required[Annotated[str, Field(max_length=512)]],
    'state': Required[Annotated[str, Field(max_length=100)]],
})
AnalyticsListSitesOutputVariant2RecoveryOperation.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


AnalyticsListSitesOutputVariant2Recovery = TypedDict('AnalyticsListSitesOutputVariant2Recovery', {
    'idempotencyKey': NotRequired[Annotated[str, Field(max_length=512)]],
    'operationId': NotRequired[Annotated[str, Field(max_length=200)]],
    'runId': NotRequired[Annotated[str, Field(max_length=200)]],
    'jobId': NotRequired[Annotated[str, Field(max_length=200)]],
    'operation': NotRequired[AnalyticsListSitesOutputVariant2RecoveryOperation],
})
AnalyticsListSitesOutputVariant2Recovery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class AnalyticsListSitesOutputVariant2(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    delivery: AnalyticsListSitesOutputVariant2Delivery = Field(..., alias='delivery', description='')
    preview: str = Field(..., alias='preview', description='')
    scope: dict[str, Union[str, Union[float, int], bool, None]] = Field(..., alias='scope', description='')
    recovery: AnalyticsListSitesOutputVariant2Recovery = Field(..., alias='recovery', description='')


# Union schema: validate external payloads with TypeAdapter(AnalyticsListSitesOutput).
AnalyticsListSitesOutput = Union[AnalyticsListSitesOutputVariant2, AnalyticsListSitesOutputVariant1]

_AnalyticsListSitesInputAdapter = TypeAdapter(AnalyticsListSitesInput)
_AnalyticsListSitesOutputAdapter = TypeAdapter(AnalyticsListSitesOutput)