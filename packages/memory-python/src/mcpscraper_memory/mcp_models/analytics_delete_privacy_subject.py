from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field


class AnalyticsDeletePrivacySubjectInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    site_id: str = Field(..., alias="siteId", description="Analytics Site id returned by analytics_list_sites.")
    subject_ref: str = Field(..., alias="subjectRef", description="Opaque Site-scoped reference returned by an X-Ray read. Raw visitor, session, device, email, phone, IP, and identity hashes are never accepted.")
    idempotency_key: str = Field(..., alias="idempotencyKey", description="Caller-owned idempotency key. Reuse it only when retrying the same logical mutation.")


class AnalyticsDeletePrivacySubjectOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    ok: bool = Field(..., alias="ok", description="")
    deleted: bool = Field(..., alias="deleted", description="")
    counts: dict[str, Any] = Field(..., alias="counts", description="")
