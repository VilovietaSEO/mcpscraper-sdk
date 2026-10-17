from typing import Annotated, Any, Literal, Union
from typing_extensions import NotRequired, Required, TypedDict
from pydantic import BaseModel, ConfigDict, Field, TypeAdapter


class SerpIdentityCreateInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=False)

    name: str = Field(..., alias='name', description='Stable caller-facing name, e.g. google-us-primary.')
    country: Union[Annotated[str, Field(min_length=2, max_length=2)], None] = Field(None, alias='country', description='Two-letter country for the static network identity. Defaults to US.')


SerpIdentityCreateOutputVariant1Identity = TypedDict('SerpIdentityCreateOutputVariant1Identity', {
    'name': Required[str],
    'country': Required[str],
    'proxy_type': Required[Literal['static_isp']],
    'profile_persistence': Required[Literal['cookies_and_storage']],
    'ip_persistence': Required[Literal['fixed_for_identity_lifetime']],
    'status': Required[Literal['ready', 'deleting', 'error']],
    'created_at': Required[str],
    'last_used_at': Required[Union[str, None]],
})
SerpIdentityCreateOutputVariant1Identity.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class SerpIdentityCreateOutputVariant1(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    ok: bool = Field(..., alias='ok', description='')
    tool: Literal['serp_identity_create'] = Field(..., alias='tool', description='')
    session_id: str = Field(..., alias='session_id', description='Live Google takeover session opened on the new persistent identity.')
    watch_url: str = Field(..., alias='watch_url', description='Give this URL to the user so they can clear consent or CAPTCHA directly on google.com.')
    url: Literal['https://www.google.com/'] = Field(..., alias='url', description='')
    identity: SerpIdentityCreateOutputVariant1Identity = Field(..., alias='identity', description='')
    next_steps: list[str] = Field(..., alias='next_steps', description='')


SerpIdentityCreateOutputVariant2DeliveryArtifactsItem = TypedDict('SerpIdentityCreateOutputVariant2DeliveryArtifactsItem', {
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
SerpIdentityCreateOutputVariant2DeliveryArtifactsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


SerpIdentityCreateOutputVariant2DeliveryAvailableExportsItem = TypedDict('SerpIdentityCreateOutputVariant2DeliveryAvailableExportsItem', {
    'artifactId': Required[str],
    'sourceArtifactId': Required[str],
    'filename': Required[Literal['result.md']],
    'contentType': Required[Literal['text/markdown; charset=utf-8']],
    'state': Required[Literal['on-demand']],
})
SerpIdentityCreateOutputVariant2DeliveryAvailableExportsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


SerpIdentityCreateOutputVariant2DeliveryStorageFailureVariant1 = TypedDict('SerpIdentityCreateOutputVariant2DeliveryStorageFailureVariant1', {
    'artifactId': Required[Union[str, None]],
    'outcome': Required[Literal['unknown', 'bytes-stored-metadata-pending', 'failed']],
})
SerpIdentityCreateOutputVariant2DeliveryStorageFailureVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


SerpIdentityCreateOutputVariant2Delivery = TypedDict('SerpIdentityCreateOutputVariant2Delivery', {
    'mode': Required[Literal['artifact']],
    'status': Required[Literal['complete', 'partial', 'unavailable']],
    'retainedRepresentation': Required[Literal['formatted-tool-result']],
    'sourceIsError': Required[bool],
    'artifacts': Required[list[SerpIdentityCreateOutputVariant2DeliveryArtifactsItem]],
    'availableExports': NotRequired[list[SerpIdentityCreateOutputVariant2DeliveryAvailableExportsItem]],
    'downloadLinksOmitted': Required[bool],
    'scopeOmittedFields': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'storageFailure': Required[Union[SerpIdentityCreateOutputVariant2DeliveryStorageFailureVariant1, None]],
    'nextAction': Required[str],
})
SerpIdentityCreateOutputVariant2Delivery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


SerpIdentityCreateOutputVariant2RecoveryOperation = TypedDict('SerpIdentityCreateOutputVariant2RecoveryOperation', {
    'runId': Required[Union[Annotated[str, Field(max_length=200)], None]],
    'idempotencyKey': Required[Annotated[str, Field(max_length=512)]],
    'state': Required[Annotated[str, Field(max_length=100)]],
})
SerpIdentityCreateOutputVariant2RecoveryOperation.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


SerpIdentityCreateOutputVariant2Recovery = TypedDict('SerpIdentityCreateOutputVariant2Recovery', {
    'idempotencyKey': NotRequired[Annotated[str, Field(max_length=512)]],
    'operationId': NotRequired[Annotated[str, Field(max_length=200)]],
    'runId': NotRequired[Annotated[str, Field(max_length=200)]],
    'jobId': NotRequired[Annotated[str, Field(max_length=200)]],
    'operation': NotRequired[SerpIdentityCreateOutputVariant2RecoveryOperation],
})
SerpIdentityCreateOutputVariant2Recovery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class SerpIdentityCreateOutputVariant2(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    delivery: SerpIdentityCreateOutputVariant2Delivery = Field(..., alias='delivery', description='')
    preview: str = Field(..., alias='preview', description='')
    scope: dict[str, Union[str, Union[float, int], bool, None]] = Field(..., alias='scope', description='')
    recovery: SerpIdentityCreateOutputVariant2Recovery = Field(..., alias='recovery', description='')


# Union schema: validate external payloads with TypeAdapter(SerpIdentityCreateOutput).
SerpIdentityCreateOutput = Union[SerpIdentityCreateOutputVariant1, SerpIdentityCreateOutputVariant2]

_SerpIdentityCreateInputAdapter = TypeAdapter(SerpIdentityCreateInput)
_SerpIdentityCreateOutputAdapter = TypeAdapter(SerpIdentityCreateOutput)