from typing import Annotated, Any, Literal, Union
from typing_extensions import NotRequired, Required, TypedDict
from pydantic import BaseModel, ConfigDict, Field, TypeAdapter


class MemorySuggestInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=False)

    query: Annotated[str, Field(min_length=1)] = Field(..., alias='query', description='Partial text typed so far, e.g. "what is the best r".')
    limit: Union[Annotated[int, Field(ge=1, le=20)], None] = Field(None, alias='limit', description='Max suggestions to return. Optional; default 8.')


MemorySuggestOutputVariant1SuggestionsItem = TypedDict('MemorySuggestOutputVariant1SuggestionsItem', {
    'vault': Required[str],
    'path': Required[str],
    'title': Required[str],
    'kind': Required[str],
})
MemorySuggestOutputVariant1SuggestionsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class MemorySuggestOutputVariant1(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    ok: bool = Field(..., alias='ok', description='True when the lookup ran; false on auth error.')
    suggestions: Union[list[MemorySuggestOutputVariant1SuggestionsItem], None] = Field(None, alias='suggestions', description='Title matches ordered prefix-first then most-recent. Present when ok is true; may be empty.')
    error: Union[str, None] = Field(None, alias='error', description='Human-readable failure reason when ok is false.')


MemorySuggestOutputVariant2DeliveryArtifactsItem = TypedDict('MemorySuggestOutputVariant2DeliveryArtifactsItem', {
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
MemorySuggestOutputVariant2DeliveryArtifactsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


MemorySuggestOutputVariant2DeliveryStorageFailureVariant1 = TypedDict('MemorySuggestOutputVariant2DeliveryStorageFailureVariant1', {
    'artifactId': Required[Union[str, None]],
    'outcome': Required[Literal['unknown', 'bytes-stored-metadata-pending', 'failed']],
})
MemorySuggestOutputVariant2DeliveryStorageFailureVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


MemorySuggestOutputVariant2Delivery = TypedDict('MemorySuggestOutputVariant2Delivery', {
    'mode': Required[Literal['artifact']],
    'status': Required[Literal['complete', 'partial', 'unavailable']],
    'retainedRepresentation': Required[Literal['formatted-tool-result']],
    'sourceIsError': Required[bool],
    'artifacts': Required[list[MemorySuggestOutputVariant2DeliveryArtifactsItem]],
    'downloadLinksOmitted': Required[bool],
    'scopeOmittedFields': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'storageFailure': Required[Union[MemorySuggestOutputVariant2DeliveryStorageFailureVariant1, None]],
    'nextAction': Required[str],
})
MemorySuggestOutputVariant2Delivery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


MemorySuggestOutputVariant2RecoveryOperation = TypedDict('MemorySuggestOutputVariant2RecoveryOperation', {
    'runId': Required[Union[Annotated[str, Field(max_length=200)], None]],
    'idempotencyKey': Required[Annotated[str, Field(max_length=512)]],
    'state': Required[Annotated[str, Field(max_length=100)]],
})
MemorySuggestOutputVariant2RecoveryOperation.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


MemorySuggestOutputVariant2Recovery = TypedDict('MemorySuggestOutputVariant2Recovery', {
    'idempotencyKey': NotRequired[Annotated[str, Field(max_length=512)]],
    'operationId': NotRequired[Annotated[str, Field(max_length=200)]],
    'runId': NotRequired[Annotated[str, Field(max_length=200)]],
    'jobId': NotRequired[Annotated[str, Field(max_length=200)]],
    'operation': NotRequired[MemorySuggestOutputVariant2RecoveryOperation],
})
MemorySuggestOutputVariant2Recovery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class MemorySuggestOutputVariant2(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    delivery: MemorySuggestOutputVariant2Delivery = Field(..., alias='delivery', description='')
    preview: str = Field(..., alias='preview', description='')
    scope: dict[str, Union[str, Union[float, int], bool, None]] = Field(..., alias='scope', description='')
    recovery: MemorySuggestOutputVariant2Recovery = Field(..., alias='recovery', description='')


# Union schema: validate external payloads with TypeAdapter(MemorySuggestOutput).
MemorySuggestOutput = Union[MemorySuggestOutputVariant2, MemorySuggestOutputVariant1]

_MemorySuggestInputAdapter = TypeAdapter(MemorySuggestInput)
_MemorySuggestOutputAdapter = TypeAdapter(MemorySuggestOutput)