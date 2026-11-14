from typing import Annotated, Any, Literal, Union
from typing_extensions import NotRequired, Required, TypedDict
from pydantic import BaseModel, ConfigDict, Field, TypeAdapter


class LinkedinSearchServicesInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=False)

    geo_id: Union[Annotated[str, Field(min_length=1)], None] = Field(None, alias='geoId', description='LinkedIn geo id to target a precise location (e.g. 103644278 for the United States); more exact than the free-text location, and overrides it when both are sent.')
    location: Union[Annotated[str, Field(min_length=1)], None] = Field(None, alias='location', description="Optional location filter as a place name (e.g. 'Australia', 'New York').")
    page: Union[Annotated[int, Field(ge=1, le=100)], None] = Field(None, alias='page', description='Which page of up to 10 people to return, starting at 1 (1-100, default 1).')
    query: Annotated[str, Field(min_length=1)] = Field(..., alias='query', description="The service to search for, as keywords (e.g. 'Web Development', 'Accounting', 'Photography').")


class LinkedinSearchServicesOutputVariant1(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    tool: str = Field(..., alias='tool', description='The tool that produced this result.')
    count: Annotated[int, Field(ge=-9007199254740991, le=9007199254740991)] = Field(..., alias='count', description='Number of records returned.')
    items: list[dict[str, Any]] = Field(..., alias='items', description='Returned records. A lookup of one thing returns a single record.')
    meta: Union[dict[str, Any], None] = Field(None, alias='meta', description='Values returned alongside the records, such as nextCursor for the next page, or totals.')
    charged_credits: Union[float, int] = Field(..., alias='chargedCredits', description='Credits charged for this call.')
    duration_ms: Union[Union[float, int], None] = Field(..., alias='durationMs', description='Time taken in milliseconds.')


LinkedinSearchServicesOutputVariant2DeliveryArtifactsItem = TypedDict('LinkedinSearchServicesOutputVariant2DeliveryArtifactsItem', {
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
LinkedinSearchServicesOutputVariant2DeliveryArtifactsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


LinkedinSearchServicesOutputVariant2DeliveryAvailableExportsItem = TypedDict('LinkedinSearchServicesOutputVariant2DeliveryAvailableExportsItem', {
    'artifactId': Required[str],
    'sourceArtifactId': Required[str],
    'filename': Required[Literal['result.md']],
    'contentType': Required[Literal['text/markdown; charset=utf-8']],
    'state': Required[Literal['on-demand']],
})
LinkedinSearchServicesOutputVariant2DeliveryAvailableExportsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


LinkedinSearchServicesOutputVariant2DeliveryStorageFailureVariant1 = TypedDict('LinkedinSearchServicesOutputVariant2DeliveryStorageFailureVariant1', {
    'artifactId': Required[Union[str, None]],
    'outcome': Required[Literal['unknown', 'bytes-stored-metadata-pending', 'failed']],
})
LinkedinSearchServicesOutputVariant2DeliveryStorageFailureVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


LinkedinSearchServicesOutputVariant2Delivery = TypedDict('LinkedinSearchServicesOutputVariant2Delivery', {
    'mode': Required[Literal['artifact']],
    'status': Required[Literal['complete', 'partial', 'unavailable']],
    'retainedRepresentation': Required[Literal['formatted-tool-result']],
    'sourceIsError': Required[bool],
    'artifacts': Required[list[LinkedinSearchServicesOutputVariant2DeliveryArtifactsItem]],
    'availableExports': NotRequired[list[LinkedinSearchServicesOutputVariant2DeliveryAvailableExportsItem]],
    'downloadLinksOmitted': Required[bool],
    'scopeOmittedFields': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'storageFailure': Required[Union[LinkedinSearchServicesOutputVariant2DeliveryStorageFailureVariant1, None]],
    'nextAction': Required[str],
})
LinkedinSearchServicesOutputVariant2Delivery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


LinkedinSearchServicesOutputVariant2RecoveryOperation = TypedDict('LinkedinSearchServicesOutputVariant2RecoveryOperation', {
    'runId': Required[Union[Annotated[str, Field(max_length=200)], None]],
    'idempotencyKey': Required[Annotated[str, Field(max_length=512)]],
    'state': Required[Annotated[str, Field(max_length=100)]],
})
LinkedinSearchServicesOutputVariant2RecoveryOperation.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


LinkedinSearchServicesOutputVariant2Recovery = TypedDict('LinkedinSearchServicesOutputVariant2Recovery', {
    'idempotencyKey': NotRequired[Annotated[str, Field(max_length=512)]],
    'operationId': NotRequired[Annotated[str, Field(max_length=200)]],
    'runId': NotRequired[Annotated[str, Field(max_length=200)]],
    'jobId': NotRequired[Annotated[str, Field(max_length=200)]],
    'operation': NotRequired[LinkedinSearchServicesOutputVariant2RecoveryOperation],
})
LinkedinSearchServicesOutputVariant2Recovery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class LinkedinSearchServicesOutputVariant2(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    delivery: LinkedinSearchServicesOutputVariant2Delivery = Field(..., alias='delivery', description='')
    preview: str = Field(..., alias='preview', description='')
    scope: dict[str, Union[str, Union[float, int], bool, None]] = Field(..., alias='scope', description='')
    recovery: LinkedinSearchServicesOutputVariant2Recovery = Field(..., alias='recovery', description='')


# Union schema: validate external payloads with TypeAdapter(LinkedinSearchServicesOutput).
LinkedinSearchServicesOutput = Union[LinkedinSearchServicesOutputVariant1, LinkedinSearchServicesOutputVariant2]

_LinkedinSearchServicesInputAdapter = TypeAdapter(LinkedinSearchServicesInput)
_LinkedinSearchServicesOutputAdapter = TypeAdapter(LinkedinSearchServicesOutput)