from typing import Annotated, Any, Literal, Union
from typing_extensions import NotRequired, Required, TypedDict
from pydantic import BaseModel, ConfigDict, Field, TypeAdapter


class GmailGetAttachmentInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=False)

    attachment_ref: Annotated[str, Field(min_length=1, max_length=500)] = Field(..., alias='attachmentRef', description='Opaque owner-bound attachmentRef returned by gmail_get_message; do not pass a provider attachment ID or URL.')


GmailGetAttachmentOutputVariant1Artifact = TypedDict('GmailGetAttachmentOutputVariant1Artifact', {
    'artifactId': Required[Annotated[str, Field(min_length=1, max_length=500)]],
    'filename': Required[Annotated[str, Field(min_length=1, max_length=500)]],
    'mimeType': Required[Annotated[str, Field(min_length=1, max_length=255)]],
    'bytes': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'sha256': Required[str],
    'createdAt': Required[str],
    'expiresAt': Required[str],
    'downloadUrl': NotRequired[str],
    'downloadUrlExpiresAt': NotRequired[str],
    'textReadable': Required[bool],
    'archiveReadable': Required[bool],
    'persistable': Required[bool],
})
GmailGetAttachmentOutputVariant1Artifact.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class GmailGetAttachmentOutputVariant1(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    ok: bool = Field(..., alias='ok', description='')
    filename: Union[Annotated[str, Field(min_length=1, max_length=500)], None] = Field(None, alias='filename', description='')
    declared_mime: Union[Annotated[str, Field(min_length=1, max_length=255)], None] = Field(None, alias='declaredMime', description='')
    observed_mime: Union[Annotated[str, Field(min_length=1, max_length=255)], None] = Field(None, alias='observedMime', description='')
    bytes: Union[Annotated[int, Field(ge=0, le=9007199254740991)], None] = Field(None, alias='bytes', description='')
    sha256: Union[str, None] = Field(None, alias='sha256', description='')
    content_complete: Union[bool, None] = Field(None, alias='contentComplete', description='')
    artifact: Union[GmailGetAttachmentOutputVariant1Artifact, None] = Field(None, alias='artifact', description='')
    text: Union[str, None] = Field(None, alias='text', description='')
    text_complete: Union[bool, None] = Field(None, alias='textComplete', description='')
    next_offset: Union[Union[Annotated[int, Field(ge=0, le=9007199254740991)], None], None] = Field(None, alias='nextOffset', description='')
    untrusted_content: Literal[True] = Field(..., alias='untrustedContent', description='')
    error: Union[str, None] = Field(..., alias='error', description='')


GmailGetAttachmentOutputVariant2DeliveryArtifactsItem = TypedDict('GmailGetAttachmentOutputVariant2DeliveryArtifactsItem', {
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
GmailGetAttachmentOutputVariant2DeliveryArtifactsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


GmailGetAttachmentOutputVariant2DeliveryAvailableExportsItem = TypedDict('GmailGetAttachmentOutputVariant2DeliveryAvailableExportsItem', {
    'artifactId': Required[str],
    'sourceArtifactId': Required[str],
    'filename': Required[Literal['result.md']],
    'contentType': Required[Literal['text/markdown; charset=utf-8']],
    'state': Required[Literal['on-demand']],
})
GmailGetAttachmentOutputVariant2DeliveryAvailableExportsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


GmailGetAttachmentOutputVariant2DeliveryStorageFailureVariant1 = TypedDict('GmailGetAttachmentOutputVariant2DeliveryStorageFailureVariant1', {
    'artifactId': Required[Union[str, None]],
    'outcome': Required[Literal['unknown', 'bytes-stored-metadata-pending', 'failed']],
})
GmailGetAttachmentOutputVariant2DeliveryStorageFailureVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


GmailGetAttachmentOutputVariant2Delivery = TypedDict('GmailGetAttachmentOutputVariant2Delivery', {
    'mode': Required[Literal['artifact']],
    'status': Required[Literal['complete', 'partial', 'unavailable']],
    'retainedRepresentation': Required[Literal['formatted-tool-result']],
    'sourceIsError': Required[bool],
    'artifacts': Required[list[GmailGetAttachmentOutputVariant2DeliveryArtifactsItem]],
    'availableExports': NotRequired[list[GmailGetAttachmentOutputVariant2DeliveryAvailableExportsItem]],
    'downloadLinksOmitted': Required[bool],
    'scopeOmittedFields': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'storageFailure': Required[Union[GmailGetAttachmentOutputVariant2DeliveryStorageFailureVariant1, None]],
    'nextAction': Required[str],
})
GmailGetAttachmentOutputVariant2Delivery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


GmailGetAttachmentOutputVariant2RecoveryOperation = TypedDict('GmailGetAttachmentOutputVariant2RecoveryOperation', {
    'runId': Required[Union[Annotated[str, Field(max_length=200)], None]],
    'idempotencyKey': Required[Annotated[str, Field(max_length=512)]],
    'state': Required[Annotated[str, Field(max_length=100)]],
})
GmailGetAttachmentOutputVariant2RecoveryOperation.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


GmailGetAttachmentOutputVariant2Recovery = TypedDict('GmailGetAttachmentOutputVariant2Recovery', {
    'idempotencyKey': NotRequired[Annotated[str, Field(max_length=512)]],
    'operationId': NotRequired[Annotated[str, Field(max_length=200)]],
    'runId': NotRequired[Annotated[str, Field(max_length=200)]],
    'jobId': NotRequired[Annotated[str, Field(max_length=200)]],
    'operation': NotRequired[GmailGetAttachmentOutputVariant2RecoveryOperation],
})
GmailGetAttachmentOutputVariant2Recovery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class GmailGetAttachmentOutputVariant2(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    delivery: GmailGetAttachmentOutputVariant2Delivery = Field(..., alias='delivery', description='')
    preview: str = Field(..., alias='preview', description='')
    scope: dict[str, Union[str, Union[float, int], bool, None]] = Field(..., alias='scope', description='')
    recovery: GmailGetAttachmentOutputVariant2Recovery = Field(..., alias='recovery', description='')


# Union schema: validate external payloads with TypeAdapter(GmailGetAttachmentOutput).
GmailGetAttachmentOutput = Union[GmailGetAttachmentOutputVariant2, GmailGetAttachmentOutputVariant1]

_GmailGetAttachmentInputAdapter = TypeAdapter(GmailGetAttachmentInput)
_GmailGetAttachmentOutputAdapter = TypeAdapter(GmailGetAttachmentOutput)