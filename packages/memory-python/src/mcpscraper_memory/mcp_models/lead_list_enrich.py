from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field, model_serializer


class LeadListEnrichInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    idempotency_key: str = Field(..., alias="idempotencyKey", description="Required stable key for this intended enrichment job. Reuse it only to retry the same job after a lost response.")
    source: Any = Field(..., alias="source", description="Exactly one source: mapped inline rows or an imported leadListId.")
    column_map: dict[str, Any] = Field(..., alias="columnMap", description="Exact source-header mapping. name is required; every mapped header must exist.")
    default_entity_type: Literal['business', 'person'] | None = Field(None, alias="defaultEntityType", description="Entity type for rows without an entityType-mapped value.")
    resolve_missing_urls: bool | None = Field(None, alias="resolveMissingUrls", description="When true, rows without supplied URLs may spend one exact-name Maps search. False restricts work to provided URLs.")
    gl: str | None = Field(None, alias="gl", description="Two-letter Google country code used only for missing-URL Maps resolution.")
    hl: str | None = Field(None, alias="hl", description="Two-letter Google language code used only for missing-URL Maps resolution.")
    max_pages_per_lead: int | None = Field(None, alias="maxPagesPerLead", description="Maximum public page extraction attempts per row, including its starting page.")
    email_search_fallback: Literal['off', 'serp_snippets'] | None = Field(None, alias="emailSearchFallback", description="Optional recovery after bounded page extraction finds no email. serp_snippets spends at most one current-rate SERP search per unresolved row and accepts only exact-domain email occurrences from result titles/snippets. These public occurrences do not verify deliverability or consent.")
    people_discovery: Literal['off', 'owners', 'leadership'] | None = Field(None, alias="peopleDiscovery", description="Optional associated-person recovery for business rows. owners finds explicit owners/founders; leadership also accepts role-bearing executives, managers, and team members. It searches AI Overview plus organic results, never opens LinkedIn pages, and returns provenance-bearing public candidates rather than verified employment.")
    people_query_templates: list[str] | None = Field(None, alias="peopleQueryTemplates", description="Ordered query templates the calling model should author when peopleDiscovery is enabled: use one role intent per template and the placeholders {business}, {city}, {region}, or {location}, for example {business} owner of company; one focused server fallback is used when omitted.")
    max_people_per_lead: int | None = Field(None, alias="maxPeoplePerLead", description="Maximum associated people retained and LinkedIn-searched per business row when peopleDiscovery is enabled; maximum added SERP cost is peopleQueryTemplates length (or one fallback) plus one profile search per retained person.")
    concurrency: int | None = Field(None, alias="concurrency", description="Maximum rows enriched concurrently. Default 3; maximum 5.")
    output_formats: list[Literal['csv', 'xlsx']] | None = Field(None, alias="outputFormats", description="Unique requested result formats. Defaults to both CSV and XLSX; this changes rendering only.")


class LeadListEnrichOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    job_id: str | None = Field(None, alias="jobId", description="")
    status: Literal['queued', 'running', 'complete', 'partial', 'empty', 'failed', 'cancelled'] | None = Field(None, alias="status", description="")
    progress: dict[str, Any] | None = Field(None, alias="progress", description="")
    billing: dict[str, Any] | None = Field(None, alias="billing", description="")
    sample_rows: list[dict[str, Any]] | None = Field(None, alias="sampleRows", description="")
    ambiguous_rows: list[dict[str, Any]] | None = Field(None, alias="ambiguousRows", description="")
    artifacts: list[dict[str, Any]] | None = Field(None, alias="artifacts", description="")
    warnings: list[str] | None = Field(None, alias="warnings", description="")
    created_at: str | None = Field(None, alias="createdAt", description="")
    updated_at: str | None = Field(None, alias="updatedAt", description="")
    completed_at: Any | None = Field(None, alias="completedAt", description="")
    error_code: Any | None = Field(None, alias="errorCode", description="")
    error: Any | None = Field(None, alias="error", description="")
    retryable: Any | None = Field(None, alias="retryable", description="")
    delivery: dict[str, Any] | None = Field(None, alias="delivery", description="")
    preview: str | None = Field(None, alias="preview", description="")
    scope: dict[str, Any] | None = Field(None, alias="scope", description="")
    recovery: dict[str, Any] | None = Field(None, alias="recovery", description="")

    @model_serializer(mode="wrap")
    def _serialize_response(self, handler, info):
        data = handler(self)
        for name, field in type(self).model_fields.items():
            if name not in self.model_fields_set:
                key = field.alias if info.by_alias and field.alias else name
                data.pop(key, None)
        return data
