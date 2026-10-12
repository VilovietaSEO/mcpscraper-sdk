from typing import Annotated, Any, Literal, Union
from typing_extensions import NotRequired, Required, TypedDict
from pydantic import BaseModel, ConfigDict, Field, TypeAdapter


class AnalyzeSiteSimilarityInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=False)

    url: Annotated[str, Field(min_length=1)] = Field(..., alias='url', description='Public live site to render and compare. Bare domains default to https://.')
    max_pages: Union[Annotated[int, Field(ge=2, le=500)], None] = Field(None, alias='maxPages', description='Maximum rendered pages to compare; default 100, maximum 500.')
    similarity_threshold: Union[Annotated[Union[float, int], Field(ge=0, le=1)], None] = Field(None, alias='similarityThreshold', description='Minimum raw cosine score retained in the pair table; default 0.90.')
    similarity_max_pairs: Union[Annotated[int, Field(ge=1, le=50000)], None] = Field(None, alias='similarityMaxPairs', description='Maximum scored pairs retained, highest first; default 10,000.')
    idempotency_key: Annotated[str, Field(min_length=8, max_length=200)] = Field(..., alias='idempotencyKey', description='Required unique opaque ID for this intended analysis. Reuse only when retrying the same call; use a new value for an intentional rerun.')


AnalyzeSiteSimilarityOutputVariant1StoppedEarlyVariant1 = TypedDict('AnalyzeSiteSimilarityOutputVariant1StoppedEarlyVariant1', {
    'code': Required[str],
    'message': Required[str],
})
AnalyzeSiteSimilarityOutputVariant1StoppedEarlyVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


AnalyzeSiteSimilarityOutputVariant1PagesItem = TypedDict('AnalyzeSiteSimilarityOutputVariant1PagesItem', {
    'url': Required[str],
    'title': Required[Union[str, None]],
    'schemaTypes': Required[list[str]],
})
AnalyzeSiteSimilarityOutputVariant1PagesItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


AnalyzeSiteSimilarityOutputVariant1Artifact = TypedDict('AnalyzeSiteSimilarityOutputVariant1Artifact', {
    'artifactId': Required[str],
    'bytes': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'expiresAt': Required[str],
    'preview': Required[str],
})
AnalyzeSiteSimilarityOutputVariant1Artifact.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


