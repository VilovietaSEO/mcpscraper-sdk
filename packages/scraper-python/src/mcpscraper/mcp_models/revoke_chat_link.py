from typing import Annotated, Any, Literal, Union
from typing_extensions import NotRequired, Required, TypedDict
from pydantic import BaseModel, ConfigDict, Field, TypeAdapter


class RevokeChatLinkInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=False)



class RevokeChatLinkOutputVariant1(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    ok: bool = Field(..., alias='ok', description='True on success; false on auth error.')
    revoked: Union[bool, None] = Field(None, alias='revoked', description='True if a link existed and was revoked; false if there was none to revoke.')
    error: Union[str, None] = Field(None, alias='error', description='Human-readable failure reason when ok is false.')


RevokeChatLinkOutputVariant2DeliveryArtifactsItem = TypedDict('RevokeChatLinkOutputVariant2DeliveryArtifactsItem', {
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
RevokeChatLinkOutputVariant2DeliveryArtifactsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


RevokeChatLinkOutputVariant2DeliveryAvailableExportsItem = TypedDict('RevokeChatLinkOutputVariant2DeliveryAvailableExportsItem', {
    'artifactId': Required[str],
    'sourceArtifactId': Required[str],
    'filename': Required[Literal['result.md']],
    'contentType': Required[Literal['text/markdown; charset=utf-8']],
    'state': Required[Literal['on-demand']],
})
RevokeChatLinkOutputVariant2DeliveryAvailableExportsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


RevokeChatLinkOutputVariant2DeliveryStorageFailureVariant1 = TypedDict('RevokeChatLinkOutputVariant2DeliveryStorageFailureVariant1', {
    'artifactId': Required[Union[str, None]],
    'outcome': Required[Literal['unknown', 'bytes-stored-metadata-pending', 'failed']],
})
RevokeChatLinkOutputVariant2DeliveryStorageFailureVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


RevokeChatLinkOutputVariant2Delivery = TypedDict('RevokeChatLinkOutputVariant2Delivery', {
    'mode': Required[Literal['artifact']],
    'status': Required[Literal['complete', 'partial', 'unavailable']],
    'retainedRepresentation': Required[Literal['formatted-tool-result']],
    'sourceIsError': Required[bool],
    'artifacts': Required[list[RevokeChatLinkOutputVariant2DeliveryArtifactsItem]],
    'availableExports': NotRequired[list[RevokeChatLinkOutputVariant2DeliveryAvailableExportsItem]],
    'downloadLinksOmitted': Required[bool],
    'scopeOmittedFields': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'storageFailure': Required[Union[RevokeChatLinkOutputVariant2DeliveryStorageFailureVariant1, None]],
    'nextAction': Required[str],
})
RevokeChatLinkOutputVariant2Delivery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


RevokeChatLinkOutputVariant2RecoveryOperation = TypedDict('RevokeChatLinkOutputVariant2RecoveryOperation', {
    'runId': Required[Union[Annotated[str, Field(max_length=200)], None]],
    'idempotencyKey': Required[Annotated[str, Field(max_length=512)]],
    'state': Required[Annotated[str, Field(max_length=100)]],
})
RevokeChatLinkOutputVariant2RecoveryOperation.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


RevokeChatLinkOutputVariant2Recovery = TypedDict('RevokeChatLinkOutputVariant2Recovery', {
    'idempotencyKey': NotRequired[Annotated[str, Field(max_length=512)]],
    'operationId': NotRequired[Annotated[str, Field(max_length=200)]],
    'runId': NotRequired[Annotated[str, Field(max_length=200)]],
    'jobId': NotRequired[Annotated[str, Field(max_length=200)]],
    'operation': NotRequired[RevokeChatLinkOutputVariant2RecoveryOperation],
})
RevokeChatLinkOutputVariant2Recovery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class RevokeChatLinkOutputVariant2(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    delivery: RevokeChatLinkOutputVariant2Delivery = Field(..., alias='delivery', description='')
    preview: str = Field(..., alias='preview', description='')
    scope: dict[str, Union[str, Union[float, int], bool, None]] = Field(..., alias='scope', description='')
    recovery: RevokeChatLinkOutputVariant2Recovery = Field(..., alias='recovery', description='')


# Union schema: validate external payloads with TypeAdapter(RevokeChatLinkOutput).
RevokeChatLinkOutput = Union[RevokeChatLinkOutputVariant2, RevokeChatLinkOutputVariant1]

_RevokeChatLinkInputAdapter = TypeAdapter(RevokeChatLinkInput)
_RevokeChatLinkOutputAdapter = TypeAdapter(RevokeChatLinkOutput)