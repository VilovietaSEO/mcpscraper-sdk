from typing import Annotated, Any, Literal, Union
from typing_extensions import NotRequired, Required, TypedDict
from pydantic import BaseModel, ConfigDict, Field, TypeAdapter


class RevokeScheduledRunViewLinkInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=False)

    run_id: Annotated[str, Field(min_length=1, max_length=200)] = Field(..., alias='runId', description='Opaque scheduled-run identifier returned by a scheduled-results tool.')
    share_id: str = Field(..., alias='shareId', description='Opaque revocable share identifier returned when the view link was created.')


class RevokeScheduledRunViewLinkOutputVariant1(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    ok: bool = Field(..., alias='ok', description='')
    revoked: Union[Literal[True], None] = Field(None, alias='revoked', description='')
    error: Union[Annotated[str, Field(min_length=1, max_length=500)], None] = Field(None, alias='error', description='')
    error_code: Union[Literal['invalid_request', 'not_found', 'conflict', 'template_archived', 'renderer_unavailable', 'artifact_unavailable', 'view_link_unavailable', 'internal_error'], None] = Field(None, alias='errorCode', description='')
    request_id: Union[Annotated[str, Field(max_length=200)], None] = Field(None, alias='requestId', description='')


RevokeScheduledRunViewLinkOutputVariant2DeliveryArtifactsItem = TypedDict('RevokeScheduledRunViewLinkOutputVariant2DeliveryArtifactsItem', {
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
RevokeScheduledRunViewLinkOutputVariant2DeliveryArtifactsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


RevokeScheduledRunViewLinkOutputVariant2DeliveryStorageFailureVariant1 = TypedDict('RevokeScheduledRunViewLinkOutputVariant2DeliveryStorageFailureVariant1', {
    'artifactId': Required[Union[str, None]],
    'outcome': Required[Literal['unknown', 'bytes-stored-metadata-pending', 'failed']],
})
RevokeScheduledRunViewLinkOutputVariant2DeliveryStorageFailureVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


RevokeScheduledRunViewLinkOutputVariant2Delivery = TypedDict('RevokeScheduledRunViewLinkOutputVariant2Delivery', {
    'mode': Required[Literal['artifact']],
    'status': Required[Literal['complete', 'partial', 'unavailable']],
    'retainedRepresentation': Required[Literal['formatted-tool-result']],
    'sourceIsError': Required[bool],
    'artifacts': Required[list[RevokeScheduledRunViewLinkOutputVariant2DeliveryArtifactsItem]],
    'downloadLinksOmitted': Required[bool],
    'scopeOmittedFields': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'storageFailure': Required[Union[RevokeScheduledRunViewLinkOutputVariant2DeliveryStorageFailureVariant1, None]],
    'nextAction': Required[str],
})
RevokeScheduledRunViewLinkOutputVariant2Delivery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


RevokeScheduledRunViewLinkOutputVariant2RecoveryOperation = TypedDict('RevokeScheduledRunViewLinkOutputVariant2RecoveryOperation', {
    'runId': Required[Union[Annotated[str, Field(max_length=200)], None]],
    'idempotencyKey': Required[Annotated[str, Field(max_length=512)]],
    'state': Required[Annotated[str, Field(max_length=100)]],
})
RevokeScheduledRunViewLinkOutputVariant2RecoveryOperation.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


RevokeScheduledRunViewLinkOutputVariant2Recovery = TypedDict('RevokeScheduledRunViewLinkOutputVariant2Recovery', {
    'idempotencyKey': NotRequired[Annotated[str, Field(max_length=512)]],
    'operationId': NotRequired[Annotated[str, Field(max_length=200)]],
    'runId': NotRequired[Annotated[str, Field(max_length=200)]],
    'jobId': NotRequired[Annotated[str, Field(max_length=200)]],
    'operation': NotRequired[RevokeScheduledRunViewLinkOutputVariant2RecoveryOperation],
})
RevokeScheduledRunViewLinkOutputVariant2Recovery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class RevokeScheduledRunViewLinkOutputVariant2(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    delivery: RevokeScheduledRunViewLinkOutputVariant2Delivery = Field(..., alias='delivery', description='')
    preview: str = Field(..., alias='preview', description='')
    scope: dict[str, Union[str, Union[float, int], bool, None]] = Field(..., alias='scope', description='')
    recovery: RevokeScheduledRunViewLinkOutputVariant2Recovery = Field(..., alias='recovery', description='')


# Union schema: validate external payloads with TypeAdapter(RevokeScheduledRunViewLinkOutput).
RevokeScheduledRunViewLinkOutput = Union[RevokeScheduledRunViewLinkOutputVariant2, RevokeScheduledRunViewLinkOutputVariant1]

_RevokeScheduledRunViewLinkInputAdapter = TypeAdapter(RevokeScheduledRunViewLinkInput)
_RevokeScheduledRunViewLinkOutputAdapter = TypeAdapter(RevokeScheduledRunViewLinkOutput)