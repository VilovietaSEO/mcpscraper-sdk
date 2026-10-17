from typing import Annotated, Any, Literal, Union
from typing_extensions import NotRequired, Required, TypedDict
from pydantic import BaseModel, ConfigDict, Field, TypeAdapter


PrepareLocalSourcebookWriteInputTagCandidatesItem = TypedDict('PrepareLocalSourcebookWriteInputTagCandidatesItem', {
    'tag': Required[Annotated[str, Field(min_length=1, max_length=60)]],
    'central': NotRequired[bool],
    'reusable': NotRequired[bool],
    'description': NotRequired[Annotated[str, Field(min_length=8, max_length=240)]],
})
PrepareLocalSourcebookWriteInputTagCandidatesItem.__pydantic_config__ = ConfigDict(extra="allow", strict=False)


class PrepareLocalSourcebookWriteInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=False)

    category: Literal['home', 'professional', 'restaurants', 'financial', 'realestate', 'auto', 'wellness'] = Field(..., alias='category', description='Canonical Local Sourcebook business category selected from the live contract.')
    state: Annotated[str, Field(min_length=2, max_length=2)] = Field(..., alias='state', description='Two-letter US state for the Local Sourcebook listing market.')
    business_name: Annotated[str, Field(min_length=2, max_length=160)] = Field(..., alias='businessName', description='Public business name supported by the listing evidence.')
    website_url: str = Field(..., alias='websiteUrl', description='Canonical public business website used for listing identity and evidence acquisition.')
    schema_org_type: Union[Literal['LocalBusiness', 'AnimalShelter', 'AutomotiveBusiness', 'AutoBodyShop', 'AutoDealer', 'AutoPartsStore', 'AutoRental', 'AutoRepair', 'AutoWash', 'GasStation', 'MotorcycleDealer', 'MotorcycleRepair', 'ChildCare', 'Dentist', 'DryCleaningOrLaundry', 'EmergencyService', 'EmploymentAgency', 'EntertainmentBusiness', 'FinancialService', 'AccountingService', 'AutomatedTeller', 'BankOrCreditUnion', 'InsuranceAgency', 'FoodEstablishment', 'Bakery', 'BarOrPub', 'Brewery', 'CafeOrCoffeeShop', 'Distillery', 'FastFoodRestaurant', 'IceCreamShop', 'Restaurant', 'Winery', 'HealthAndBeautyBusiness', 'BeautySalon', 'DaySpa', 'HairSalon', 'HealthClub', 'NailSalon', 'TattooParlor', 'HomeAndConstructionBusiness', 'Electrician', 'GeneralContractor', 'HVACBusiness', 'HousePainter', 'Locksmith', 'MovingCompany', 'Plumber', 'RoofingContractor', 'LegalService', 'Library', 'LodgingBusiness', 'MedicalBusiness', 'Pharmacy', 'Physician', 'RealEstateAgent', 'RecyclingCenter', 'SelfStorage', 'ShoppingCenter', 'SportsActivityLocation', 'Store', 'TouristInformationCenter', 'TravelAgency'], None] = Field(None, alias='schemaOrgType', description='Optional Schema.org LocalBusiness subtype. Omit to receive the category default; use a more specific accepted subtype when the business evidence supports it.')
    slug: Union[Annotated[str, Field(max_length=100)], None] = Field(None, alias='slug', description='Optional stable public slug; omit only when the tool is documented to derive it.')
    tags: Union[Annotated[list[Annotated[str, Field(min_length=1, max_length=60)]], Field(max_length=20)], None] = Field(None, alias='tags', description='Canonical tag filter or tag set; use the appropriate vocabulary-listing tool before writing new tags.')
    idempotency_key: Annotated[str, Field(min_length=8, max_length=200)] = Field(..., alias='idempotencyKey', description='Caller-owned opaque key for this intended operation; reuse only when retrying the same operation.')
    tag_candidates: Union[Annotated[list[PrepareLocalSourcebookWriteInputTagCandidatesItem], Field(max_length=20)], None] = Field(None, alias='tagCandidates', description='Proposed listing or memory tags to resolve against the live canonical vocabulary.')


class PrepareLocalSourcebookWriteOutputVariant1(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)



