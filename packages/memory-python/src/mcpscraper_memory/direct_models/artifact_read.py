from typing import Annotated, Any, Literal, Union
from typing_extensions import NotRequired, Required, TypedDict
from pydantic import BaseModel, ConfigDict, Field


class ArtifactReadInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="forbid")

    api_key: str | None = Field(None, alias="apiKey", description="Omit when the Memory transport is authenticated.")
    session_id: str | None = Field(None, alias="sessionId", description="Memory session used by the authentication owner; omit to use the authenticated transport session.")
    artifact_id: str = Field(..., alias="artifactId", description="Exact retained Memory artifact ID; access remains bound to this authenticated recipient.")
    offset: int | None = Field(None, alias="offset", description="UTF-8 byte offset; use the exact returned nextOffset.")
    max_bytes: int | None = Field(None, alias="maxBytes", description="Maximum requested bytes. The final serialized response budget may yield a smaller window; continue until nextOffset is null.")


class ArtifactReadOutputVariant1(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=False)

    artifact_id: str = Field(..., alias='artifactId', description='')
    text: str = Field(..., alias='text', description='')
    total_bytes: Union[float, int] = Field(..., alias='totalBytes', description='')
    offset: Union[float, int] = Field(..., alias='offset', description='')
    consumed_bytes: Union[float, int] = Field(..., alias='consumedBytes', description='')
    next_offset: Union[Union[float, int], None] = Field(..., alias='nextOffset', description='')
    content_type: str = Field(..., alias='contentType', description='')
    sha256: Union[str, None] = Field(..., alias='sha256', description='')


class ArtifactReadOutputVariant2(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=False)

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


class ArtifactReadOutputVariant3(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=False)

    error: str = Field(..., alias='error', description='')


# Union schema: validate external payloads with TypeAdapter(ArtifactReadOutput).
ArtifactReadOutput = Union[ArtifactReadOutputVariant2, ArtifactReadOutputVariant1, ArtifactReadOutputVariant3]
