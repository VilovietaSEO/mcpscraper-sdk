export interface Input {
  /**
   * Instagram handle, with or without @. Provide handle or url.
   */
  handle?: string;
  /**
   * Instagram profile URL. Provide handle or url.
   */
  url?: string;
  /**
   * Optional saved hosted browser profile name for authenticated Instagram access.
   */
  profile?: string;
  /**
   * Save browser changes back to the hosted profile. Leave unset unless intentionally updating the saved login.
   */
  saveProfileChanges?: boolean;
  /**
   * Maximum grid URLs to collect. Default 50, maximum 2000.
   */
  maxItems?: number;
  /**
   * Maximum pagination scroll attempts. Default 10, maximum 250.
   */
  maxScrolls?: number;
  /**
   * Delay after each scroll before collecting new links. Default 1200ms.
   */
  scrollDelayMs?: number;
  /**
   * Stop after this many consecutive scrolls with no new links.
   */
  stableScrollLimit?: number;
}

export interface Output {
  handle: string;
  profileUrl: string;
  pageUrl: string;
  browser: {
    mode: "hosted";
    requestedMode: "hosted";
    profileName: string | null;
    profileSource: "hosted";
    profileDirConfigured: boolean;
    executablePathConfigured: boolean;
  };
  profileName: string | null;
  reportedPostCount: number | null;
  reportedPostCountText: string | null;
  followerCountText: string | null;
  followingCountText: string | null;
  collectedContentCount: number;
  typeCounts: {
    post: number;
    reel: number;
    tv: number;
  };
  pagination: {
    maxItems: number;
    maxScrolls: number;
    attemptedScrolls: number;
    stableScrolls: number;
    stableScrollLimit: number;
    scrollDelayMs: number;
    reachedMaxItems: boolean;
    reachedReportedPostCount: boolean;
    finalScrollHeight: number | null;
    stoppedReason: "max_items" | "reported_post_count" | "stable_scrolls" | "max_scrolls" | "no_scrolls";
    stages: {
      stage: string;
      itemCount: number;
      addedCount: number;
      scrollY: number | null;
      scrollHeight: number | null;
    }[];
  };
  limited: boolean;
  limitations: string[];
  items: {
    url: string;
    type: "post" | "reel" | "tv";
    shortcode: string;
    anchorText: string | null;
    firstSeenStage: string;
  }[];
}
