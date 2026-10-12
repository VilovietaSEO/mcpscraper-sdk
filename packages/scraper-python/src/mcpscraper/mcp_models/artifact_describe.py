from typing import Annotated, Any, Literal, Union
from typing_extensions import NotRequired, Required, TypedDict
from pydantic import BaseModel, ConfigDict, Field, TypeAdapter


class ArtifactDescribeInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=False)

    artifact_id: Annotated[str, Field(min_length=1, max_length=1024)] = Field(..., alias='artifactId', description='Artifact ID returned by a completed MCP result. Access remains bound to this authenticated caller.')


class ArtifactDescribeOutputVariant1(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    artifact_id: str = Field(..., alias='artifactId', description='')
    filename: str = Field(..., alias='filename', description='')
    content_type: str = Field(..., alias='contentType', description='')
    bytes: Union[float, int] = Field(..., alias='bytes', description='')
    sha256: str = Field(..., alias='sha256', description='')
    created_at: str = Field(..., alias='createdAt', description='')
    expires_at: str = Field(..., alias='expiresAt', description='')
    capabilities: list[str] = Field(..., alias='capabilities', description='')
    download_url: Union[str, None] = Field(..., alias='downloadUrl', description='')
    download_url_expires_at: Union[str, None] = Field(..., alias='downloadUrlExpiresAt', description='')
    download_state: Literal['available', 'local', 'unavailable'] = Field(..., alias='downloadState', description='')
    local_path: Union[str, None] = Field(..., alias='localPath', description='')
    local_path_scope: Union[str, None] = Field(..., alias='localPathScope', description='')
    next_action: str = Field(..., alias='nextAction', description='')


ArtifactDescribeOutputVariant2DeliveryArtifactsItem = TypedDict('ArtifactDescribeOutputVariant2DeliveryArtifactsItem', {
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
ArtifactDescribeOutputVariant2DeliveryArtifactsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


ArtifactDescribeOutputVariant2DeliveryStorageFailureVariant1 = TypedDict('ArtifactDescribeOutputVariant2DeliveryStorageFailureVariant1', {
    'artifactId': Required[Union[str, None]],
    'outcome': Required[Literal['unknown', 'bytes-stored-metadata-pending', 'failed']],
})
ArtifactDescribeOutputVariant2DeliveryStorageFailureVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


ArtifactDescribeOutputVariant2Delivery = TypedDict('ArtifactDescribeOutputVariant2Delivery', {
    'mode': Required[Literal['artifact']],
    'status': Required[Literal['complete', 'partial', 'unavailable']],
    'retainedRepresentation': Required[Literal['formatted-tool-result']],
    'sourceIsError': Required[bool],
    'artifacts': Required[list[ArtifactDescribeOutputVariant2DeliveryArtifactsItem]],
    'downloadLinksOmitted': Required[bool],
    'scopeOmittedFields': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'storageFailure': Required[Union[ArtifactDescribeOutputVariant2DeliveryStorageFailureVariant1, None]],
    'nextAction': Required[str],
})
ArtifactDescribeOutputVariant2Delivery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


ArtifactDescribeOutputVariant2RecoveryOperation = TypedDict('ArtifactDescribeOutputVariant2RecoveryOperation', {
    'runId': Required[Union[Annotated[str, Field(max_length=200)], None]],
    'idempotencyKey': Required[Annotated[str, Field(max_length=512)]],
    'state': Required[Annotated[str, Field(max_length=100)]],
})
ArtifactDescribeOutputVariant2RecoveryOperation.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


ArtifactDescribeOutputVariant2Recovery = TypedDict('ArtifactDescribeOutputVariant2Recovery', {
    'idempotencyKey': NotRequired[Annotated[str, Field(max_length=512)]],
    'operationId': NotRequired[Annotated[str, Field(max_length=200)]],
    'runId': NotRequired[Annotated[str, Field(max_length=200)]],
    'jobId': NotRequired[Annotated[str, Field(max_length=200)]],
    'operation': NotRequired[ArtifactDescribeOutputVariant2RecoveryOperation],
})
ArtifactDescribeOutputVariant2Recovery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class ArtifactDescribeOutputVariant2(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    delivery: ArtifactDescribeOutputVariant2Delivery = Field(..., alias='delivery', description='')
    preview: str = Field(..., alias='preview', description='')
    scope: dict[str, Union[str, Union[float, int], bool, None]] = Field(..., alias='scope', description='')
    recovery: ArtifactDescribeOutputVariant2Recovery = Field(..., alias='recovery', description='')


# Union schema: validate external payloads with TypeAdapter(ArtifactDescribeOutput).
ArtifactDescribeOutput = Union[ArtifactDescribeOutputVariant1, ArtifactDescribeOutputVariant2]

_ArtifactDescribeInputAdapter = TypeAdapter(ArtifactDescribeInput)
_ArtifactDescribeOutputAdapter = TypeAdapter(ArtifactDescribeOutput)