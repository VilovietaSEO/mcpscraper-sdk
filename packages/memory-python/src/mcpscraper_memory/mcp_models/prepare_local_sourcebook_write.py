from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field


class PrepareLocalSourcebookWriteInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    category: Literal['home', 'professional', 'restaurants', 'financial', 'realestate', 'auto', 'wellness'] = Field(..., alias="category", description="Canonical Local Sourcebook business category selected from the live contract.")
    state: str = Field(..., alias="state", description="Two-letter US state for the Local Sourcebook listing market.")
    business_name: str = Field(..., alias="businessName", description="Public business name supported by the listing evidence.")
    website_url: str = Field(..., alias="websiteUrl", description="Canonical public business website used for listing identity and evidence acquisition.")
    schema_org_type: Literal['LocalBusiness', 'AnimalShelter', 'AutomotiveBusiness', 'AutoBodyShop', 'AutoDealer', 'AutoPartsStore', 'AutoRental', 'AutoRepair', 'AutoWash', 'GasStation', 'MotorcycleDealer', 'MotorcycleRepair', 'ChildCare', 'Dentist', 'DryCleaningOrLaundry', 'EmergencyService', 'EmploymentAgency', 'EntertainmentBusiness', 'FinancialService', 'AccountingService', 'AutomatedTeller', 'BankOrCreditUnion', 'InsuranceAgency', 'FoodEstablishment', 'Bakery', 'BarOrPub', 'Brewery', 'CafeOrCoffeeShop', 'Distillery', 'FastFoodRestaurant', 'IceCreamShop', 'Restaurant', 'Winery', 'HealthAndBeautyBusiness', 'BeautySalon', 'DaySpa', 'HairSalon', 'HealthClub', 'NailSalon', 'TattooParlor', 'HomeAndConstructionBusiness', 'Electrician', 'GeneralContractor', 'HVACBusiness', 'HousePainter', 'Locksmith', 'MovingCompany', 'Plumber', 'RoofingContractor', 'LegalService', 'Library', 'LodgingBusiness', 'MedicalBusiness', 'Pharmacy', 'Physician', 'RealEstateAgent', 'RecyclingCenter', 'SelfStorage', 'ShoppingCenter', 'SportsActivityLocation', 'Store', 'TouristInformationCenter', 'TravelAgency'] | None = Field(None, alias="schemaOrgType", description="Optional Schema.org LocalBusiness subtype. Omit to receive the category default; use a more specific accepted subtype when the business evidence supports it.")
    slug: str | None = Field(None, alias="slug", description="Optional stable public slug; omit only when the tool is documented to derive it.")
    tags: list[str] | None = Field(None, alias="tags", description="Canonical tag filter or tag set; use the appropriate vocabulary-listing tool before writing new tags.")
    idempotency_key: str = Field(..., alias="idempotencyKey", description="Caller-owned opaque key for this intended operation; reuse only when retrying the same operation.")
    tag_candidates: list[dict[str, Any]] | None = Field(None, alias="tagCandidates", description="Proposed listing or memory tags to resolve against the live canonical vocabulary.")


class PrepareLocalSourcebookWriteOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")
