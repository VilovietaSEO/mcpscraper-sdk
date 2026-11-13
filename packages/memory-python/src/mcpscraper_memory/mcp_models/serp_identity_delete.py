from typing import Annotated, Any, Literal, Union
from typing_extensions import NotRequired, Required, TypedDict
from pydantic import BaseModel, ConfigDict, Field, TypeAdapter


class SerpIdentityDeleteInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=False)

    name: str = Field(..., alias='name', description='Identity name returned by serp_identity_list.')
    confirm: Literal[True] = Field(..., alias='confirm', description='Must be true because deletion permanently removes the saved browser state and its fixed proxy.')


class SerpIdentityDeleteOutputVariant1(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    ok: bool = Field(..., alias='ok', description='')
    tool: Literal['serp_identity_delete'] = Field(..., alias='tool', description='')
    session_id: None = Field(..., alias='session_id', description='')
    name: str = Field(..., alias='name', description='')
    deleted: bool = Field(..., alias='deleted', description='')


SerpIdentityDeleteOutputVariant2DeliveryArtifactsItem = TypedDict('SerpIdentityDeleteOutputVariant2DeliveryArtifactsItem', {
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
SerpIdentityDeleteOutputVariant2DeliveryArtifactsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


SerpIdentityDeleteOutputVariant2DeliveryAvailableExportsItem = TypedDict('SerpIdentityDeleteOutputVariant2DeliveryAvailableExportsItem', {
    'artifactId': Required[str],
    'sourceArtifactId': Required[str],
    'filename': Required[Literal['result.md']],
    'contentType': Required[Literal['text/markdown; charset=utf-8']],
    'state': Required[Literal['on-demand']],
})
SerpIdentityDeleteOutputVariant2DeliveryAvailableExportsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


SerpIdentityDeleteOutputVariant2DeliveryStorageFailureVariant1 = TypedDict('SerpIdentityDeleteOutputVariant2DeliveryStorageFailureVariant1', {
    'artifactId': Required[Union[str, None]],
    'outcome': Required[Literal['unknown', 'bytes-stored-metadata-pending', 'failed']],
})
SerpIdentityDeleteOutputVariant2DeliveryStorageFailureVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


SerpIdentityDeleteOutputVariant2Delivery = TypedDict('SerpIdentityDeleteOutputVariant2Delivery', {
    'mode': Required[Literal['artifact']],
    'status': Required[Literal['complete', 'partial', 'unavailable']],
    'retainedRepresentation': Required[Literal['formatted-tool-result']],
    'sourceIsError': Required[bool],
    'artifacts': Required[list[SerpIdentityDeleteOutputVariant2DeliveryArtifactsItem]],
    'availableExports': NotRequired[list[SerpIdentityDeleteOutputVariant2DeliveryAvailableExportsItem]],
    'downloadLinksOmitted': Required[bool],
    'scopeOmittedFields': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'storageFailure': Required[Union[SerpIdentityDeleteOutputVariant2DeliveryStorageFailureVariant1, None]],
    'nextAction': Required[str],
})
SerpIdentityDeleteOutputVariant2Delivery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


SerpIdentityDeleteOutputVariant2RecoveryOperation = TypedDict('SerpIdentityDeleteOutputVariant2RecoveryOperation', {
    'runId': Required[Union[Annotated[str, Field(max_length=200)], None]],
    'idempotencyKey': Required[Annotated[str, Field(max_length=512)]],
    'state': Required[Annotated[str, Field(max_length=100)]],
})
SerpIdentityDeleteOutputVariant2RecoveryOperation.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


SerpIdentityDeleteOutputVariant2Recovery = TypedDict('SerpIdentityDeleteOutputVariant2Recovery', {
    'idempotencyKey': NotRequired[Annotated[str, Field(max_length=512)]],
    'operationId': NotRequired[Annotated[str, Field(max_length=200)]],
    'runId': NotRequired[Annotated[str, Field(max_length=200)]],
    'jobId': NotRequired[Annotated[str, Field(max_length=200)]],
    'operation': NotRequired[SerpIdentityDeleteOutputVariant2RecoveryOperation],
})
SerpIdentityDeleteOutputVariant2Recovery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class SerpIdentityDeleteOutputVariant2(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    delivery: SerpIdentityDeleteOutputVariant2Delivery = Field(..., alias='delivery', description='')
    preview: str = Field(..., alias='preview', description='')
    scope: dict[str, Union[str, Union[float, int], bool, None]] = Field(..., alias='scope', description='')
    recovery: SerpIdentityDeleteOutputVariant2Recovery = Field(..., alias='recovery', description='')


# Union schema: validate external payloads with TypeAdapter(SerpIdentityDeleteOutput).
SerpIdentityDeleteOutput = Union[SerpIdentityDeleteOutputVariant1, SerpIdentityDeleteOutputVariant2]

_SerpIdentityDeleteInputAdapter = TypeAdapter(SerpIdentityDeleteInput)
_SerpIdentityDeleteOutputAdapter = TypeAdapter(SerpIdentityDeleteOutput)