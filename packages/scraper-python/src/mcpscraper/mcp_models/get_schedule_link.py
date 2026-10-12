from typing import Annotated, Any, Literal, Union
from typing_extensions import NotRequired, Required, TypedDict
from pydantic import BaseModel, ConfigDict, Field, TypeAdapter


class GetScheduleLinkInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=False)



class GetScheduleLinkOutputVariant1(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    ok: bool = Field(..., alias='ok', description='True on success; false on auth error.')
    url: Union[str, None] = Field(None, alias='url', description='The schedule link. Present only the first time a link is minted for this identity.')
    already_exists: Union[bool, None] = Field(None, alias='alreadyExists', description='True when a link already exists and was NOT re-shown. Use revoke-schedule-link then call this again to get a fresh one.')
    code: Union[str, None] = Field(None, alias='code', description='Machine-readable denial code when the link cannot be issued.')
    error: Union[str, None] = Field(None, alias='error', description='Human-readable failure reason when ok is false.')


GetScheduleLinkOutputVariant2DeliveryArtifactsItem = TypedDict('GetScheduleLinkOutputVariant2DeliveryArtifactsItem', {
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
GetScheduleLinkOutputVariant2DeliveryArtifactsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


GetScheduleLinkOutputVariant2DeliveryStorageFailureVariant1 = TypedDict('GetScheduleLinkOutputVariant2DeliveryStorageFailureVariant1', {
    'artifactId': Required[Union[str, None]],
    'outcome': Required[Literal['unknown', 'bytes-stored-metadata-pending', 'failed']],
})
GetScheduleLinkOutputVariant2DeliveryStorageFailureVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


GetScheduleLinkOutputVariant2Delivery = TypedDict('GetScheduleLinkOutputVariant2Delivery', {
    'mode': Required[Literal['artifact']],
    'status': Required[Literal['complete', 'partial', 'unavailable']],
    'retainedRepresentation': Required[Literal['formatted-tool-result']],
    'sourceIsError': Required[bool],
    'artifacts': Required[list[GetScheduleLinkOutputVariant2DeliveryArtifactsItem]],
    'downloadLinksOmitted': Required[bool],
    'scopeOmittedFields': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'storageFailure': Required[Union[GetScheduleLinkOutputVariant2DeliveryStorageFailureVariant1, None]],
    'nextAction': Required[str],
})
GetScheduleLinkOutputVariant2Delivery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


GetScheduleLinkOutputVariant2RecoveryOperation = TypedDict('GetScheduleLinkOutputVariant2RecoveryOperation', {
    'runId': Required[Union[Annotated[str, Field(max_length=200)], None]],
    'idempotencyKey': Required[Annotated[str, Field(max_length=512)]],
    'state': Required[Annotated[str, Field(max_length=100)]],
})
GetScheduleLinkOutputVariant2RecoveryOperation.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


GetScheduleLinkOutputVariant2Recovery = TypedDict('GetScheduleLinkOutputVariant2Recovery', {
    'idempotencyKey': NotRequired[Annotated[str, Field(max_length=512)]],
    'operationId': NotRequired[Annotated[str, Field(max_length=200)]],
    'runId': NotRequired[Annotated[str, Field(max_length=200)]],
    'jobId': NotRequired[Annotated[str, Field(max_length=200)]],
    'operation': NotRequired[GetScheduleLinkOutputVariant2RecoveryOperation],
})
GetScheduleLinkOutputVariant2Recovery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class GetScheduleLinkOutputVariant2(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    delivery: GetScheduleLinkOutputVariant2Delivery = Field(..., alias='delivery', description='')
    preview: str = Field(..., alias='preview', description='')
    scope: dict[str, Union[str, Union[float, int], bool, None]] = Field(..., alias='scope', description='')
    recovery: GetScheduleLinkOutputVariant2Recovery = Field(..., alias='recovery', description='')


# Union schema: validate external payloads with TypeAdapter(GetScheduleLinkOutput).
GetScheduleLinkOutput = Union[GetScheduleLinkOutputVariant2, GetScheduleLinkOutputVariant1]

_GetScheduleLinkInputAdapter = TypeAdapter(GetScheduleLinkInput)
_GetScheduleLinkOutputAdapter = TypeAdapter(GetScheduleLinkOutput)