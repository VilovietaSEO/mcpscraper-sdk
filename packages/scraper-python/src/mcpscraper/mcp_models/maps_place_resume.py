from typing import Annotated, Any, Literal, Union
from typing_extensions import NotRequired, Required, TypedDict
from pydantic import BaseModel, ConfigDict, Field, TypeAdapter


class MapsPlaceResumeInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=False)

    run_id: str = Field(..., alias='runId', description='Partial or reconciled interrupted Maps place run to resume.')
    resume_idempotency_key: Annotated[str, Field(min_length=1, max_length=500)] = Field(..., alias='resumeIdempotencyKey', description='A new key for this explicit attempt; reuse the same key to read its status.')


MapsPlaceResumeOutputVariant1HoursTableItem = TypedDict('MapsPlaceResumeOutputVariant1HoursTableItem', {
    'day': Required[str],
    'hours': Required[str],
})
MapsPlaceResumeOutputVariant1HoursTableItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


MapsPlaceResumeOutputVariant1ReviewsItem = TypedDict('MapsPlaceResumeOutputVariant1ReviewsItem', {
    'reviewId': Required[Union[str, None]],
    'author': Required[Union[str, None]],
    'stars': Required[Union[str, None]],
    'date': Required[Union[str, None]],
    'text': Required[Union[str, None]],
    'ownerResponse': Required[Union[str, None]],
    'reviewExpansionIncomplete': NotRequired[bool],
})
MapsPlaceResumeOutputVariant1ReviewsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


MapsPlaceResumeOutputVariant1ReviewHistogramItem = TypedDict('MapsPlaceResumeOutputVariant1ReviewHistogramItem', {
    'stars': Required[Annotated[int, Field(ge=1, le=5)]],
    'count': Required[str],
})
MapsPlaceResumeOutputVariant1ReviewHistogramItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


MapsPlaceResumeOutputVariant1ReviewTopicsItem = TypedDict('MapsPlaceResumeOutputVariant1ReviewTopicsItem', {
    'label': Required[str],
    'count': Required[str],
})
MapsPlaceResumeOutputVariant1ReviewTopicsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


MapsPlaceResumeOutputVariant1AboutAttributesItem = TypedDict('MapsPlaceResumeOutputVariant1AboutAttributesItem', {
    'section': Required[str],
    'attribute': Required[str],
})
MapsPlaceResumeOutputVariant1AboutAttributesItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


