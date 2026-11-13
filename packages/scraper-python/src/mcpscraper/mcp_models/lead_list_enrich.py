from typing import Annotated, Any, Literal, Union
from typing_extensions import NotRequired, Required, TypedDict
from pydantic import BaseModel, ConfigDict, Field, TypeAdapter


LeadListEnrichInputSourceVariant1 = TypedDict('LeadListEnrichInputSourceVariant1', {
    'kind': Required[Literal['rows']],
    'rows': Required[Annotated[list[dict[str, Union[str, Union[float, int], bool, None]]], Field(min_length=1, max_length=250)]],
})
LeadListEnrichInputSourceVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=False)


LeadListEnrichInputSourceVariant2 = TypedDict('LeadListEnrichInputSourceVariant2', {
    'kind': Required[Literal['lead_list']],
    'leadListId': Required[Annotated[str, Field(min_length=1)]],
})
LeadListEnrichInputSourceVariant2.__pydantic_config__ = ConfigDict(extra="allow", strict=False)


LeadListEnrichInputColumnMap = TypedDict('LeadListEnrichInputColumnMap', {
    'name': Required[Annotated[str, Field(min_length=1)]],
    'location': NotRequired[Annotated[str, Field(min_length=1)]],
    'city': NotRequired[Annotated[str, Field(min_length=1)]],
    'region': NotRequired[Annotated[str, Field(min_length=1)]],
    'organization': NotRequired[Annotated[str, Field(min_length=1)]],
    'websiteUrl': NotRequired[Annotated[str, Field(min_length=1)]],
    'profileUrl': NotRequired[Annotated[str, Field(min_length=1)]],
    'phone': NotRequired[Annotated[str, Field(min_length=1)]],
    'entityType': NotRequired[Annotated[str, Field(min_length=1)]],
})
LeadListEnrichInputColumnMap.__pydantic_config__ = ConfigDict(extra="allow", strict=False)


class LeadListEnrichInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=False)

    idempotency_key: Annotated[str, Field(min_length=8, max_length=200)] = Field(..., alias='idempotencyKey', description='Required stable key for this intended enrichment job. Reuse it only to retry the same job after a lost response.')
    source: Union[LeadListEnrichInputSourceVariant1, LeadListEnrichInputSourceVariant2] = Field(..., alias='source', description='Exactly one source: mapped inline rows or an imported leadListId.')
    column_map: LeadListEnrichInputColumnMap = Field(..., alias='columnMap', description='Exact source-header mapping. name is required; every mapped header must exist.')
    default_entity_type: Union[Literal['business', 'person'], None] = Field(None, alias='defaultEntityType', description='Entity type for rows without an entityType-mapped value.')
    resolve_missing_urls: Union[bool, None] = Field(None, alias='resolveMissingUrls', description='When true, rows without supplied URLs may spend one exact-name Maps search. False restricts work to provided URLs.')
    gl: Union[Annotated[str, Field(min_length=2, max_length=2)], None] = Field(None, alias='gl', description='Two-letter Google country code used only for missing-URL Maps resolution.')
    hl: Union[Annotated[str, Field(min_length=2, max_length=2)], None] = Field(None, alias='hl', description='Two-letter Google language code used only for missing-URL Maps resolution.')
    max_pages_per_lead: Union[Annotated[int, Field(ge=1, le=4)], None] = Field(None, alias='maxPagesPerLead', description='Maximum public page extraction attempts per row, including its starting page.')
    email_search_fallback: Union[Literal['off', 'serp_snippets'], None] = Field(None, alias='emailSearchFallback', description='Optional recovery after bounded page extraction finds no email. serp_snippets spends at most one current-rate SERP search per unresolved row and accepts only exact-domain email occurrences from result titles/snippets. These public occurrences do not verify deliverability or consent.')
    people_discovery: Union[Literal['off', 'owners', 'leadership'], None] = Field(None, alias='peopleDiscovery', description='Optional associated-person recovery for business rows. owners finds explicit owners/founders; leadership also accepts role-bearing executives, managers, and team members. It searches AI Overview plus organic results, never opens LinkedIn pages, and returns provenance-bearing public candidates rather than verified employment.')
    people_query_templates: Union[Annotated[list[Annotated[str, Field(min_length=1, max_length=240)]], Field(min_length=1, max_length=3)], None] = Field(None, alias='peopleQueryTemplates', description='Ordered query templates the calling model should author when peopleDiscovery is enabled: use one role intent per template and the placeholders {business}, {city}, {region}, or {location}, for example {business} owner of company; one focused server fallback is used when omitted.')
    max_people_per_lead: Union[Annotated[int, Field(ge=1, le=3)], None] = Field(None, alias='maxPeoplePerLead', description='Maximum associated people retained and LinkedIn-searched per business row when peopleDiscovery is enabled; maximum added SERP cost is peopleQueryTemplates length (or one fallback) plus one profile search per retained person.')
    concurrency: Union[Annotated[int, Field(ge=1, le=5)], None] = Field(None, alias='concurrency', description='Maximum rows enriched concurrently. Default 3; maximum 5.')
    output_formats: Union[Annotated[list[Literal['csv', 'xlsx']], Field(min_length=1, max_length=2)], None] = Field(None, alias='outputFormats', description='Unique requested result formats. Defaults to both CSV and XLSX; this changes rendering only.')