AnalyzeSiteSimilarityOutputVariant1Delivery = TypedDict('AnalyzeSiteSimilarityOutputVariant1Delivery', {
    'requested': Required[Literal['auto', 'artifact']],
    'effective': Required[Literal['artifact']],
    'retained': Required[bool],
    'preserveMedia': Required[bool],
    'nextAction': Required[str],
})
AnalyzeSiteSimilarityOutputVariant1Delivery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class AnalyzeSiteSimilarityOutputVariant1(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    url: str = Field(..., alias='url', description='')
    stopped_early: Union[Union[AnalyzeSiteSimilarityOutputVariant1StoppedEarlyVariant1, None], None] = Field(None, alias='stoppedEarly', description='Present when the crawl stopped before finishing. The returned pages are everything that was captured, and billing covers only those pages - treat the result as partial, not as the whole site.')
    page_count: Union[Annotated[int, Field(ge=0, le=9007199254740991)], None] = Field(None, alias='pageCount', description='Absent when background is true — the crawl has not finished yet.')
    pages: Union[list[AnalyzeSiteSimilarityOutputVariant1PagesItem], None] = Field(None, alias='pages', description='Absent when background is true — the crawl has not finished yet.')
    duration_ms: Union[Annotated[Union[float, int], Field(ge=0)], None] = Field(None, alias='durationMs', description='Absent when background is true — the crawl has not finished yet.')
    truncated_count: Union[Annotated[int, Field(ge=0, le=9007199254740991)], None] = Field(None, alias='truncatedCount', description='')
    artifact: Union[AnalyzeSiteSimilarityOutputVariant1Artifact, None] = Field(None, alias='artifact', description='')
    job_id: Union[str, None] = Field(None, alias='jobId', description='Present when background (or downloadImages) was set — poll with check_site_export.')
    status: Union[Literal['pending'], None] = Field(None, alias='status', description='Present when background (or downloadImages) was set.')
    status_url: Union[str, None] = Field(None, alias='statusUrl', description='Present when background (or downloadImages) was set — informational; use check_site_export with jobId, not this URL directly.')
    requested_max_pages: Union[Annotated[int, Field(ge=1, le=9007199254740991)], None] = Field(None, alias='requestedMaxPages', description='')
    effective_max_pages: Union[Annotated[int, Field(ge=1, le=9007199254740991)], None] = Field(None, alias='effectiveMaxPages', description='')
    credit_limited: Union[bool, None] = Field(None, alias='creditLimited', description='')
    credit_truncated: Union[bool, None] = Field(None, alias='creditTruncated', description='')
    delivery: Union[AnalyzeSiteSimilarityOutputVariant1Delivery, None] = Field(None, alias='delivery', description='')


AnalyzeSiteSimilarityOutputVariant2DeliveryArtifactsItem = TypedDict('AnalyzeSiteSimilarityOutputVariant2DeliveryArtifactsItem', {
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
AnalyzeSiteSimilarityOutputVariant2DeliveryArtifactsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


AnalyzeSiteSimilarityOutputVariant2DeliveryStorageFailureVariant1 = TypedDict('AnalyzeSiteSimilarityOutputVariant2DeliveryStorageFailureVariant1', {
    'artifactId': Required[Union[str, None]],
    'outcome': Required[Literal['unknown', 'bytes-stored-metadata-pending', 'failed']],
})
AnalyzeSiteSimilarityOutputVariant2DeliveryStorageFailureVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


AnalyzeSiteSimilarityOutputVariant2Delivery = TypedDict('AnalyzeSiteSimilarityOutputVariant2Delivery', {
    'mode': Required[Literal['artifact']],
    'status': Required[Literal['complete', 'partial', 'unavailable']],
    'retainedRepresentation': Required[Literal['formatted-tool-result']],
    'sourceIsError': Required[bool],
    'artifacts': Required[list[AnalyzeSiteSimilarityOutputVariant2DeliveryArtifactsItem]],
    'downloadLinksOmitted': Required[bool],
    'scopeOmittedFields': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'storageFailure': Required[Union[AnalyzeSiteSimilarityOutputVariant2DeliveryStorageFailureVariant1, None]],
    'nextAction': Required[str],
})
AnalyzeSiteSimilarityOutputVariant2Delivery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


AnalyzeSiteSimilarityOutputVariant2RecoveryOperation = TypedDict('AnalyzeSiteSimilarityOutputVariant2RecoveryOperation', {
    'runId': Required[Union[Annotated[str, Field(max_length=200)], None]],
    'idempotencyKey': Required[Annotated[str, Field(max_length=512)]],
    'state': Required[Annotated[str, Field(max_length=100)]],
})
AnalyzeSiteSimilarityOutputVariant2RecoveryOperation.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


AnalyzeSiteSimilarityOutputVariant2Recovery = TypedDict('AnalyzeSiteSimilarityOutputVariant2Recovery', {
    'idempotencyKey': NotRequired[Annotated[str, Field(max_length=512)]],
    'operationId': NotRequired[Annotated[str, Field(max_length=200)]],
    'runId': NotRequired[Annotated[str, Field(max_length=200)]],
    'jobId': NotRequired[Annotated[str, Field(max_length=200)]],
    'operation': NotRequired[AnalyzeSiteSimilarityOutputVariant2RecoveryOperation],
})
AnalyzeSiteSimilarityOutputVariant2Recovery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class AnalyzeSiteSimilarityOutputVariant2(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    delivery: AnalyzeSiteSimilarityOutputVariant2Delivery = Field(..., alias='delivery', description='')
    preview: str = Field(..., alias='preview', description='')
    scope: dict[str, Union[str, Union[float, int], bool, None]] = Field(..., alias='scope', description='')
    recovery: AnalyzeSiteSimilarityOutputVariant2Recovery = Field(..., alias='recovery', description='')


# Union schema: validate external payloads with TypeAdapter(AnalyzeSiteSimilarityOutput).
AnalyzeSiteSimilarityOutput = Union[AnalyzeSiteSimilarityOutputVariant2, AnalyzeSiteSimilarityOutputVariant1]

_AnalyzeSiteSimilarityInputAdapter = TypeAdapter(AnalyzeSiteSimilarityInput)
_AnalyzeSiteSimilarityOutputAdapter = TypeAdapter(AnalyzeSiteSimilarityOutput)