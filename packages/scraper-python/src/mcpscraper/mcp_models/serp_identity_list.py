from typing import Annotated, Any, Literal, Union
from typing_extensions import NotRequired, Required, TypedDict
from pydantic import BaseModel, ConfigDict, Field, TypeAdapter


class SerpIdentityListInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=False)



SerpIdentityListOutputVariant1IdentitiesItem = TypedDict('SerpIdentityListOutputVariant1IdentitiesItem', {
    'name': Required[str],
    'country': Required[str],
    'proxy_type': Required[Literal['static_isp']],
    'profile_persistence': Required[Literal['cookies_and_storage']],
    'ip_persistence': Required[Literal['fixed_for_identity_lifetime']],
    'status': Required[Literal['ready', 'deleting', 'error']],
    'created_at': Required[str],
    'last_used_at': Required[Union[str, None]],
})
SerpIdentityListOutputVariant1IdentitiesItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class SerpIdentityListOutputVariant1(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    ok: bool = Field(..., alias='ok', description='')
    tool: Literal['serp_identity_list'] = Field(..., alias='tool', description='')
    session_id: None = Field(..., alias='session_id', description='')
    identities: list[SerpIdentityListOutputVariant1IdentitiesItem] = Field(..., alias='identities', description='')
    count: Annotated[int, Field(ge=0, le=9007199254740991)] = Field(..., alias='count', description='')


SerpIdentityListOutputVariant2DeliveryArtifactsItem = TypedDict('SerpIdentityListOutputVariant2DeliveryArtifactsItem', {
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
SerpIdentityListOutputVariant2DeliveryArtifactsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


SerpIdentityListOutputVariant2DeliveryAvailableExportsItem = TypedDict('SerpIdentityListOutputVariant2DeliveryAvailableExportsItem', {
    'artifactId': Required[str],
    'sourceArtifactId': Required[str],
    'filename': Required[Literal['result.md']],
    'contentType': Required[Literal['text/markdown; charset=utf-8']],
    'state': Required[Literal['on-demand']],
})
SerpIdentityListOutputVariant2DeliveryAvailableExportsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


SerpIdentityListOutputVariant2DeliveryStorageFailureVariant1 = TypedDict('SerpIdentityListOutputVariant2DeliveryStorageFailureVariant1', {
    'artifactId': Required[Union[str, None]],
    'outcome': Required[Literal['unknown', 'bytes-stored-metadata-pending', 'failed']],
})
SerpIdentityListOutputVariant2DeliveryStorageFailureVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


SerpIdentityListOutputVariant2Delivery = TypedDict('SerpIdentityListOutputVariant2Delivery', {
    'mode': Required[Literal['artifact']],
    'status': Required[Literal['complete', 'partial', 'unavailable']],
    'retainedRepresentation': Required[Literal['formatted-tool-result']],
    'sourceIsError': Required[bool],
    'artifacts': Required[list[SerpIdentityListOutputVariant2DeliveryArtifactsItem]],
    'availableExports': NotRequired[list[SerpIdentityListOutputVariant2DeliveryAvailableExportsItem]],
    'downloadLinksOmitted': Required[bool],
    'scopeOmittedFields': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'storageFailure': Required[Union[SerpIdentityListOutputVariant2DeliveryStorageFailureVariant1, None]],
    'nextAction': Required[str],
})
SerpIdentityListOutputVariant2Delivery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


SerpIdentityListOutputVariant2RecoveryOperation = TypedDict('SerpIdentityListOutputVariant2RecoveryOperation', {
    'runId': Required[Union[Annotated[str, Field(max_length=200)], None]],
    'idempotencyKey': Required[Annotated[str, Field(max_length=512)]],
    'state': Required[Annotated[str, Field(max_length=100)]],
})
SerpIdentityListOutputVariant2RecoveryOperation.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


SerpIdentityListOutputVariant2Recovery = TypedDict('SerpIdentityListOutputVariant2Recovery', {
    'idempotencyKey': NotRequired[Annotated[str, Field(max_length=512)]],
    'operationId': NotRequired[Annotated[str, Field(max_length=200)]],
    'runId': NotRequired[Annotated[str, Field(max_length=200)]],
    'jobId': NotRequired[Annotated[str, Field(max_length=200)]],
    'operation': NotRequired[SerpIdentityListOutputVariant2RecoveryOperation],
})
SerpIdentityListOutputVariant2Recovery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class SerpIdentityListOutputVariant2(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    delivery: SerpIdentityListOutputVariant2Delivery = Field(..., alias='delivery', description='')
    preview: str = Field(..., alias='preview', description='')
    scope: dict[str, Union[str, Union[float, int], bool, None]] = Field(..., alias='scope', description='')
    recovery: SerpIdentityListOutputVariant2Recovery = Field(..., alias='recovery', description='')


# Union schema: validate external payloads with TypeAdapter(SerpIdentityListOutput).
SerpIdentityListOutput = Union[SerpIdentityListOutputVariant1, SerpIdentityListOutputVariant2]

_SerpIdentityListInputAdapter = TypeAdapter(SerpIdentityListInput)
_SerpIdentityListOutputAdapter = TypeAdapter(SerpIdentityListOutput)