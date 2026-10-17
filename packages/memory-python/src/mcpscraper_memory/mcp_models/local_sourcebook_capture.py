from typing import Annotated, Any, Literal, Union
from typing_extensions import NotRequired, Required, TypedDict
from pydantic import BaseModel, ConfigDict, Field, TypeAdapter


LocalSourcebookCaptureInputIdentity = TypedDict('LocalSourcebookCaptureInputIdentity', {
    'category': Required[Literal['home', 'professional', 'restaurants', 'financial', 'realestate', 'auto', 'wellness']],
    'state': Required[Annotated[str, Field(min_length=2, max_length=2)]],
    'businessName': Required[Annotated[str, Field(min_length=2, max_length=160)]],
    'websiteUrl': Required[str],
    'schemaOrgType': NotRequired[Literal['LocalBusiness', 'AnimalShelter', 'AutomotiveBusiness', 'AutoBodyShop', 'AutoDealer', 'AutoPartsStore', 'AutoRental', 'AutoRepair', 'AutoWash', 'GasStation', 'MotorcycleDealer', 'MotorcycleRepair', 'ChildCare', 'Dentist', 'DryCleaningOrLaundry', 'EmergencyService', 'EmploymentAgency', 'EntertainmentBusiness', 'FinancialService', 'AccountingService', 'AutomatedTeller', 'BankOrCreditUnion', 'InsuranceAgency', 'FoodEstablishment', 'Bakery', 'BarOrPub', 'Brewery', 'CafeOrCoffeeShop', 'Distillery', 'FastFoodRestaurant', 'IceCreamShop', 'Restaurant', 'Winery', 'HealthAndBeautyBusiness', 'BeautySalon', 'DaySpa', 'HairSalon', 'HealthClub', 'NailSalon', 'TattooParlor', 'HomeAndConstructionBusiness', 'Electrician', 'GeneralContractor', 'HVACBusiness', 'HousePainter', 'Locksmith', 'MovingCompany', 'Plumber', 'RoofingContractor', 'LegalService', 'Library', 'LodgingBusiness', 'MedicalBusiness', 'Pharmacy', 'Physician', 'RealEstateAgent', 'RecyclingCenter', 'SelfStorage', 'ShoppingCenter', 'SportsActivityLocation', 'Store', 'TouristInformationCenter', 'TravelAgency']],
    'slug': NotRequired[Annotated[str, Field(max_length=100)]],
    'tags': NotRequired[Annotated[list[Annotated[str, Field(min_length=1, max_length=60)]], Field(max_length=20)]],
    'idempotencyKey': Required[Annotated[str, Field(min_length=8, max_length=200)]],
})
LocalSourcebookCaptureInputIdentity.__pydantic_config__ = ConfigDict(extra="allow", strict=False)


LocalSourcebookCaptureInputTagCandidatesItem = TypedDict('LocalSourcebookCaptureInputTagCandidatesItem', {
    'tag': Required[Annotated[str, Field(min_length=1, max_length=60)]],
    'central': NotRequired[bool],
    'reusable': NotRequired[bool],
    'description': NotRequired[Annotated[str, Field(min_length=8, max_length=240)]],
})
LocalSourcebookCaptureInputTagCandidatesItem.__pydantic_config__ = ConfigDict(extra="allow", strict=False)


LocalSourcebookCaptureInputTagDecisionsItem = TypedDict('LocalSourcebookCaptureInputTagDecisionsItem', {
    'tag': Required[Annotated[str, Field(min_length=1, max_length=60)]],
    'central': Required[bool],
    'reusable': Required[bool],
    'description': NotRequired[Annotated[str, Field(min_length=8, max_length=240)]],
    'acceptCanonical': NotRequired[Annotated[str, Field(min_length=1, max_length=60)]],
})
LocalSourcebookCaptureInputTagDecisionsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=False)


class LocalSourcebookCaptureInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=False)

    identity: LocalSourcebookCaptureInputIdentity = Field(..., alias='identity', description='New-listing identity returned by prepare-local-sourcebook-write. Evidence-bearing public fields are compiled by MCP Scraper and cannot be supplied here.')
    tag_candidates: Union[Annotated[list[LocalSourcebookCaptureInputTagCandidatesItem], Field(max_length=20)], None] = Field(None, alias='tagCandidates', description='Proposed listing or memory tags to resolve against the live canonical vocabulary.')
    tag_decisions: Union[Annotated[list[LocalSourcebookCaptureInputTagDecisionsItem], Field(max_length=20)], None] = Field(None, alias='tagDecisions', description='Explicit reuse, creation, or omission decisions for proposed non-canonical tags.')
    idempotency_key: Union[Annotated[str, Field(min_length=8, max_length=200)], None] = Field(None, alias='idempotencyKey', description='Stable retry key for a new capture. Required either here or in identity.')


