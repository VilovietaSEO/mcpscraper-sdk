from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field


class ReportArtifactReadInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    artifact_id: str = Field(..., alias="artifactId", description="Artifact id returned inline by a tool whose result was too large to inline. Use only a returned artifactId; do not construct one yourself.")
    offset: int | None = Field(None, alias="offset", description="Byte offset to start reading from. Pass the previous call's nextOffset to continue.")
    max_bytes: int | None = Field(None, alias="maxBytes", description="Maximum bytes of artifact text to return in this window.")


class ReportArtifactReadOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    artifact_id: str = Field(..., alias="artifactId", description="")
    text: str = Field(..., alias="text", description="")
    total_bytes: int = Field(..., alias="totalBytes", description="")
    next_offset: Any = Field(..., alias="nextOffset", description="")
