from typing import Annotated, Any, Literal, Union
from typing_extensions import NotRequired, Required, TypedDict
from pydantic import BaseModel, ConfigDict, Field, TypeAdapter


class LinkedinCompanyEmployeesInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=False)

    company: Annotated[str, Field(min_length=1)] = Field(..., alias='company', description='Company name or LinkedIn company URL (e.g. google or https://www.linkedin.com/company/google/).')
    job_title: Union[Annotated[str, Field(min_length=1)], None] = Field(None, alias='jobTitle', description='Optional job-title filter supporting boolean operators (e.g. CEO OR CTO).')
    limit: Union[Annotated[int, Field(ge=1, le=10)], None] = Field(None, alias='limit', description='Maximum number of results to return (1-10, default 10).')


class LinkedinCompanyEmployeesOutputVariant1(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    tool: str = Field(..., alias='tool', description='The tool that produced this result.')
    count: Annotated[int, Field(ge=-9007199254740991, le=9007199254740991)] = Field(..., alias='count', description='Number of records returned.')
    items: list[dict[str, Any]] = Field(..., alias='items', description='Returned records. A lookup of one thing returns a single record.')
    meta: Union[dict[str, Any], None] = Field(None, alias='meta', description='Values returned alongside the records, such as nextCursor for the next page, or totals.')
    charged_credits: Union[float, int] = Field(..., alias='chargedCredits', description='Credits charged for this call.')
    duration_ms: Union[Union[float, int], None] = Field(..., alias='durationMs', description='Time taken in milliseconds.')


LinkedinCompanyEmployeesOutputVariant2DeliveryArtifactsItem = TypedDict('LinkedinCompanyEmployeesOutputVariant2DeliveryArtifactsItem', {
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
LinkedinCompanyEmployeesOutputVariant2DeliveryArtifactsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


LinkedinCompanyEmployeesOutputVariant2DeliveryAvailableExportsItem = TypedDict('LinkedinCompanyEmployeesOutputVariant2DeliveryAvailableExportsItem', {
    'artifactId': Required[str],
    'sourceArtifactId': Required[str],
    'filename': Required[Literal['result.md']],
    'contentType': Required[Literal['text/markdown; charset=utf-8']],
    'state': Required[Literal['on-demand']],
})
LinkedinCompanyEmployeesOutputVariant2DeliveryAvailableExportsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


LinkedinCompanyEmployeesOutputVariant2DeliveryStorageFailureVariant1 = TypedDict('LinkedinCompanyEmployeesOutputVariant2DeliveryStorageFailureVariant1', {
    'artifactId': Required[Union[str, None]],
    'outcome': Required[Literal['unknown', 'bytes-stored-metadata-pending', 'failed']],
})
LinkedinCompanyEmployeesOutputVariant2DeliveryStorageFailureVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


LinkedinCompanyEmployeesOutputVariant2Delivery = TypedDict('LinkedinCompanyEmployeesOutputVariant2Delivery', {
    'mode': Required[Literal['artifact']],
    'status': Required[Literal['complete', 'partial', 'unavailable']],
    'retainedRepresentation': Required[Literal['formatted-tool-result']],
    'sourceIsError': Required[bool],
    'artifacts': Required[list[LinkedinCompanyEmployeesOutputVariant2DeliveryArtifactsItem]],
    'availableExports': NotRequired[list[LinkedinCompanyEmployeesOutputVariant2DeliveryAvailableExportsItem]],
    'downloadLinksOmitted': Required[bool],
    'scopeOmittedFields': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'storageFailure': Required[Union[LinkedinCompanyEmployeesOutputVariant2DeliveryStorageFailureVariant1, None]],
    'nextAction': Required[str],
})
LinkedinCompanyEmployeesOutputVariant2Delivery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


LinkedinCompanyEmployeesOutputVariant2RecoveryOperation = TypedDict('LinkedinCompanyEmployeesOutputVariant2RecoveryOperation', {
    'runId': Required[Union[Annotated[str, Field(max_length=200)], None]],
    'idempotencyKey': Required[Annotated[str, Field(max_length=512)]],
    'state': Required[Annotated[str, Field(max_length=100)]],
})
LinkedinCompanyEmployeesOutputVariant2RecoveryOperation.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


LinkedinCompanyEmployeesOutputVariant2Recovery = TypedDict('LinkedinCompanyEmployeesOutputVariant2Recovery', {
    'idempotencyKey': NotRequired[Annotated[str, Field(max_length=512)]],
    'operationId': NotRequired[Annotated[str, Field(max_length=200)]],
    'runId': NotRequired[Annotated[str, Field(max_length=200)]],
    'jobId': NotRequired[Annotated[str, Field(max_length=200)]],
    'operation': NotRequired[LinkedinCompanyEmployeesOutputVariant2RecoveryOperation],
})
LinkedinCompanyEmployeesOutputVariant2Recovery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class LinkedinCompanyEmployeesOutputVariant2(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    delivery: LinkedinCompanyEmployeesOutputVariant2Delivery = Field(..., alias='delivery', description='')
    preview: str = Field(..., alias='preview', description='')
    scope: dict[str, Union[str, Union[float, int], bool, None]] = Field(..., alias='scope', description='')
    recovery: LinkedinCompanyEmployeesOutputVariant2Recovery = Field(..., alias='recovery', description='')


# Union schema: validate external payloads with TypeAdapter(LinkedinCompanyEmployeesOutput).
LinkedinCompanyEmployeesOutput = Union[LinkedinCompanyEmployeesOutputVariant1, LinkedinCompanyEmployeesOutputVariant2]

_LinkedinCompanyEmployeesInputAdapter = TypeAdapter(LinkedinCompanyEmployeesInput)
_LinkedinCompanyEmployeesOutputAdapter = TypeAdapter(LinkedinCompanyEmployeesOutput)