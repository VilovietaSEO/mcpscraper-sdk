from typing import Annotated, Any, Literal, Union
from typing_extensions import NotRequired, Required, TypedDict
from pydantic import BaseModel, ConfigDict, Field, TypeAdapter


class UpsertMemoryTagInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=False)

    tag: Annotated[str, Field(min_length=1)] = Field(..., alias='tag', description='Canonical tag name to create or curate.')
    description: Union[str, None] = Field(None, alias='description', description='Human-readable summary that distinguishes this record from similarly named records.')
    aliases: Union[list[str], None] = Field(None, alias='aliases', description='Alternative spellings that should resolve to this canonical value.')
    status: Union[Literal['active', 'deprecated'], None] = Field(None, alias='status', description='Lifecycle status used to filter or update the selected records.')


UpsertMemoryTagOutputVariant1Tag = TypedDict('UpsertMemoryTagOutputVariant1Tag', {
    'tag': Required[str],
    'description': Required[Union[str, None]],
    'aliases': Required[list[str]],
    'status': Required[Literal['active', 'deprecated']],
})
UpsertMemoryTagOutputVariant1Tag.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class UpsertMemoryTagOutputVariant1(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    ok: bool = Field(..., alias='ok', description='')
    tag: Union[UpsertMemoryTagOutputVariant1Tag, None] = Field(None, alias='tag', description='')
    error: Union[str, None] = Field(None, alias='error', description='')


UpsertMemoryTagOutputVariant2DeliveryArtifactsItem = TypedDict('UpsertMemoryTagOutputVariant2DeliveryArtifactsItem', {
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
UpsertMemoryTagOutputVariant2DeliveryArtifactsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


UpsertMemoryTagOutputVariant2DeliveryStorageFailureVariant1 = TypedDict('UpsertMemoryTagOutputVariant2DeliveryStorageFailureVariant1', {
    'artifactId': Required[Union[str, None]],
    'outcome': Required[Literal['unknown', 'bytes-stored-metadata-pending', 'failed']],
})
UpsertMemoryTagOutputVariant2DeliveryStorageFailureVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


UpsertMemoryTagOutputVariant2Delivery = TypedDict('UpsertMemoryTagOutputVariant2Delivery', {
    'mode': Required[Literal['artifact']],
    'status': Required[Literal['complete', 'partial', 'unavailable']],
    'retainedRepresentation': Required[Literal['formatted-tool-result']],
    'sourceIsError': Required[bool],
    'artifacts': Required[list[UpsertMemoryTagOutputVariant2DeliveryArtifactsItem]],
    'downloadLinksOmitted': Required[bool],
    'scopeOmittedFields': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'storageFailure': Required[Union[UpsertMemoryTagOutputVariant2DeliveryStorageFailureVariant1, None]],
    'nextAction': Required[str],
})
UpsertMemoryTagOutputVariant2Delivery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


UpsertMemoryTagOutputVariant2RecoveryOperation = TypedDict('UpsertMemoryTagOutputVariant2RecoveryOperation', {
    'runId': Required[Union[Annotated[str, Field(max_length=200)], None]],
    'idempotencyKey': Required[Annotated[str, Field(max_length=512)]],
    'state': Required[Annotated[str, Field(max_length=100)]],
})
UpsertMemoryTagOutputVariant2RecoveryOperation.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


UpsertMemoryTagOutputVariant2Recovery = TypedDict('UpsertMemoryTagOutputVariant2Recovery', {
    'idempotencyKey': NotRequired[Annotated[str, Field(max_length=512)]],
    'operationId': NotRequired[Annotated[str, Field(max_length=200)]],
    'runId': NotRequired[Annotated[str, Field(max_length=200)]],
    'jobId': NotRequired[Annotated[str, Field(max_length=200)]],
    'operation': NotRequired[UpsertMemoryTagOutputVariant2RecoveryOperation],
})
UpsertMemoryTagOutputVariant2Recovery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class UpsertMemoryTagOutputVariant2(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    delivery: UpsertMemoryTagOutputVariant2Delivery = Field(..., alias='delivery', description='')
    preview: str = Field(..., alias='preview', description='')
    scope: dict[str, Union[str, Union[float, int], bool, None]] = Field(..., alias='scope', description='')
    recovery: UpsertMemoryTagOutputVariant2Recovery = Field(..., alias='recovery', description='')


# Union schema: validate external payloads with TypeAdapter(UpsertMemoryTagOutput).
UpsertMemoryTagOutput = Union[UpsertMemoryTagOutputVariant2, UpsertMemoryTagOutputVariant1]

_UpsertMemoryTagInputAdapter = TypeAdapter(UpsertMemoryTagInput)
_UpsertMemoryTagOutputAdapter = TypeAdapter(UpsertMemoryTagOutput)