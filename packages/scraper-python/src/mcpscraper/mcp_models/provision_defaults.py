from typing import Annotated, Any, Literal, Union
from typing_extensions import NotRequired, Required, TypedDict
from pydantic import BaseModel, ConfigDict, Field, TypeAdapter


class ProvisionDefaultsInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=False)

    grantee_identity: Annotated[str, Field(min_length=1)] = Field(..., alias='granteeIdentity', description='Identity that should OWN the 16 default vaults (e.g. an email or user id).')
    issue_key: Union[bool, None] = Field(None, alias='issueKey', description='When true, also issue a new API key for the identity entitled to all 16 vaults and return its secret once. Default false.')
    plan: Union[Literal['free', 'pro', 'team', 'enterprise'], None] = Field(None, alias='plan', description='Subscription plan carried by the issued key. Optional; defaults to free. Only used when issueKey is true.')


class ProvisionDefaultsOutputVariant1(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    ok: bool = Field(..., alias='ok', description='True when provisioning succeeded; false on auth/scope error.')
    identity: Union[str, None] = Field(None, alias='identity', description='Identity the vaults were provisioned for.')
    created: Union[list[str], None] = Field(None, alias='created', description='Vault names newly created on this call (empty when all 16 already existed).')
    vaults: Union[list[str], None] = Field(None, alias='vaults', description='All 16 default vault names the identity now owns.')
    key_id: Union[str, None] = Field(None, alias='keyId', description='Stable id of the issued key. Present only when issueKey was true.')
    secret: Union[str, None] = Field(None, alias='secret', description='The issued key secret — RETURNED ONCE. Present only when issueKey was true.')
    plan: Union[str, None] = Field(None, alias='plan', description='Plan assigned to the issued key. Present only when issueKey was true.')
    error: Union[str, None] = Field(None, alias='error', description='Human-readable failure reason when ok is false.')


ProvisionDefaultsOutputVariant2DeliveryArtifactsItem = TypedDict('ProvisionDefaultsOutputVariant2DeliveryArtifactsItem', {
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
ProvisionDefaultsOutputVariant2DeliveryArtifactsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


ProvisionDefaultsOutputVariant2DeliveryStorageFailureVariant1 = TypedDict('ProvisionDefaultsOutputVariant2DeliveryStorageFailureVariant1', {
    'artifactId': Required[Union[str, None]],
    'outcome': Required[Literal['unknown', 'bytes-stored-metadata-pending', 'failed']],
})
ProvisionDefaultsOutputVariant2DeliveryStorageFailureVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


ProvisionDefaultsOutputVariant2Delivery = TypedDict('ProvisionDefaultsOutputVariant2Delivery', {
    'mode': Required[Literal['artifact']],
    'status': Required[Literal['complete', 'partial', 'unavailable']],
    'retainedRepresentation': Required[Literal['formatted-tool-result']],
    'sourceIsError': Required[bool],
    'artifacts': Required[list[ProvisionDefaultsOutputVariant2DeliveryArtifactsItem]],
    'downloadLinksOmitted': Required[bool],
    'scopeOmittedFields': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'storageFailure': Required[Union[ProvisionDefaultsOutputVariant2DeliveryStorageFailureVariant1, None]],
    'nextAction': Required[str],
})
ProvisionDefaultsOutputVariant2Delivery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


ProvisionDefaultsOutputVariant2RecoveryOperation = TypedDict('ProvisionDefaultsOutputVariant2RecoveryOperation', {
    'runId': Required[Union[Annotated[str, Field(max_length=200)], None]],
    'idempotencyKey': Required[Annotated[str, Field(max_length=512)]],
    'state': Required[Annotated[str, Field(max_length=100)]],
})
ProvisionDefaultsOutputVariant2RecoveryOperation.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


ProvisionDefaultsOutputVariant2Recovery = TypedDict('ProvisionDefaultsOutputVariant2Recovery', {
    'idempotencyKey': NotRequired[Annotated[str, Field(max_length=512)]],
    'operationId': NotRequired[Annotated[str, Field(max_length=200)]],
    'runId': NotRequired[Annotated[str, Field(max_length=200)]],
    'jobId': NotRequired[Annotated[str, Field(max_length=200)]],
    'operation': NotRequired[ProvisionDefaultsOutputVariant2RecoveryOperation],
})
ProvisionDefaultsOutputVariant2Recovery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class ProvisionDefaultsOutputVariant2(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    delivery: ProvisionDefaultsOutputVariant2Delivery = Field(..., alias='delivery', description='')
    preview: str = Field(..., alias='preview', description='')
    scope: dict[str, Union[str, Union[float, int], bool, None]] = Field(..., alias='scope', description='')
    recovery: ProvisionDefaultsOutputVariant2Recovery = Field(..., alias='recovery', description='')


# Union schema: validate external payloads with TypeAdapter(ProvisionDefaultsOutput).
ProvisionDefaultsOutput = Union[ProvisionDefaultsOutputVariant2, ProvisionDefaultsOutputVariant1]

_ProvisionDefaultsInputAdapter = TypeAdapter(ProvisionDefaultsInput)
_ProvisionDefaultsOutputAdapter = TypeAdapter(ProvisionDefaultsOutput)