from typing import Annotated, Any, Literal, Union
from typing_extensions import NotRequired, Required, TypedDict
from pydantic import BaseModel, ConfigDict, Field, TypeAdapter


class LinkedinSearchProfilesInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=False)

    company_headcount: Union[list[Literal['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']], None] = Field(None, alias='companyHeadcount', description='Filter by current company size (employee count). Codes: A=Self-Employed, B=1-10, C=11-50, D=51-200, E=201-500, F=501-1,000, G=1,001-5,000, H=5,001-10,000, I=10,001+.')
    company_headquarter_locations: Union[list[Annotated[str, Field(min_length=1)]], None] = Field(None, alias='companyHeadquarterLocations', description="Filter by the location of the person's current company headquarters, by place name (e.g. ['United States']).")
    current_companies: Union[list[Annotated[str, Field(min_length=1)]], None] = Field(None, alias='currentCompanies', description="Filter to people who currently work at any of these companies, by name (e.g. ['Google','Meta']). Multiple names widen the match (OR).")
    exclude_company_headquarter_locations: Union[list[Annotated[str, Field(min_length=1)]], None] = Field(None, alias='excludeCompanyHeadquarterLocations', description='Exclude people whose current company is headquartered in any of these locations.')
    exclude_current_companies: Union[list[Annotated[str, Field(min_length=1)]], None] = Field(None, alias='excludeCurrentCompanies', description='Exclude people who currently work at any of these companies, by name.')
    exclude_current_job_titles: Union[list[Annotated[str, Field(min_length=1)]], None] = Field(None, alias='excludeCurrentJobTitles', description='Exclude people whose current job title matches any of these.')
    exclude_function_ids: Union[list[Literal['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26']], None] = Field(None, alias='excludeFunctionIds', description='Exclude these job functions (same codes as functionIds).')
    exclude_locations: Union[list[Annotated[str, Field(min_length=1)]], None] = Field(None, alias='excludeLocations', description='Exclude people in any of these locations, by place name.')
    exclude_past_companies: Union[list[Annotated[str, Field(min_length=1)]], None] = Field(None, alias='excludePastCompanies', description='Exclude people who previously worked at any of these companies, by name.')
    exclude_past_job_titles: Union[list[Annotated[str, Field(min_length=1)]], None] = Field(None, alias='excludePastJobTitles', description='Exclude people who held any of these past job titles.')
    exclude_schools: Union[list[Annotated[str, Field(min_length=1)]], None] = Field(None, alias='excludeSchools', description='Exclude people who attended any of these schools, by name.')
    exclude_seniority_level_ids: Union[list[Literal['100', '110', '120', '130', '200', '210', '220', '300', '310', '320']], None] = Field(None, alias='excludeSeniorityLevelIds', description='Exclude these seniority levels (same codes as seniorityLevelIds).')
    first_names: Union[list[Annotated[str, Field(min_length=1)]], None] = Field(None, alias='firstNames', description='Filter to people whose first name matches any of these.')
    function_ids: Union[list[Literal['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26']], None] = Field(None, alias='functionIds', description='Filter by job function. Codes: 1=Accounting, 2=Administrative, 3=Arts and Design, 4=Business Development, 5=Community and Social Services, 6=Consulting, 7=Education, 8=Engineering, 9=Entrepreneurship, 10=Finance, 11=Healthcare Services, 12=Human Resources, 13=Information Technology, 14=Legal, 15=Marketing, 16=Media and Communication, 17=Military and Protective Services, 18=Operations, 19=Product Management, 20=Program and Project Management, 21=Purchasing, 22=Quality Assurance, 23=Real Estate, 24=Research, 25=Sales, 26=Customer Success and Support.')
    job_title: Union[Annotated[str, Field(min_length=1)], None] = Field(None, alias='jobTitle', description="Optional current job title filter (e.g. 'Software Engineer').")
    last_names: Union[list[Annotated[str, Field(min_length=1)]], None] = Field(None, alias='lastNames', description='Filter to people whose last name matches any of these.')
    limit: Union[Annotated[int, Field(ge=1, le=25)], None] = Field(None, alias='limit', description='Maximum number of full profiles to return (1-25, default 10).')
    location: Union[Annotated[str, Field(min_length=1)], None] = Field(None, alias='location', description="Optional location filter (e.g. 'San Francisco').")
    past_companies: Union[list[Annotated[str, Field(min_length=1)]], None] = Field(None, alias='pastCompanies', description='Filter to people who previously worked at any of these companies, by name.')
    past_job_titles: Union[list[Annotated[str, Field(min_length=1)]], None] = Field(None, alias='pastJobTitles', description="Filter by a past job title the person held (e.g. ['Product Manager']).")
    profile_languages: Union[list[Literal['Arabic', 'English', 'Spanish', 'Portuguese', 'Chinese', 'French', 'Italian', 'Russian', 'German', 'Dutch', 'Turkish', 'Tagalog', 'Polish', 'Korean', 'Japanese', 'Malay', 'Norwegian', 'Danish', 'Romanian', 'Swedish', 'Bahasa Indonesia', 'Czech']], None] = Field(None, alias='profileLanguages', description="Filter by the profile's primary language.")
    query: Annotated[str, Field(min_length=1)] = Field(..., alias='query', description="Search query for LinkedIn profiles: a role, name, or keywords (e.g. 'Marketing Manager').")
    recently_changed_jobs: Union[bool, None] = Field(None, alias='recentlyChangedJobs', description='When true, only return people who recently changed jobs (a strong sales/recruiting signal).')
    recently_posted_on_linked_in: Union[bool, None] = Field(None, alias='recentlyPostedOnLinkedIn', description='When true, only return people who recently posted on LinkedIn (an activity signal).')
    schools: Union[list[Annotated[str, Field(min_length=1)]], None] = Field(None, alias='schools', description='Filter to people who attended any of these schools, by name.')
    seniority_level_ids: Union[list[Literal['100', '110', '120', '130', '200', '210', '220', '300', '310', '320']], None] = Field(None, alias='seniorityLevelIds', description='Filter by seniority level. Codes: 100=In Training, 110=Entry Level, 120=Senior, 130=Strategic, 200=Entry Level Manager, 210=Experienced Manager, 220=Director, 300=Vice President, 310=CXO, 320=Owner/Partner.')
    years_at_current_company_ids: Union[list[Literal['1', '2', '3', '4', '5']], None] = Field(None, alias='yearsAtCurrentCompanyIds', description='Filter by tenure at the current company. Codes: 1=Less than 1 year, 2=1 to 2 years, 3=3 to 5 years, 4=6 to 10 years, 5=More than 10 years.')
    years_of_experience_ids: Union[list[Literal['1', '2', '3', '4', '5']], None] = Field(None, alias='yearsOfExperienceIds', description='Filter by total years of experience. Codes: 1=Less than 1 year, 2=1 to 2 years, 3=3 to 5 years, 4=6 to 10 years, 5=More than 10 years.')


