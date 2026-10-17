"""Generated from artifact_describe in contracts/mcp.tools.json."""

from typing import Annotated, Any, Literal, TypeVar, Union
from typing_extensions import NotRequired, Required, TypedDict
from pydantic import BaseModel, ConfigDict, Field, TypeAdapter

ArtifactDeliveryDeliveryArtifactsItem = TypedDict('ArtifactDeliveryDeliveryArtifactsItem', {
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
ArtifactDeliveryDeliveryArtifactsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


ArtifactDeliveryDeliveryAvailableExportsItem = TypedDict('ArtifactDeliveryDeliveryAvailableExportsItem', {
    'artifactId': Required[str],
    'sourceArtifactId': Required[str],
    'filename': Required[Literal['result.md']],
    'contentType': Required[Literal['text/markdown; charset=utf-8']],
    'state': Required[Literal['on-demand']],
})
ArtifactDeliveryDeliveryAvailableExportsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


ArtifactDeliveryDeliveryStorageFailureVariant1 = TypedDict('ArtifactDeliveryDeliveryStorageFailureVariant1', {
    'artifactId': Required[Union[str, None]],
    'outcome': Required[Literal['unknown', 'bytes-stored-metadata-pending', 'failed']],
})
ArtifactDeliveryDeliveryStorageFailureVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


ArtifactDeliveryDelivery = TypedDict('ArtifactDeliveryDelivery', {
    'mode': Required[Literal['artifact']],
    'status': Required[Literal['complete', 'partial', 'unavailable']],
    'retainedRepresentation': Required[Literal['formatted-tool-result']],
    'sourceIsError': Required[bool],
    'artifacts': Required[list[ArtifactDeliveryDeliveryArtifactsItem]],
    'availableExports': NotRequired[list[ArtifactDeliveryDeliveryAvailableExportsItem]],
    'downloadLinksOmitted': Required[bool],
    'scopeOmittedFields': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'storageFailure': Required[Union[ArtifactDeliveryDeliveryStorageFailureVariant1, None]],
    'nextAction': Required[str],
})
ArtifactDeliveryDelivery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


ArtifactDeliveryRecoveryOperation = TypedDict('ArtifactDeliveryRecoveryOperation', {
    'runId': Required[Union[Annotated[str, Field(max_length=200)], None]],
    'idempotencyKey': Required[Annotated[str, Field(max_length=512)]],
    'state': Required[Annotated[str, Field(max_length=100)]],
})
ArtifactDeliveryRecoveryOperation.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


ArtifactDeliveryRecovery = TypedDict('ArtifactDeliveryRecovery', {
    'idempotencyKey': NotRequired[Annotated[str, Field(max_length=512)]],
    'operationId': NotRequired[Annotated[str, Field(max_length=200)]],
    'runId': NotRequired[Annotated[str, Field(max_length=200)]],
    'jobId': NotRequired[Annotated[str, Field(max_length=200)]],
    'operation': NotRequired[ArtifactDeliveryRecoveryOperation],
})
ArtifactDeliveryRecovery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class ArtifactDelivery(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    delivery: ArtifactDeliveryDelivery = Field(..., alias='delivery', description='')
    preview: str = Field(..., alias='preview', description='')
    scope: dict[str, Union[str, Union[float, int], bool, None]] = Field(..., alias='scope', description='')
    recovery: ArtifactDeliveryRecovery = Field(..., alias='recovery', description='')

_ArtifactDeliveryAdapter = TypeAdapter(ArtifactDelivery)
_OutputModel = TypeVar("_OutputModel", bound=BaseModel)

def validate_tool_output(value: Any, output_model: type[_OutputModel]) -> _OutputModel | ArtifactDelivery:
    if isinstance(value, dict) and "delivery" in value:
        return _ArtifactDeliveryAdapter.validate_python(value)
    return output_model.model_validate(value)
