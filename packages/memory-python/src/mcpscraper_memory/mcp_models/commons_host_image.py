from typing import Annotated, Any, Literal, Union
from typing_extensions import NotRequired, Required, TypedDict
from pydantic import BaseModel, ConfigDict, Field, TypeAdapter


class CommonsHostImageInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=False)

    source_url: Union[str, None] = Field(None, alias='sourceUrl', description='Public HTTPS direct image URL or webpage URL. A direct image is hosted as-is; an HTML page is inspected for Open Graph, Twitter, JSON-LD, and meaningful content images, then the first usable candidate is hosted. Temporary signed URLs are consumed immediately and query credentials are not retained as provenance.')
    image_base64: Union[Annotated[str, Field(min_length=16)], None] = Field(None, alias='imageBase64', description='Base64 image bytes for an image already available to the caller, including a pasted attachment or AI-generated image. Use sourceType to preserve whether it was uploaded or generated. Keep the complete serialized request within the client transport limit.')
    artifact_id: Union[Annotated[str, Field(min_length=1, max_length=500)], None] = Field(None, alias='artifactId', description='Owner-scoped image artifact returned by an MCP Scraper media or screenshot workflow. The server reauthorizes ownership and reads the bytes directly; do not construct an artifact ID.')
    source_type: Union[Literal['uploaded', 'ai_generated'], None] = Field(None, alias='sourceType', description='Provenance for imageBase64 or artifactId. Use ai_generated only when an image model created the supplied bytes; otherwise use uploaded or omit it.')
    alt: Union[Annotated[str, Field(max_length=500)], None] = Field(None, alias='alt', description='Alt text describing the image for readers who cannot see it.')
    license: Union[Annotated[str, Field(max_length=240)], None] = Field(None, alias='license', description='License or usage terms of the original image, preserved with the hosted copy.')
    attribution: Union[Annotated[str, Field(max_length=500)], None] = Field(None, alias='attribution', description='Credit line for the original photographer, publication, or archive.')


CommonsHostImageOutputVariant1Data = TypedDict('CommonsHostImageOutputVariant1Data', {
    'id': Required[str],
    'url': Required[str],
    'contentType': Required[Literal['image/jpeg', 'image/png', 'image/gif', 'image/webp']],
    'bytes': Required[Annotated[int, Field(le=9007199254740991, gt=0)]],
    'digest': Required[str],
    'sourceUrl': Required[Union[str, None]],
    'sourcePageUrl': Required[Union[str, None]],
    'sourceKind': Required[Literal['uploaded', 'ai_generated', 'artifact', 'direct_url', 'webpage', 'registered']],
    'selectionSource': Required[Literal['provided_bytes', 'artifact', 'direct_url', 'og:image', 'twitter:image', 'json-ld', 'content-image', 'registered']],
    'reused': Required[bool],
})
CommonsHostImageOutputVariant1Data.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class CommonsHostImageOutputVariant1(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    ok: bool = Field(..., alias='ok', description='')
    data: Union[CommonsHostImageOutputVariant1Data, None] = Field(None, alias='data', description='')
    error: Union[str, None] = Field(None, alias='error', description='')
    message: Union[str, None] = Field(None, alias='message', description='')


CommonsHostImageOutputVariant2DeliveryArtifactsItem = TypedDict('CommonsHostImageOutputVariant2DeliveryArtifactsItem', {
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
CommonsHostImageOutputVariant2DeliveryArtifactsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


CommonsHostImageOutputVariant2DeliveryAvailableExportsItem = TypedDict('CommonsHostImageOutputVariant2DeliveryAvailableExportsItem', {
    'artifactId': Required[str],
    'sourceArtifactId': Required[str],
    'filename': Required[Literal['result.md']],
    'contentType': Required[Literal['text/markdown; charset=utf-8']],
    'state': Required[Literal['on-demand']],
})
CommonsHostImageOutputVariant2DeliveryAvailableExportsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


CommonsHostImageOutputVariant2DeliveryStorageFailureVariant1 = TypedDict('CommonsHostImageOutputVariant2DeliveryStorageFailureVariant1', {
    'artifactId': Required[Union[str, None]],
    'outcome': Required[Literal['unknown', 'bytes-stored-metadata-pending', 'failed']],
})
CommonsHostImageOutputVariant2DeliveryStorageFailureVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


CommonsHostImageOutputVariant2Delivery = TypedDict('CommonsHostImageOutputVariant2Delivery', {
    'mode': Required[Literal['artifact']],
    'status': Required[Literal['complete', 'partial', 'unavailable']],
    'retainedRepresentation': Required[Literal['formatted-tool-result']],
    'sourceIsError': Required[bool],
    'artifacts': Required[list[CommonsHostImageOutputVariant2DeliveryArtifactsItem]],
    'availableExports': NotRequired[list[CommonsHostImageOutputVariant2DeliveryAvailableExportsItem]],
    'downloadLinksOmitted': Required[bool],
    'scopeOmittedFields': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'storageFailure': Required[Union[CommonsHostImageOutputVariant2DeliveryStorageFailureVariant1, None]],
    'nextAction': Required[str],
})
CommonsHostImageOutputVariant2Delivery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


CommonsHostImageOutputVariant2RecoveryOperation = TypedDict('CommonsHostImageOutputVariant2RecoveryOperation', {
    'runId': Required[Union[Annotated[str, Field(max_length=200)], None]],
    'idempotencyKey': Required[Annotated[str, Field(max_length=512)]],
    'state': Required[Annotated[str, Field(max_length=100)]],
})
CommonsHostImageOutputVariant2RecoveryOperation.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


CommonsHostImageOutputVariant2Recovery = TypedDict('CommonsHostImageOutputVariant2Recovery', {
    'idempotencyKey': NotRequired[Annotated[str, Field(max_length=512)]],
    'operationId': NotRequired[Annotated[str, Field(max_length=200)]],
    'runId': NotRequired[Annotated[str, Field(max_length=200)]],
    'jobId': NotRequired[Annotated[str, Field(max_length=200)]],
    'operation': NotRequired[CommonsHostImageOutputVariant2RecoveryOperation],
})
CommonsHostImageOutputVariant2Recovery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class CommonsHostImageOutputVariant2(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    delivery: CommonsHostImageOutputVariant2Delivery = Field(..., alias='delivery', description='')
    preview: str = Field(..., alias='preview', description='')
    scope: dict[str, Union[str, Union[float, int], bool, None]] = Field(..., alias='scope', description='')
    recovery: CommonsHostImageOutputVariant2Recovery = Field(..., alias='recovery', description='')


# Union schema: validate external payloads with TypeAdapter(CommonsHostImageOutput).
CommonsHostImageOutput = Union[CommonsHostImageOutputVariant2, CommonsHostImageOutputVariant1]

_CommonsHostImageInputAdapter = TypeAdapter(CommonsHostImageInput)
_CommonsHostImageOutputAdapter = TypeAdapter(CommonsHostImageOutput)