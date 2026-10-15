from typing import Annotated, Any, Literal, Union
from typing_extensions import NotRequired, Required, TypedDict
from pydantic import BaseModel, ConfigDict, Field, TypeAdapter


class MapsPlaceIntelInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=False)

    business_name: Annotated[str, Field(min_length=1)] = Field(..., alias='businessName', description='Business name only, e.g. "Elite Roofing" (not "Elite Roofing Denver CO" — put the city in location).')
    location: Annotated[str, Field(min_length=1)] = Field(..., alias='location', description='City/region/country where the business should be searched, e.g. "Denver, CO".')
    gl: Union[Annotated[str, Field(min_length=2, max_length=2)], None] = Field(None, alias='gl', description='Google country code inferred from location.')
    hl: Union[Annotated[str, Field(min_length=2, max_length=2)], None] = Field(None, alias='hl', description='Language inferred from user request.')
    include_reviews: Union[bool, None] = Field(None, alias='includeReviews', description='Fetch individual review cards — for reviews, customer pain, complaints, or praise themes.')
    max_reviews: Union[Annotated[int, Field(ge=1, le=1000)], None] = Field(None, alias='maxReviews', description='Max review cards when includeReviews is true. Default 50, maximum 1,000. Availability depends on the profile. Partial or interrupted runs can resume.')
    include_services: Union[bool, None] = Field(None, alias='includeServices', description="Collect the exact business's configured services and areas served when available. These fields are absent on some profiles.")
    include_images: Union[bool, None] = Field(None, alias='includeImages', description='Collect Google Maps listing photos, download them, and return an AI-readable manifest plus an owner-scoped ZIP artifact. The gallery is scrolled until quiescent or maxImages is reached.')
    include: Union[list[Literal['core', 'hours', 'services', 'areasServed', 'reviews', 'images', 'all']], None] = Field(None, alias='include', description='Requested place field groups. all requests every supported group while maxReviews and maxImages still cap collection. Existing includeReviews, includeServices, and includeImages flags remain valid.')
    image_scope: Union[Literal['owner', 'all'], None] = Field(None, alias='imageScope', description='owner collects only the Google Maps By owner gallery. all collects the full gallery and labels exact owner matches versus other/unknown media.')
    max_images: Union[Annotated[int, Field(ge=1, le=250)], None] = Field(None, alias='maxImages', description='Maximum photos to collect when includeImages is true. Default 100, maximum 250.')
    max_inline_images: Union[Annotated[int, Field(ge=0, le=5)], None] = Field(None, alias='maxInlineImages', description='Maximum downloaded photos attached as MCP image blocks for direct AI vision. The ZIP and structured manifest still contain the wider result.')


MapsPlaceIntelOutputVariant1HoursTableItem = TypedDict('MapsPlaceIntelOutputVariant1HoursTableItem', {
    'day': Required[str],
    'hours': Required[str],
})
MapsPlaceIntelOutputVariant1HoursTableItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


MapsPlaceIntelOutputVariant1ReviewsItem = TypedDict('MapsPlaceIntelOutputVariant1ReviewsItem', {
    'reviewId': Required[Union[str, None]],
    'author': Required[Union[str, None]],
    'stars': Required[Union[str, None]],
    'date': Required[Union[str, None]],
    'text': Required[Union[str, None]],
    'ownerResponse': Required[Union[str, None]],
    'reviewExpansionIncomplete': NotRequired[bool],
})
MapsPlaceIntelOutputVariant1ReviewsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


MapsPlaceIntelOutputVariant1ReviewHistogramItem = TypedDict('MapsPlaceIntelOutputVariant1ReviewHistogramItem', {
    'stars': Required[Annotated[int, Field(ge=1, le=5)]],
    'count': Required[str],
})
MapsPlaceIntelOutputVariant1ReviewHistogramItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


MapsPlaceIntelOutputVariant1ReviewTopicsItem = TypedDict('MapsPlaceIntelOutputVariant1ReviewTopicsItem', {
    'label': Required[str],
    'count': Required[str],
})
MapsPlaceIntelOutputVariant1ReviewTopicsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


MapsPlaceIntelOutputVariant1AboutAttributesItem = TypedDict('MapsPlaceIntelOutputVariant1AboutAttributesItem', {
    'section': Required[str],
    'attribute': Required[str],
})
MapsPlaceIntelOutputVariant1AboutAttributesItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


MapsPlaceIntelOutputVariant1MediaImagesItem = TypedDict('MapsPlaceIntelOutputVariant1MediaImagesItem', {
    'index': Required[Annotated[int, Field(ge=1, le=9007199254740991)]],
    'galleryPosition': Required[Union[Annotated[int, Field(ge=1, le=9007199254740991)], None]],
    'sourceUrl': Required[str],
    'mediaKey': Required[str],
    'origin': Required[Literal['owner', 'other', 'unknown']],
    'originConfidence': Required[str],
    'filename': Required[Union[str, None]],
    'mimeType': Required[Union[str, None]],
    'bytes': Required[Union[Annotated[int, Field(ge=0, le=9007199254740991)], None]],
    'downloadStatus': Required[str],
    'downloadError': Required[Union[str, None]],
    'contentIndex': Required[Union[Annotated[int, Field(ge=1, le=9007199254740991)], None]],
})
MapsPlaceIntelOutputVariant1MediaImagesItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


