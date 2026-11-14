from typing import Annotated, Any, Literal, Union
from typing_extensions import NotRequired, Required, TypedDict
from pydantic import BaseModel, ConfigDict, Field, TypeAdapter


class LinkedinSearchProfilesThinInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=False)

    current_company_id: Union[Annotated[str, Field(min_length=1)], None] = Field(None, alias='currentCompanyId', description='Filter by current employer, using a numeric LinkedIn company id. Comma-separate for several.')
    cursor: Union[Annotated[str, Field(min_length=1)], None] = Field(None, alias='cursor', description="Opaque pagination cursor from a previous response's nextCursor. Omit for the first page; a page holds 10 profiles.")
    first_name: Union[Annotated[str, Field(min_length=1)], None] = Field(None, alias='firstName', description='Filter by first name (e.g. Jane).')
    follower_of_urn: Union[Annotated[str, Field(min_length=1)], None] = Field(None, alias='followerOfUrn', description="Return only people who follow this member, given the member's LinkedIn URN.")
    industry_id: Union[Annotated[str, Field(min_length=1)], None] = Field(None, alias='industryId', description='Filter by industry, using a LinkedIn industry id.')
    last_name: Union[Annotated[str, Field(min_length=1)], None] = Field(None, alias='lastName', description='Filter by last name (e.g. Okafor).')
    location_id: Union[Annotated[str, Field(min_length=1)], None] = Field(None, alias='locationId', description='Filter by location, using a LinkedIn geocode id.')
    past_company_id: Union[Annotated[str, Field(min_length=1)], None] = Field(None, alias='pastCompanyId', description='Filter by a previous employer, using a numeric LinkedIn company id.')
    profile_language: Union[Annotated[str, Field(min_length=1)], None] = Field(None, alias='profileLanguage', description='Filter by the language the profile is written in (ISO 2-letter code, e.g. en).')
    query: Annotated[str, Field(min_length=1)] = Field(..., alias='query', description="Search query for LinkedIn profiles - a role, name, or keywords (e.g. 'Marketing Manager').")
    school_id: Union[Annotated[str, Field(min_length=1)], None] = Field(None, alias='schoolId', description='Filter by school, using a LinkedIn school id.')
    service_category_id: Union[Annotated[str, Field(min_length=1)], None] = Field(None, alias='serviceCategoryId', description='Filter by service category, using a numeric service-category id.')
    title: Union[Annotated[str, Field(min_length=1)], None] = Field(None, alias='title', description='Filter by job title or headline (e.g. Head of Talent).')


class LinkedinSearchProfilesThinOutputVariant1(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    tool: str = Field(..., alias='tool', description='The tool that produced this result.')
    count: Annotated[int, Field(ge=-9007199254740991, le=9007199254740991)] = Field(..., alias='count', description='Number of records returned.')
    items: list[dict[str, Any]] = Field(..., alias='items', description='Returned records. A lookup of one thing returns a single record.')
    meta: Union[dict[str, Any], None] = Field(None, alias='meta', description='Values returned alongside the records, such as nextCursor for the next page, or totals.')
    charged_credits: Union[float, int] = Field(..., alias='chargedCredits', description='Credits charged for this call.')
    duration_ms: Union[Union[float, int], None] = Field(..., alias='durationMs', description='Time taken in milliseconds.')


LinkedinSearchProfilesThinOutputVariant2DeliveryArtifactsItem = TypedDict('LinkedinSearchProfilesThinOutputVariant2DeliveryArtifactsItem', {
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
LinkedinSearchProfilesThinOutputVariant2DeliveryArtifactsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


LinkedinSearchProfilesThinOutputVariant2DeliveryAvailableExportsItem = TypedDict('LinkedinSearchProfilesThinOutputVariant2DeliveryAvailableExportsItem', {
    'artifactId': Required[str],
    'sourceArtifactId': Required[str],
    'filename': Required[Literal['result.md']],
    'contentType': Required[Literal['text/markdown; charset=utf-8']],
    'state': Required[Literal['on-demand']],
})
LinkedinSearchProfilesThinOutputVariant2DeliveryAvailableExportsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


LinkedinSearchProfilesThinOutputVariant2DeliveryStorageFailureVariant1 = TypedDict('LinkedinSearchProfilesThinOutputVariant2DeliveryStorageFailureVariant1', {
    'artifactId': Required[Union[str, None]],
    'outcome': Required[Literal['unknown', 'bytes-stored-metadata-pending', 'failed']],
})
LinkedinSearchProfilesThinOutputVariant2DeliveryStorageFailureVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


LinkedinSearchProfilesThinOutputVariant2Delivery = TypedDict('LinkedinSearchProfilesThinOutputVariant2Delivery', {
    'mode': Required[Literal['artifact']],
    'status': Required[Literal['complete', 'partial', 'unavailable']],
    'retainedRepresentation': Required[Literal['formatted-tool-result']],
    'sourceIsError': Required[bool],
    'artifacts': Required[list[LinkedinSearchProfilesThinOutputVariant2DeliveryArtifactsItem]],
    'availableExports': NotRequired[list[LinkedinSearchProfilesThinOutputVariant2DeliveryAvailableExportsItem]],
    'downloadLinksOmitted': Required[bool],
    'scopeOmittedFields': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'storageFailure': Required[Union[LinkedinSearchProfilesThinOutputVariant2DeliveryStorageFailureVariant1, None]],
    'nextAction': Required[str],
})
LinkedinSearchProfilesThinOutputVariant2Delivery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


LinkedinSearchProfilesThinOutputVariant2RecoveryOperation = TypedDict('LinkedinSearchProfilesThinOutputVariant2RecoveryOperation', {
    'runId': Required[Union[Annotated[str, Field(max_length=200)], None]],
    'idempotencyKey': Required[Annotated[str, Field(max_length=512)]],
    'state': Required[Annotated[str, Field(max_length=100)]],
})
LinkedinSearchProfilesThinOutputVariant2RecoveryOperation.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


LinkedinSearchProfilesThinOutputVariant2Recovery = TypedDict('LinkedinSearchProfilesThinOutputVariant2Recovery', {
    'idempotencyKey': NotRequired[Annotated[str, Field(max_length=512)]],
    'operationId': NotRequired[Annotated[str, Field(max_length=200)]],
    'runId': NotRequired[Annotated[str, Field(max_length=200)]],
    'jobId': NotRequired[Annotated[str, Field(max_length=200)]],
    'operation': NotRequired[LinkedinSearchProfilesThinOutputVariant2RecoveryOperation],
})
LinkedinSearchProfilesThinOutputVariant2Recovery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class LinkedinSearchProfilesThinOutputVariant2(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    delivery: LinkedinSearchProfilesThinOutputVariant2Delivery = Field(..., alias='delivery', description='')
    preview: str = Field(..., alias='preview', description='')
    scope: dict[str, Union[str, Union[float, int], bool, None]] = Field(..., alias='scope', description='')
    recovery: LinkedinSearchProfilesThinOutputVariant2Recovery = Field(..., alias='recovery', description='')


# Union schema: validate external payloads with TypeAdapter(LinkedinSearchProfilesThinOutput).
LinkedinSearchProfilesThinOutput = Union[LinkedinSearchProfilesThinOutputVariant1, LinkedinSearchProfilesThinOutputVariant2]

_LinkedinSearchProfilesThinInputAdapter = TypeAdapter(LinkedinSearchProfilesThinInput)
_LinkedinSearchProfilesThinOutputAdapter = TypeAdapter(LinkedinSearchProfilesThinOutput)