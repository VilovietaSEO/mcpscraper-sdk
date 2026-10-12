from typing import Annotated, Any, Literal, Union
from typing_extensions import NotRequired, Required, TypedDict
from pydantic import BaseModel, ConfigDict, Field, TypeAdapter


ExtractSiteInputWayback = TypedDict('ExtractSiteInputWayback', {
    'months': NotRequired[Annotated[list[str], Field(min_length=1, max_length=60)]],
    'from': NotRequired[str],
    'to': NotRequired[str],
    'intervalMonths': NotRequired[Annotated[int, Field(ge=1, le=12)]],
    'urls': NotRequired[Annotated[list[str], Field(min_length=1, max_length=100)]],
})
ExtractSiteInputWayback.__pydantic_config__ = ConfigDict(extra="allow", strict=False)


class ExtractSiteInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=False)

    url: Annotated[str, Field(min_length=1)] = Field(..., alias='url', description='Public website URL/domain or web.archive.org replay URL. Without wayback, this crawls live content or one archived site snapshot. With wayback, it creates a multi-month archive timeline.')
    max_pages: Union[Annotated[int, Field(ge=1, le=10000)], None] = Field(None, alias='maxPages', description='Maximum pages per Wayback month, or maximum total pages for a normal crawl. Multi-month jobs remain capped at 10,000 total captures and 500 pages per month.')
    wayback: Union[ExtractSiteInputWayback, None] = Field(None, alias='wayback', description='Optional temporal archive plan. Provide explicit YYYY-MM months or a from/to range plus intervalMonths. Omit urls for whole-site monthly snapshots, provide one URL for a single-page timeline, or several URLs for selected-page timelines. All results share one durable export.')
    idempotency_key: Annotated[str, Field(min_length=8, max_length=200)] = Field(..., alias='idempotencyKey', description='Required unique opaque ID for this intended export (a UUID is ideal). Reuse the same value only when retrying the same call after a timeout; use a new value for every intentional rerun. This prevents a lost response from creating or charging for a duplicate job.')
    rotate_proxies: Union[bool, None] = Field(None, alias='rotateProxies', description='Route page fetches through rotating residential proxies to defeat rate-limiting and bot blocks (403/429). Slower and pricier — use only when a site blocks normal crawling.')
    rotate_proxy_every: Union[Annotated[int, Field(ge=1, le=100)], None] = Field(None, alias='rotateProxyEvery', description='When rotateProxies is on, pages fetched per proxy before rotating. Default 30.')
    formats: Union[list[Literal['markdown', 'html', 'links', 'json', 'images', 'branding']], None] = Field(None, alias='formats', description='Requested export views. Every successful page is durably retained as complete JSON, acquired HTML, and Markdown; links and image references are included in page JSON. branding adds a browser-based site summary.')
    background: Union[Literal[True], None] = Field(None, alias='background', description='MCP multi-page crawls always run as durable background jobs. Poll check_site_export, then use site_export_read for complete JSON/HTML/Markdown and site_export_image for downloaded images.')
    delivery: Union[Literal['auto', 'artifact'], None] = Field(None, alias='delivery', description='Multi-page crawls are durable exports. auto and artifact both return a job handle followed by an owner-scoped ZIP; artifact explicitly requests that durable destination.')
    preserve_media: Union[bool, None] = Field(None, alias='preserveMedia', description='Include supported images in the export bundle. This is the preferred replacement for downloadImages.')
    download_images: Union[bool, None] = Field(None, alias='downloadImages', description='Deprecated alias for preserveMedia. Omit when using preserveMedia; when omitted, image preservation defaults to false.')


ExtractSiteOutputVariant1StoppedEarlyVariant1 = TypedDict('ExtractSiteOutputVariant1StoppedEarlyVariant1', {
    'code': Required[str],
    'message': Required[str],
})
ExtractSiteOutputVariant1StoppedEarlyVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


ExtractSiteOutputVariant1PagesItem = TypedDict('ExtractSiteOutputVariant1PagesItem', {
    'url': Required[str],
    'title': Required[Union[str, None]],
    'schemaTypes': Required[list[str]],
})
ExtractSiteOutputVariant1PagesItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


ExtractSiteOutputVariant1Artifact = TypedDict('ExtractSiteOutputVariant1Artifact', {
    'artifactId': Required[str],
    'bytes': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'expiresAt': Required[str],
    'preview': Required[str],
})
ExtractSiteOutputVariant1Artifact.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


