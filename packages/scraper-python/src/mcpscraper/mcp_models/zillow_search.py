from typing import Annotated, Any, Literal, Union
from typing_extensions import NotRequired, Required, TypedDict
from pydantic import BaseModel, ConfigDict, Field, TypeAdapter


class ZillowSearchInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=False)

    days_on_zillow: Union[Literal['1_day', '1_week', '2_weeks', '1_month', '3_months', '6_months', '12_months', '24_months', '36_months'], None] = Field(None, alias='daysOnZillow', description='Only include listings on Zillow at most this long.')
    home_types: Union[list[Literal['singleFamily', 'multiFamily', 'townhome', 'condo', 'apartment', 'manufactured', 'land']], None] = Field(None, alias='homeTypes', description='Filter by property type; omit for any.')
    include_accepting_backup_offers: Union[bool, None] = Field(None, alias='includeAcceptingBackupOffers', description='Include listings accepting backup offers, which Zillow excludes by default.')
    include_pending_and_under_contract: Union[bool, None] = Field(None, alias='includePendingAndUnderContract', description='Include pending and under-contract listings, which Zillow excludes by default.')
    include_room_for_rent: Union[bool, None] = Field(None, alias='includeRoomForRent', description='Include room-for-rent listings in rent searches; when omitted or false only entire places are returned.')
    limit: Union[Annotated[int, Field(ge=1, le=25)], None] = Field(None, alias='limit', description='Maximum number of results to return (1-25, default 25).')
    listing_types: Union[list[Literal['fsba', 'fsbo', 'newConstruction', 'comingSoon', 'auction', 'foreclosure', 'foreclosed', 'preforeclosure']], None] = Field(None, alias='listingTypes', description='Listing types to include for buy searches; omit for all standard types. fsba = agent listed, fsbo = for sale by owner.')
    location: Annotated[str, Field(min_length=1)] = Field(..., alias='location', description='Region-level location to search: ZIP code, city and state, county, or neighborhood.')
    max_bedrooms: Union[Annotated[int, Field(ge=0, le=9007199254740991)], None] = Field(None, alias='maxBedrooms', description='Maximum number of bedrooms.')
    max_living_area_sqft: Union[Annotated[int, Field(ge=0, le=9007199254740991)], None] = Field(None, alias='maxLivingAreaSqft', description='Maximum living area in square feet.')
    max_price: Union[Annotated[int, Field(ge=0, le=9007199254740991)], None] = Field(None, alias='maxPrice', description='Maximum price in USD: monthly rent for rentals, total price for buy/sold.')
    min_bedrooms: Union[Annotated[int, Field(ge=0, le=9007199254740991)], None] = Field(None, alias='minBedrooms', description='Minimum number of bedrooms.')
    min_living_area_sqft: Union[Annotated[int, Field(ge=0, le=9007199254740991)], None] = Field(None, alias='minLivingAreaSqft', description='Minimum living area in square feet.')
    min_price: Union[Annotated[int, Field(ge=0, le=9007199254740991)], None] = Field(None, alias='minPrice', description='Minimum price in USD: monthly rent for rentals, total price for buy/sold.')
    operation: Union[Literal['buy', 'rent', 'sold'], None] = Field(None, alias='operation', description='Listing type: buy (for sale), rent, or sold.')
    show_only_price_reductions: Union[bool, None] = Field(None, alias='showOnlyPriceReductions', description='Only show listings with a price reduction.')
    sort_by: Union[Literal['newest', 'recentlyChanged', 'price_high', 'price_low', 'bedrooms', 'bathrooms', 'rentalPriorityScore'], None] = Field(None, alias='sortBy', description="Sort order for results; omit for Zillow's default relevance. rentalPriorityScore applies to rent searches only.")


