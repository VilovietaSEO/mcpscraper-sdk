from typing import Annotated, Any, Literal, Union
from typing_extensions import NotRequired, Required, TypedDict
from pydantic import BaseModel, ConfigDict, Field, TypeAdapter


class MyMentionsInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=False)

    limit: Union[Annotated[int, Field(ge=1, le=100)], None] = Field(None, alias='limit', description='Max mentions to return. Optional; default 25.')


MyMentionsOutputVariant1MentionsItem = TypedDict('MyMentionsOutputVariant1MentionsItem', {
    'channel': Required[str],
    'messageId': Required[str],
    'authorIdentity': Required[Union[str, None]],
    'content': Required[str],
    'mentionedAt': Required[str],
})
MyMentionsOutputVariant1MentionsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class MyMentionsOutputVariant1(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    ok: bool = Field(..., alias='ok', description='True on success; false on auth error.')
    mentions: Union[list[MyMentionsOutputVariant1MentionsItem], None] = Field(None, alias='mentions', description='Present when ok is true.')
    error: Union[str, None] = Field(None, alias='error', description='Human-readable failure reason when ok is false.')


MyMentionsOutputVariant2DeliveryArtifactsItem = TypedDict('MyMentionsOutputVariant2DeliveryArtifactsItem', {
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
MyMentionsOutputVariant2DeliveryArtifactsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


MyMentionsOutputVariant2DeliveryStorageFailureVariant1 = TypedDict('MyMentionsOutputVariant2DeliveryStorageFailureVariant1', {
    'artifactId': Required[Union[str, None]],
    'outcome': Required[Literal['unknown', 'bytes-stored-metadata-pending', 'failed']],
})
MyMentionsOutputVariant2DeliveryStorageFailureVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


MyMentionsOutputVariant2Delivery = TypedDict('MyMentionsOutputVariant2Delivery', {
    'mode': Required[Literal['artifact']],
    'status': Required[Literal['complete', 'partial', 'unavailable']],
    'retainedRepresentation': Required[Literal['formatted-tool-result']],
    'sourceIsError': Required[bool],
    'artifacts': Required[list[MyMentionsOutputVariant2DeliveryArtifactsItem]],
    'downloadLinksOmitted': Required[bool],
    'scopeOmittedFields': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'storageFailure': Required[Union[MyMentionsOutputVariant2DeliveryStorageFailureVariant1, None]],
    'nextAction': Required[str],
})
MyMentionsOutputVariant2Delivery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


MyMentionsOutputVariant2RecoveryOperation = TypedDict('MyMentionsOutputVariant2RecoveryOperation', {
    'runId': Required[Union[Annotated[str, Field(max_length=200)], None]],
    'idempotencyKey': Required[Annotated[str, Field(max_length=512)]],
    'state': Required[Annotated[str, Field(max_length=100)]],
})
MyMentionsOutputVariant2RecoveryOperation.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


MyMentionsOutputVariant2Recovery = TypedDict('MyMentionsOutputVariant2Recovery', {
    'idempotencyKey': NotRequired[Annotated[str, Field(max_length=512)]],
    'operationId': NotRequired[Annotated[str, Field(max_length=200)]],
    'runId': NotRequired[Annotated[str, Field(max_length=200)]],
    'jobId': NotRequired[Annotated[str, Field(max_length=200)]],
    'operation': NotRequired[MyMentionsOutputVariant2RecoveryOperation],
})
MyMentionsOutputVariant2Recovery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class MyMentionsOutputVariant2(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    delivery: MyMentionsOutputVariant2Delivery = Field(..., alias='delivery', description='')
    preview: str = Field(..., alias='preview', description='')
    scope: dict[str, Union[str, Union[float, int], bool, None]] = Field(..., alias='scope', description='')
    recovery: MyMentionsOutputVariant2Recovery = Field(..., alias='recovery', description='')


# Union schema: validate external payloads with TypeAdapter(MyMentionsOutput).
MyMentionsOutput = Union[MyMentionsOutputVariant2, MyMentionsOutputVariant1]

_MyMentionsInputAdapter = TypeAdapter(MyMentionsInput)
_MyMentionsOutputAdapter = TypeAdapter(MyMentionsOutput)