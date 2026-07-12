export interface Input {
  /**
   * Public website URL or domain to crawl for page CONTENT (map + scrape). For a technical SEO audit use audit_site instead — this returns content only, not analysis.
   */
  url: string;
  /**
   * Maximum pages to extract. Bulk crawls (over 25 pages) switch to folder mode: each page saved as its own Markdown file, with a summary plus folder path returned instead of inlining content.
   */
  maxPages?: number;
  /**
   * Route page fetches through rotating residential proxies to defeat rate-limiting and bot blocks (403/429). Slower and pricier — use only when a site blocks normal crawling.
   */
  rotateProxies?: boolean;
  /**
   * When rotateProxies is on, pages fetched per proxy before rotating. Default 30.
   */
  rotateProxyEvery?: number;
  /**
   * Per-page output formats: markdown, links, json, images are captured cheaply from HTML; branding (site-level logo/colors/fonts) requires a browser and adds time. Defaults to markdown+links.
   */
  formats?: ("markdown" | "links" | "json" | "images" | "branding")[];
}

export interface Output {
  url: string;
  pageCount: number;
  pages: {
    url: string;
    title: string | null;
    schemaTypes: string[];
  }[];
  durationMs: number;
  truncatedCount?: number;
  artifact?: {
    artifactId: string;
    bytes: number;
    expiresAt: string;
    preview: string;
  };
}
