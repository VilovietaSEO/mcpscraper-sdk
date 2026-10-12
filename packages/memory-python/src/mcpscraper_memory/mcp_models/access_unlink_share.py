from typing import Annotated, Any, Literal, Union
from typing_extensions import NotRequired, Required, TypedDict
from pydantic import BaseModel, ConfigDict, Field, TypeAdapter


class AccessUnlinkShareInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=False)

    share_id: Annotated[str, Field(min_length=1)] = Field(..., alias='shareId', description='The shareId to unlink from your "Shared with me" notes.')


class AccessUnlinkShareOutputVariant1(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    ok: bool = Field(..., alias='ok', description='True on success; false on auth/scope/lookup error.')
    share_id: Union[str, None] = Field(None, alias='shareId', description='The unlinked share.')
    error: Union[str, None] = Field(None, alias='error', description='Human-readable failure reason when ok is false.')


AccessUnlinkShareOutputVariant2DeliveryArtifactsItem = TypedDict('AccessUnlinkShareOutputVariant2DeliveryArtifactsItem', {
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
AccessUnlinkShareOutputVariant2DeliveryArtifactsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


AccessUnlinkShareOutputVariant2DeliveryStorageFailureVariant1 = TypedDict('AccessUnlinkShareOutputVariant2DeliveryStorageFailureVariant1', {
    'artifactId': Required[Union[str, None]],
    'outcome': Required[Literal['unknown', 'bytes-stored-metadata-pending', 'failed']],
})
AccessUnlinkShareOutputVariant2DeliveryStorageFailureVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


AccessUnlinkShareOutputVariant2Delivery = TypedDict('AccessUnlinkShareOutputVariant2Delivery', {
    'mode': Required[Literal['artifact']],
    'status': Required[Literal['complete', 'partial', 'unavailable']],
    'retainedRepresentation': Required[Literal['formatted-tool-result']],
    'sourceIsError': Required[bool],
    'artifacts': Required[list[AccessUnlinkShareOutputVariant2DeliveryArtifactsItem]],
    'downloadLinksOmitted': Required[bool],
    'scopeOmittedFields': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'storageFailure': Required[Union[AccessUnlinkShareOutputVariant2DeliveryStorageFailureVariant1, None]],
    'nextAction': Required[str],
})
AccessUnlinkShareOutputVariant2Delivery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


AccessUnlinkShareOutputVariant2RecoveryOperation = TypedDict('AccessUnlinkShareOutputVariant2RecoveryOperation', {
    'runId': Required[Union[Annotated[str, Field(max_length=200)], None]],
    'idempotencyKey': Required[Annotated[str, Field(max_length=512)]],
    'state': Required[Annotated[str, Field(max_length=100)]],
})
AccessUnlinkShareOutputVariant2RecoveryOperation.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


AccessUnlinkShareOutputVariant2Recovery = TypedDict('AccessUnlinkShareOutputVariant2Recovery', {
    'idempotencyKey': NotRequired[Annotated[str, Field(max_length=512)]],
    'operationId': NotRequired[Annotated[str, Field(max_length=200)]],
    'runId': NotRequired[Annotated[str, Field(max_length=200)]],
    'jobId': NotRequired[Annotated[str, Field(max_length=200)]],
    'operation': NotRequired[AccessUnlinkShareOutputVariant2RecoveryOperation],
})
AccessUnlinkShareOutputVariant2Recovery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class AccessUnlinkShareOutputVariant2(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    delivery: AccessUnlinkShareOutputVariant2Delivery = Field(..., alias='delivery', description='')
    preview: str = Field(..., alias='preview', description='')
    scope: dict[str, Union[str, Union[float, int], bool, None]] = Field(..., alias='scope', description='')
    recovery: AccessUnlinkShareOutputVariant2Recovery = Field(..., alias='recovery', description='')


# Union schema: validate external payloads with TypeAdapter(AccessUnlinkShareOutput).
AccessUnlinkShareOutput = Union[AccessUnlinkShareOutputVariant2, AccessUnlinkShareOutputVariant1]

_AccessUnlinkShareInputAdapter = TypeAdapter(AccessUnlinkShareInput)
_AccessUnlinkShareOutputAdapter = TypeAdapter(AccessUnlinkShareOutput)