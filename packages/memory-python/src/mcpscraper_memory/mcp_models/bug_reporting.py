from typing import Annotated, Any, Literal, Union
from typing_extensions import NotRequired, Required, TypedDict
from pydantic import BaseModel, ConfigDict, Field, TypeAdapter


BugReportingInputReportAttemptsItem = TypedDict('BugReportingInputReportAttemptsItem', {
    'tool': Required[Annotated[str, Field(min_length=1, max_length=120)]],
    'submittedAt': NotRequired[str],
    'arguments': Required[Annotated[str, Field(min_length=1, max_length=8000)]],
    'result': Required[Annotated[str, Field(min_length=1, max_length=8000)]],
    'requestId': NotRequired[Annotated[str, Field(min_length=1, max_length=200)]],
    'jobId': NotRequired[Annotated[str, Field(min_length=1, max_length=200)]],
})
BugReportingInputReportAttemptsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=False)


BugReportingInputReportClient = TypedDict('BugReportingInputReportClient', {
    'name': Required[Annotated[str, Field(min_length=1, max_length=120)]],
    'version': NotRequired[Annotated[str, Field(min_length=1, max_length=120)]],
    'transport': Required[Literal['oauth', 'api-key', 'npx', 'npm', 'sdk', 'mcpb', 'rest', 'unknown']],
    'operatingSystem': NotRequired[Annotated[str, Field(min_length=1, max_length=120)]],
    'model': NotRequired[Annotated[str, Field(min_length=1, max_length=120)]],
})
BugReportingInputReportClient.__pydantic_config__ = ConfigDict(extra="allow", strict=False)


BugReportingInputReport = TypedDict('BugReportingInputReport', {
    'title': Required[Annotated[str, Field(min_length=1, max_length=160)]],
    'goal': Required[Annotated[str, Field(min_length=1, max_length=2000)]],
    'expected': Required[Annotated[str, Field(min_length=1, max_length=2000)]],
    'actual': Required[Annotated[str, Field(min_length=1, max_length=4000)]],
    'steps': Required[Annotated[list[Annotated[str, Field(min_length=1, max_length=1000)]], Field(min_length=1, max_length=30)]],
    'attempts': Required[Annotated[list[BugReportingInputReportAttemptsItem], Field(min_length=1, max_length=20)]],
    'client': Required[BugReportingInputReportClient],
    'context': NotRequired[Annotated[str, Field(min_length=1, max_length=4000)]],
    'missing': NotRequired[Annotated[list[Annotated[str, Field(min_length=1, max_length=500)]], Field(max_length=20)]],
})
BugReportingInputReport.__pydantic_config__ = ConfigDict(extra="allow", strict=False)


class BugReportingInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=False)

    action: Union[Literal['prepare', 'submit', 'status'], None] = Field(None, alias='action', description='prepare saves a private one-day draft for review; submit sends that exact draft to support; status reads your report receipt.')
    report: Union[BugReportingInputReport, None] = Field(None, alias='report', description='Required for prepare. Collect known evidence from the conversation before asking the user for missing details.')
    report_id: Union[str, None] = Field(None, alias='reportId', description='ID returned by prepare; required for submit or status.')
    review_token: Union[Annotated[str, Field(min_length=1, max_length=128)], None] = Field(None, alias='reviewToken', description='Exact token returned by prepare; required for submit. A changed report requires a new prepare.')
    user_approved: Union[bool, None] = Field(None, alias='userApproved', description='Set true only when the user has asked to submit this bug or approved the reviewed draft. Repeated errors alone do not authorize submission.')


BugReportingOutputVariant1ReportClient = TypedDict('BugReportingOutputVariant1ReportClient', {
    'name': Required[Annotated[str, Field(min_length=1, max_length=120)]],
    'version': NotRequired[Annotated[str, Field(min_length=1, max_length=120)]],
    'transport': Required[Literal['oauth', 'api-key', 'npx', 'npm', 'sdk', 'mcpb', 'rest', 'unknown']],
    'operatingSystem': NotRequired[Annotated[str, Field(min_length=1, max_length=120)]],
    'model': NotRequired[Annotated[str, Field(min_length=1, max_length=120)]],
})
BugReportingOutputVariant1ReportClient.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


