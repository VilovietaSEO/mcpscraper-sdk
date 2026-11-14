from typing import Annotated, Any, Literal, Union
from typing_extensions import NotRequired, Required, TypedDict
from pydantic import BaseModel, ConfigDict, Field, TypeAdapter


class LinkedinAdsSearchInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=False)

    company: Union[Annotated[str, Field(min_length=1)], None] = Field(None, alias='company', description='Company name to search (e.g. "microsoft").')
    company_id: Union[Annotated[str, Field(min_length=1)], None] = Field(None, alias='companyId', description='LinkedIn company identifier.')
    countries: Union[Annotated[str, Field(min_length=1)], None] = Field(None, alias='countries', description='Comma-separated two-letter country codes (e.g. "US,CA,MX").')
    cursor: Union[Annotated[str, Field(min_length=1)], None] = Field(None, alias='cursor', description="Opaque pagination cursor from a previous response's nextCursor; omit for the first page.")
    end_date: Union[Annotated[str, Field(min_length=1)], None] = Field(None, alias='endDate', description="Search end date in YYYY-MM-DD format. Today or a later date is moved back to yesterday in UTC when your range overlaps LinkedIn's accepted dates.")
    keyword: Union[Annotated[str, Field(min_length=1)], None] = Field(None, alias='keyword', description='Keyword term for the ad search.')
    start_date: Union[Annotated[str, Field(min_length=1)], None] = Field(None, alias='startDate', description="Search start date in YYYY-MM-DD format. An earlier date is moved up to one year ago in UTC when your range overlaps LinkedIn's accepted dates.")


class LinkedinAdsSearchOutputVariant1(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    tool: str = Field(..., alias='tool', description='The tool that produced this result.')
    count: Annotated[int, Field(ge=-9007199254740991, le=9007199254740991)] = Field(..., alias='count', description='Number of records returned.')
    items: list[dict[str, Any]] = Field(..., alias='items', description='Returned records. A lookup of one thing returns a single record.')
    meta: Union[dict[str, Any], None] = Field(None, alias='meta', description='Values returned alongside the records, such as nextCursor for the next page, or totals.')
    charged_credits: Union[float, int] = Field(..., alias='chargedCredits', description='Credits charged for this call.')
    duration_ms: Union[Union[float, int], None] = Field(..., alias='durationMs', description='Time taken in milliseconds.')


LinkedinAdsSearchOutputVariant2DeliveryArtifactsItem = TypedDict('LinkedinAdsSearchOutputVariant2DeliveryArtifactsItem', {
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
LinkedinAdsSearchOutputVariant2DeliveryArtifactsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


LinkedinAdsSearchOutputVariant2DeliveryAvailableExportsItem = TypedDict('LinkedinAdsSearchOutputVariant2DeliveryAvailableExportsItem', {
    'artifactId': Required[str],
    'sourceArtifactId': Required[str],
    'filename': Required[Literal['result.md']],
    'contentType': Required[Literal['text/markdown; charset=utf-8']],
    'state': Required[Literal['on-demand']],
})
LinkedinAdsSearchOutputVariant2DeliveryAvailableExportsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


LinkedinAdsSearchOutputVariant2DeliveryStorageFailureVariant1 = TypedDict('LinkedinAdsSearchOutputVariant2DeliveryStorageFailureVariant1', {
    'artifactId': Required[Union[str, None]],
    'outcome': Required[Literal['unknown', 'bytes-stored-metadata-pending', 'failed']],
})
LinkedinAdsSearchOutputVariant2DeliveryStorageFailureVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


LinkedinAdsSearchOutputVariant2Delivery = TypedDict('LinkedinAdsSearchOutputVariant2Delivery', {
    'mode': Required[Literal['artifact']],
    'status': Required[Literal['complete', 'partial', 'unavailable']],
    'retainedRepresentation': Required[Literal['formatted-tool-result']],
    'sourceIsError': Required[bool],
    'artifacts': Required[list[LinkedinAdsSearchOutputVariant2DeliveryArtifactsItem]],
    'availableExports': NotRequired[list[LinkedinAdsSearchOutputVariant2DeliveryAvailableExportsItem]],
    'downloadLinksOmitted': Required[bool],
    'scopeOmittedFields': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'storageFailure': Required[Union[LinkedinAdsSearchOutputVariant2DeliveryStorageFailureVariant1, None]],
    'nextAction': Required[str],
})
LinkedinAdsSearchOutputVariant2Delivery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


LinkedinAdsSearchOutputVariant2RecoveryOperation = TypedDict('LinkedinAdsSearchOutputVariant2RecoveryOperation', {
    'runId': Required[Union[Annotated[str, Field(max_length=200)], None]],
    'idempotencyKey': Required[Annotated[str, Field(max_length=512)]],
    'state': Required[Annotated[str, Field(max_length=100)]],
})
LinkedinAdsSearchOutputVariant2RecoveryOperation.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


LinkedinAdsSearchOutputVariant2Recovery = TypedDict('LinkedinAdsSearchOutputVariant2Recovery', {
    'idempotencyKey': NotRequired[Annotated[str, Field(max_length=512)]],
    'operationId': NotRequired[Annotated[str, Field(max_length=200)]],
    'runId': NotRequired[Annotated[str, Field(max_length=200)]],
    'jobId': NotRequired[Annotated[str, Field(max_length=200)]],
    'operation': NotRequired[LinkedinAdsSearchOutputVariant2RecoveryOperation],
})
LinkedinAdsSearchOutputVariant2Recovery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class LinkedinAdsSearchOutputVariant2(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    delivery: LinkedinAdsSearchOutputVariant2Delivery = Field(..., alias='delivery', description='')
    preview: str = Field(..., alias='preview', description='')
    scope: dict[str, Union[str, Union[float, int], bool, None]] = Field(..., alias='scope', description='')
    recovery: LinkedinAdsSearchOutputVariant2Recovery = Field(..., alias='recovery', description='')


# Union schema: validate external payloads with TypeAdapter(LinkedinAdsSearchOutput).
LinkedinAdsSearchOutput = Union[LinkedinAdsSearchOutputVariant1, LinkedinAdsSearchOutputVariant2]

_LinkedinAdsSearchInputAdapter = TypeAdapter(LinkedinAdsSearchInput)
_LinkedinAdsSearchOutputAdapter = TypeAdapter(LinkedinAdsSearchOutput)