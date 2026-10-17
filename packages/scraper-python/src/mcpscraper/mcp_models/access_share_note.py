from typing import Annotated, Any, Literal, Union
from typing_extensions import NotRequired, Required, TypedDict
from pydantic import BaseModel, ConfigDict, Field, TypeAdapter


AccessShareNoteInputPermissions = TypedDict('AccessShareNoteInputPermissions', {
    'edit': NotRequired[bool],
    'delete': NotRequired[bool],
    'reshare': NotRequired[bool],
})
AccessShareNoteInputPermissions.__pydantic_config__ = ConfigDict(extra="allow", strict=False)


class AccessShareNoteInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=False)

    vault: Union[str, None] = Field(None, alias='vault', description='Vault containing the note to share. Required (with path) unless shareId is given. Must be a vault you own.')
    path: Union[str, None] = Field(None, alias='path', description='Vault-relative path of the note to share. Required (with vault) unless shareId is given.')
    share_id: Union[str, None] = Field(None, alias='shareId', description='Instead of vault+path, re-share a note already shared to you by this shareId. Requires reshare permission on that share.')
    grantee_identity: Annotated[str, Field(min_length=1)] = Field(..., alias='granteeIdentity', description='Identity to offer the note to.')
    permissions: Union[AccessShareNoteInputPermissions, None] = Field(None, alias='permissions', description='Permissions to grant beyond read (always granted): edit (write back to the canonical note), delete (destroy the canonical note — dangerous), reshare (grantee may re-share onward). All default false.')
    bundle_links: Union[Union[bool, list[str]], None] = Field(None, alias='bundleLinks', description="true to also share every detected linked note (same permissions as this share); an array of specific link refs (path or title, from a prior call's linkCandidates) to share only those. Omit or false to share none — default, and the safest choice when unsure.")


AccessShareNoteOutputVariant1Permissions = TypedDict('AccessShareNoteOutputVariant1Permissions', {
    'read': Required[bool],
    'edit': Required[bool],
    'delete': Required[bool],
    'reshare': Required[bool],
})
AccessShareNoteOutputVariant1Permissions.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


AccessShareNoteOutputVariant1LinkCandidatesItem = TypedDict('AccessShareNoteOutputVariant1LinkCandidatesItem', {
    'ref': Required[str],
    'path': Required[str],
    'title': Required[str],
})
AccessShareNoteOutputVariant1LinkCandidatesItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


