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

export type Output = unknown
