from typing import Annotated, Any, Literal, Union
from typing_extensions import NotRequired, Required, TypedDict
from pydantic import BaseModel, ConfigDict, Field, TypeAdapter


class RecordFactInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=False)

    vault: Union[str, None] = Field(None, alias='vault', description='Vault to record the fact in. Optional; defaults to the session active vault, then the first vault the caller is entitled to.')
    subject: Annotated[str, Field(min_length=1)] = Field(..., alias='subject', description='The thing the fact is about (e.g. "db preference"). Canonicalized (lowercased/trimmed) to a stable key.')
    value: Annotated[str, Field(min_length=1)] = Field(..., alias='value', description='The current asserted value or conclusion for the subject (e.g. "Postgres").')
    source: Union[str, None] = Field(None, alias='source', description='Where the fact came from: user / tool / chat / library:… . Optional; drives the source-priority precedence policy.')
    confidence: Union[Annotated[Union[float, int], Field(ge=0, le=1)], None] = Field(None, alias='confidence', description='Salience/confidence in 0..1 on write. Optional; defaults to 0.5.')
    reason: Union[str, None] = Field(None, alias='reason', description='Why this assertion replaces the previous one — the audit reason recorded on the superseded fact. Optional; a default is used.')


RecordFactOutputVariant1Fact = TypedDict('RecordFactOutputVariant1Fact', {
    'id': Required[str],
    'subject': Required[str],
    'value': Required[str],
    'source': Required[str],
    'confidence': Required[Union[float, int]],
    'status': Required[Literal['active', 'superseded']],
    'resolution': Required[Union[str, None]],
    'precedence': Required[Union[str, None]],
    'createdAt': Required[str],
    'updatedAt': Required[str],
})
RecordFactOutputVariant1Fact.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


RecordFactOutputVariant1Superseded = TypedDict('RecordFactOutputVariant1Superseded', {
    'id': Required[str],
    'subject': Required[str],
    'value': Required[str],
    'source': Required[str],
    'confidence': Required[Union[float, int]],
    'status': Required[Literal['active', 'superseded']],
    'resolution': Required[Union[str, None]],
    'precedence': Required[Union[str, None]],
    'createdAt': Required[str],
    'updatedAt': Required[str],
})
RecordFactOutputVariant1Superseded.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class RecordFactOutputVariant1(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    ok: bool = Field(..., alias='ok', description='True when the fact was recorded (whether or not it superseded one); false on auth/scope/validation error.')
    fact: Union[RecordFactOutputVariant1Fact, None] = Field(None, alias='fact', description='The new (or refreshed) active fact. Present when ok is true.')
    superseded: Union[RecordFactOutputVariant1Superseded, None] = Field(None, alias='superseded', description='The previously-active fact that this one replaced, with its resolution/precedence. Absent on an idempotent no-op or first assertion.')
    error: Union[str, None] = Field(None, alias='error', description='Human-readable failure reason when ok is false.')


RecordFactOutputVariant2DeliveryArtifactsItem = TypedDict('RecordFactOutputVariant2DeliveryArtifactsItem', {
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
RecordFactOutputVariant2DeliveryArtifactsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


RecordFactOutputVariant2DeliveryStorageFailureVariant1 = TypedDict('RecordFactOutputVariant2DeliveryStorageFailureVariant1', {
    'artifactId': Required[Union[str, None]],
    'outcome': Required[Literal['unknown', 'bytes-stored-metadata-pending', 'failed']],
})
RecordFactOutputVariant2DeliveryStorageFailureVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


RecordFactOutputVariant2Delivery = TypedDict('RecordFactOutputVariant2Delivery', {
    'mode': Required[Literal['artifact']],
    'status': Required[Literal['complete', 'partial', 'unavailable']],
    'retainedRepresentation': Required[Literal['formatted-tool-result']],
    'sourceIsError': Required[bool],
    'artifacts': Required[list[RecordFactOutputVariant2DeliveryArtifactsItem]],
    'downloadLinksOmitted': Required[bool],
    'scopeOmittedFields': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'storageFailure': Required[Union[RecordFactOutputVariant2DeliveryStorageFailureVariant1, None]],
    'nextAction': Required[str],
})
RecordFactOutputVariant2Delivery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


RecordFactOutputVariant2RecoveryOperation = TypedDict('RecordFactOutputVariant2RecoveryOperation', {
    'runId': Required[Union[Annotated[str, Field(max_length=200)], None]],
    'idempotencyKey': Required[Annotated[str, Field(max_length=512)]],
    'state': Required[Annotated[str, Field(max_length=100)]],
})
RecordFactOutputVariant2RecoveryOperation.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


RecordFactOutputVariant2Recovery = TypedDict('RecordFactOutputVariant2Recovery', {
    'idempotencyKey': NotRequired[Annotated[str, Field(max_length=512)]],
    'operationId': NotRequired[Annotated[str, Field(max_length=200)]],
    'runId': NotRequired[Annotated[str, Field(max_length=200)]],
    'jobId': NotRequired[Annotated[str, Field(max_length=200)]],
    'operation': NotRequired[RecordFactOutputVariant2RecoveryOperation],
})
RecordFactOutputVariant2Recovery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class RecordFactOutputVariant2(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    delivery: RecordFactOutputVariant2Delivery = Field(..., alias='delivery', description='')
    preview: str = Field(..., alias='preview', description='')
    scope: dict[str, Union[str, Union[float, int], bool, None]] = Field(..., alias='scope', description='')
    recovery: RecordFactOutputVariant2Recovery = Field(..., alias='recovery', description='')


# Union schema: validate external payloads with TypeAdapter(RecordFactOutput).
RecordFactOutput = Union[RecordFactOutputVariant2, RecordFactOutputVariant1]

_RecordFactInputAdapter = TypeAdapter(RecordFactInput)
_RecordFactOutputAdapter = TypeAdapter(RecordFactOutput)