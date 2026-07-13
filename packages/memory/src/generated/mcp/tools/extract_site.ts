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
  /**
   * Run the crawl as a background job instead of blocking this call, returning a jobId immediately — poll it with check_site_export to get a downloadable zip (all page content, plus real image files if downloadImages is set) once ready. Use for large sites where a synchronous call would be slow.
   */
  background?: boolean;
  /**
   * Download every discovered image as a real file into the export bundle (not just image URLs/stats). OFF by default — must be explicitly set true. Implies background regardless of the background flag, since downloading a whole site's images is too slow to run synchronously. Capped at 20 images/page and 500 images/site.
   */
  downloadImages?: boolean;
}

export type Output = unknown