class LinkedinSearchProfilesOutputVariant1(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    tool: str = Field(..., alias='tool', description='The tool that produced this result.')
    count: Annotated[int, Field(ge=-9007199254740991, le=9007199254740991)] = Field(..., alias='count', description='Number of records returned.')
    items: list[dict[str, Any]] = Field(..., alias='items', description='Returned records. A lookup of one thing returns a single record.')
    meta: Union[dict[str, Any], None] = Field(None, alias='meta', description='Values returned alongside the records, such as nextCursor for the next page, or totals.')
    charged_credits: Union[float, int] = Field(..., alias='chargedCredits', description='Credits charged for this call.')
    duration_ms: Union[Union[float, int], None] = Field(..., alias='durationMs', description='Time taken in milliseconds.')


LinkedinSearchProfilesOutputVariant2DeliveryArtifactsItem = TypedDict('LinkedinSearchProfilesOutputVariant2DeliveryArtifactsItem', {
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
LinkedinSearchProfilesOutputVariant2DeliveryArtifactsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


LinkedinSearchProfilesOutputVariant2DeliveryAvailableExportsItem = TypedDict('LinkedinSearchProfilesOutputVariant2DeliveryAvailableExportsItem', {
    'artifactId': Required[str],
    'sourceArtifactId': Required[str],
    'filename': Required[Literal['result.md']],
    'contentType': Required[Literal['text/markdown; charset=utf-8']],
    'state': Required[Literal['on-demand']],
})
LinkedinSearchProfilesOutputVariant2DeliveryAvailableExportsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


LinkedinSearchProfilesOutputVariant2DeliveryStorageFailureVariant1 = TypedDict('LinkedinSearchProfilesOutputVariant2DeliveryStorageFailureVariant1', {
    'artifactId': Required[Union[str, None]],
    'outcome': Required[Literal['unknown', 'bytes-stored-metadata-pending', 'failed']],
})
LinkedinSearchProfilesOutputVariant2DeliveryStorageFailureVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


LinkedinSearchProfilesOutputVariant2Delivery = TypedDict('LinkedinSearchProfilesOutputVariant2Delivery', {
    'mode': Required[Literal['artifact']],
    'status': Required[Literal['complete', 'partial', 'unavailable']],
    'retainedRepresentation': Required[Literal['formatted-tool-result']],
    'sourceIsError': Required[bool],
    'artifacts': Required[list[LinkedinSearchProfilesOutputVariant2DeliveryArtifactsItem]],
    'availableExports': NotRequired[list[LinkedinSearchProfilesOutputVariant2DeliveryAvailableExportsItem]],
    'downloadLinksOmitted': Required[bool],
    'scopeOmittedFields': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'storageFailure': Required[Union[LinkedinSearchProfilesOutputVariant2DeliveryStorageFailureVariant1, None]],
    'nextAction': Required[str],
})
LinkedinSearchProfilesOutputVariant2Delivery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


LinkedinSearchProfilesOutputVariant2RecoveryOperation = TypedDict('LinkedinSearchProfilesOutputVariant2RecoveryOperation', {
    'runId': Required[Union[Annotated[str, Field(max_length=200)], None]],
    'idempotencyKey': Required[Annotated[str, Field(max_length=512)]],
    'state': Required[Annotated[str, Field(max_length=100)]],
})
LinkedinSearchProfilesOutputVariant2RecoveryOperation.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


LinkedinSearchProfilesOutputVariant2Recovery = TypedDict('LinkedinSearchProfilesOutputVariant2Recovery', {
    'idempotencyKey': NotRequired[Annotated[str, Field(max_length=512)]],
    'operationId': NotRequired[Annotated[str, Field(max_length=200)]],
    'runId': NotRequired[Annotated[str, Field(max_length=200)]],
    'jobId': NotRequired[Annotated[str, Field(max_length=200)]],
    'operation': NotRequired[LinkedinSearchProfilesOutputVariant2RecoveryOperation],
})
LinkedinSearchProfilesOutputVariant2Recovery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class LinkedinSearchProfilesOutputVariant2(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    delivery: LinkedinSearchProfilesOutputVariant2Delivery = Field(..., alias='delivery', description='')
    preview: str = Field(..., alias='preview', description='')
    scope: dict[str, Union[str, Union[float, int], bool, None]] = Field(..., alias='scope', description='')
    recovery: LinkedinSearchProfilesOutputVariant2Recovery = Field(..., alias='recovery', description='')


# Union schema: validate external payloads with TypeAdapter(LinkedinSearchProfilesOutput).
LinkedinSearchProfilesOutput = Union[LinkedinSearchProfilesOutputVariant1, LinkedinSearchProfilesOutputVariant2]

_LinkedinSearchProfilesInputAdapter = TypeAdapter(LinkedinSearchProfilesInput)
_LinkedinSearchProfilesOutputAdapter = TypeAdapter(LinkedinSearchProfilesOutput)