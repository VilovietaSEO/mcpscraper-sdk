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

export type Output = unknown
