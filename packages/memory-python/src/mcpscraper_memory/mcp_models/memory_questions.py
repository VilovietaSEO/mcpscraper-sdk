from typing import Annotated, Any, Literal, Union
from typing_extensions import NotRequired, Required, TypedDict
from pydantic import BaseModel, ConfigDict, Field, TypeAdapter


MemoryQuestionsInputAnswersItem = TypedDict('MemoryQuestionsInputAnswersItem', {
    'question': Required[Annotated[str, Field(min_length=1)]],
    'answer': Required[Annotated[str, Field(min_length=1)]],
})
MemoryQuestionsInputAnswersItem.__pydantic_config__ = ConfigDict(extra="allow", strict=False)


class MemoryQuestionsInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=False)

    vault: Union[str, None] = Field(None, alias='vault', description='Vault to capture into. Optional; defaults to the session active vault, then the first vault the caller is entitled to.')
    answers: Union[Annotated[list[MemoryQuestionsInputAnswersItem], Field(max_length=5)], None] = Field(None, alias='answers', description='Up to 5 question/answer pairs to ingest. Omit (or empty) to instead RECEIVE the day questions.')


class MemoryQuestionsOutputVariant1(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    ok: bool = Field(..., alias='ok', description='True when questions were returned or answers were ingested; false on auth/scope error.')
    questions: Union[Annotated[list[str], Field(max_length=5)], None] = Field(None, alias='questions', description='The day capture questions. Present only when called with no answers.')
    ingested: Union[Union[float, int], None] = Field(None, alias='ingested', description='Number of answers stored as captures. Present only when answers were supplied.')
    error: Union[str, None] = Field(None, alias='error', description='Human-readable failure reason when ok is false.')


MemoryQuestionsOutputVariant2DeliveryArtifactsItem = TypedDict('MemoryQuestionsOutputVariant2DeliveryArtifactsItem', {
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
MemoryQuestionsOutputVariant2DeliveryArtifactsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


MemoryQuestionsOutputVariant2DeliveryAvailableExportsItem = TypedDict('MemoryQuestionsOutputVariant2DeliveryAvailableExportsItem', {
    'artifactId': Required[str],
    'sourceArtifactId': Required[str],
    'filename': Required[Literal['result.md']],
    'contentType': Required[Literal['text/markdown; charset=utf-8']],
    'state': Required[Literal['on-demand']],
})
MemoryQuestionsOutputVariant2DeliveryAvailableExportsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


MemoryQuestionsOutputVariant2DeliveryStorageFailureVariant1 = TypedDict('MemoryQuestionsOutputVariant2DeliveryStorageFailureVariant1', {
    'artifactId': Required[Union[str, None]],
    'outcome': Required[Literal['unknown', 'bytes-stored-metadata-pending', 'failed']],
})
MemoryQuestionsOutputVariant2DeliveryStorageFailureVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


MemoryQuestionsOutputVariant2Delivery = TypedDict('MemoryQuestionsOutputVariant2Delivery', {
    'mode': Required[Literal['artifact']],
    'status': Required[Literal['complete', 'partial', 'unavailable']],
    'retainedRepresentation': Required[Literal['formatted-tool-result']],
    'sourceIsError': Required[bool],
    'artifacts': Required[list[MemoryQuestionsOutputVariant2DeliveryArtifactsItem]],
    'availableExports': NotRequired[list[MemoryQuestionsOutputVariant2DeliveryAvailableExportsItem]],
    'downloadLinksOmitted': Required[bool],
    'scopeOmittedFields': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'storageFailure': Required[Union[MemoryQuestionsOutputVariant2DeliveryStorageFailureVariant1, None]],
    'nextAction': Required[str],
})
MemoryQuestionsOutputVariant2Delivery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


MemoryQuestionsOutputVariant2RecoveryOperation = TypedDict('MemoryQuestionsOutputVariant2RecoveryOperation', {
    'runId': Required[Union[Annotated[str, Field(max_length=200)], None]],
    'idempotencyKey': Required[Annotated[str, Field(max_length=512)]],
    'state': Required[Annotated[str, Field(max_length=100)]],
})
MemoryQuestionsOutputVariant2RecoveryOperation.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


MemoryQuestionsOutputVariant2Recovery = TypedDict('MemoryQuestionsOutputVariant2Recovery', {
    'idempotencyKey': NotRequired[Annotated[str, Field(max_length=512)]],
    'operationId': NotRequired[Annotated[str, Field(max_length=200)]],
    'runId': NotRequired[Annotated[str, Field(max_length=200)]],
    'jobId': NotRequired[Annotated[str, Field(max_length=200)]],
    'operation': NotRequired[MemoryQuestionsOutputVariant2RecoveryOperation],
})
MemoryQuestionsOutputVariant2Recovery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class MemoryQuestionsOutputVariant2(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    delivery: MemoryQuestionsOutputVariant2Delivery = Field(..., alias='delivery', description='')
    preview: str = Field(..., alias='preview', description='')
    scope: dict[str, Union[str, Union[float, int], bool, None]] = Field(..., alias='scope', description='')
    recovery: MemoryQuestionsOutputVariant2Recovery = Field(..., alias='recovery', description='')


# Union schema: validate external payloads with TypeAdapter(MemoryQuestionsOutput).
MemoryQuestionsOutput = Union[MemoryQuestionsOutputVariant2, MemoryQuestionsOutputVariant1]

_MemoryQuestionsInputAdapter = TypeAdapter(MemoryQuestionsInput)
_MemoryQuestionsOutputAdapter = TypeAdapter(MemoryQuestionsOutput)