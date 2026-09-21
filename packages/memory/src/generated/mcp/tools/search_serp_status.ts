export interface Input {
  /**
   * The jobId returned by search_serp.
   */
  jobId: string;
}

export interface Output {
  jobId: string | null;
  status: "pending" | "running" | "done";
  statusTool: string | null;
  replayed: boolean;
  query: string;
  location: string | null;
  resultQuality: string | null;
  degradedResult: boolean | null;
  degradationReasons: string[];
  retryRecommended: boolean | null;
  organicResults: {
    position: number;
    title: string;
    url: string;
    rawUrl: string;
    resolvedUrl: string | null;
    linkType: "plain" | "google_url_redirect" | "google_goto_redirect";
    resolutionStatus: "not_needed" | "resolved" | "unresolved" | "rejected";
    domain: string;
    snippet: string | null;
  }[];
  localPack: {
    position: number;
    name: string;
    rating: string | null;
    reviewCount: string | null;
    websiteUrl: string | null;
  }[];
  aiOverview: {
    detected: boolean;
    text: string | null;
    citations: {
      text: string;
      href: string;
      rawUrl: string;
      resolvedUrl: string | null;
      linkType: "plain" | "google_url_redirect" | "google_goto_redirect";
      resolutionStatus: "not_needed" | "resolved" | "unresolved" | "rejected";
    }[];
    expanded: boolean;
    fullyExpanded: boolean;
    sections: string[];
    shareUrl?: string | null;
  } | null;
  entityIds: {
    /**
     * Entities named on the page with their kgId/cid/gcid. Flat lists below are the same IDs deduplicated, kept for backward compatibility.
     */
    entities: {
      name: string;
      kgId: string | null;
      cid: string | null;
      gcid: string | null;
    }[];
    kgIds: string[];
    cids: string[];
    gcids: string[];
  } | null;
}
