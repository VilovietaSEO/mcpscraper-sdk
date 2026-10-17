from typing import Annotated, Any, Literal, Union
from typing_extensions import NotRequired, Required, TypedDict
from pydantic import BaseModel, ConfigDict, Field, TypeAdapter


class LocalSourcebookSubmissionStatusInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=False)

    submission_id: Annotated[str, Field(min_length=1)] = Field(..., alias='submissionId', description='The owner-scoped submission ID returned by local-sourcebook-capture.')


class LocalSourcebookSubmissionStatusOutputVariant1(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)



LocalSourcebookSubmissionStatusOutputVariant2DeliveryArtifactsItem = TypedDict('LocalSourcebookSubmissionStatusOutputVariant2DeliveryArtifactsItem', {
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
LocalSourcebookSubmissionStatusOutputVariant2DeliveryArtifactsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


LocalSourcebookSubmissionStatusOutputVariant2DeliveryAvailableExportsItem = TypedDict('LocalSourcebookSubmissionStatusOutputVariant2DeliveryAvailableExportsItem', {
    'artifactId': Required[str],
    'sourceArtifactId': Required[str],
    'filename': Required[Literal['result.md']],
    'contentType': Required[Literal['text/markdown; charset=utf-8']],
    'state': Required[Literal['on-demand']],
})
LocalSourcebookSubmissionStatusOutputVariant2DeliveryAvailableExportsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


LocalSourcebookSubmissionStatusOutputVariant2DeliveryStorageFailureVariant1 = TypedDict('LocalSourcebookSubmissionStatusOutputVariant2DeliveryStorageFailureVariant1', {
    'artifactId': Required[Union[str, None]],
    'outcome': Required[Literal['unknown', 'bytes-stored-metadata-pending', 'failed']],
})
LocalSourcebookSubmissionStatusOutputVariant2DeliveryStorageFailureVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


LocalSourcebookSubmissionStatusOutputVariant2Delivery = TypedDict('LocalSourcebookSubmissionStatusOutputVariant2Delivery', {
    'mode': Required[Literal['artifact']],
    'status': Required[Literal['complete', 'partial', 'unavailable']],
    'retainedRepresentation': Required[Literal['formatted-tool-result']],
    'sourceIsError': Required[bool],
    'artifacts': Required[list[LocalSourcebookSubmissionStatusOutputVariant2DeliveryArtifactsItem]],
    'availableExports': NotRequired[list[LocalSourcebookSubmissionStatusOutputVariant2DeliveryAvailableExportsItem]],
    'downloadLinksOmitted': Required[bool],
    'scopeOmittedFields': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'storageFailure': Required[Union[LocalSourcebookSubmissionStatusOutputVariant2DeliveryStorageFailureVariant1, None]],
    'nextAction': Required[str],
})
LocalSourcebookSubmissionStatusOutputVariant2Delivery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


LocalSourcebookSubmissionStatusOutputVariant2RecoveryOperation = TypedDict('LocalSourcebookSubmissionStatusOutputVariant2RecoveryOperation', {
    'runId': Required[Union[Annotated[str, Field(max_length=200)], None]],
    'idempotencyKey': Required[Annotated[str, Field(max_length=512)]],
    'state': Required[Annotated[str, Field(max_length=100)]],
})
LocalSourcebookSubmissionStatusOutputVariant2RecoveryOperation.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


LocalSourcebookSubmissionStatusOutputVariant2Recovery = TypedDict('LocalSourcebookSubmissionStatusOutputVariant2Recovery', {
    'idempotencyKey': NotRequired[Annotated[str, Field(max_length=512)]],
    'operationId': NotRequired[Annotated[str, Field(max_length=200)]],
    'runId': NotRequired[Annotated[str, Field(max_length=200)]],
    'jobId': NotRequired[Annotated[str, Field(max_length=200)]],
    'operation': NotRequired[LocalSourcebookSubmissionStatusOutputVariant2RecoveryOperation],
})
LocalSourcebookSubmissionStatusOutputVariant2Recovery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class LocalSourcebookSubmissionStatusOutputVariant2(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    delivery: LocalSourcebookSubmissionStatusOutputVariant2Delivery = Field(..., alias='delivery', description='')
    preview: str = Field(..., alias='preview', description='')
    scope: dict[str, Union[str, Union[float, int], bool, None]] = Field(..., alias='scope', description='')
    recovery: LocalSourcebookSubmissionStatusOutputVariant2Recovery = Field(..., alias='recovery', description='')


# Union schema: validate external payloads with TypeAdapter(LocalSourcebookSubmissionStatusOutput).
LocalSourcebookSubmissionStatusOutput = Union[LocalSourcebookSubmissionStatusOutputVariant2, LocalSourcebookSubmissionStatusOutputVariant1]

_LocalSourcebookSubmissionStatusInputAdapter = TypeAdapter(LocalSourcebookSubmissionStatusInput)
_LocalSourcebookSubmissionStatusOutputAdapter = TypeAdapter(LocalSourcebookSubmissionStatusOutput)