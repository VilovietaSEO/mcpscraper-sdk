from typing import Annotated, Any, Literal, Union
from typing_extensions import NotRequired, Required, TypedDict
from pydantic import BaseModel, ConfigDict, Field, TypeAdapter


class EditorialReadingRoomGuideInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=False)

    focus: Union[Literal['workflow', 'content_contract', 'example'], None] = Field(None, alias='focus', description='Which part of the reusable editorial-reading-room guide to return. Start with workflow; fetch the content contract or compact example only when needed.')


class EditorialReadingRoomGuideOutputVariant1(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    ok: bool = Field(..., alias='ok', description='')
    focus: Literal['workflow', 'content_contract', 'example'] = Field(..., alias='focus', description='')
    guide: str = Field(..., alias='guide', description='')


EditorialReadingRoomGuideOutputVariant2DeliveryArtifactsItem = TypedDict('EditorialReadingRoomGuideOutputVariant2DeliveryArtifactsItem', {
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
EditorialReadingRoomGuideOutputVariant2DeliveryArtifactsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


EditorialReadingRoomGuideOutputVariant2DeliveryStorageFailureVariant1 = TypedDict('EditorialReadingRoomGuideOutputVariant2DeliveryStorageFailureVariant1', {
    'artifactId': Required[Union[str, None]],
    'outcome': Required[Literal['unknown', 'bytes-stored-metadata-pending', 'failed']],
})
EditorialReadingRoomGuideOutputVariant2DeliveryStorageFailureVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


EditorialReadingRoomGuideOutputVariant2Delivery = TypedDict('EditorialReadingRoomGuideOutputVariant2Delivery', {
    'mode': Required[Literal['artifact']],
    'status': Required[Literal['complete', 'partial', 'unavailable']],
    'retainedRepresentation': Required[Literal['formatted-tool-result']],
    'sourceIsError': Required[bool],
    'artifacts': Required[list[EditorialReadingRoomGuideOutputVariant2DeliveryArtifactsItem]],
    'downloadLinksOmitted': Required[bool],
    'scopeOmittedFields': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'storageFailure': Required[Union[EditorialReadingRoomGuideOutputVariant2DeliveryStorageFailureVariant1, None]],
    'nextAction': Required[str],
})
EditorialReadingRoomGuideOutputVariant2Delivery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


EditorialReadingRoomGuideOutputVariant2RecoveryOperation = TypedDict('EditorialReadingRoomGuideOutputVariant2RecoveryOperation', {
    'runId': Required[Union[Annotated[str, Field(max_length=200)], None]],
    'idempotencyKey': Required[Annotated[str, Field(max_length=512)]],
    'state': Required[Annotated[str, Field(max_length=100)]],
})
EditorialReadingRoomGuideOutputVariant2RecoveryOperation.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


EditorialReadingRoomGuideOutputVariant2Recovery = TypedDict('EditorialReadingRoomGuideOutputVariant2Recovery', {
    'idempotencyKey': NotRequired[Annotated[str, Field(max_length=512)]],
    'operationId': NotRequired[Annotated[str, Field(max_length=200)]],
    'runId': NotRequired[Annotated[str, Field(max_length=200)]],
    'jobId': NotRequired[Annotated[str, Field(max_length=200)]],
    'operation': NotRequired[EditorialReadingRoomGuideOutputVariant2RecoveryOperation],
})
EditorialReadingRoomGuideOutputVariant2Recovery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class EditorialReadingRoomGuideOutputVariant2(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    delivery: EditorialReadingRoomGuideOutputVariant2Delivery = Field(..., alias='delivery', description='')
    preview: str = Field(..., alias='preview', description='')
    scope: dict[str, Union[str, Union[float, int], bool, None]] = Field(..., alias='scope', description='')
    recovery: EditorialReadingRoomGuideOutputVariant2Recovery = Field(..., alias='recovery', description='')


# Union schema: validate external payloads with TypeAdapter(EditorialReadingRoomGuideOutput).
EditorialReadingRoomGuideOutput = Union[EditorialReadingRoomGuideOutputVariant2, EditorialReadingRoomGuideOutputVariant1]

_EditorialReadingRoomGuideInputAdapter = TypeAdapter(EditorialReadingRoomGuideInput)
_EditorialReadingRoomGuideOutputAdapter = TypeAdapter(EditorialReadingRoomGuideOutput)