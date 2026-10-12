from typing import Annotated, Any, Literal, Union
from typing_extensions import NotRequired, Required, TypedDict
from pydantic import BaseModel, ConfigDict, Field, TypeAdapter


class SetAgentIdentityInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=False)

    is_agent: bool = Field(..., alias='isAgent', description='true to mark this identity as an AI agent; false to unmark it.')


class SetAgentIdentityOutputVariant1(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    ok: bool = Field(..., alias='ok', description='True on success; false on auth error.')
    is_agent: Union[bool, None] = Field(None, alias='isAgent', description='The flag now in effect.')
    error: Union[str, None] = Field(None, alias='error', description='Human-readable failure reason when ok is false.')


SetAgentIdentityOutputVariant2DeliveryArtifactsItem = TypedDict('SetAgentIdentityOutputVariant2DeliveryArtifactsItem', {
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
SetAgentIdentityOutputVariant2DeliveryArtifactsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


SetAgentIdentityOutputVariant2DeliveryStorageFailureVariant1 = TypedDict('SetAgentIdentityOutputVariant2DeliveryStorageFailureVariant1', {
    'artifactId': Required[Union[str, None]],
    'outcome': Required[Literal['unknown', 'bytes-stored-metadata-pending', 'failed']],
})
SetAgentIdentityOutputVariant2DeliveryStorageFailureVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


SetAgentIdentityOutputVariant2Delivery = TypedDict('SetAgentIdentityOutputVariant2Delivery', {
    'mode': Required[Literal['artifact']],
    'status': Required[Literal['complete', 'partial', 'unavailable']],
    'retainedRepresentation': Required[Literal['formatted-tool-result']],
    'sourceIsError': Required[bool],
    'artifacts': Required[list[SetAgentIdentityOutputVariant2DeliveryArtifactsItem]],
    'downloadLinksOmitted': Required[bool],
    'scopeOmittedFields': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'storageFailure': Required[Union[SetAgentIdentityOutputVariant2DeliveryStorageFailureVariant1, None]],
    'nextAction': Required[str],
})
SetAgentIdentityOutputVariant2Delivery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


SetAgentIdentityOutputVariant2RecoveryOperation = TypedDict('SetAgentIdentityOutputVariant2RecoveryOperation', {
    'runId': Required[Union[Annotated[str, Field(max_length=200)], None]],
    'idempotencyKey': Required[Annotated[str, Field(max_length=512)]],
    'state': Required[Annotated[str, Field(max_length=100)]],
})
SetAgentIdentityOutputVariant2RecoveryOperation.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


SetAgentIdentityOutputVariant2Recovery = TypedDict('SetAgentIdentityOutputVariant2Recovery', {
    'idempotencyKey': NotRequired[Annotated[str, Field(max_length=512)]],
    'operationId': NotRequired[Annotated[str, Field(max_length=200)]],
    'runId': NotRequired[Annotated[str, Field(max_length=200)]],
    'jobId': NotRequired[Annotated[str, Field(max_length=200)]],
    'operation': NotRequired[SetAgentIdentityOutputVariant2RecoveryOperation],
})
SetAgentIdentityOutputVariant2Recovery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class SetAgentIdentityOutputVariant2(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    delivery: SetAgentIdentityOutputVariant2Delivery = Field(..., alias='delivery', description='')
    preview: str = Field(..., alias='preview', description='')
    scope: dict[str, Union[str, Union[float, int], bool, None]] = Field(..., alias='scope', description='')
    recovery: SetAgentIdentityOutputVariant2Recovery = Field(..., alias='recovery', description='')


# Union schema: validate external payloads with TypeAdapter(SetAgentIdentityOutput).
SetAgentIdentityOutput = Union[SetAgentIdentityOutputVariant2, SetAgentIdentityOutputVariant1]

_SetAgentIdentityInputAdapter = TypeAdapter(SetAgentIdentityInput)
_SetAgentIdentityOutputAdapter = TypeAdapter(SetAgentIdentityOutput)