BugReportingOutputVariant1Report = TypedDict('BugReportingOutputVariant1Report', {
    'title': Required[Annotated[str, Field(min_length=1, max_length=160)]],
    'goal': Required[Annotated[str, Field(min_length=1, max_length=2000)]],
    'expected': Required[Annotated[str, Field(min_length=1, max_length=2000)]],
    'actual': Required[Annotated[str, Field(min_length=1, max_length=4000)]],
    'steps': Required[Annotated[list[Annotated[str, Field(min_length=1, max_length=1000)]], Field(min_length=1, max_length=30)]],
    'client': Required[BugReportingOutputVariant1ReportClient],
    'context': NotRequired[Annotated[str, Field(min_length=1, max_length=4000)]],
    'missing': Required[Annotated[list[Annotated[str, Field(min_length=1, max_length=500)]], Field(max_length=20)]],
})
BugReportingOutputVariant1Report.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class BugReportingOutputVariant1(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    ok: Literal[True] = Field(..., alias='ok', description='')
    account_email: str = Field(..., alias='accountEmail', description='')
    report_id: str = Field(..., alias='reportId', description='')
    status: Literal['draft', 'submitted'] = Field(..., alias='status', description='')
    received_at: str = Field(..., alias='receivedAt', description='')
    submitted_at: Union[str, None] = Field(..., alias='submittedAt', description='')
    expires_at: str = Field(..., alias='expiresAt', description='')
    report: BugReportingOutputVariant1Report = Field(..., alias='report', description='')
    review_token: Union[str, None] = Field(None, alias='reviewToken', description='')
    redacted: bool = Field(..., alias='redacted', description='')
    message: str = Field(..., alias='message', description='')


BugReportingOutputVariant2DeliveryArtifactsItem = TypedDict('BugReportingOutputVariant2DeliveryArtifactsItem', {
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
BugReportingOutputVariant2DeliveryArtifactsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


BugReportingOutputVariant2DeliveryAvailableExportsItem = TypedDict('BugReportingOutputVariant2DeliveryAvailableExportsItem', {
    'artifactId': Required[str],
    'sourceArtifactId': Required[str],
    'filename': Required[Literal['result.md']],
    'contentType': Required[Literal['text/markdown; charset=utf-8']],
    'state': Required[Literal['on-demand']],
})
BugReportingOutputVariant2DeliveryAvailableExportsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


BugReportingOutputVariant2DeliveryStorageFailureVariant1 = TypedDict('BugReportingOutputVariant2DeliveryStorageFailureVariant1', {
    'artifactId': Required[Union[str, None]],
    'outcome': Required[Literal['unknown', 'bytes-stored-metadata-pending', 'failed']],
})
BugReportingOutputVariant2DeliveryStorageFailureVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


BugReportingOutputVariant2Delivery = TypedDict('BugReportingOutputVariant2Delivery', {
    'mode': Required[Literal['artifact']],
    'status': Required[Literal['complete', 'partial', 'unavailable']],
    'retainedRepresentation': Required[Literal['formatted-tool-result']],
    'sourceIsError': Required[bool],
    'artifacts': Required[list[BugReportingOutputVariant2DeliveryArtifactsItem]],
    'availableExports': NotRequired[list[BugReportingOutputVariant2DeliveryAvailableExportsItem]],
    'downloadLinksOmitted': Required[bool],
    'scopeOmittedFields': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'storageFailure': Required[Union[BugReportingOutputVariant2DeliveryStorageFailureVariant1, None]],
    'nextAction': Required[str],
})
BugReportingOutputVariant2Delivery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


BugReportingOutputVariant2RecoveryOperation = TypedDict('BugReportingOutputVariant2RecoveryOperation', {
    'runId': Required[Union[Annotated[str, Field(max_length=200)], None]],
    'idempotencyKey': Required[Annotated[str, Field(max_length=512)]],
    'state': Required[Annotated[str, Field(max_length=100)]],
})
BugReportingOutputVariant2RecoveryOperation.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


BugReportingOutputVariant2Recovery = TypedDict('BugReportingOutputVariant2Recovery', {
    'idempotencyKey': NotRequired[Annotated[str, Field(max_length=512)]],
    'operationId': NotRequired[Annotated[str, Field(max_length=200)]],
    'runId': NotRequired[Annotated[str, Field(max_length=200)]],
    'jobId': NotRequired[Annotated[str, Field(max_length=200)]],
    'operation': NotRequired[BugReportingOutputVariant2RecoveryOperation],
})
BugReportingOutputVariant2Recovery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class BugReportingOutputVariant2(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    delivery: BugReportingOutputVariant2Delivery = Field(..., alias='delivery', description='')
    preview: str = Field(..., alias='preview', description='')
    scope: dict[str, Union[str, Union[float, int], bool, None]] = Field(..., alias='scope', description='')
    recovery: BugReportingOutputVariant2Recovery = Field(..., alias='recovery', description='')


# Union schema: validate external payloads with TypeAdapter(BugReportingOutput).
BugReportingOutput = Union[BugReportingOutputVariant1, BugReportingOutputVariant2]

_BugReportingInputAdapter = TypeAdapter(BugReportingInput)
_BugReportingOutputAdapter = TypeAdapter(BugReportingOutput)