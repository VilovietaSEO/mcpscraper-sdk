from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field


class GmailPrepareMemoryImportInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    connection_id: str = Field(..., alias="connectionId", description="The tenant-owned Gmail connectionId bound into this immutable selection.")
    selection_id: str = Field(..., alias="selectionId", description="Immutable selectionId returned by gmail_prepare_selection with purpose memory_import.")
    selection_sha256: str = Field(..., alias="selectionSha256", description="Unchanged selection digest to bind the reviewed Memory plan.")
    filing_policy: Literal['source_archive', 'relationship_communications'] | None = Field(None, alias="filingPolicy", description="source_archive preserves evidence in Library by default; relationship_communications requires exact existing identity resolution and never creates People, Tasks, Deals, or Projects.")
    destination: Any | None = Field(None, alias="destination", description="Use auto for the policy-correct Library or Communications vault, or name one exact existing vault.")
    attachment_policy: Literal['preserve_all', 'index_supported', 'metadata_only', 'exclude'] | None = Field(None, alias="attachmentPolicy", description="How original attachment bytes are handled; preserve_all is the default complete-evidence route.")


class GmailPrepareMemoryImportOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    ok: bool = Field(..., alias="ok", description="")
    plan: dict[str, Any] | None = Field(None, alias="plan", description="")
    untrusted_content: bool = Field(..., alias="untrustedContent", description="")
    error: Any = Field(..., alias="error", description="")
