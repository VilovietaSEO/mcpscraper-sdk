from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field


class ArchiveReadInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    artifact_id: str | None = Field(None, alias="artifactId", description="Preferred: private artifactId returned by check_site_export. The server reauthorizes ownership on every read.")
    url: str | None = Field(None, alias="url", description="Fallback: bounded public HTTPS ZIP URL. Use artifactId for MCP Scraper-owned exports.")
    path: str | None = Field(None, alias="path", description="Exact ZIP entry path to read. Omit to list the archive. Use a path returned by a previous archive_read listing.")
    offset: int | None = Field(None, alias="offset", description="Byte offset for a text-file read. Continue from nextOffset until it is null. Ignored when path is omitted.")
    max_bytes: int | None = Field(None, alias="maxBytes", description="Maximum UTF-8 bytes to return from the selected text file. Default 50,000; maximum 200,000.")
    max_entries: int | None = Field(None, alias="maxEntries", description="Maximum entry rows returned when listing. The server still validates the complete archive. Default 200; maximum 1,000.")
    deposit_to_library: bool | None = Field(None, alias="depositToLibrary", description="Store the complete selected text file in the tenant Library vault through library-ingest. Requires path. Preserves the ZIP URL and entry path as source provenance.")


class ArchiveReadOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    mode: Literal["list", "read"] = Field(..., alias="mode", description="")
    archive_url: str = Field(..., alias="archiveUrl", description="")
    compressed_bytes: int = Field(..., alias="compressedBytes", description="")
    entry_count: int = Field(..., alias="entryCount", description="")
    total_uncompressed_bytes: int = Field(..., alias="totalUncompressedBytes", description="")
    entries: list[dict[str, Any]] | None = Field(None, alias="entries", description="")
    entries_truncated: bool | None = Field(None, alias="entriesTruncated", description="")
    path: str | None = Field(None, alias="path", description="")
    content_type: str | None = Field(None, alias="contentType", description="")
    file_bytes: int | None = Field(None, alias="fileBytes", description="")
    offset: int | None = Field(None, alias="offset", description="")
    content: str | None = Field(None, alias="content", description="")
    next_offset: Any | None = Field(None, alias="nextOffset", description="")
    memory: dict[str, Any] | None = Field(None, alias="memory", description="")
