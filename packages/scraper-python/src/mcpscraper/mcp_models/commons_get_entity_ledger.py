from typing import Annotated, Any, Literal, Union
from typing_extensions import NotRequired, Required, TypedDict
from pydantic import BaseModel, ConfigDict, Field, TypeAdapter


class CommonsGetEntityLedgerInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=False)

    id_or_slug: Annotated[str, Field(min_length=1, max_length=180)] = Field(..., alias='idOrSlug', description='Published entity id or /wiki/ slug whose contribution ledger should be read.')


class CommonsGetEntityLedgerOutputVariant1(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    ok: bool = Field(..., alias='ok', description='')
    data: Union[Any, None] = Field(None, alias='data', description='')
    error: Union[str, None] = Field(None, alias='error', description='')
    message: Union[str, None] = Field(None, alias='message', description='')


CommonsGetEntityLedgerOutputVariant2DeliveryArtifactsItem = TypedDict('CommonsGetEntityLedgerOutputVariant2DeliveryArtifactsItem', {
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
CommonsGetEntityLedgerOutputVariant2DeliveryArtifactsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


CommonsGetEntityLedgerOutputVariant2DeliveryAvailableExportsItem = TypedDict('CommonsGetEntityLedgerOutputVariant2DeliveryAvailableExportsItem', {
    'artifactId': Required[str],
    'sourceArtifactId': Required[str],
    'filename': Required[Literal['result.md']],
    'contentType': Required[Literal['text/markdown; charset=utf-8']],
    'state': Required[Literal['on-demand']],
})
CommonsGetEntityLedgerOutputVariant2DeliveryAvailableExportsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


CommonsGetEntityLedgerOutputVariant2DeliveryStorageFailureVariant1 = TypedDict('CommonsGetEntityLedgerOutputVariant2DeliveryStorageFailureVariant1', {
    'artifactId': Required[Union[str, None]],
    'outcome': Required[Literal['unknown', 'bytes-stored-metadata-pending', 'failed']],
})
CommonsGetEntityLedgerOutputVariant2DeliveryStorageFailureVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


CommonsGetEntityLedgerOutputVariant2Delivery = TypedDict('CommonsGetEntityLedgerOutputVariant2Delivery', {
    'mode': Required[Literal['artifact']],
    'status': Required[Literal['complete', 'partial', 'unavailable']],
    'retainedRepresentation': Required[Literal['formatted-tool-result']],
    'sourceIsError': Required[bool],
    'artifacts': Required[list[CommonsGetEntityLedgerOutputVariant2DeliveryArtifactsItem]],
    'availableExports': NotRequired[list[CommonsGetEntityLedgerOutputVariant2DeliveryAvailableExportsItem]],
    'downloadLinksOmitted': Required[bool],
    'scopeOmittedFields': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'storageFailure': Required[Union[CommonsGetEntityLedgerOutputVariant2DeliveryStorageFailureVariant1, None]],
    'nextAction': Required[str],
})
CommonsGetEntityLedgerOutputVariant2Delivery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


CommonsGetEntityLedgerOutputVariant2RecoveryOperation = TypedDict('CommonsGetEntityLedgerOutputVariant2RecoveryOperation', {
    'runId': Required[Union[Annotated[str, Field(max_length=200)], None]],
    'idempotencyKey': Required[Annotated[str, Field(max_length=512)]],
    'state': Required[Annotated[str, Field(max_length=100)]],
})
CommonsGetEntityLedgerOutputVariant2RecoveryOperation.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


CommonsGetEntityLedgerOutputVariant2Recovery = TypedDict('CommonsGetEntityLedgerOutputVariant2Recovery', {
    'idempotencyKey': NotRequired[Annotated[str, Field(max_length=512)]],
    'operationId': NotRequired[Annotated[str, Field(max_length=200)]],
    'runId': NotRequired[Annotated[str, Field(max_length=200)]],
    'jobId': NotRequired[Annotated[str, Field(max_length=200)]],
    'operation': NotRequired[CommonsGetEntityLedgerOutputVariant2RecoveryOperation],
})
CommonsGetEntityLedgerOutputVariant2Recovery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class CommonsGetEntityLedgerOutputVariant2(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    delivery: CommonsGetEntityLedgerOutputVariant2Delivery = Field(..., alias='delivery', description='')
    preview: str = Field(..., alias='preview', description='')
    scope: dict[str, Union[str, Union[float, int], bool, None]] = Field(..., alias='scope', description='')
    recovery: CommonsGetEntityLedgerOutputVariant2Recovery = Field(..., alias='recovery', description='')


# Union schema: validate external payloads with TypeAdapter(CommonsGetEntityLedgerOutput).
CommonsGetEntityLedgerOutput = Union[CommonsGetEntityLedgerOutputVariant2, CommonsGetEntityLedgerOutputVariant1]

_CommonsGetEntityLedgerInputAdapter = TypeAdapter(CommonsGetEntityLedgerInput)
_CommonsGetEntityLedgerOutputAdapter = TypeAdapter(CommonsGetEntityLedgerOutput)