LeadListEnrichOutputVariant1Progress = TypedDict('LeadListEnrichOutputVariant1Progress', {
    'totalRows': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'completedRows': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'failedRows': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'cancelledRows': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'rowsWithContact': NotRequired[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'rowsWithPeople': NotRequired[Annotated[int, Field(ge=0, le=9007199254740991)]],
})
LeadListEnrichOutputVariant1Progress.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


LeadListEnrichOutputVariant1Billing = TypedDict('LeadListEnrichOutputVariant1Billing', {
    'heldMc': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'finalMc': Required[Union[Annotated[int, Field(ge=0, le=9007199254740991)], None]],
    'refundMc': Required[Union[Annotated[int, Field(ge=0, le=9007199254740991)], None]],
    'mapsSearches': NotRequired[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'pageAttempts': NotRequired[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'serpSearches': NotRequired[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'mapsMc': NotRequired[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'pageMc': NotRequired[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'serpMc': NotRequired[Annotated[int, Field(ge=0, le=9007199254740991)]],
})
LeadListEnrichOutputVariant1Billing.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


LeadListEnrichOutputVariant1SampleRowsItemPeopleItemSourcesItem = TypedDict('LeadListEnrichOutputVariant1SampleRowsItemPeopleItemSourcesItem', {
    'sourceType': Required[Literal['serp_snippet', 'ai_overview']],
    'purpose': Required[Literal['role', 'linkedin']],
    'sourceUrl': Required[str],
    'sourceTitle': Required[str],
    'sourcePosition': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'context': Required[str],
    'citationUrls': NotRequired[Annotated[list[str], Field(max_length=5)]],
})
LeadListEnrichOutputVariant1SampleRowsItemPeopleItemSourcesItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


LeadListEnrichOutputVariant1SampleRowsItemPeopleItem = TypedDict('LeadListEnrichOutputVariant1SampleRowsItemPeopleItem', {
    'name': Required[str],
    'role': Required[str],
    'relationship': Required[Literal['owner', 'founder', 'executive', 'manager', 'team_member']],
    'linkedinUrl': Required[Union[str, None]],
    'confidence': Required[Annotated[Union[float, int], Field(ge=0, le=1)]],
    'reasons': Required[Annotated[list[str], Field(max_length=10)]],
    'sources': Required[Annotated[list[LeadListEnrichOutputVariant1SampleRowsItemPeopleItemSourcesItem], Field(max_length=3)]],
})
LeadListEnrichOutputVariant1SampleRowsItemPeopleItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


LeadListEnrichOutputVariant1SampleRowsItem = TypedDict('LeadListEnrichOutputVariant1SampleRowsItem', {
    'people': NotRequired[Annotated[list[LeadListEnrichOutputVariant1SampleRowsItemPeopleItem], Field(max_length=3)]],
})
LeadListEnrichOutputVariant1SampleRowsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


LeadListEnrichOutputVariant1AmbiguousRowsItemCandidatesItem = TypedDict('LeadListEnrichOutputVariant1AmbiguousRowsItemCandidatesItem', {
    'name': Required[str],
    'websiteUrl': NotRequired[Union[str, None]],
    'mapsUrl': NotRequired[Union[str, None]],
    'confidence': NotRequired[Annotated[Union[float, int], Field(ge=0, le=1)]],
    'evidence': NotRequired[list[str]],
})
LeadListEnrichOutputVariant1AmbiguousRowsItemCandidatesItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


LeadListEnrichOutputVariant1AmbiguousRowsItem = TypedDict('LeadListEnrichOutputVariant1AmbiguousRowsItem', {
    'ordinal': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'candidates': Required[Annotated[list[LeadListEnrichOutputVariant1AmbiguousRowsItemCandidatesItem], Field(max_length=3)]],
})
LeadListEnrichOutputVariant1AmbiguousRowsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


LeadListEnrichOutputVariant1ArtifactsItem = TypedDict('LeadListEnrichOutputVariant1ArtifactsItem', {
    'artifactId': Required[str],
    'filename': Required[str],
    'contentType': Required[str],
    'bytes': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'rowCount': NotRequired[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'sha256': Required[str],
    'expiresAt': Required[str],
    'downloadUrl': Required[Union[str, None]],
    'downloadUrlExpiresAt': Required[Union[str, None]],
})
LeadListEnrichOutputVariant1ArtifactsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class LeadListEnrichOutputVariant1(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    job_id: str = Field(..., alias='jobId', description='')
    status: Literal['queued', 'running', 'complete', 'partial', 'empty', 'failed', 'cancelled'] = Field(..., alias='status', description='')
    progress: LeadListEnrichOutputVariant1Progress = Field(..., alias='progress', description='')
    billing: LeadListEnrichOutputVariant1Billing = Field(..., alias='billing', description='')
    sample_rows: Annotated[list[LeadListEnrichOutputVariant1SampleRowsItem], Field(max_length=10)] = Field(..., alias='sampleRows', description='')
    ambiguous_rows: Union[Annotated[list[LeadListEnrichOutputVariant1AmbiguousRowsItem], Field(max_length=10)], None] = Field(None, alias='ambiguousRows', description='')
    artifacts: Annotated[list[LeadListEnrichOutputVariant1ArtifactsItem], Field(max_length=2)] = Field(..., alias='artifacts', description='')
    warnings: list[str] = Field(..., alias='warnings', description='')
    created_at: Union[str, None] = Field(None, alias='createdAt', description='')
    updated_at: Union[str, None] = Field(None, alias='updatedAt', description='')
    completed_at: Union[Union[str, None], None] = Field(None, alias='completedAt', description='')
    error_code: Union[Union[str, None], None] = Field(None, alias='errorCode', description='')
    error: Union[Union[str, None], None] = Field(None, alias='error', description='')
    retryable: Union[Union[bool, None], None] = Field(None, alias='retryable', description='')


LeadListEnrichOutputVariant2DeliveryArtifactsItem = TypedDict('LeadListEnrichOutputVariant2DeliveryArtifactsItem', {
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
LeadListEnrichOutputVariant2DeliveryArtifactsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


LeadListEnrichOutputVariant2DeliveryAvailableExportsItem = TypedDict('LeadListEnrichOutputVariant2DeliveryAvailableExportsItem', {
    'artifactId': Required[str],
    'sourceArtifactId': Required[str],
    'filename': Required[Literal['result.md']],
    'contentType': Required[Literal['text/markdown; charset=utf-8']],
    'state': Required[Literal['on-demand']],
})
LeadListEnrichOutputVariant2DeliveryAvailableExportsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


LeadListEnrichOutputVariant2DeliveryStorageFailureVariant1 = TypedDict('LeadListEnrichOutputVariant2DeliveryStorageFailureVariant1', {
    'artifactId': Required[Union[str, None]],
    'outcome': Required[Literal['unknown', 'bytes-stored-metadata-pending', 'failed']],
})
LeadListEnrichOutputVariant2DeliveryStorageFailureVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


LeadListEnrichOutputVariant2Delivery = TypedDict('LeadListEnrichOutputVariant2Delivery', {
    'mode': Required[Literal['artifact']],
    'status': Required[Literal['complete', 'partial', 'unavailable']],
    'retainedRepresentation': Required[Literal['formatted-tool-result']],
    'sourceIsError': Required[bool],
    'artifacts': Required[list[LeadListEnrichOutputVariant2DeliveryArtifactsItem]],
    'availableExports': NotRequired[list[LeadListEnrichOutputVariant2DeliveryAvailableExportsItem]],
    'downloadLinksOmitted': Required[bool],
    'scopeOmittedFields': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'storageFailure': Required[Union[LeadListEnrichOutputVariant2DeliveryStorageFailureVariant1, None]],
    'nextAction': Required[str],
})
LeadListEnrichOutputVariant2Delivery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


LeadListEnrichOutputVariant2RecoveryOperation = TypedDict('LeadListEnrichOutputVariant2RecoveryOperation', {
    'runId': Required[Union[Annotated[str, Field(max_length=200)], None]],
    'idempotencyKey': Required[Annotated[str, Field(max_length=512)]],
    'state': Required[Annotated[str, Field(max_length=100)]],
})
LeadListEnrichOutputVariant2RecoveryOperation.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


LeadListEnrichOutputVariant2Recovery = TypedDict('LeadListEnrichOutputVariant2Recovery', {
    'idempotencyKey': NotRequired[Annotated[str, Field(max_length=512)]],
    'operationId': NotRequired[Annotated[str, Field(max_length=200)]],
    'runId': NotRequired[Annotated[str, Field(max_length=200)]],
    'jobId': NotRequired[Annotated[str, Field(max_length=200)]],
    'operation': NotRequired[LeadListEnrichOutputVariant2RecoveryOperation],
})
LeadListEnrichOutputVariant2Recovery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class LeadListEnrichOutputVariant2(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    delivery: LeadListEnrichOutputVariant2Delivery = Field(..., alias='delivery', description='')
    preview: str = Field(..., alias='preview', description='')
    scope: dict[str, Union[str, Union[float, int], bool, None]] = Field(..., alias='scope', description='')
    recovery: LeadListEnrichOutputVariant2Recovery = Field(..., alias='recovery', description='')


# Union schema: validate external payloads with TypeAdapter(LeadListEnrichOutput).
LeadListEnrichOutput = Union[LeadListEnrichOutputVariant1, LeadListEnrichOutputVariant2]

_LeadListEnrichInputAdapter = TypeAdapter(LeadListEnrichInput)
_LeadListEnrichOutputAdapter = TypeAdapter(LeadListEnrichOutput)