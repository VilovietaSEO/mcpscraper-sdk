from typing import Annotated, Any, Literal, Union
from typing_extensions import NotRequired, Required, TypedDict
from pydantic import BaseModel, ConfigDict, Field, TypeAdapter


class FactHistoryInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=False)

    vault: Union[str, None] = Field(None, alias='vault', description='Vault to read from. Optional; defaults to the session active vault, then the first vault the caller is entitled to.')
    subject: Annotated[str, Field(min_length=1)] = Field(..., alias='subject', description='The subject whose history to read (e.g. "db preference"). Canonicalized to match how it was recorded.')


FactHistoryOutputVariant1CurrentVariant1 = TypedDict('FactHistoryOutputVariant1CurrentVariant1', {
    'value': Required[str],
    'source': Required[str],
    'status': Required[Literal['active', 'superseded']],
    'resolution': Required[Union[str, None]],
    'precedence': Required[Union[str, None]],
    'updatedAt': Required[str],
})
FactHistoryOutputVariant1CurrentVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


FactHistoryOutputVariant1HistoryItem = TypedDict('FactHistoryOutputVariant1HistoryItem', {
    'value': Required[str],
    'source': Required[str],
    'status': Required[Literal['active', 'superseded']],
    'resolution': Required[Union[str, None]],
    'precedence': Required[Union[str, None]],
    'updatedAt': Required[str],
})
FactHistoryOutputVariant1HistoryItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class FactHistoryOutputVariant1(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    ok: bool = Field(..., alias='ok', description='True when the history was read; false on an auth/scope error.')
    current: Union[Union[FactHistoryOutputVariant1CurrentVariant1, None], None] = Field(None, alias='current', description='The current active fact for the subject, or null if none exists. Present when ok is true.')
    history: Union[list[FactHistoryOutputVariant1HistoryItem], None] = Field(None, alias='history', description='The superseded chain newest → oldest — the audit trail. Empty when nothing has been superseded. Present when ok is true.')
    error: Union[str, None] = Field(None, alias='error', description='Human-readable failure reason when ok is false.')


FactHistoryOutputVariant2DeliveryArtifactsItem = TypedDict('FactHistoryOutputVariant2DeliveryArtifactsItem', {
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
FactHistoryOutputVariant2DeliveryArtifactsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


FactHistoryOutputVariant2DeliveryStorageFailureVariant1 = TypedDict('FactHistoryOutputVariant2DeliveryStorageFailureVariant1', {
    'artifactId': Required[Union[str, None]],
    'outcome': Required[Literal['unknown', 'bytes-stored-metadata-pending', 'failed']],
})
FactHistoryOutputVariant2DeliveryStorageFailureVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


FactHistoryOutputVariant2Delivery = TypedDict('FactHistoryOutputVariant2Delivery', {
    'mode': Required[Literal['artifact']],
    'status': Required[Literal['complete', 'partial', 'unavailable']],
    'retainedRepresentation': Required[Literal['formatted-tool-result']],
    'sourceIsError': Required[bool],
    'artifacts': Required[list[FactHistoryOutputVariant2DeliveryArtifactsItem]],
    'downloadLinksOmitted': Required[bool],
    'scopeOmittedFields': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'storageFailure': Required[Union[FactHistoryOutputVariant2DeliveryStorageFailureVariant1, None]],
    'nextAction': Required[str],
})
FactHistoryOutputVariant2Delivery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


FactHistoryOutputVariant2RecoveryOperation = TypedDict('FactHistoryOutputVariant2RecoveryOperation', {
    'runId': Required[Union[Annotated[str, Field(max_length=200)], None]],
    'idempotencyKey': Required[Annotated[str, Field(max_length=512)]],
    'state': Required[Annotated[str, Field(max_length=100)]],
})
FactHistoryOutputVariant2RecoveryOperation.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


FactHistoryOutputVariant2Recovery = TypedDict('FactHistoryOutputVariant2Recovery', {
    'idempotencyKey': NotRequired[Annotated[str, Field(max_length=512)]],
    'operationId': NotRequired[Annotated[str, Field(max_length=200)]],
    'runId': NotRequired[Annotated[str, Field(max_length=200)]],
    'jobId': NotRequired[Annotated[str, Field(max_length=200)]],
    'operation': NotRequired[FactHistoryOutputVariant2RecoveryOperation],
})
FactHistoryOutputVariant2Recovery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class FactHistoryOutputVariant2(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    delivery: FactHistoryOutputVariant2Delivery = Field(..., alias='delivery', description='')
    preview: str = Field(..., alias='preview', description='')
    scope: dict[str, Union[str, Union[float, int], bool, None]] = Field(..., alias='scope', description='')
    recovery: FactHistoryOutputVariant2Recovery = Field(..., alias='recovery', description='')


# Union schema: validate external payloads with TypeAdapter(FactHistoryOutput).
FactHistoryOutput = Union[FactHistoryOutputVariant2, FactHistoryOutputVariant1]

_FactHistoryInputAdapter = TypeAdapter(FactHistoryInput)
_FactHistoryOutputAdapter = TypeAdapter(FactHistoryOutput)