AccessShareNoteOutputVariant1BundledItem = TypedDict('AccessShareNoteOutputVariant1BundledItem', {
    'ref': Required[str],
    'shareId': Required[str],
    'title': Required[str],
})
AccessShareNoteOutputVariant1BundledItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class AccessShareNoteOutputVariant1(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    ok: bool = Field(..., alias='ok', description='True when the offer was created; false on auth/scope/lookup error.')
    share_id: Union[str, None] = Field(None, alias='shareId', description='Identifier the grantee will use to accept-share, then address the note on get/put/delete.')
    grantee: Union[str, None] = Field(None, alias='grantee', description='The identity the note was offered to.')
    permissions: Union[AccessShareNoteOutputVariant1Permissions, None] = Field(None, alias='permissions', description='The permissions in effect for this share.')
    note: Union[str, None] = Field(None, alias='note', description='Guidance: the offer is pending until the grantee calls accept-share.')
    link_candidates: Union[list[AccessShareNoteOutputVariant1LinkCandidatesItem], None] = Field(None, alias='linkCandidates', description='Notes this one links to (same vault) that were NOT bundled into this share. Relay these to the human and ask before calling share-note again with bundleLinks if they want them included — otherwise they render as [[private note]] to this grantee.')
    bundled: Union[list[AccessShareNoteOutputVariant1BundledItem], None] = Field(None, alias='bundled', description='Linked notes that WERE bundled into this share as their own pending offers (per bundleLinks).')
    error: Union[str, None] = Field(None, alias='error', description='Human-readable failure reason when ok is false.')


AccessShareNoteOutputVariant2DeliveryArtifactsItem = TypedDict('AccessShareNoteOutputVariant2DeliveryArtifactsItem', {
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
AccessShareNoteOutputVariant2DeliveryArtifactsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


AccessShareNoteOutputVariant2DeliveryAvailableExportsItem = TypedDict('AccessShareNoteOutputVariant2DeliveryAvailableExportsItem', {
    'artifactId': Required[str],
    'sourceArtifactId': Required[str],
    'filename': Required[Literal['result.md']],
    'contentType': Required[Literal['text/markdown; charset=utf-8']],
    'state': Required[Literal['on-demand']],
})
AccessShareNoteOutputVariant2DeliveryAvailableExportsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


AccessShareNoteOutputVariant2DeliveryStorageFailureVariant1 = TypedDict('AccessShareNoteOutputVariant2DeliveryStorageFailureVariant1', {
    'artifactId': Required[Union[str, None]],
    'outcome': Required[Literal['unknown', 'bytes-stored-metadata-pending', 'failed']],
})
AccessShareNoteOutputVariant2DeliveryStorageFailureVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


AccessShareNoteOutputVariant2Delivery = TypedDict('AccessShareNoteOutputVariant2Delivery', {
    'mode': Required[Literal['artifact']],
    'status': Required[Literal['complete', 'partial', 'unavailable']],
    'retainedRepresentation': Required[Literal['formatted-tool-result']],
    'sourceIsError': Required[bool],
    'artifacts': Required[list[AccessShareNoteOutputVariant2DeliveryArtifactsItem]],
    'availableExports': NotRequired[list[AccessShareNoteOutputVariant2DeliveryAvailableExportsItem]],
    'downloadLinksOmitted': Required[bool],
    'scopeOmittedFields': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'storageFailure': Required[Union[AccessShareNoteOutputVariant2DeliveryStorageFailureVariant1, None]],
    'nextAction': Required[str],
})
AccessShareNoteOutputVariant2Delivery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


AccessShareNoteOutputVariant2RecoveryOperation = TypedDict('AccessShareNoteOutputVariant2RecoveryOperation', {
    'runId': Required[Union[Annotated[str, Field(max_length=200)], None]],
    'idempotencyKey': Required[Annotated[str, Field(max_length=512)]],
    'state': Required[Annotated[str, Field(max_length=100)]],
})
AccessShareNoteOutputVariant2RecoveryOperation.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


AccessShareNoteOutputVariant2Recovery = TypedDict('AccessShareNoteOutputVariant2Recovery', {
    'idempotencyKey': NotRequired[Annotated[str, Field(max_length=512)]],
    'operationId': NotRequired[Annotated[str, Field(max_length=200)]],
    'runId': NotRequired[Annotated[str, Field(max_length=200)]],
    'jobId': NotRequired[Annotated[str, Field(max_length=200)]],
    'operation': NotRequired[AccessShareNoteOutputVariant2RecoveryOperation],
})
AccessShareNoteOutputVariant2Recovery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class AccessShareNoteOutputVariant2(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    delivery: AccessShareNoteOutputVariant2Delivery = Field(..., alias='delivery', description='')
    preview: str = Field(..., alias='preview', description='')
    scope: dict[str, Union[str, Union[float, int], bool, None]] = Field(..., alias='scope', description='')
    recovery: AccessShareNoteOutputVariant2Recovery = Field(..., alias='recovery', description='')


# Union schema: validate external payloads with TypeAdapter(AccessShareNoteOutput).
AccessShareNoteOutput = Union[AccessShareNoteOutputVariant2, AccessShareNoteOutputVariant1]

_AccessShareNoteInputAdapter = TypeAdapter(AccessShareNoteInput)
_AccessShareNoteOutputAdapter = TypeAdapter(AccessShareNoteOutput)