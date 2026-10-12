from typing import Annotated, Any, Literal, Union
from typing_extensions import NotRequired, Required, TypedDict
from pydantic import BaseModel, ConfigDict, Field, TypeAdapter


class AuditSiteInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=False)

    url: Annotated[str, Field(min_length=1)] = Field(..., alias='url', description='Public website URL or domain for a full technical SEO audit (issues, link graph, indexability, headings, images). Bare domains default to https://. For plain content use extract_site instead.')
    max_pages: Union[Annotated[int, Field(ge=1, le=10000)], None] = Field(None, alias='maxPages', description='Maximum pages to crawl and audit. MCP audits always run as durable background exports and return a jobId; poll check_site_export for the hosted audit ZIP.')
    idempotency_key: Annotated[str, Field(min_length=8, max_length=200)] = Field(..., alias='idempotencyKey', description='Required unique opaque ID for this intended audit (a UUID is ideal). Reuse the same value only when retrying the same call after a timeout; use a new value for every intentional rerun. This prevents a lost response from creating or charging for a duplicate job.')
    rotate_proxies: Union[bool, None] = Field(None, alias='rotateProxies', description='Route page fetches through rotating residential proxies to defeat rate-limiting and bot blocks. Slower/pricier — use only when a site blocks normal crawling.')
    rotate_proxy_every: Union[Annotated[int, Field(ge=1, le=100)], None] = Field(None, alias='rotateProxyEvery', description='When rotateProxies is on, pages fetched per proxy before rotating. Default 30.')
    background: Union[Literal[True], None] = Field(None, alias='background', description='MCP technical audits always run as durable background jobs. Poll check_site_export for progress, outcome counters, and the hosted audit ZIP.')
    delivery: Union[Literal['auto', 'artifact'], None] = Field(None, alias='delivery', description='Technical audits are durable exports. auto and artifact both return a job handle followed by an owner-scoped ZIP; artifact explicitly requests that durable destination.')
    preserve_media: Union[bool, None] = Field(None, alias='preserveMedia', description='Include supported images in the export bundle. This is the preferred replacement for downloadImages.')
    download_images: Union[bool, None] = Field(None, alias='downloadImages', description='Deprecated alias for preserveMedia. Omit when using preserveMedia; when omitted, image preservation defaults to false.')


AuditSiteOutputVariant1Images = TypedDict('AuditSiteOutputVariant1Images', {
    'unique': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'totalBytes': Required[Annotated[Union[float, int], Field(ge=0)]],
    'over100kb': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'legacyFormat': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
})
AuditSiteOutputVariant1Images.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


AuditSiteOutputVariant1Links = TypedDict('AuditSiteOutputVariant1Links', {
    'internal': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'external': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'orphans': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'brokenInternal': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'externalDomains': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
})
AuditSiteOutputVariant1Links.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


AuditSiteOutputVariant1Artifact = TypedDict('AuditSiteOutputVariant1Artifact', {
    'artifactId': Required[str],
    'bytes': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'expiresAt': Required[str],
    'preview': Required[str],
})
AuditSiteOutputVariant1Artifact.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


