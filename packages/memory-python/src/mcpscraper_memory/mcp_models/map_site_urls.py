from typing import Annotated, Any, Literal, Union
from typing_extensions import NotRequired, Required, TypedDict
from pydantic import BaseModel, ConfigDict, Field, TypeAdapter


class MapSiteUrlsInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=False)

    url: Annotated[str, Field(min_length=1)] = Field(..., alias='url', description='Public website URL or domain to crawl for internal URLs. Bare domains default to https://. Use before extract_site when the user asks to audit/map/crawl a site.')
    max_urls: Union[Annotated[int, Field(ge=1, le=10000)], None] = Field(None, alias='maxUrls', description='Maximum URLs to discover. Use 100 for normal maps, up to 10000 for a full inventory. Large maps (over 500 URLs) write the complete inventory to a local file and return only a summary plus the file path instead of the full list inline.')
    delivery: Union[Literal['auto', 'inline', 'artifact'], None] = Field(None, alias='delivery', description='auto returns a bounded inline map and offloads large inventories; inline requests bounded inline delivery but still offloads above the hard context limit; artifact always creates an owner-scoped report artifact.')


MapSiteUrlsOutputVariant1UrlsItem = TypedDict('MapSiteUrlsOutputVariant1UrlsItem', {
    'url': Required[str],
    'status': Required[Union[Annotated[int, Field(ge=-9007199254740991, le=9007199254740991)], None]],
})
MapSiteUrlsOutputVariant1UrlsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


MapSiteUrlsOutputVariant1Artifact = TypedDict('MapSiteUrlsOutputVariant1Artifact', {
    'artifactId': Required[str],
    'bytes': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'expiresAt': Required[str],
    'preview': Required[str],
})
MapSiteUrlsOutputVariant1Artifact.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


MapSiteUrlsOutputVariant1Delivery = TypedDict('MapSiteUrlsOutputVariant1Delivery', {
    'requested': Required[Literal['auto', 'inline', 'artifact']],
    'effective': Required[Literal['inline', 'artifact']],
    'retained': Required[bool],
    'nextAction': Required[Union[str, None]],
})
MapSiteUrlsOutputVariant1Delivery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class MapSiteUrlsOutputVariant1(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    start_url: str = Field(..., alias='startUrl', description='')
    total_found: Annotated[int, Field(ge=0, le=9007199254740991)] = Field(..., alias='totalFound', description='')
    truncated: bool = Field(..., alias='truncated', description='')
    ok_count: Annotated[int, Field(ge=0, le=9007199254740991)] = Field(..., alias='okCount', description='')
    redirect_count: Annotated[int, Field(ge=0, le=9007199254740991)] = Field(..., alias='redirectCount', description='')
    broken_count: Annotated[int, Field(ge=0, le=9007199254740991)] = Field(..., alias='brokenCount', description='')
    urls: list[MapSiteUrlsOutputVariant1UrlsItem] = Field(..., alias='urls', description='')
    duration_ms: Annotated[Union[float, int], Field(ge=0)] = Field(..., alias='durationMs', description='')
    truncated_count: Union[Annotated[int, Field(ge=0, le=9007199254740991)], None] = Field(None, alias='truncatedCount', description='')
    artifact: Union[MapSiteUrlsOutputVariant1Artifact, None] = Field(None, alias='artifact', description='')
    delivery: MapSiteUrlsOutputVariant1Delivery = Field(..., alias='delivery', description='')


MapSiteUrlsOutputVariant2DeliveryArtifactsItem = TypedDict('MapSiteUrlsOutputVariant2DeliveryArtifactsItem', {
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
MapSiteUrlsOutputVariant2DeliveryArtifactsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


MapSiteUrlsOutputVariant2DeliveryStorageFailureVariant1 = TypedDict('MapSiteUrlsOutputVariant2DeliveryStorageFailureVariant1', {
    'artifactId': Required[Union[str, None]],
    'outcome': Required[Literal['unknown', 'bytes-stored-metadata-pending', 'failed']],
})
MapSiteUrlsOutputVariant2DeliveryStorageFailureVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


MapSiteUrlsOutputVariant2Delivery = TypedDict('MapSiteUrlsOutputVariant2Delivery', {
    'mode': Required[Literal['artifact']],
    'status': Required[Literal['complete', 'partial', 'unavailable']],
    'retainedRepresentation': Required[Literal['formatted-tool-result']],
    'sourceIsError': Required[bool],
    'artifacts': Required[list[MapSiteUrlsOutputVariant2DeliveryArtifactsItem]],
    'downloadLinksOmitted': Required[bool],
    'scopeOmittedFields': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'storageFailure': Required[Union[MapSiteUrlsOutputVariant2DeliveryStorageFailureVariant1, None]],
    'nextAction': Required[str],
})
MapSiteUrlsOutputVariant2Delivery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


MapSiteUrlsOutputVariant2RecoveryOperation = TypedDict('MapSiteUrlsOutputVariant2RecoveryOperation', {
    'runId': Required[Union[Annotated[str, Field(max_length=200)], None]],
    'idempotencyKey': Required[Annotated[str, Field(max_length=512)]],
    'state': Required[Annotated[str, Field(max_length=100)]],
})
MapSiteUrlsOutputVariant2RecoveryOperation.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


MapSiteUrlsOutputVariant2Recovery = TypedDict('MapSiteUrlsOutputVariant2Recovery', {
    'idempotencyKey': NotRequired[Annotated[str, Field(max_length=512)]],
    'operationId': NotRequired[Annotated[str, Field(max_length=200)]],
    'runId': NotRequired[Annotated[str, Field(max_length=200)]],
    'jobId': NotRequired[Annotated[str, Field(max_length=200)]],
    'operation': NotRequired[MapSiteUrlsOutputVariant2RecoveryOperation],
})
MapSiteUrlsOutputVariant2Recovery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class MapSiteUrlsOutputVariant2(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    delivery: MapSiteUrlsOutputVariant2Delivery = Field(..., alias='delivery', description='')
    preview: str = Field(..., alias='preview', description='')
    scope: dict[str, Union[str, Union[float, int], bool, None]] = Field(..., alias='scope', description='')
    recovery: MapSiteUrlsOutputVariant2Recovery = Field(..., alias='recovery', description='')


# Union schema: validate external payloads with TypeAdapter(MapSiteUrlsOutput).
MapSiteUrlsOutput = Union[MapSiteUrlsOutputVariant1, MapSiteUrlsOutputVariant2]

_MapSiteUrlsInputAdapter = TypeAdapter(MapSiteUrlsInput)
_MapSiteUrlsOutputAdapter = TypeAdapter(MapSiteUrlsOutput)