class LocalSourcebookCaptureOutputVariant1(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)



LocalSourcebookCaptureOutputVariant2DeliveryArtifactsItem = TypedDict('LocalSourcebookCaptureOutputVariant2DeliveryArtifactsItem', {
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
LocalSourcebookCaptureOutputVariant2DeliveryArtifactsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


LocalSourcebookCaptureOutputVariant2DeliveryAvailableExportsItem = TypedDict('LocalSourcebookCaptureOutputVariant2DeliveryAvailableExportsItem', {
    'artifactId': Required[str],
    'sourceArtifactId': Required[str],
    'filename': Required[Literal['result.md']],
    'contentType': Required[Literal['text/markdown; charset=utf-8']],
    'state': Required[Literal['on-demand']],
})
LocalSourcebookCaptureOutputVariant2DeliveryAvailableExportsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


LocalSourcebookCaptureOutputVariant2DeliveryStorageFailureVariant1 = TypedDict('LocalSourcebookCaptureOutputVariant2DeliveryStorageFailureVariant1', {
    'artifactId': Required[Union[str, None]],
    'outcome': Required[Literal['unknown', 'bytes-stored-metadata-pending', 'failed']],
})
LocalSourcebookCaptureOutputVariant2DeliveryStorageFailureVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


LocalSourcebookCaptureOutputVariant2Delivery = TypedDict('LocalSourcebookCaptureOutputVariant2Delivery', {
    'mode': Required[Literal['artifact']],
    'status': Required[Literal['complete', 'partial', 'unavailable']],
    'retainedRepresentation': Required[Literal['formatted-tool-result']],
    'sourceIsError': Required[bool],
    'artifacts': Required[list[LocalSourcebookCaptureOutputVariant2DeliveryArtifactsItem]],
    'availableExports': NotRequired[list[LocalSourcebookCaptureOutputVariant2DeliveryAvailableExportsItem]],
    'downloadLinksOmitted': Required[bool],
    'scopeOmittedFields': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'storageFailure': Required[Union[LocalSourcebookCaptureOutputVariant2DeliveryStorageFailureVariant1, None]],
    'nextAction': Required[str],
})
LocalSourcebookCaptureOutputVariant2Delivery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


LocalSourcebookCaptureOutputVariant2RecoveryOperation = TypedDict('LocalSourcebookCaptureOutputVariant2RecoveryOperation', {
    'runId': Required[Union[Annotated[str, Field(max_length=200)], None]],
    'idempotencyKey': Required[Annotated[str, Field(max_length=512)]],
    'state': Required[Annotated[str, Field(max_length=100)]],
})
LocalSourcebookCaptureOutputVariant2RecoveryOperation.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


LocalSourcebookCaptureOutputVariant2Recovery = TypedDict('LocalSourcebookCaptureOutputVariant2Recovery', {
    'idempotencyKey': NotRequired[Annotated[str, Field(max_length=512)]],
    'operationId': NotRequired[Annotated[str, Field(max_length=200)]],
    'runId': NotRequired[Annotated[str, Field(max_length=200)]],
    'jobId': NotRequired[Annotated[str, Field(max_length=200)]],
    'operation': NotRequired[LocalSourcebookCaptureOutputVariant2RecoveryOperation],
})
LocalSourcebookCaptureOutputVariant2Recovery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class LocalSourcebookCaptureOutputVariant2(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    delivery: LocalSourcebookCaptureOutputVariant2Delivery = Field(..., alias='delivery', description='')
    preview: str = Field(..., alias='preview', description='')
    scope: dict[str, Union[str, Union[float, int], bool, None]] = Field(..., alias='scope', description='')
    recovery: LocalSourcebookCaptureOutputVariant2Recovery = Field(..., alias='recovery', description='')


# Union schema: validate external payloads with TypeAdapter(LocalSourcebookCaptureOutput).
LocalSourcebookCaptureOutput = Union[LocalSourcebookCaptureOutputVariant2, LocalSourcebookCaptureOutputVariant1]

_LocalSourcebookCaptureInputAdapter = TypeAdapter(LocalSourcebookCaptureInput)
_LocalSourcebookCaptureOutputAdapter = TypeAdapter(LocalSourcebookCaptureOutput)