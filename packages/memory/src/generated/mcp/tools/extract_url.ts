export interface Input {
  /**
   * Public http/https URL to extract.
   */
  url: string;
  /**
   * Capture a full-page screenshot, saved to ~/Downloads/mcp-scraper/screenshots/ and returned inline.
   */
  screenshot?: boolean;
  /**
   * Viewport for screenshot. desktop = 1440×900, mobile = 390×844.
   */
  screenshotDevice?: "desktop" | "mobile";
  /**
   * Extract brand colors, fonts, logo, and favicon via a rendered browser session.
   */
  extractBranding?: boolean;
  /**
   * Extract and download page media (images/video/audio) to ~/Downloads/mcp-scraper/media/. Ad/tracking noise is filtered automatically.
   */
  downloadMedia?: boolean;
  /**
   * Which media types to download. Default all three.
   */
  mediaTypes?: ("image" | "video" | "audio")[];
  /**
   * Allow localhost and private-network URLs. Local development only.
   */
  allowLocal?: boolean;
  /**
   * Save the full page content into the user's MCP Memory vault server-side, embedded for semantic recall — the full body is NOT returned to chat.
   */
  depositToVault?: boolean;
  /**
   * Optional vault to deposit into. Defaults to the user's personal vault.
   */
  vaultName?: string;
}

export type Output = unknown
