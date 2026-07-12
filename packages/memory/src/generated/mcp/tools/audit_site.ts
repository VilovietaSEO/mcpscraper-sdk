export interface Input {
  /**
   * Public website URL or domain for a full technical SEO audit (issues, link graph, indexability, headings, images). For plain content use extract_site instead.
   */
  url: string;
  /**
   * Maximum pages to crawl and audit. Always writes a folder of analysis files plus per-page content, returning a summary plus the folder path.
   */
  maxPages?: number;
  /**
   * Route page fetches through rotating residential proxies to defeat rate-limiting and bot blocks. Slower/pricier — use only when a site blocks normal crawling.
   */
  rotateProxies?: boolean;
  /**
   * When rotateProxies is on, pages fetched per proxy before rotating. Default 30.
   */
  rotateProxyEvery?: number;
}

export interface Output {
  url: string;
  pageCount: number;
  durationMs: number;
  bulkFolder: string | null;
  issues: {
    [k: string]: number;
  };
  images: {
    unique: number;
    totalBytes: number;
    over100kb: number;
    legacyFormat: number;
  };
  links: {
    internal: number;
    external: number;
    orphans: number;
    brokenInternal: number;
    externalDomains: number;
  };
  artifact?: {
    artifactId: string;
    bytes: number;
    expiresAt: string;
    preview: string;
  };
}
