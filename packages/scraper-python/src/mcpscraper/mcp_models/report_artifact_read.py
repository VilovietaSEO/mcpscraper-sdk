from typing import Annotated, Any, Literal, Union
from typing_extensions import NotRequired, Required, TypedDict
from pydantic import BaseModel, ConfigDict, Field, TypeAdapter


class ReportArtifactReadInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=False)

    artifact_id: Annotated[str, Field(min_length=1)] = Field(..., alias='artifactId', description='Artifact id returned inline by a tool whose result was too large to inline. Use only a returned artifactId; do not construct one yourself.')
    offset: Union[Annotated[int, Field(ge=0, le=9007199254740991)], None] = Field(None, alias='offset', description="Byte offset to start reading from. Pass the previous call's nextOffset to continue.")
    max_bytes: Union[Annotated[int, Field(ge=1000, le=100000)], None] = Field(None, alias='maxBytes', description='Maximum bytes of artifact text to return in this window.')


class ReportArtifactReadOutputVariant1(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    artifact_id: str = Field(..., alias='artifactId', description='')
    text: str = Field(..., alias='text', description='')
    total_bytes: Annotated[int, Field(ge=0, le=9007199254740991)] = Field(..., alias='totalBytes', description='')
    next_offset: Union[Annotated[int, Field(ge=0, le=9007199254740991)], None] = Field(..., alias='nextOffset', description='')


ReportArtifactReadOutputVariant2DeliveryArtifactsItem = TypedDict('ReportArtifactReadOutputVariant2DeliveryArtifactsItem', {
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
ReportArtifactReadOutputVariant2DeliveryArtifactsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


ReportArtifactReadOutputVariant2DeliveryStorageFailureVariant1 = TypedDict('ReportArtifactReadOutputVariant2DeliveryStorageFailureVariant1', {
    'artifactId': Required[Union[str, None]],
    'outcome': Required[Literal['unknown', 'bytes-stored-metadata-pending', 'failed']],
})
ReportArtifactReadOutputVariant2DeliveryStorageFailureVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


ReportArtifactReadOutputVariant2Delivery = TypedDict('ReportArtifactReadOutputVariant2Delivery', {
    'mode': Required[Literal['artifact']],
    'status': Required[Literal['complete', 'partial', 'unavailable']],
    'retainedRepresentation': Required[Literal['formatted-tool-result']],
    'sourceIsError': Required[bool],
    'artifacts': Required[list[ReportArtifactReadOutputVariant2DeliveryArtifactsItem]],
    'downloadLinksOmitted': Required[bool],
    'scopeOmittedFields': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'storageFailure': Required[Union[ReportArtifactReadOutputVariant2DeliveryStorageFailureVariant1, None]],
    'nextAction': Required[str],
})
ReportArtifactReadOutputVariant2Delivery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


ReportArtifactReadOutputVariant2RecoveryOperation = TypedDict('ReportArtifactReadOutputVariant2RecoveryOperation', {
    'runId': Required[Union[Annotated[str, Field(max_length=200)], None]],
    'idempotencyKey': Required[Annotated[str, Field(max_length=512)]],
    'state': Required[Annotated[str, Field(max_length=100)]],
})
ReportArtifactReadOutputVariant2RecoveryOperation.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


ReportArtifactReadOutputVariant2Recovery = TypedDict('ReportArtifactReadOutputVariant2Recovery', {
    'idempotencyKey': NotRequired[Annotated[str, Field(max_length=512)]],
    'operationId': NotRequired[Annotated[str, Field(max_length=200)]],
    'runId': NotRequired[Annotated[str, Field(max_length=200)]],
    'jobId': NotRequired[Annotated[str, Field(max_length=200)]],
    'operation': NotRequired[ReportArtifactReadOutputVariant2RecoveryOperation],
})
ReportArtifactReadOutputVariant2Recovery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class ReportArtifactReadOutputVariant2(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    delivery: ReportArtifactReadOutputVariant2Delivery = Field(..., alias='delivery', description='')
    preview: str = Field(..., alias='preview', description='')
    scope: dict[str, Union[str, Union[float, int], bool, None]] = Field(..., alias='scope', description='')
    recovery: ReportArtifactReadOutputVariant2Recovery = Field(..., alias='recovery', description='')


# Union schema: validate external payloads with TypeAdapter(ReportArtifactReadOutput).
ReportArtifactReadOutput = Union[ReportArtifactReadOutputVariant1, ReportArtifactReadOutputVariant2]

_ReportArtifactReadInputAdapter = TypeAdapter(ReportArtifactReadInput)
_ReportArtifactReadOutputAdapter = TypeAdapter(ReportArtifactReadOutput)