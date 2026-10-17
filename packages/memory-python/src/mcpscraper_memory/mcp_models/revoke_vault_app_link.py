from typing import Annotated, Any, Literal, Union
from typing_extensions import NotRequired, Required, TypedDict
from pydantic import BaseModel, ConfigDict, Field, TypeAdapter


class RevokeVaultAppLinkInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=False)



class RevokeVaultAppLinkOutputVariant1(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    ok: bool = Field(..., alias='ok', description='True when the request succeeded.')
    revoked: Union[bool, None] = Field(None, alias='revoked', description='True when an active Vault App link was revoked.')
    error: Union[str, None] = Field(None, alias='error', description='Human-readable error when the request cannot be completed.')


RevokeVaultAppLinkOutputVariant2DeliveryArtifactsItem = TypedDict('RevokeVaultAppLinkOutputVariant2DeliveryArtifactsItem', {
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
RevokeVaultAppLinkOutputVariant2DeliveryArtifactsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


RevokeVaultAppLinkOutputVariant2DeliveryAvailableExportsItem = TypedDict('RevokeVaultAppLinkOutputVariant2DeliveryAvailableExportsItem', {
    'artifactId': Required[str],
    'sourceArtifactId': Required[str],
    'filename': Required[Literal['result.md']],
    'contentType': Required[Literal['text/markdown; charset=utf-8']],
    'state': Required[Literal['on-demand']],
})
RevokeVaultAppLinkOutputVariant2DeliveryAvailableExportsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


RevokeVaultAppLinkOutputVariant2DeliveryStorageFailureVariant1 = TypedDict('RevokeVaultAppLinkOutputVariant2DeliveryStorageFailureVariant1', {
    'artifactId': Required[Union[str, None]],
    'outcome': Required[Literal['unknown', 'bytes-stored-metadata-pending', 'failed']],
})
RevokeVaultAppLinkOutputVariant2DeliveryStorageFailureVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


RevokeVaultAppLinkOutputVariant2Delivery = TypedDict('RevokeVaultAppLinkOutputVariant2Delivery', {
    'mode': Required[Literal['artifact']],
    'status': Required[Literal['complete', 'partial', 'unavailable']],
    'retainedRepresentation': Required[Literal['formatted-tool-result']],
    'sourceIsError': Required[bool],
    'artifacts': Required[list[RevokeVaultAppLinkOutputVariant2DeliveryArtifactsItem]],
    'availableExports': NotRequired[list[RevokeVaultAppLinkOutputVariant2DeliveryAvailableExportsItem]],
    'downloadLinksOmitted': Required[bool],
    'scopeOmittedFields': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'storageFailure': Required[Union[RevokeVaultAppLinkOutputVariant2DeliveryStorageFailureVariant1, None]],
    'nextAction': Required[str],
})
RevokeVaultAppLinkOutputVariant2Delivery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


RevokeVaultAppLinkOutputVariant2RecoveryOperation = TypedDict('RevokeVaultAppLinkOutputVariant2RecoveryOperation', {
    'runId': Required[Union[Annotated[str, Field(max_length=200)], None]],
    'idempotencyKey': Required[Annotated[str, Field(max_length=512)]],
    'state': Required[Annotated[str, Field(max_length=100)]],
})
RevokeVaultAppLinkOutputVariant2RecoveryOperation.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


RevokeVaultAppLinkOutputVariant2Recovery = TypedDict('RevokeVaultAppLinkOutputVariant2Recovery', {
    'idempotencyKey': NotRequired[Annotated[str, Field(max_length=512)]],
    'operationId': NotRequired[Annotated[str, Field(max_length=200)]],
    'runId': NotRequired[Annotated[str, Field(max_length=200)]],
    'jobId': NotRequired[Annotated[str, Field(max_length=200)]],
    'operation': NotRequired[RevokeVaultAppLinkOutputVariant2RecoveryOperation],
})
RevokeVaultAppLinkOutputVariant2Recovery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class RevokeVaultAppLinkOutputVariant2(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    delivery: RevokeVaultAppLinkOutputVariant2Delivery = Field(..., alias='delivery', description='')
    preview: str = Field(..., alias='preview', description='')
    scope: dict[str, Union[str, Union[float, int], bool, None]] = Field(..., alias='scope', description='')
    recovery: RevokeVaultAppLinkOutputVariant2Recovery = Field(..., alias='recovery', description='')


# Union schema: validate external payloads with TypeAdapter(RevokeVaultAppLinkOutput).
RevokeVaultAppLinkOutput = Union[RevokeVaultAppLinkOutputVariant2, RevokeVaultAppLinkOutputVariant1]

_RevokeVaultAppLinkInputAdapter = TypeAdapter(RevokeVaultAppLinkInput)
_RevokeVaultAppLinkOutputAdapter = TypeAdapter(RevokeVaultAppLinkOutput)