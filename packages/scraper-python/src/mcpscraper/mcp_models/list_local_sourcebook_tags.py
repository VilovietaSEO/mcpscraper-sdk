from typing import Annotated, Any, Literal, Union
from typing_extensions import NotRequired, Required, TypedDict
from pydantic import BaseModel, ConfigDict, Field, TypeAdapter


class ListLocalSourcebookTagsInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=False)

    include_deprecated: Union[bool, None] = Field(None, alias='includeDeprecated', description='Include deprecated and pending tags so the caller sees the complete directory vocabulary.')


class ListLocalSourcebookTagsOutputVariant1(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)



ListLocalSourcebookTagsOutputVariant2DeliveryArtifactsItem = TypedDict('ListLocalSourcebookTagsOutputVariant2DeliveryArtifactsItem', {
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
ListLocalSourcebookTagsOutputVariant2DeliveryArtifactsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


ListLocalSourcebookTagsOutputVariant2DeliveryAvailableExportsItem = TypedDict('ListLocalSourcebookTagsOutputVariant2DeliveryAvailableExportsItem', {
    'artifactId': Required[str],
    'sourceArtifactId': Required[str],
    'filename': Required[Literal['result.md']],
    'contentType': Required[Literal['text/markdown; charset=utf-8']],
    'state': Required[Literal['on-demand']],
})
ListLocalSourcebookTagsOutputVariant2DeliveryAvailableExportsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


ListLocalSourcebookTagsOutputVariant2DeliveryStorageFailureVariant1 = TypedDict('ListLocalSourcebookTagsOutputVariant2DeliveryStorageFailureVariant1', {
    'artifactId': Required[Union[str, None]],
    'outcome': Required[Literal['unknown', 'bytes-stored-metadata-pending', 'failed']],
})
ListLocalSourcebookTagsOutputVariant2DeliveryStorageFailureVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


ListLocalSourcebookTagsOutputVariant2Delivery = TypedDict('ListLocalSourcebookTagsOutputVariant2Delivery', {
    'mode': Required[Literal['artifact']],
    'status': Required[Literal['complete', 'partial', 'unavailable']],
    'retainedRepresentation': Required[Literal['formatted-tool-result']],
    'sourceIsError': Required[bool],
    'artifacts': Required[list[ListLocalSourcebookTagsOutputVariant2DeliveryArtifactsItem]],
    'availableExports': NotRequired[list[ListLocalSourcebookTagsOutputVariant2DeliveryAvailableExportsItem]],
    'downloadLinksOmitted': Required[bool],
    'scopeOmittedFields': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'storageFailure': Required[Union[ListLocalSourcebookTagsOutputVariant2DeliveryStorageFailureVariant1, None]],
    'nextAction': Required[str],
})
ListLocalSourcebookTagsOutputVariant2Delivery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


ListLocalSourcebookTagsOutputVariant2RecoveryOperation = TypedDict('ListLocalSourcebookTagsOutputVariant2RecoveryOperation', {
    'runId': Required[Union[Annotated[str, Field(max_length=200)], None]],
    'idempotencyKey': Required[Annotated[str, Field(max_length=512)]],
    'state': Required[Annotated[str, Field(max_length=100)]],
})
ListLocalSourcebookTagsOutputVariant2RecoveryOperation.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


ListLocalSourcebookTagsOutputVariant2Recovery = TypedDict('ListLocalSourcebookTagsOutputVariant2Recovery', {
    'idempotencyKey': NotRequired[Annotated[str, Field(max_length=512)]],
    'operationId': NotRequired[Annotated[str, Field(max_length=200)]],
    'runId': NotRequired[Annotated[str, Field(max_length=200)]],
    'jobId': NotRequired[Annotated[str, Field(max_length=200)]],
    'operation': NotRequired[ListLocalSourcebookTagsOutputVariant2RecoveryOperation],
})
ListLocalSourcebookTagsOutputVariant2Recovery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class ListLocalSourcebookTagsOutputVariant2(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    delivery: ListLocalSourcebookTagsOutputVariant2Delivery = Field(..., alias='delivery', description='')
    preview: str = Field(..., alias='preview', description='')
    scope: dict[str, Union[str, Union[float, int], bool, None]] = Field(..., alias='scope', description='')
    recovery: ListLocalSourcebookTagsOutputVariant2Recovery = Field(..., alias='recovery', description='')


# Union schema: validate external payloads with TypeAdapter(ListLocalSourcebookTagsOutput).
ListLocalSourcebookTagsOutput = Union[ListLocalSourcebookTagsOutputVariant2, ListLocalSourcebookTagsOutputVariant1]

_ListLocalSourcebookTagsInputAdapter = TypeAdapter(ListLocalSourcebookTagsInput)
_ListLocalSourcebookTagsOutputAdapter = TypeAdapter(ListLocalSourcebookTagsOutput)