from typing import Annotated, Any, Literal, Union
from typing_extensions import NotRequired, Required, TypedDict
from pydantic import BaseModel, ConfigDict, Field, TypeAdapter


class RenewEditorialReadingRoomDownloadInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=False)

    artifact_id: Annotated[str, Field(min_length=1)] = Field(..., alias='artifactId', description='Private artifactId returned by create_editorial_reading_room.')


class RenewEditorialReadingRoomDownloadOutputVariant1(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    ok: bool = Field(..., alias='ok', description='')
    artifact_id: str = Field(..., alias='artifactId', description='')
    download_url: str = Field(..., alias='downloadUrl', description='')
    download_url_expires_at: str = Field(..., alias='downloadUrlExpiresAt', description='')
    expires_at: str = Field(..., alias='expiresAt', description='')


RenewEditorialReadingRoomDownloadOutputVariant2DeliveryArtifactsItem = TypedDict('RenewEditorialReadingRoomDownloadOutputVariant2DeliveryArtifactsItem', {
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
RenewEditorialReadingRoomDownloadOutputVariant2DeliveryArtifactsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


RenewEditorialReadingRoomDownloadOutputVariant2DeliveryStorageFailureVariant1 = TypedDict('RenewEditorialReadingRoomDownloadOutputVariant2DeliveryStorageFailureVariant1', {
    'artifactId': Required[Union[str, None]],
    'outcome': Required[Literal['unknown', 'bytes-stored-metadata-pending', 'failed']],
})
RenewEditorialReadingRoomDownloadOutputVariant2DeliveryStorageFailureVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


RenewEditorialReadingRoomDownloadOutputVariant2Delivery = TypedDict('RenewEditorialReadingRoomDownloadOutputVariant2Delivery', {
    'mode': Required[Literal['artifact']],
    'status': Required[Literal['complete', 'partial', 'unavailable']],
    'retainedRepresentation': Required[Literal['formatted-tool-result']],
    'sourceIsError': Required[bool],
    'artifacts': Required[list[RenewEditorialReadingRoomDownloadOutputVariant2DeliveryArtifactsItem]],
    'downloadLinksOmitted': Required[bool],
    'scopeOmittedFields': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'storageFailure': Required[Union[RenewEditorialReadingRoomDownloadOutputVariant2DeliveryStorageFailureVariant1, None]],
    'nextAction': Required[str],
})
RenewEditorialReadingRoomDownloadOutputVariant2Delivery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


RenewEditorialReadingRoomDownloadOutputVariant2RecoveryOperation = TypedDict('RenewEditorialReadingRoomDownloadOutputVariant2RecoveryOperation', {
    'runId': Required[Union[Annotated[str, Field(max_length=200)], None]],
    'idempotencyKey': Required[Annotated[str, Field(max_length=512)]],
    'state': Required[Annotated[str, Field(max_length=100)]],
})
RenewEditorialReadingRoomDownloadOutputVariant2RecoveryOperation.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


RenewEditorialReadingRoomDownloadOutputVariant2Recovery = TypedDict('RenewEditorialReadingRoomDownloadOutputVariant2Recovery', {
    'idempotencyKey': NotRequired[Annotated[str, Field(max_length=512)]],
    'operationId': NotRequired[Annotated[str, Field(max_length=200)]],
    'runId': NotRequired[Annotated[str, Field(max_length=200)]],
    'jobId': NotRequired[Annotated[str, Field(max_length=200)]],
    'operation': NotRequired[RenewEditorialReadingRoomDownloadOutputVariant2RecoveryOperation],
})
RenewEditorialReadingRoomDownloadOutputVariant2Recovery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class RenewEditorialReadingRoomDownloadOutputVariant2(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    delivery: RenewEditorialReadingRoomDownloadOutputVariant2Delivery = Field(..., alias='delivery', description='')
    preview: str = Field(..., alias='preview', description='')
    scope: dict[str, Union[str, Union[float, int], bool, None]] = Field(..., alias='scope', description='')
    recovery: RenewEditorialReadingRoomDownloadOutputVariant2Recovery = Field(..., alias='recovery', description='')


# Union schema: validate external payloads with TypeAdapter(RenewEditorialReadingRoomDownloadOutput).
RenewEditorialReadingRoomDownloadOutput = Union[RenewEditorialReadingRoomDownloadOutputVariant1, RenewEditorialReadingRoomDownloadOutputVariant2]

_RenewEditorialReadingRoomDownloadInputAdapter = TypeAdapter(RenewEditorialReadingRoomDownloadInput)
_RenewEditorialReadingRoomDownloadOutputAdapter = TypeAdapter(RenewEditorialReadingRoomDownloadOutput)