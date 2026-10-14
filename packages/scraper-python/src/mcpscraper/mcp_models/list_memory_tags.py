from typing import Annotated, Any, Literal, Union
from typing_extensions import NotRequired, Required, TypedDict
from pydantic import BaseModel, ConfigDict, Field, TypeAdapter


class ListMemoryTagsInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=False)

    include_deprecated: Union[bool, None] = Field(None, alias='includeDeprecated', description='Include deprecated tags as well as active tags. Defaults true so the AI sees the complete vocabulary; pass false only for an active-only display.')


ListMemoryTagsOutputVariant1TagsItem = TypedDict('ListMemoryTagsOutputVariant1TagsItem', {
    'tag': Required[str],
    'description': Required[Union[str, None]],
    'aliases': Required[list[str]],
    'status': Required[Literal['active', 'deprecated']],
    'usageCount': Required[Union[float, int]],
    'vaultUsage': Required[dict[str, Union[float, int]]],
    'control': Required[bool],
})
ListMemoryTagsOutputVariant1TagsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class ListMemoryTagsOutputVariant1(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    ok: bool = Field(..., alias='ok', description='')
    tags: Union[list[ListMemoryTagsOutputVariant1TagsItem], None] = Field(None, alias='tags', description='')
    error: Union[str, None] = Field(None, alias='error', description='')


ListMemoryTagsOutputVariant2DeliveryArtifactsItem = TypedDict('ListMemoryTagsOutputVariant2DeliveryArtifactsItem', {
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
ListMemoryTagsOutputVariant2DeliveryArtifactsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


ListMemoryTagsOutputVariant2DeliveryStorageFailureVariant1 = TypedDict('ListMemoryTagsOutputVariant2DeliveryStorageFailureVariant1', {
    'artifactId': Required[Union[str, None]],
    'outcome': Required[Literal['unknown', 'bytes-stored-metadata-pending', 'failed']],
})
ListMemoryTagsOutputVariant2DeliveryStorageFailureVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


ListMemoryTagsOutputVariant2Delivery = TypedDict('ListMemoryTagsOutputVariant2Delivery', {
    'mode': Required[Literal['artifact']],
    'status': Required[Literal['complete', 'partial', 'unavailable']],
    'retainedRepresentation': Required[Literal['formatted-tool-result']],
    'sourceIsError': Required[bool],
    'artifacts': Required[list[ListMemoryTagsOutputVariant2DeliveryArtifactsItem]],
    'downloadLinksOmitted': Required[bool],
    'scopeOmittedFields': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'storageFailure': Required[Union[ListMemoryTagsOutputVariant2DeliveryStorageFailureVariant1, None]],
    'nextAction': Required[str],
})
ListMemoryTagsOutputVariant2Delivery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


ListMemoryTagsOutputVariant2RecoveryOperation = TypedDict('ListMemoryTagsOutputVariant2RecoveryOperation', {
    'runId': Required[Union[Annotated[str, Field(max_length=200)], None]],
    'idempotencyKey': Required[Annotated[str, Field(max_length=512)]],
    'state': Required[Annotated[str, Field(max_length=100)]],
})
ListMemoryTagsOutputVariant2RecoveryOperation.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


ListMemoryTagsOutputVariant2Recovery = TypedDict('ListMemoryTagsOutputVariant2Recovery', {
    'idempotencyKey': NotRequired[Annotated[str, Field(max_length=512)]],
    'operationId': NotRequired[Annotated[str, Field(max_length=200)]],
    'runId': NotRequired[Annotated[str, Field(max_length=200)]],
    'jobId': NotRequired[Annotated[str, Field(max_length=200)]],
    'operation': NotRequired[ListMemoryTagsOutputVariant2RecoveryOperation],
})
ListMemoryTagsOutputVariant2Recovery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class ListMemoryTagsOutputVariant2(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    delivery: ListMemoryTagsOutputVariant2Delivery = Field(..., alias='delivery', description='')
    preview: str = Field(..., alias='preview', description='')
    scope: dict[str, Union[str, Union[float, int], bool, None]] = Field(..., alias='scope', description='')
    recovery: ListMemoryTagsOutputVariant2Recovery = Field(..., alias='recovery', description='')


# Union schema: validate external payloads with TypeAdapter(ListMemoryTagsOutput).
ListMemoryTagsOutput = Union[ListMemoryTagsOutputVariant2, ListMemoryTagsOutputVariant1]

_ListMemoryTagsInputAdapter = TypeAdapter(ListMemoryTagsInput)
_ListMemoryTagsOutputAdapter = TypeAdapter(ListMemoryTagsOutput)