AuditSiteOutputVariant1Delivery = TypedDict('AuditSiteOutputVariant1Delivery', {
    'requested': Required[Literal['auto', 'artifact']],
    'effective': Required[Literal['artifact']],
    'retained': Required[bool],
    'preserveMedia': Required[bool],
    'nextAction': Required[str],
})
AuditSiteOutputVariant1Delivery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class AuditSiteOutputVariant1(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    url: str = Field(..., alias='url', description='')
    page_count: Union[Annotated[int, Field(ge=0, le=9007199254740991)], None] = Field(None, alias='pageCount', description='Absent when background is true — the audit has not finished yet.')
    duration_ms: Union[Annotated[Union[float, int], Field(ge=0)], None] = Field(None, alias='durationMs', description='Absent when background is true — the audit has not finished yet.')
    bulk_folder: Union[Union[str, None], None] = Field(None, alias='bulkFolder', description='Absent when background is true — the audit has not finished yet.')
    issues: Union[dict[str, Union[float, int]], None] = Field(None, alias='issues', description='Absent when background is true — the audit has not finished yet.')
    images: Union[AuditSiteOutputVariant1Images, None] = Field(None, alias='images', description='Absent when background is true — the audit has not finished yet.')
    links: Union[AuditSiteOutputVariant1Links, None] = Field(None, alias='links', description='Absent when background is true — the audit has not finished yet.')
    artifact: Union[AuditSiteOutputVariant1Artifact, None] = Field(None, alias='artifact', description='')
    job_id: Union[str, None] = Field(None, alias='jobId', description='Present when background (or downloadImages) was set — poll with check_site_export.')
    status: Union[Literal['pending'], None] = Field(None, alias='status', description='Present when background (or downloadImages) was set.')
    status_url: Union[str, None] = Field(None, alias='statusUrl', description='Present when background (or downloadImages) was set — informational; use check_site_export with jobId, not this URL directly.')
    requested_max_pages: Union[Annotated[int, Field(ge=1, le=9007199254740991)], None] = Field(None, alias='requestedMaxPages', description='')
    effective_max_pages: Union[Annotated[int, Field(ge=1, le=9007199254740991)], None] = Field(None, alias='effectiveMaxPages', description='')
    credit_limited: Union[bool, None] = Field(None, alias='creditLimited', description='')
    credit_truncated: Union[bool, None] = Field(None, alias='creditTruncated', description='')
    delivery: Union[AuditSiteOutputVariant1Delivery, None] = Field(None, alias='delivery', description='')


AuditSiteOutputVariant2DeliveryArtifactsItem = TypedDict('AuditSiteOutputVariant2DeliveryArtifactsItem', {
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
AuditSiteOutputVariant2DeliveryArtifactsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


AuditSiteOutputVariant2DeliveryStorageFailureVariant1 = TypedDict('AuditSiteOutputVariant2DeliveryStorageFailureVariant1', {
    'artifactId': Required[Union[str, None]],
    'outcome': Required[Literal['unknown', 'bytes-stored-metadata-pending', 'failed']],
})
AuditSiteOutputVariant2DeliveryStorageFailureVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


AuditSiteOutputVariant2Delivery = TypedDict('AuditSiteOutputVariant2Delivery', {
    'mode': Required[Literal['artifact']],
    'status': Required[Literal['complete', 'partial', 'unavailable']],
    'retainedRepresentation': Required[Literal['formatted-tool-result']],
    'sourceIsError': Required[bool],
    'artifacts': Required[list[AuditSiteOutputVariant2DeliveryArtifactsItem]],
    'downloadLinksOmitted': Required[bool],
    'scopeOmittedFields': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'storageFailure': Required[Union[AuditSiteOutputVariant2DeliveryStorageFailureVariant1, None]],
    'nextAction': Required[str],
})
AuditSiteOutputVariant2Delivery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


AuditSiteOutputVariant2RecoveryOperation = TypedDict('AuditSiteOutputVariant2RecoveryOperation', {
    'runId': Required[Union[Annotated[str, Field(max_length=200)], None]],
    'idempotencyKey': Required[Annotated[str, Field(max_length=512)]],
    'state': Required[Annotated[str, Field(max_length=100)]],
})
AuditSiteOutputVariant2RecoveryOperation.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


AuditSiteOutputVariant2Recovery = TypedDict('AuditSiteOutputVariant2Recovery', {
    'idempotencyKey': NotRequired[Annotated[str, Field(max_length=512)]],
    'operationId': NotRequired[Annotated[str, Field(max_length=200)]],
    'runId': NotRequired[Annotated[str, Field(max_length=200)]],
    'jobId': NotRequired[Annotated[str, Field(max_length=200)]],
    'operation': NotRequired[AuditSiteOutputVariant2RecoveryOperation],
})
AuditSiteOutputVariant2Recovery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class AuditSiteOutputVariant2(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    delivery: AuditSiteOutputVariant2Delivery = Field(..., alias='delivery', description='')
    preview: str = Field(..., alias='preview', description='')
    scope: dict[str, Union[str, Union[float, int], bool, None]] = Field(..., alias='scope', description='')
    recovery: AuditSiteOutputVariant2Recovery = Field(..., alias='recovery', description='')


# Union schema: validate external payloads with TypeAdapter(AuditSiteOutput).
AuditSiteOutput = Union[AuditSiteOutputVariant2, AuditSiteOutputVariant1]

_AuditSiteInputAdapter = TypeAdapter(AuditSiteInput)
_AuditSiteOutputAdapter = TypeAdapter(AuditSiteOutput)