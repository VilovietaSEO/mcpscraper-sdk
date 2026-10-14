from typing import Annotated, Any, Literal, Union
from typing_extensions import NotRequired, Required, TypedDict
from pydantic import BaseModel, ConfigDict, Field, TypeAdapter


class GmailSearchContactsInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=False)

    connection_id: Annotated[str, Field(min_length=1)] = Field(..., alias='connectionId', description='A Gmail connectionId from list_service_connections. Read-only — does not require actionsEnabled.')
    query: Annotated[str, Field(min_length=1, max_length=500)] = Field(..., alias='query', description='Gmail search syntax, e.g. "from:brandnorth.com after:2026/03/22" or "brandnorth.com".')
    max_messages: Union[Annotated[int, Field(ge=1, le=150)], None] = Field(None, alias='maxMessages', description='Max messages to fetch and aggregate in this call. Paginate with pageToken for more; the response reports totalMatches and truncated so undercoverage is never silent.')
    page_token: Union[str, None] = Field(None, alias='pageToken', description='Continuation token from a prior response to fetch the next page.')


GmailSearchContactsOutputVariant1MessagesItem = TypedDict('GmailSearchContactsOutputVariant1MessagesItem', {
    'id': Required[str],
    'date': Required[Union[str, None]],
    'from': Required[Union[str, None]],
    'to': Required[Union[str, None]],
    'subject': Required[Union[str, None]],
    'snippet': Required[Union[str, None]],
})
GmailSearchContactsOutputVariant1MessagesItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


GmailSearchContactsOutputVariant1ContactsItem = TypedDict('GmailSearchContactsOutputVariant1ContactsItem', {
    'email': Required[str],
    'name': Required[Union[str, None]],
    'domain': Required[Union[str, None]],
    'messageCount': Required[Union[float, int]],
    'firstSeen': Required[Union[str, None]],
    'lastSeen': Required[Union[str, None]],
    'sampleSubjects': Required[list[str]],
})
GmailSearchContactsOutputVariant1ContactsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class GmailSearchContactsOutputVariant1(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    ok: bool = Field(..., alias='ok', description='')
    total_matches: Union[Union[float, int], None] = Field(None, alias='totalMatches', description="Gmail's estimated total matches for the query, independent of how many were fetched this call.")
    messages_fetched: Union[Union[float, int], None] = Field(None, alias='messagesFetched', description='')
    truncated: Union[bool, None] = Field(None, alias='truncated', description='True when totalMatches exceeds messagesFetched — more results exist, use nextPageToken.')
    next_page_token: Union[str, None] = Field(..., alias='nextPageToken', description='')
    messages: Union[list[GmailSearchContactsOutputVariant1MessagesItem], None] = Field(None, alias='messages', description='')
    contacts: Union[list[GmailSearchContactsOutputVariant1ContactsItem], None] = Field(None, alias='contacts', description='Messages deduped by sender email address, newest-to-oldest within this fetch only — not the full query result set when truncated.')
    error: Union[str, None] = Field(..., alias='error', description='')


GmailSearchContactsOutputVariant2DeliveryArtifactsItem = TypedDict('GmailSearchContactsOutputVariant2DeliveryArtifactsItem', {
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
GmailSearchContactsOutputVariant2DeliveryArtifactsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


GmailSearchContactsOutputVariant2DeliveryStorageFailureVariant1 = TypedDict('GmailSearchContactsOutputVariant2DeliveryStorageFailureVariant1', {
    'artifactId': Required[Union[str, None]],
    'outcome': Required[Literal['unknown', 'bytes-stored-metadata-pending', 'failed']],
})
GmailSearchContactsOutputVariant2DeliveryStorageFailureVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


GmailSearchContactsOutputVariant2Delivery = TypedDict('GmailSearchContactsOutputVariant2Delivery', {
    'mode': Required[Literal['artifact']],
    'status': Required[Literal['complete', 'partial', 'unavailable']],
    'retainedRepresentation': Required[Literal['formatted-tool-result']],
    'sourceIsError': Required[bool],
    'artifacts': Required[list[GmailSearchContactsOutputVariant2DeliveryArtifactsItem]],
    'downloadLinksOmitted': Required[bool],
    'scopeOmittedFields': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'storageFailure': Required[Union[GmailSearchContactsOutputVariant2DeliveryStorageFailureVariant1, None]],
    'nextAction': Required[str],
})
GmailSearchContactsOutputVariant2Delivery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


GmailSearchContactsOutputVariant2RecoveryOperation = TypedDict('GmailSearchContactsOutputVariant2RecoveryOperation', {
    'runId': Required[Union[Annotated[str, Field(max_length=200)], None]],
    'idempotencyKey': Required[Annotated[str, Field(max_length=512)]],
    'state': Required[Annotated[str, Field(max_length=100)]],
})
GmailSearchContactsOutputVariant2RecoveryOperation.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


GmailSearchContactsOutputVariant2Recovery = TypedDict('GmailSearchContactsOutputVariant2Recovery', {
    'idempotencyKey': NotRequired[Annotated[str, Field(max_length=512)]],
    'operationId': NotRequired[Annotated[str, Field(max_length=200)]],
    'runId': NotRequired[Annotated[str, Field(max_length=200)]],
    'jobId': NotRequired[Annotated[str, Field(max_length=200)]],
    'operation': NotRequired[GmailSearchContactsOutputVariant2RecoveryOperation],
})
GmailSearchContactsOutputVariant2Recovery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class GmailSearchContactsOutputVariant2(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    delivery: GmailSearchContactsOutputVariant2Delivery = Field(..., alias='delivery', description='')
    preview: str = Field(..., alias='preview', description='')
    scope: dict[str, Union[str, Union[float, int], bool, None]] = Field(..., alias='scope', description='')
    recovery: GmailSearchContactsOutputVariant2Recovery = Field(..., alias='recovery', description='')


# Union schema: validate external payloads with TypeAdapter(GmailSearchContactsOutput).
GmailSearchContactsOutput = Union[GmailSearchContactsOutputVariant2, GmailSearchContactsOutputVariant1]

_GmailSearchContactsInputAdapter = TypeAdapter(GmailSearchContactsInput)
_GmailSearchContactsOutputAdapter = TypeAdapter(GmailSearchContactsOutput)