MapsPlaceIntelOutputVariant1MediaArtifactVariant1 = TypedDict('MapsPlaceIntelOutputVariant1MediaArtifactVariant1', {
    'artifactId': Required[str],
    'filename': Required[str],
    'contentType': Required[str],
    'bytes': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'sha256': Required[str],
    'expiresAt': Required[str],
    'downloadUrl': Required[Union[str, None]],
    'downloadUrlExpiresAt': Required[Union[str, None]],
    'localPath': Required[Union[str, None]],
})
MapsPlaceIntelOutputVariant1MediaArtifactVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


MapsPlaceIntelOutputVariant1Media = TypedDict('MapsPlaceIntelOutputVariant1Media', {
    'status': NotRequired[str],
    'scope': NotRequired[Literal['owner', 'all']],
    'requestedMaxImages': NotRequired[Annotated[int, Field(ge=1, le=9007199254740991)]],
    'imagesCollected': NotRequired[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'imagesDownloaded': NotRequired[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'ownerImagesCollected': NotRequired[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'otherImagesCollected': NotRequired[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'unknownOriginImagesCollected': NotRequired[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'ownerGalleryAvailable': NotRequired[bool],
    'ownerGalleryExhausted': NotRequired[bool],
    'ownerPhotosDiscovered': NotRequired[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'allPhotosDiscovered': NotRequired[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'exhausted': NotRequired[bool],
    'stopReason': NotRequired[str],
    'images': NotRequired[list[MapsPlaceIntelOutputVariant1MediaImagesItem]],
    'artifact': NotRequired[Union[MapsPlaceIntelOutputVariant1MediaArtifactVariant1, None]],
    'warnings': NotRequired[list[str]],
})
MapsPlaceIntelOutputVariant1Media.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class MapsPlaceIntelOutputVariant1(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    run_id: Union[str, None] = Field(None, alias='runId', description='')
    run_status: Union[Literal['queued', 'running', 'interrupted', 'complete', 'partial', 'failed', 'cancelled'], None] = Field(None, alias='runStatus', description='')
    verified: Union[bool, None] = Field(None, alias='verified', description='')
    checkpoint_revision: Union[Annotated[int, Field(ge=0, le=9007199254740991)], None] = Field(None, alias='checkpointRevision', description='')
    completed_fields: Union[list[str], None] = Field(None, alias='completedFields', description='')
    pending_fields: Union[list[str], None] = Field(None, alias='pendingFields', description='')
    unavailable_fields: Union[list[str], None] = Field(None, alias='unavailableFields', description='')
    requested_max_reviews: Union[Annotated[int, Field(ge=0, le=9007199254740991)], None] = Field(None, alias='requestedMaxReviews', description='')
    requested_max_images: Union[Annotated[int, Field(ge=0, le=9007199254740991)], None] = Field(None, alias='requestedMaxImages', description='')
    images_collected: Union[Annotated[int, Field(ge=0, le=9007199254740991)], None] = Field(None, alias='imagesCollected', description='')
    billing_state: Union[str, None] = Field(None, alias='billingState', description='')
    status_path: Union[str, None] = Field(None, alias='statusPath', description='')
    reviews_next_cursor: Union[Union[str, None], None] = Field(None, alias='reviewsNextCursor', description='')
    images_next_cursor: Union[Union[str, None], None] = Field(None, alias='imagesNextCursor', description='')
    maximum_authorization_mc: Union[Annotated[int, Field(ge=0, le=9007199254740991)], None] = Field(None, alias='maximumAuthorizationMc', description='')
    name: Union[Union[str, None], None] = Field(None, alias='name', description='')
    place_url: Union[Union[str, None], None] = Field(None, alias='placeUrl', description='')
    rating: Union[Union[str, None], None] = Field(None, alias='rating', description='')
    review_count: Union[Union[str, None], None] = Field(None, alias='reviewCount', description='')
    category: Union[Union[str, None], None] = Field(None, alias='category', description='')
    address: Union[Union[str, None], None] = Field(None, alias='address', description='')
    phone: Union[Union[str, None], None] = Field(None, alias='phone', description='')
    website: Union[Union[str, None], None] = Field(None, alias='website', description='')
    hours_summary: Union[Union[str, None], None] = Field(None, alias='hoursSummary', description='')
    hours_table: Union[list[MapsPlaceIntelOutputVariant1HoursTableItem], None] = Field(None, alias='hoursTable', description='')
    plus_code: Union[Union[str, None], None] = Field(None, alias='plusCode', description='')
    booking_url: Union[Union[str, None], None] = Field(None, alias='bookingUrl', description='')
    kgmid: Union[Union[str, None], None] = Field(None, alias='kgmid', description='')
    cid_decimal: Union[Union[str, None], None] = Field(None, alias='cidDecimal', description='')
    cid_url: Union[Union[str, None], None] = Field(None, alias='cidUrl', description='')
    lat: Union[Union[Union[float, int], None], None] = Field(None, alias='lat', description='')
    lng: Union[Union[Union[float, int], None], None] = Field(None, alias='lng', description='')
    reviews_status: Union[str, None] = Field(None, alias='reviewsStatus', description='')
    reviews_collected: Union[Annotated[int, Field(ge=0, le=9007199254740991)], None] = Field(None, alias='reviewsCollected', description='')
    reviews: Union[list[MapsPlaceIntelOutputVariant1ReviewsItem], None] = Field(None, alias='reviews', description='')
    review_histogram: Union[list[MapsPlaceIntelOutputVariant1ReviewHistogramItem], None] = Field(None, alias='reviewHistogram', description='')
    review_topics: Union[list[MapsPlaceIntelOutputVariant1ReviewTopicsItem], None] = Field(None, alias='reviewTopics', description='')
    services: Union[list[str], None] = Field(None, alias='services', description='')
    areas_served: Union[list[str], None] = Field(None, alias='areasServed', description='')
    services_status: Union[str, None] = Field(None, alias='servicesStatus', description='')
    about_attributes: Union[list[MapsPlaceIntelOutputVariant1AboutAttributesItem], None] = Field(None, alias='aboutAttributes', description='')
    media: Union[MapsPlaceIntelOutputVariant1Media, None] = Field(None, alias='media', description='')


MapsPlaceIntelOutputVariant2DeliveryArtifactsItem = TypedDict('MapsPlaceIntelOutputVariant2DeliveryArtifactsItem', {
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
MapsPlaceIntelOutputVariant2DeliveryArtifactsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


MapsPlaceIntelOutputVariant2DeliveryStorageFailureVariant1 = TypedDict('MapsPlaceIntelOutputVariant2DeliveryStorageFailureVariant1', {
    'artifactId': Required[Union[str, None]],
    'outcome': Required[Literal['unknown', 'bytes-stored-metadata-pending', 'failed']],
})
MapsPlaceIntelOutputVariant2DeliveryStorageFailureVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


MapsPlaceIntelOutputVariant2Delivery = TypedDict('MapsPlaceIntelOutputVariant2Delivery', {
    'mode': Required[Literal['artifact']],
    'status': Required[Literal['complete', 'partial', 'unavailable']],
    'retainedRepresentation': Required[Literal['formatted-tool-result']],
    'sourceIsError': Required[bool],
    'artifacts': Required[list[MapsPlaceIntelOutputVariant2DeliveryArtifactsItem]],
    'downloadLinksOmitted': Required[bool],
    'scopeOmittedFields': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'storageFailure': Required[Union[MapsPlaceIntelOutputVariant2DeliveryStorageFailureVariant1, None]],
    'nextAction': Required[str],
})
MapsPlaceIntelOutputVariant2Delivery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


MapsPlaceIntelOutputVariant2RecoveryOperation = TypedDict('MapsPlaceIntelOutputVariant2RecoveryOperation', {
    'runId': Required[Union[Annotated[str, Field(max_length=200)], None]],
    'idempotencyKey': Required[Annotated[str, Field(max_length=512)]],
    'state': Required[Annotated[str, Field(max_length=100)]],
})
MapsPlaceIntelOutputVariant2RecoveryOperation.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


MapsPlaceIntelOutputVariant2Recovery = TypedDict('MapsPlaceIntelOutputVariant2Recovery', {
    'idempotencyKey': NotRequired[Annotated[str, Field(max_length=512)]],
    'operationId': NotRequired[Annotated[str, Field(max_length=200)]],
    'runId': NotRequired[Annotated[str, Field(max_length=200)]],
    'jobId': NotRequired[Annotated[str, Field(max_length=200)]],
    'operation': NotRequired[MapsPlaceIntelOutputVariant2RecoveryOperation],
})
MapsPlaceIntelOutputVariant2Recovery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class MapsPlaceIntelOutputVariant2(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    delivery: MapsPlaceIntelOutputVariant2Delivery = Field(..., alias='delivery', description='')
    preview: str = Field(..., alias='preview', description='')
    scope: dict[str, Union[str, Union[float, int], bool, None]] = Field(..., alias='scope', description='')
    recovery: MapsPlaceIntelOutputVariant2Recovery = Field(..., alias='recovery', description='')


# Union schema: validate external payloads with TypeAdapter(MapsPlaceIntelOutput).
MapsPlaceIntelOutput = Union[MapsPlaceIntelOutputVariant2, MapsPlaceIntelOutputVariant1]

_MapsPlaceIntelInputAdapter = TypeAdapter(MapsPlaceIntelInput)
_MapsPlaceIntelOutputAdapter = TypeAdapter(MapsPlaceIntelOutput)