PrepareLocalSourcebookWriteOutputVariant2DeliveryArtifactsItem = TypedDict('PrepareLocalSourcebookWriteOutputVariant2DeliveryArtifactsItem', {
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
PrepareLocalSourcebookWriteOutputVariant2DeliveryArtifactsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


PrepareLocalSourcebookWriteOutputVariant2DeliveryAvailableExportsItem = TypedDict('PrepareLocalSourcebookWriteOutputVariant2DeliveryAvailableExportsItem', {
    'artifactId': Required[str],
    'sourceArtifactId': Required[str],
    'filename': Required[Literal['result.md']],
    'contentType': Required[Literal['text/markdown; charset=utf-8']],
    'state': Required[Literal['on-demand']],
})
PrepareLocalSourcebookWriteOutputVariant2DeliveryAvailableExportsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


PrepareLocalSourcebookWriteOutputVariant2DeliveryStorageFailureVariant1 = TypedDict('PrepareLocalSourcebookWriteOutputVariant2DeliveryStorageFailureVariant1', {
    'artifactId': Required[Union[str, None]],
    'outcome': Required[Literal['unknown', 'bytes-stored-metadata-pending', 'failed']],
})
PrepareLocalSourcebookWriteOutputVariant2DeliveryStorageFailureVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


PrepareLocalSourcebookWriteOutputVariant2Delivery = TypedDict('PrepareLocalSourcebookWriteOutputVariant2Delivery', {
    'mode': Required[Literal['artifact']],
    'status': Required[Literal['complete', 'partial', 'unavailable']],
    'retainedRepresentation': Required[Literal['formatted-tool-result']],
    'sourceIsError': Required[bool],
    'artifacts': Required[list[PrepareLocalSourcebookWriteOutputVariant2DeliveryArtifactsItem]],
    'availableExports': NotRequired[list[PrepareLocalSourcebookWriteOutputVariant2DeliveryAvailableExportsItem]],
    'downloadLinksOmitted': Required[bool],
    'scopeOmittedFields': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'storageFailure': Required[Union[PrepareLocalSourcebookWriteOutputVariant2DeliveryStorageFailureVariant1, None]],
    'nextAction': Required[str],
})
PrepareLocalSourcebookWriteOutputVariant2Delivery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


PrepareLocalSourcebookWriteOutputVariant2RecoveryOperation = TypedDict('PrepareLocalSourcebookWriteOutputVariant2RecoveryOperation', {
    'runId': Required[Union[Annotated[str, Field(max_length=200)], None]],
    'idempotencyKey': Required[Annotated[str, Field(max_length=512)]],
    'state': Required[Annotated[str, Field(max_length=100)]],
})
PrepareLocalSourcebookWriteOutputVariant2RecoveryOperation.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


PrepareLocalSourcebookWriteOutputVariant2Recovery = TypedDict('PrepareLocalSourcebookWriteOutputVariant2Recovery', {
    'idempotencyKey': NotRequired[Annotated[str, Field(max_length=512)]],
    'operationId': NotRequired[Annotated[str, Field(max_length=200)]],
    'runId': NotRequired[Annotated[str, Field(max_length=200)]],
    'jobId': NotRequired[Annotated[str, Field(max_length=200)]],
    'operation': NotRequired[PrepareLocalSourcebookWriteOutputVariant2RecoveryOperation],
})
PrepareLocalSourcebookWriteOutputVariant2Recovery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class PrepareLocalSourcebookWriteOutputVariant2(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    delivery: PrepareLocalSourcebookWriteOutputVariant2Delivery = Field(..., alias='delivery', description='')
    preview: str = Field(..., alias='preview', description='')
    scope: dict[str, Union[str, Union[float, int], bool, None]] = Field(..., alias='scope', description='')
    recovery: PrepareLocalSourcebookWriteOutputVariant2Recovery = Field(..., alias='recovery', description='')


# Union schema: validate external payloads with TypeAdapter(PrepareLocalSourcebookWriteOutput).
PrepareLocalSourcebookWriteOutput = Union[PrepareLocalSourcebookWriteOutputVariant2, PrepareLocalSourcebookWriteOutputVariant1]

_PrepareLocalSourcebookWriteInputAdapter = TypeAdapter(PrepareLocalSourcebookWriteInput)
_PrepareLocalSourcebookWriteOutputAdapter = TypeAdapter(PrepareLocalSourcebookWriteOutput)