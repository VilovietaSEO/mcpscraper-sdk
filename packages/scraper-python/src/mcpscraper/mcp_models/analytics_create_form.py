from typing import Annotated, Any, Literal, Union
from typing_extensions import NotRequired, Required, TypedDict
from pydantic import BaseModel, ConfigDict, Field, TypeAdapter


AnalyticsCreateFormInputFieldsItem = TypedDict('AnalyticsCreateFormInputFieldsItem', {
    'id': Required[str],
    'type': Required[Literal['text', 'email', 'tel', 'textarea', 'select', 'checkbox', 'radio', 'number']],
    'label': Required[Annotated[str, Field(min_length=1, max_length=120)]],
    'required': Required[bool],
    'options': NotRequired[Annotated[list[Annotated[str, Field(min_length=1, max_length=120)]], Field(max_length=30)]],
})
AnalyticsCreateFormInputFieldsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=False)


AnalyticsCreateFormInputBrand = TypedDict('AnalyticsCreateFormInputBrand', {
    'primaryColor': Required[str],
    'backgroundColor': Required[str],
    'textColor': Required[str],
    'radius': Required[Annotated[int, Field(ge=0, le=32)]],
})
AnalyticsCreateFormInputBrand.__pydantic_config__ = ConfigDict(extra="allow", strict=False)


class AnalyticsCreateFormInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=False)

    site_id: str = Field(..., alias='siteId', description='Analytics Site id returned by analytics_list_sites.')
    pixel_id: str = Field(..., alias='pixelId', description='Analytics Pixel id belonging to the selected Site.')
    name: Annotated[str, Field(min_length=1, max_length=120)] = Field(..., alias='name', description='Human-readable name for the record being created or updated.')
    fields: Annotated[list[AnalyticsCreateFormInputFieldsItem], Field(min_length=1, max_length=30)] = Field(..., alias='fields', description='Ordered form-field definitions to render and validate for submissions.')
    brand: AnalyticsCreateFormInputBrand = Field(..., alias='brand', description='Validated visual-brand settings applied to the generated form.')
    submit_label: Union[Annotated[str, Field(min_length=1, max_length=80)], None] = Field(None, alias='submitLabel', description='Optional text displayed on the form submission button.')
    success_message: Union[Annotated[str, Field(min_length=1, max_length=500)], None] = Field(None, alias='successMessage', description='Optional confirmation shown after a successful form submission.')
    consent_text: Union[Annotated[str, Field(max_length=1000)], None] = Field(None, alias='consentText', description='Optional consent disclosure displayed with the form submission control.')
    publish: Union[bool, None] = Field(None, alias='publish', description='When true, publish the created form immediately; set false to keep it unpublished.')
    idempotency_key: Annotated[str, Field(min_length=8, max_length=160)] = Field(..., alias='idempotencyKey', description='Retry key; reuse only for this exact mutation.')


class AnalyticsCreateFormOutputVariant1(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    ok: bool = Field(..., alias='ok', description='')
    form: dict[str, Any] = Field(..., alias='form', description='')


AnalyticsCreateFormOutputVariant2DeliveryArtifactsItem = TypedDict('AnalyticsCreateFormOutputVariant2DeliveryArtifactsItem', {
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
AnalyticsCreateFormOutputVariant2DeliveryArtifactsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


AnalyticsCreateFormOutputVariant2DeliveryStorageFailureVariant1 = TypedDict('AnalyticsCreateFormOutputVariant2DeliveryStorageFailureVariant1', {
    'artifactId': Required[Union[str, None]],
    'outcome': Required[Literal['unknown', 'bytes-stored-metadata-pending', 'failed']],
})
AnalyticsCreateFormOutputVariant2DeliveryStorageFailureVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


AnalyticsCreateFormOutputVariant2Delivery = TypedDict('AnalyticsCreateFormOutputVariant2Delivery', {
    'mode': Required[Literal['artifact']],
    'status': Required[Literal['complete', 'partial', 'unavailable']],
    'retainedRepresentation': Required[Literal['formatted-tool-result']],
    'sourceIsError': Required[bool],
    'artifacts': Required[list[AnalyticsCreateFormOutputVariant2DeliveryArtifactsItem]],
    'downloadLinksOmitted': Required[bool],
    'scopeOmittedFields': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'storageFailure': Required[Union[AnalyticsCreateFormOutputVariant2DeliveryStorageFailureVariant1, None]],
    'nextAction': Required[str],
})
AnalyticsCreateFormOutputVariant2Delivery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


AnalyticsCreateFormOutputVariant2RecoveryOperation = TypedDict('AnalyticsCreateFormOutputVariant2RecoveryOperation', {
    'runId': Required[Union[Annotated[str, Field(max_length=200)], None]],
    'idempotencyKey': Required[Annotated[str, Field(max_length=512)]],
    'state': Required[Annotated[str, Field(max_length=100)]],
})
AnalyticsCreateFormOutputVariant2RecoveryOperation.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


AnalyticsCreateFormOutputVariant2Recovery = TypedDict('AnalyticsCreateFormOutputVariant2Recovery', {
    'idempotencyKey': NotRequired[Annotated[str, Field(max_length=512)]],
    'operationId': NotRequired[Annotated[str, Field(max_length=200)]],
    'runId': NotRequired[Annotated[str, Field(max_length=200)]],
    'jobId': NotRequired[Annotated[str, Field(max_length=200)]],
    'operation': NotRequired[AnalyticsCreateFormOutputVariant2RecoveryOperation],
})
AnalyticsCreateFormOutputVariant2Recovery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class AnalyticsCreateFormOutputVariant2(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    delivery: AnalyticsCreateFormOutputVariant2Delivery = Field(..., alias='delivery', description='')
    preview: str = Field(..., alias='preview', description='')
    scope: dict[str, Union[str, Union[float, int], bool, None]] = Field(..., alias='scope', description='')
    recovery: AnalyticsCreateFormOutputVariant2Recovery = Field(..., alias='recovery', description='')


# Union schema: validate external payloads with TypeAdapter(AnalyticsCreateFormOutput).
AnalyticsCreateFormOutput = Union[AnalyticsCreateFormOutputVariant2, AnalyticsCreateFormOutputVariant1]

_AnalyticsCreateFormInputAdapter = TypeAdapter(AnalyticsCreateFormInput)
_AnalyticsCreateFormOutputAdapter = TypeAdapter(AnalyticsCreateFormOutput)