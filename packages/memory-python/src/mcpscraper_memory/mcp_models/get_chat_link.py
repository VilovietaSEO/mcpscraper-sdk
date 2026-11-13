from typing import Annotated, Any, Literal, Union
from typing_extensions import NotRequired, Required, TypedDict
from pydantic import BaseModel, ConfigDict, Field, TypeAdapter


class GetChatLinkInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=False)



class GetChatLinkOutputVariant1(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    ok: bool = Field(..., alias='ok', description='True on success; false on auth error.')
    url: Union[str, None] = Field(None, alias='url', description='The chat link. Present only the first time a link is minted for this identity.')
    already_exists: Union[bool, None] = Field(None, alias='alreadyExists', description='True when a link already exists and was NOT re-shown. Use revoke-chat-link then call this again to get a fresh one.')
    error: Union[str, None] = Field(None, alias='error', description='Human-readable failure reason when ok is false.')


GetChatLinkOutputVariant2DeliveryArtifactsItem = TypedDict('GetChatLinkOutputVariant2DeliveryArtifactsItem', {
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
GetChatLinkOutputVariant2DeliveryArtifactsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


GetChatLinkOutputVariant2DeliveryAvailableExportsItem = TypedDict('GetChatLinkOutputVariant2DeliveryAvailableExportsItem', {
    'artifactId': Required[str],
    'sourceArtifactId': Required[str],
    'filename': Required[Literal['result.md']],
    'contentType': Required[Literal['text/markdown; charset=utf-8']],
    'state': Required[Literal['on-demand']],
})
GetChatLinkOutputVariant2DeliveryAvailableExportsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


GetChatLinkOutputVariant2DeliveryStorageFailureVariant1 = TypedDict('GetChatLinkOutputVariant2DeliveryStorageFailureVariant1', {
    'artifactId': Required[Union[str, None]],
    'outcome': Required[Literal['unknown', 'bytes-stored-metadata-pending', 'failed']],
})
GetChatLinkOutputVariant2DeliveryStorageFailureVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


GetChatLinkOutputVariant2Delivery = TypedDict('GetChatLinkOutputVariant2Delivery', {
    'mode': Required[Literal['artifact']],
    'status': Required[Literal['complete', 'partial', 'unavailable']],
    'retainedRepresentation': Required[Literal['formatted-tool-result']],
    'sourceIsError': Required[bool],
    'artifacts': Required[list[GetChatLinkOutputVariant2DeliveryArtifactsItem]],
    'availableExports': NotRequired[list[GetChatLinkOutputVariant2DeliveryAvailableExportsItem]],
    'downloadLinksOmitted': Required[bool],
    'scopeOmittedFields': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'storageFailure': Required[Union[GetChatLinkOutputVariant2DeliveryStorageFailureVariant1, None]],
    'nextAction': Required[str],
})
GetChatLinkOutputVariant2Delivery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


GetChatLinkOutputVariant2RecoveryOperation = TypedDict('GetChatLinkOutputVariant2RecoveryOperation', {
    'runId': Required[Union[Annotated[str, Field(max_length=200)], None]],
    'idempotencyKey': Required[Annotated[str, Field(max_length=512)]],
    'state': Required[Annotated[str, Field(max_length=100)]],
})
GetChatLinkOutputVariant2RecoveryOperation.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


GetChatLinkOutputVariant2Recovery = TypedDict('GetChatLinkOutputVariant2Recovery', {
    'idempotencyKey': NotRequired[Annotated[str, Field(max_length=512)]],
    'operationId': NotRequired[Annotated[str, Field(max_length=200)]],
    'runId': NotRequired[Annotated[str, Field(max_length=200)]],
    'jobId': NotRequired[Annotated[str, Field(max_length=200)]],
    'operation': NotRequired[GetChatLinkOutputVariant2RecoveryOperation],
})
GetChatLinkOutputVariant2Recovery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class GetChatLinkOutputVariant2(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    delivery: GetChatLinkOutputVariant2Delivery = Field(..., alias='delivery', description='')
    preview: str = Field(..., alias='preview', description='')
    scope: dict[str, Union[str, Union[float, int], bool, None]] = Field(..., alias='scope', description='')
    recovery: GetChatLinkOutputVariant2Recovery = Field(..., alias='recovery', description='')


# Union schema: validate external payloads with TypeAdapter(GetChatLinkOutput).
GetChatLinkOutput = Union[GetChatLinkOutputVariant2, GetChatLinkOutputVariant1]

_GetChatLinkInputAdapter = TypeAdapter(GetChatLinkInput)
_GetChatLinkOutputAdapter = TypeAdapter(GetChatLinkOutput)