class ZillowSearchOutputVariant1(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    tool: str = Field(..., alias='tool', description='The tool that produced this result.')
    count: Annotated[int, Field(ge=-9007199254740991, le=9007199254740991)] = Field(..., alias='count', description='Number of records returned.')
    items: list[dict[str, Any]] = Field(..., alias='items', description='Returned records. A lookup of one thing returns a single record.')
    meta: Union[dict[str, Any], None] = Field(None, alias='meta', description='Values returned alongside the records, such as nextCursor for the next page, or totals.')
    charged_credits: Union[float, int] = Field(..., alias='chargedCredits', description='Credits charged for this call.')
    duration_ms: Union[Union[float, int], None] = Field(..., alias='durationMs', description='Time taken in milliseconds.')


ZillowSearchOutputVariant2DeliveryArtifactsItem = TypedDict('ZillowSearchOutputVariant2DeliveryArtifactsItem', {
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
ZillowSearchOutputVariant2DeliveryArtifactsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


ZillowSearchOutputVariant2DeliveryAvailableExportsItem = TypedDict('ZillowSearchOutputVariant2DeliveryAvailableExportsItem', {
    'artifactId': Required[str],
    'sourceArtifactId': Required[str],
    'filename': Required[Literal['result.md']],
    'contentType': Required[Literal['text/markdown; charset=utf-8']],
    'state': Required[Literal['on-demand']],
})
ZillowSearchOutputVariant2DeliveryAvailableExportsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


ZillowSearchOutputVariant2DeliveryStorageFailureVariant1 = TypedDict('ZillowSearchOutputVariant2DeliveryStorageFailureVariant1', {
    'artifactId': Required[Union[str, None]],
    'outcome': Required[Literal['unknown', 'bytes-stored-metadata-pending', 'failed']],
})
ZillowSearchOutputVariant2DeliveryStorageFailureVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


ZillowSearchOutputVariant2Delivery = TypedDict('ZillowSearchOutputVariant2Delivery', {
    'mode': Required[Literal['artifact']],
    'status': Required[Literal['complete', 'partial', 'unavailable']],
    'retainedRepresentation': Required[Literal['formatted-tool-result']],
    'sourceIsError': Required[bool],
    'artifacts': Required[list[ZillowSearchOutputVariant2DeliveryArtifactsItem]],
    'availableExports': NotRequired[list[ZillowSearchOutputVariant2DeliveryAvailableExportsItem]],
    'downloadLinksOmitted': Required[bool],
    'scopeOmittedFields': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'storageFailure': Required[Union[ZillowSearchOutputVariant2DeliveryStorageFailureVariant1, None]],
    'nextAction': Required[str],
})
ZillowSearchOutputVariant2Delivery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


ZillowSearchOutputVariant2RecoveryOperation = TypedDict('ZillowSearchOutputVariant2RecoveryOperation', {
    'runId': Required[Union[Annotated[str, Field(max_length=200)], None]],
    'idempotencyKey': Required[Annotated[str, Field(max_length=512)]],
    'state': Required[Annotated[str, Field(max_length=100)]],
})
ZillowSearchOutputVariant2RecoveryOperation.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


ZillowSearchOutputVariant2Recovery = TypedDict('ZillowSearchOutputVariant2Recovery', {
    'idempotencyKey': NotRequired[Annotated[str, Field(max_length=512)]],
    'operationId': NotRequired[Annotated[str, Field(max_length=200)]],
    'runId': NotRequired[Annotated[str, Field(max_length=200)]],
    'jobId': NotRequired[Annotated[str, Field(max_length=200)]],
    'operation': NotRequired[ZillowSearchOutputVariant2RecoveryOperation],
})
ZillowSearchOutputVariant2Recovery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class ZillowSearchOutputVariant2(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    delivery: ZillowSearchOutputVariant2Delivery = Field(..., alias='delivery', description='')
    preview: str = Field(..., alias='preview', description='')
    scope: dict[str, Union[str, Union[float, int], bool, None]] = Field(..., alias='scope', description='')
    recovery: ZillowSearchOutputVariant2Recovery = Field(..., alias='recovery', description='')


# Union schema: validate external payloads with TypeAdapter(ZillowSearchOutput).
ZillowSearchOutput = Union[ZillowSearchOutputVariant1, ZillowSearchOutputVariant2]

_ZillowSearchInputAdapter = TypeAdapter(ZillowSearchInput)
_ZillowSearchOutputAdapter = TypeAdapter(ZillowSearchOutput)