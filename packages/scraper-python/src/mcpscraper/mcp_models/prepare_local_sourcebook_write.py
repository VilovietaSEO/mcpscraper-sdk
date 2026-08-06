from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field


class PrepareLocalSourcebookWriteInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    category: Literal['home', 'professional', 'restaurants', 'financial', 'realestate', 'auto', 'wellness'] = Field(..., alias="category", description="")
    state: str = Field(..., alias="state", description="")
    business_name: str = Field(..., alias="businessName", description="")
    website_url: str = Field(..., alias="websiteUrl", description="")
    schema_org_type: Literal['LocalBusiness', 'AnimalShelter', 'AutomotiveBusiness', 'AutoBodyShop', 'AutoDealer', 'AutoPartsStore', 'AutoRental', 'AutoRepair', 'AutoWash', 'GasStation', 'MotorcycleDealer', 'MotorcycleRepair', 'ChildCare', 'Dentist', 'DryCleaningOrLaundry', 'EmergencyService', 'EmploymentAgency', 'EntertainmentBusiness', 'FinancialService', 'AccountingService', 'AutomatedTeller', 'BankOrCreditUnion', 'InsuranceAgency', 'FoodEstablishment', 'Bakery', 'BarOrPub', 'Brewery', 'CafeOrCoffeeShop', 'Distillery', 'FastFoodRestaurant', 'IceCreamShop', 'Restaurant', 'Winery', 'HealthAndBeautyBusiness', 'BeautySalon', 'DaySpa', 'HairSalon', 'HealthClub', 'NailSalon', 'TattooParlor', 'HomeAndConstructionBusiness', 'Electrician', 'GeneralContractor', 'HVACBusiness', 'HousePainter', 'Locksmith', 'MovingCompany', 'Plumber', 'RoofingContractor', 'LegalService', 'Library', 'LodgingBusiness', 'MedicalBusiness', 'Pharmacy', 'Physician', 'RealEstateAgent', 'RecyclingCenter', 'SelfStorage', 'ShoppingCenter', 'SportsActivityLocation', 'Store', 'TouristInformationCenter', 'TravelAgency'] | None = Field(None, alias="schemaOrgType", description="Optional Schema.org LocalBusiness subtype. Omit to receive the category default; use a more specific accepted subtype when the business evidence supports it.")
    slug: str | None = Field(None, alias="slug", description="")
    tags: list[str] | None = Field(None, alias="tags", description="")
    idempotency_key: str = Field(..., alias="idempotencyKey", description="")
    tag_candidates: list[dict[str, Any]] | None = Field(None, alias="tagCandidates", description="")


class PrepareLocalSourcebookWriteOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")
