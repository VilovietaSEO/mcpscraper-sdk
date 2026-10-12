from typing import Annotated, Any, Literal, Union
from typing_extensions import NotRequired, Required, TypedDict
from pydantic import BaseModel, ConfigDict, Field, TypeAdapter


class LocalSourcebookRefreshInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=False)

    submission_id: Annotated[str, Field(min_length=1)] = Field(..., alias='submissionId', description='Owner-scoped listing submission to re-crawl and refresh.')


class LocalSourcebookRefreshOutputVariant1(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)



LocalSourcebookRefreshOutputVariant2DeliveryArtifactsItem = TypedDict('LocalSourcebookRefreshOutputVariant2DeliveryArtifactsItem', {
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
LocalSourcebookRefreshOutputVariant2DeliveryArtifactsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


LocalSourcebookRefreshOutputVariant2DeliveryStorageFailureVariant1 = TypedDict('LocalSourcebookRefreshOutputVariant2DeliveryStorageFailureVariant1', {
    'artifactId': Required[Union[str, None]],
    'outcome': Required[Literal['unknown', 'bytes-stored-metadata-pending', 'failed']],
})
LocalSourcebookRefreshOutputVariant2DeliveryStorageFailureVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


LocalSourcebookRefreshOutputVariant2Delivery = TypedDict('LocalSourcebookRefreshOutputVariant2Delivery', {
    'mode': Required[Literal['artifact']],
    'status': Required[Literal['complete', 'partial', 'unavailable']],
    'retainedRepresentation': Required[Literal['formatted-tool-result']],
    'sourceIsError': Required[bool],
    'artifacts': Required[list[LocalSourcebookRefreshOutputVariant2DeliveryArtifactsItem]],
    'downloadLinksOmitted': Required[bool],
    'scopeOmittedFields': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'storageFailure': Required[Union[LocalSourcebookRefreshOutputVariant2DeliveryStorageFailureVariant1, None]],
    'nextAction': Required[str],
})
LocalSourcebookRefreshOutputVariant2Delivery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


LocalSourcebookRefreshOutputVariant2RecoveryOperation = TypedDict('LocalSourcebookRefreshOutputVariant2RecoveryOperation', {
    'runId': Required[Union[Annotated[str, Field(max_length=200)], None]],
    'idempotencyKey': Required[Annotated[str, Field(max_length=512)]],
    'state': Required[Annotated[str, Field(max_length=100)]],
})
LocalSourcebookRefreshOutputVariant2RecoveryOperation.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


LocalSourcebookRefreshOutputVariant2Recovery = TypedDict('LocalSourcebookRefreshOutputVariant2Recovery', {
    'idempotencyKey': NotRequired[Annotated[str, Field(max_length=512)]],
    'operationId': NotRequired[Annotated[str, Field(max_length=200)]],
    'runId': NotRequired[Annotated[str, Field(max_length=200)]],
    'jobId': NotRequired[Annotated[str, Field(max_length=200)]],
    'operation': NotRequired[LocalSourcebookRefreshOutputVariant2RecoveryOperation],
})
LocalSourcebookRefreshOutputVariant2Recovery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class LocalSourcebookRefreshOutputVariant2(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    delivery: LocalSourcebookRefreshOutputVariant2Delivery = Field(..., alias='delivery', description='')
    preview: str = Field(..., alias='preview', description='')
    scope: dict[str, Union[str, Union[float, int], bool, None]] = Field(..., alias='scope', description='')
    recovery: LocalSourcebookRefreshOutputVariant2Recovery = Field(..., alias='recovery', description='')


# Union schema: validate external payloads with TypeAdapter(LocalSourcebookRefreshOutput).
LocalSourcebookRefreshOutput = Union[LocalSourcebookRefreshOutputVariant2, LocalSourcebookRefreshOutputVariant1]

_LocalSourcebookRefreshInputAdapter = TypeAdapter(LocalSourcebookRefreshInput)
_LocalSourcebookRefreshOutputAdapter = TypeAdapter(LocalSourcebookRefreshOutput)