ExtractSiteOutputVariant1Delivery = TypedDict('ExtractSiteOutputVariant1Delivery', {
    'requested': Required[Literal['auto', 'artifact']],
    'effective': Required[Literal['artifact']],
    'retained': Required[bool],
    'preserveMedia': Required[bool],
    'nextAction': Required[str],
})
ExtractSiteOutputVariant1Delivery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class ExtractSiteOutputVariant1(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    url: str = Field(..., alias='url', description='')
    stopped_early: Union[Union[ExtractSiteOutputVariant1StoppedEarlyVariant1, None], None] = Field(None, alias='stoppedEarly', description='Present when the crawl stopped before finishing. The returned pages are everything that was captured, and billing covers only those pages - treat the result as partial, not as the whole site.')
    page_count: Union[Annotated[int, Field(ge=0, le=9007199254740991)], None] = Field(None, alias='pageCount', description='Absent when background is true — the crawl has not finished yet.')
    pages: Union[list[ExtractSiteOutputVariant1PagesItem], None] = Field(None, alias='pages', description='Absent when background is true — the crawl has not finished yet.')
    duration_ms: Union[Annotated[Union[float, int], Field(ge=0)], None] = Field(None, alias='durationMs', description='Absent when background is true — the crawl has not finished yet.')
    truncated_count: Union[Annotated[int, Field(ge=0, le=9007199254740991)], None] = Field(None, alias='truncatedCount', description='')
    artifact: Union[ExtractSiteOutputVariant1Artifact, None] = Field(None, alias='artifact', description='')
    job_id: Union[str, None] = Field(None, alias='jobId', description='Present when background (or downloadImages) was set — poll with check_site_export.')
    status: Union[Literal['pending'], None] = Field(None, alias='status', description='Present when background (or downloadImages) was set.')
    status_url: Union[str, None] = Field(None, alias='statusUrl', description='Present when background (or downloadImages) was set — informational; use check_site_export with jobId, not this URL directly.')
    requested_max_pages: Union[Annotated[int, Field(ge=1, le=9007199254740991)], None] = Field(None, alias='requestedMaxPages', description='')
    effective_max_pages: Union[Annotated[int, Field(ge=1, le=9007199254740991)], None] = Field(None, alias='effectiveMaxPages', description='')
    credit_limited: Union[bool, None] = Field(None, alias='creditLimited', description='')
    credit_truncated: Union[bool, None] = Field(None, alias='creditTruncated', description='')
    delivery: Union[ExtractSiteOutputVariant1Delivery, None] = Field(None, alias='delivery', description='')


ExtractSiteOutputVariant2DeliveryArtifactsItem = TypedDict('ExtractSiteOutputVariant2DeliveryArtifactsItem', {
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
ExtractSiteOutputVariant2DeliveryArtifactsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


ExtractSiteOutputVariant2DeliveryStorageFailureVariant1 = TypedDict('ExtractSiteOutputVariant2DeliveryStorageFailureVariant1', {
    'artifactId': Required[Union[str, None]],
    'outcome': Required[Literal['unknown', 'bytes-stored-metadata-pending', 'failed']],
})
ExtractSiteOutputVariant2DeliveryStorageFailureVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


ExtractSiteOutputVariant2Delivery = TypedDict('ExtractSiteOutputVariant2Delivery', {
    'mode': Required[Literal['artifact']],
    'status': Required[Literal['complete', 'partial', 'unavailable']],
    'retainedRepresentation': Required[Literal['formatted-tool-result']],
    'sourceIsError': Required[bool],
    'artifacts': Required[list[ExtractSiteOutputVariant2DeliveryArtifactsItem]],
    'downloadLinksOmitted': Required[bool],
    'scopeOmittedFields': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'storageFailure': Required[Union[ExtractSiteOutputVariant2DeliveryStorageFailureVariant1, None]],
    'nextAction': Required[str],
})
ExtractSiteOutputVariant2Delivery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


ExtractSiteOutputVariant2RecoveryOperation = TypedDict('ExtractSiteOutputVariant2RecoveryOperation', {
    'runId': Required[Union[Annotated[str, Field(max_length=200)], None]],
    'idempotencyKey': Required[Annotated[str, Field(max_length=512)]],
    'state': Required[Annotated[str, Field(max_length=100)]],
})
ExtractSiteOutputVariant2RecoveryOperation.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


ExtractSiteOutputVariant2Recovery = TypedDict('ExtractSiteOutputVariant2Recovery', {
    'idempotencyKey': NotRequired[Annotated[str, Field(max_length=512)]],
    'operationId': NotRequired[Annotated[str, Field(max_length=200)]],
    'runId': NotRequired[Annotated[str, Field(max_length=200)]],
    'jobId': NotRequired[Annotated[str, Field(max_length=200)]],
    'operation': NotRequired[ExtractSiteOutputVariant2RecoveryOperation],
})
ExtractSiteOutputVariant2Recovery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class ExtractSiteOutputVariant2(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    delivery: ExtractSiteOutputVariant2Delivery = Field(..., alias='delivery', description='')
    preview: str = Field(..., alias='preview', description='')
    scope: dict[str, Union[str, Union[float, int], bool, None]] = Field(..., alias='scope', description='')
    recovery: ExtractSiteOutputVariant2Recovery = Field(..., alias='recovery', description='')


# Union schema: validate external payloads with TypeAdapter(ExtractSiteOutput).
ExtractSiteOutput = Union[ExtractSiteOutputVariant2, ExtractSiteOutputVariant1]

_ExtractSiteInputAdapter = TypeAdapter(ExtractSiteInput)
_ExtractSiteOutputAdapter = TypeAdapter(ExtractSiteOutput)