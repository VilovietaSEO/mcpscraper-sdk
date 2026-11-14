from typing import Annotated, Any, Literal, Union
from typing_extensions import NotRequired, Required, TypedDict
from pydantic import BaseModel, ConfigDict, Field, TypeAdapter


class LinkedinJobsInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=False)

    company: Union[Annotated[str, Field(min_length=1)], None] = Field(None, alias='company', description='Filter to a specific company by name (e.g. Google).')
    cursor: Union[Annotated[str, Field(min_length=1)], None] = Field(None, alias='cursor', description="Opaque pagination cursor from a previous response's nextCursor. Omit for the first page; pass it to fetch the next page of job listings.")
    easy_apply: Union[bool, None] = Field(None, alias='easyApply', description='When true, only return jobs offering LinkedIn Easy Apply.')
    employment_type: Union[Literal['full-time', 'part-time', 'contract', 'internship', 'temporary'], None] = Field(None, alias='employmentType', description='Filter by employment type.')
    experience_level: Union[Literal['internship', 'entry', 'associate', 'mid-senior', 'director', 'executive'], None] = Field(None, alias='experienceLevel', description='Filter by required seniority/experience level.')
    location: Union[Annotated[str, Field(min_length=1)], None] = Field(None, alias='location', description='City, region, or country to search within (e.g. United States, San Francisco).')
    posted_limit: Union[Literal['1h', '24h', 'week', 'month'], None] = Field(None, alias='postedLimit', description='Only jobs posted within this window (past hour, 24 hours, week, or month).')
    query: Annotated[str, Field(min_length=1)] = Field(..., alias='query', description='Job title or keywords to search. Supports LinkedIn boolean operators.')
    salary: Union[Literal['40k+', '60k+', '80k+', '100k+', '120k+', '140k+', '160k+', '180k+', '200k+'], None] = Field(None, alias='salary', description='Filter by minimum base salary band (US dollars).')
    sort_by: Union[Literal['date', 'relevance'], None] = Field(None, alias='sortBy', description='Sort order: most recent (date) or best match (relevance).')
    under10_applicants: Union[bool, None] = Field(None, alias='under10Applicants', description='When true, only return jobs with fewer than 10 applicants (lower competition).')
    workplace_type: Union[Literal['remote', 'hybrid', 'onsite'], None] = Field(None, alias='workplaceType', description='Filter by workplace type (remote, hybrid, or onsite).')


class LinkedinJobsOutputVariant1(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    tool: str = Field(..., alias='tool', description='The tool that produced this result.')
    count: Annotated[int, Field(ge=-9007199254740991, le=9007199254740991)] = Field(..., alias='count', description='Number of records returned.')
    items: list[dict[str, Any]] = Field(..., alias='items', description='Returned records. A lookup of one thing returns a single record.')
    meta: Union[dict[str, Any], None] = Field(None, alias='meta', description='Values returned alongside the records, such as nextCursor for the next page, or totals.')
    charged_credits: Union[float, int] = Field(..., alias='chargedCredits', description='Credits charged for this call.')
    duration_ms: Union[Union[float, int], None] = Field(..., alias='durationMs', description='Time taken in milliseconds.')


LinkedinJobsOutputVariant2DeliveryArtifactsItem = TypedDict('LinkedinJobsOutputVariant2DeliveryArtifactsItem', {
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
LinkedinJobsOutputVariant2DeliveryArtifactsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


LinkedinJobsOutputVariant2DeliveryAvailableExportsItem = TypedDict('LinkedinJobsOutputVariant2DeliveryAvailableExportsItem', {
    'artifactId': Required[str],
    'sourceArtifactId': Required[str],
    'filename': Required[Literal['result.md']],
    'contentType': Required[Literal['text/markdown; charset=utf-8']],
    'state': Required[Literal['on-demand']],
})
LinkedinJobsOutputVariant2DeliveryAvailableExportsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


LinkedinJobsOutputVariant2DeliveryStorageFailureVariant1 = TypedDict('LinkedinJobsOutputVariant2DeliveryStorageFailureVariant1', {
    'artifactId': Required[Union[str, None]],
    'outcome': Required[Literal['unknown', 'bytes-stored-metadata-pending', 'failed']],
})
LinkedinJobsOutputVariant2DeliveryStorageFailureVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


LinkedinJobsOutputVariant2Delivery = TypedDict('LinkedinJobsOutputVariant2Delivery', {
    'mode': Required[Literal['artifact']],
    'status': Required[Literal['complete', 'partial', 'unavailable']],
    'retainedRepresentation': Required[Literal['formatted-tool-result']],
    'sourceIsError': Required[bool],
    'artifacts': Required[list[LinkedinJobsOutputVariant2DeliveryArtifactsItem]],
    'availableExports': NotRequired[list[LinkedinJobsOutputVariant2DeliveryAvailableExportsItem]],
    'downloadLinksOmitted': Required[bool],
    'scopeOmittedFields': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'storageFailure': Required[Union[LinkedinJobsOutputVariant2DeliveryStorageFailureVariant1, None]],
    'nextAction': Required[str],
})
LinkedinJobsOutputVariant2Delivery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


LinkedinJobsOutputVariant2RecoveryOperation = TypedDict('LinkedinJobsOutputVariant2RecoveryOperation', {
    'runId': Required[Union[Annotated[str, Field(max_length=200)], None]],
    'idempotencyKey': Required[Annotated[str, Field(max_length=512)]],
    'state': Required[Annotated[str, Field(max_length=100)]],
})
LinkedinJobsOutputVariant2RecoveryOperation.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


LinkedinJobsOutputVariant2Recovery = TypedDict('LinkedinJobsOutputVariant2Recovery', {
    'idempotencyKey': NotRequired[Annotated[str, Field(max_length=512)]],
    'operationId': NotRequired[Annotated[str, Field(max_length=200)]],
    'runId': NotRequired[Annotated[str, Field(max_length=200)]],
    'jobId': NotRequired[Annotated[str, Field(max_length=200)]],
    'operation': NotRequired[LinkedinJobsOutputVariant2RecoveryOperation],
})
LinkedinJobsOutputVariant2Recovery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class LinkedinJobsOutputVariant2(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    delivery: LinkedinJobsOutputVariant2Delivery = Field(..., alias='delivery', description='')
    preview: str = Field(..., alias='preview', description='')
    scope: dict[str, Union[str, Union[float, int], bool, None]] = Field(..., alias='scope', description='')
    recovery: LinkedinJobsOutputVariant2Recovery = Field(..., alias='recovery', description='')


# Union schema: validate external payloads with TypeAdapter(LinkedinJobsOutput).
LinkedinJobsOutput = Union[LinkedinJobsOutputVariant1, LinkedinJobsOutputVariant2]

_LinkedinJobsInputAdapter = TypeAdapter(LinkedinJobsInput)
_LinkedinJobsOutputAdapter = TypeAdapter(LinkedinJobsOutput)