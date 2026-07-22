export interface Input {
  /**
   * Tenant-owned Meta Marketing connectionId from list_service_connections.
   */
  connectionId: string;
  /**
   * Meta ad ID from the connected ad account. This is not an Ad Library archive ID.
   */
  adId: string;
  /**
   * inline_preview returns bounded MCP image content that a vision-capable client can inspect. resource_only returns descriptors/URLs only. none skips image delivery.
   */
  imageMode?: "inline_preview" | "resource_only" | "none";
  /**
   * Maximum creative image/thumbnail previews to attach as MCP image blocks. Default 2; maximum 4.
   */
  maxInlineImages?: number;
}

export interface Output {
  ok: boolean;
  adId: string;
  adName: string | null;
  adAccountId: string | null;
  creativeId: string;
  creativeName: string | null;
  effectiveObjectStoryId: string | null;
  sourceFacebookPostId: string | null;
  objectStoryId: string | null;
  pageId: string | null;
  postId: string | null;
  publicPostCandidateUrl: string | null;
  publicPostStatus: "unverified";
  mediaType: "image" | "video" | "carousel" | "mixed" | "unknown";
  images: {
    [k: string]: unknown;
  }[];
  videos: {
    [k: string]: unknown;
  }[];
  inlineImages: {
    sourceUrl: string;
    mimeType: string;
    bytes: number;
    contentIndex: number;
  }[];
  nextActions: {
    tool: "facebook_ad_transcribe" | "facebook_video_transcribe" | "video_frame_analysis";
    args: {
      [k: string]: unknown;
    };
    reason: string;
  }[];
  warnings: string[];
  limitations: string[];
}