MapsPlaceResumeOutputVariant1MediaImagesItem = TypedDict('MapsPlaceResumeOutputVariant1MediaImagesItem', {
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
MapsPlaceResumeOutputVariant1MediaImagesItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


MapsPlaceResumeOutputVariant1MediaArtifactVariant1 = TypedDict('MapsPlaceResumeOutputVariant1MediaArtifactVariant1', {
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
MapsPlaceResumeOutputVariant1MediaArtifactVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


MapsPlaceResumeOutputVariant1Media = TypedDict('MapsPlaceResumeOutputVariant1Media', {
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
    'images': NotRequired[list[MapsPlaceResumeOutputVariant1MediaImagesItem]],
    'artifact': NotRequired[Union[MapsPlaceResumeOutputVariant1MediaArtifactVariant1, None]],
    'warnings': NotRequired[list[str]],
})
MapsPlaceResumeOutputVariant1Media.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class MapsPlaceResumeOutputVariant1(BaseModel):
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
    hours_table: Union[list[MapsPlaceResumeOutputVariant1HoursTableItem], None] = Field(None, alias='hoursTable', description='')
    plus_code: Union[Union[str, None], None] = Field(None, alias='plusCode', description='')
    booking_url: Union[Union[str, None], None] = Field(None, alias='bookingUrl', description='')
    kgmid: Union[Union[str, None], None] = Field(None, alias='kgmid', description='')
    cid_decimal: Union[Union[str, None], None] = Field(None, alias='cidDecimal', description='')
    cid_url: Union[Union[str, None], None] = Field(None, alias='cidUrl', description='')
    lat: Union[Union[Union[float, int], None], None] = Field(None, alias='lat', description='')
    lng: Union[Union[Union[float, int], None], None] = Field(None, alias='lng', description='')
    reviews_status: Union[str, None] = Field(None, alias='reviewsStatus', description='')
    reviews_collected: Union[Annotated[int, Field(ge=0, le=9007199254740991)], None] = Field(None, alias='reviewsCollected', description='')
    reviews: Union[list[MapsPlaceResumeOutputVariant1ReviewsItem], None] = Field(None, alias='reviews', description='')
    review_histogram: Union[list[MapsPlaceResumeOutputVariant1ReviewHistogramItem], None] = Field(None, alias='reviewHistogram', description='')
    review_topics: Union[list[MapsPlaceResumeOutputVariant1ReviewTopicsItem], None] = Field(None, alias='reviewTopics', description='')
    services: Union[list[str], None] = Field(None, alias='services', description='')
    areas_served: Union[list[str], None] = Field(None, alias='areasServed', description='')
    services_status: Union[str, None] = Field(None, alias='servicesStatus', description='')
    about_attributes: Union[list[MapsPlaceResumeOutputVariant1AboutAttributesItem], None] = Field(None, alias='aboutAttributes', description='')
    media: Union[MapsPlaceResumeOutputVariant1Media, None] = Field(None, alias='media', description='')


MapsPlaceResumeOutputVariant2DeliveryArtifactsItem = TypedDict('MapsPlaceResumeOutputVariant2DeliveryArtifactsItem', {
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
MapsPlaceResumeOutputVariant2DeliveryArtifactsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


MapsPlaceResumeOutputVariant2DeliveryAvailableExportsItem = TypedDict('MapsPlaceResumeOutputVariant2DeliveryAvailableExportsItem', {
    'artifactId': Required[str],
    'sourceArtifactId': Required[str],
    'filename': Required[Literal['result.md']],
    'contentType': Required[Literal['text/markdown; charset=utf-8']],
    'state': Required[Literal['on-demand']],
})
MapsPlaceResumeOutputVariant2DeliveryAvailableExportsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


MapsPlaceResumeOutputVariant2DeliveryStorageFailureVariant1 = TypedDict('MapsPlaceResumeOutputVariant2DeliveryStorageFailureVariant1', {
    'artifactId': Required[Union[str, None]],
    'outcome': Required[Literal['unknown', 'bytes-stored-metadata-pending', 'failed']],
})
MapsPlaceResumeOutputVariant2DeliveryStorageFailureVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


MapsPlaceResumeOutputVariant2Delivery = TypedDict('MapsPlaceResumeOutputVariant2Delivery', {
    'mode': Required[Literal['artifact']],
    'status': Required[Literal['complete', 'partial', 'unavailable']],
    'retainedRepresentation': Required[Literal['formatted-tool-result']],
    'sourceIsError': Required[bool],
    'artifacts': Required[list[MapsPlaceResumeOutputVariant2DeliveryArtifactsItem]],
    'availableExports': NotRequired[list[MapsPlaceResumeOutputVariant2DeliveryAvailableExportsItem]],
    'downloadLinksOmitted': Required[bool],
    'scopeOmittedFields': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'storageFailure': Required[Union[MapsPlaceResumeOutputVariant2DeliveryStorageFailureVariant1, None]],
    'nextAction': Required[str],
})
MapsPlaceResumeOutputVariant2Delivery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


MapsPlaceResumeOutputVariant2RecoveryOperation = TypedDict('MapsPlaceResumeOutputVariant2RecoveryOperation', {
    'runId': Required[Union[Annotated[str, Field(max_length=200)], None]],
    'idempotencyKey': Required[Annotated[str, Field(max_length=512)]],
    'state': Required[Annotated[str, Field(max_length=100)]],
})
MapsPlaceResumeOutputVariant2RecoveryOperation.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


MapsPlaceResumeOutputVariant2Recovery = TypedDict('MapsPlaceResumeOutputVariant2Recovery', {
    'idempotencyKey': NotRequired[Annotated[str, Field(max_length=512)]],
    'operationId': NotRequired[Annotated[str, Field(max_length=200)]],
    'runId': NotRequired[Annotated[str, Field(max_length=200)]],
    'jobId': NotRequired[Annotated[str, Field(max_length=200)]],
    'operation': NotRequired[MapsPlaceResumeOutputVariant2RecoveryOperation],
})
MapsPlaceResumeOutputVariant2Recovery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class MapsPlaceResumeOutputVariant2(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    delivery: MapsPlaceResumeOutputVariant2Delivery = Field(..., alias='delivery', description='')
    preview: str = Field(..., alias='preview', description='')
    scope: dict[str, Union[str, Union[float, int], bool, None]] = Field(..., alias='scope', description='')
    recovery: MapsPlaceResumeOutputVariant2Recovery = Field(..., alias='recovery', description='')


# Union schema: validate external payloads with TypeAdapter(MapsPlaceResumeOutput).
MapsPlaceResumeOutput = Union[MapsPlaceResumeOutputVariant2, MapsPlaceResumeOutputVariant1]

_MapsPlaceResumeInputAdapter = TypeAdapter(MapsPlaceResumeInput)
_MapsPlaceResumeOutputAdapter = TypeAdapter(MapsPlaceResumeOutput)