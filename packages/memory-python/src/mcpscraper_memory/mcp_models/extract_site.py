from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field


class ExtractSiteInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    url: str = Field(..., alias="url", description="Public website URL or domain to crawl for page CONTENT (map + scrape). For a technical SEO audit use audit_site instead — this returns content only, not analysis.")
    max_pages: int | None = Field(None, alias="maxPages", description="Maximum pages to extract. Bulk crawls (over 25 pages) switch to folder mode: each page saved as its own Markdown file, with a summary plus folder path returned instead of inlining content.")
    rotate_proxies: bool | None = Field(None, alias="rotateProxies", description="Route page fetches through rotating residential proxies to defeat rate-limiting and bot blocks (403/429). Slower and pricier — use only when a site blocks normal crawling.")
    rotate_proxy_every: int | None = Field(None, alias="rotateProxyEvery", description="When rotateProxies is on, pages fetched per proxy before rotating. Default 30.")
    formats: list[Literal["markdown", "links", "json", "images", "branding"]] | None = Field(None, alias="formats", description="Per-page output formats: markdown, links, json, images are captured cheaply from HTML; branding (site-level logo/colors/fonts) requires a browser and adds time. Defaults to markdown+links.")


class ExtractSiteOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    url: str = Field(..., alias="url", description="")
    page_count: int = Field(..., alias="pageCount", description="")
    pages: list[dict[str, Any]] = Field(..., alias="pages", description="")
    duration_ms: float = Field(..., alias="durationMs", description="")
    truncated_count: int | None = Field(None, alias="truncatedCount", description="")
    artifact: dict[str, Any] | None = Field(None, alias="artifact", description="")
