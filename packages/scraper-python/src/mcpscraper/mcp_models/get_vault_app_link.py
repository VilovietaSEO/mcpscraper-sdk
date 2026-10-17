from typing import Annotated, Any, Literal, Union
from typing_extensions import NotRequired, Required, TypedDict
from pydantic import BaseModel, ConfigDict, Field, TypeAdapter


class GetVaultAppLinkInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=False)



class GetVaultAppLinkOutputVariant1(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    ok: bool = Field(..., alias='ok', description='True when the request succeeded.')
    url: Union[str, None] = Field(None, alias='url', description='Vault App link. Present only when the secret is first minted; anyone holding it can use the Vault App as this identity.')
    already_exists: Union[bool, None] = Field(None, alias='alreadyExists', description='True when an active Vault App link exists but its secret cannot be shown again.')
    error: Union[str, None] = Field(None, alias='error', description='Human-readable error when the request cannot be completed.')


GetVaultAppLinkOutputVariant2DeliveryArtifactsItem = TypedDict('GetVaultAppLinkOutputVariant2DeliveryArtifactsItem', {
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
GetVaultAppLinkOutputVariant2DeliveryArtifactsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


GetVaultAppLinkOutputVariant2DeliveryAvailableExportsItem = TypedDict('GetVaultAppLinkOutputVariant2DeliveryAvailableExportsItem', {
    'artifactId': Required[str],
    'sourceArtifactId': Required[str],
    'filename': Required[Literal['result.md']],
    'contentType': Required[Literal['text/markdown; charset=utf-8']],
    'state': Required[Literal['on-demand']],
})
GetVaultAppLinkOutputVariant2DeliveryAvailableExportsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


GetVaultAppLinkOutputVariant2DeliveryStorageFailureVariant1 = TypedDict('GetVaultAppLinkOutputVariant2DeliveryStorageFailureVariant1', {
    'artifactId': Required[Union[str, None]],
    'outcome': Required[Literal['unknown', 'bytes-stored-metadata-pending', 'failed']],
})
GetVaultAppLinkOutputVariant2DeliveryStorageFailureVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


GetVaultAppLinkOutputVariant2Delivery = TypedDict('GetVaultAppLinkOutputVariant2Delivery', {
    'mode': Required[Literal['artifact']],
    'status': Required[Literal['complete', 'partial', 'unavailable']],
    'retainedRepresentation': Required[Literal['formatted-tool-result']],
    'sourceIsError': Required[bool],
    'artifacts': Required[list[GetVaultAppLinkOutputVariant2DeliveryArtifactsItem]],
    'availableExports': NotRequired[list[GetVaultAppLinkOutputVariant2DeliveryAvailableExportsItem]],
    'downloadLinksOmitted': Required[bool],
    'scopeOmittedFields': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'storageFailure': Required[Union[GetVaultAppLinkOutputVariant2DeliveryStorageFailureVariant1, None]],
    'nextAction': Required[str],
})
GetVaultAppLinkOutputVariant2Delivery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


GetVaultAppLinkOutputVariant2RecoveryOperation = TypedDict('GetVaultAppLinkOutputVariant2RecoveryOperation', {
    'runId': Required[Union[Annotated[str, Field(max_length=200)], None]],
    'idempotencyKey': Required[Annotated[str, Field(max_length=512)]],
    'state': Required[Annotated[str, Field(max_length=100)]],
})
GetVaultAppLinkOutputVariant2RecoveryOperation.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


GetVaultAppLinkOutputVariant2Recovery = TypedDict('GetVaultAppLinkOutputVariant2Recovery', {
    'idempotencyKey': NotRequired[Annotated[str, Field(max_length=512)]],
    'operationId': NotRequired[Annotated[str, Field(max_length=200)]],
    'runId': NotRequired[Annotated[str, Field(max_length=200)]],
    'jobId': NotRequired[Annotated[str, Field(max_length=200)]],
    'operation': NotRequired[GetVaultAppLinkOutputVariant2RecoveryOperation],
})
GetVaultAppLinkOutputVariant2Recovery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class GetVaultAppLinkOutputVariant2(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    delivery: GetVaultAppLinkOutputVariant2Delivery = Field(..., alias='delivery', description='')
    preview: str = Field(..., alias='preview', description='')
    scope: dict[str, Union[str, Union[float, int], bool, None]] = Field(..., alias='scope', description='')
    recovery: GetVaultAppLinkOutputVariant2Recovery = Field(..., alias='recovery', description='')


# Union schema: validate external payloads with TypeAdapter(GetVaultAppLinkOutput).
GetVaultAppLinkOutput = Union[GetVaultAppLinkOutputVariant2, GetVaultAppLinkOutputVariant1]

_GetVaultAppLinkInputAdapter = TypeAdapter(GetVaultAppLinkInput)
_GetVaultAppLinkOutputAdapter = TypeAdapter(GetVaultAppLinkOutput)