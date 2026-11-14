from typing import Annotated, Any, Literal, Union
from typing_extensions import NotRequired, Required, TypedDict
from pydantic import BaseModel, ConfigDict, Field, TypeAdapter


class LinkedinJobsThinInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=False)

    company_id: Union[Annotated[str, Field(min_length=1)], None] = Field(None, alias='companyId', description='Filter to a specific company by its LinkedIn numeric company id.')
    cursor: Union[Annotated[str, Field(min_length=1)], None] = Field(None, alias='cursor', description="Opaque pagination cursor from a previous response's nextCursor. Omit for the first page; pass it to fetch the next page of job listings.")
    employment_type: Union[Literal['full-time', 'part-time', 'contract', 'internship', 'temporary'], None] = Field(None, alias='employmentType', description='Filter by employment type.')
    experience_level: Union[Literal['internship', 'entry', 'associate', 'mid-senior', 'director', 'executive'], None] = Field(None, alias='experienceLevel', description='Filter by required seniority/experience level.')
    geo_id: Union[Annotated[str, Field(min_length=1)], None] = Field(None, alias='geoId', description='LinkedIn geo id to target a precise location (e.g. 103644278 for the United States); more exact than the free-text location.')
    location: Union[Annotated[str, Field(min_length=1)], None] = Field(None, alias='location', description='City, region, or country to search within.')
    posted_limit: Union[Literal['24h', 'week', 'month'], None] = Field(None, alias='postedLimit', description='Only jobs posted within this window (past 24 hours, week, or month).')
    query: Annotated[str, Field(min_length=1)] = Field(..., alias='query', description='Job title or keywords to search.')
    workplace_type: Union[Literal['remote', 'hybrid', 'onsite'], None] = Field(None, alias='workplaceType', description='Filter by workplace type (remote, hybrid, or onsite).')


class LinkedinJobsThinOutputVariant1(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    tool: str = Field(..., alias='tool', description='The tool that produced this result.')
    count: Annotated[int, Field(ge=-9007199254740991, le=9007199254740991)] = Field(..., alias='count', description='Number of records returned.')
    items: list[dict[str, Any]] = Field(..., alias='items', description='Returned records. A lookup of one thing returns a single record.')
    meta: Union[dict[str, Any], None] = Field(None, alias='meta', description='Values returned alongside the records, such as nextCursor for the next page, or totals.')
    charged_credits: Union[float, int] = Field(..., alias='chargedCredits', description='Credits charged for this call.')
    duration_ms: Union[Union[float, int], None] = Field(..., alias='durationMs', description='Time taken in milliseconds.')


LinkedinJobsThinOutputVariant2DeliveryArtifactsItem = TypedDict('LinkedinJobsThinOutputVariant2DeliveryArtifactsItem', {
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
LinkedinJobsThinOutputVariant2DeliveryArtifactsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


LinkedinJobsThinOutputVariant2DeliveryAvailableExportsItem = TypedDict('LinkedinJobsThinOutputVariant2DeliveryAvailableExportsItem', {
    'artifactId': Required[str],
    'sourceArtifactId': Required[str],
    'filename': Required[Literal['result.md']],
    'contentType': Required[Literal['text/markdown; charset=utf-8']],
    'state': Required[Literal['on-demand']],
})
LinkedinJobsThinOutputVariant2DeliveryAvailableExportsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


LinkedinJobsThinOutputVariant2DeliveryStorageFailureVariant1 = TypedDict('LinkedinJobsThinOutputVariant2DeliveryStorageFailureVariant1', {
    'artifactId': Required[Union[str, None]],
    'outcome': Required[Literal['unknown', 'bytes-stored-metadata-pending', 'failed']],
})
LinkedinJobsThinOutputVariant2DeliveryStorageFailureVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


LinkedinJobsThinOutputVariant2Delivery = TypedDict('LinkedinJobsThinOutputVariant2Delivery', {
    'mode': Required[Literal['artifact']],
    'status': Required[Literal['complete', 'partial', 'unavailable']],
    'retainedRepresentation': Required[Literal['formatted-tool-result']],
    'sourceIsError': Required[bool],
    'artifacts': Required[list[LinkedinJobsThinOutputVariant2DeliveryArtifactsItem]],
    'availableExports': NotRequired[list[LinkedinJobsThinOutputVariant2DeliveryAvailableExportsItem]],
    'downloadLinksOmitted': Required[bool],
    'scopeOmittedFields': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'storageFailure': Required[Union[LinkedinJobsThinOutputVariant2DeliveryStorageFailureVariant1, None]],
    'nextAction': Required[str],
})
LinkedinJobsThinOutputVariant2Delivery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


LinkedinJobsThinOutputVariant2RecoveryOperation = TypedDict('LinkedinJobsThinOutputVariant2RecoveryOperation', {
    'runId': Required[Union[Annotated[str, Field(max_length=200)], None]],
    'idempotencyKey': Required[Annotated[str, Field(max_length=512)]],
    'state': Required[Annotated[str, Field(max_length=100)]],
})
LinkedinJobsThinOutputVariant2RecoveryOperation.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


LinkedinJobsThinOutputVariant2Recovery = TypedDict('LinkedinJobsThinOutputVariant2Recovery', {
    'idempotencyKey': NotRequired[Annotated[str, Field(max_length=512)]],
    'operationId': NotRequired[Annotated[str, Field(max_length=200)]],
    'runId': NotRequired[Annotated[str, Field(max_length=200)]],
    'jobId': NotRequired[Annotated[str, Field(max_length=200)]],
    'operation': NotRequired[LinkedinJobsThinOutputVariant2RecoveryOperation],
})
LinkedinJobsThinOutputVariant2Recovery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class LinkedinJobsThinOutputVariant2(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    delivery: LinkedinJobsThinOutputVariant2Delivery = Field(..., alias='delivery', description='')
    preview: str = Field(..., alias='preview', description='')
    scope: dict[str, Union[str, Union[float, int], bool, None]] = Field(..., alias='scope', description='')
    recovery: LinkedinJobsThinOutputVariant2Recovery = Field(..., alias='recovery', description='')


# Union schema: validate external payloads with TypeAdapter(LinkedinJobsThinOutput).
LinkedinJobsThinOutput = Union[LinkedinJobsThinOutputVariant1, LinkedinJobsThinOutputVariant2]

_LinkedinJobsThinInputAdapter = TypeAdapter(LinkedinJobsThinInput)
_LinkedinJobsThinOutputAdapter = TypeAdapter(LinkedinJobsThinOutput)