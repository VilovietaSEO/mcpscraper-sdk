export interface Input {
  /**
   * Caller API key (Bearer secret). Optional when the MCP session is already authenticated; the server resolves auth from the session.
   */
  apiKey?: string;
  /**
   * Session identifier. Optional; defaults to the current MCP session.
   */
  sessionId?: string;
  /**
   * Vault containing the note to share. Required (with path) unless shareId is given. Must be a vault you own.
   */
  vault?: string;
  /**
   * Vault-relative path of the note to share. Required (with vault) unless shareId is given.
   */
  path?: string;
  /**
   * Instead of vault+path, re-share a note already shared to you by this shareId. Requires reshare permission on that share.
   */
  shareId?: string;
  /**
   * Identity to offer the note to.
   */
  granteeIdentity: string;
  /**
   * Permissions to grant beyond read (always granted): edit (write back to the canonical note), delete (destroy the canonical note — dangerous), reshare (grantee may re-share onward). All default false.
   */
  permissions?: {
    edit?: boolean;
    delete?: boolean;
    reshare?: boolean;
  };
  /**
   * true to also share every detected linked note (same permissions as this share); an array of specific link refs (path or title, from a prior call's linkCandidates) to share only those. Omit or false to share none — default, and the safest choice when unsure.
   */
  bundleLinks?: boolean | string[];
}

export interface Output {
  /**
   * True when the offer was created; false on auth/scope/lookup error.
   */
  ok: boolean;
  /**
   * Identifier the grantee will use to accept-share, then address the note on get/put/delete.
   */
  shareId?: string;
  /**
   * The identity the note was offered to.
   */
  grantee?: string;
  /**
   * The permissions in effect for this share.
   */
  permissions?: {
    read: boolean;
    edit: boolean;
    delete: boolean;
    reshare: boolean;
  };
  /**
   * Guidance: the offer is pending until the grantee calls accept-share.
   */
  note?: string;
  /**
   * Notes this one links to (same vault) that were NOT bundled into this share. Relay these to the human and ask before calling share-note again with bundleLinks if they want them included — otherwise they render as [[private note]] to this grantee.
   */
  linkCandidates?: {
    /**
     * The link text/title as written.
     */
    ref: string;
    path: string;
    title: string;
  }[];
  /**
   * Linked notes that WERE bundled into this share as their own pending offers (per bundleLinks).
   */
  bundled?: {
    ref: string;
    shareId: string;
    title: string;
  }[];
  /**
   * Human-readable failure reason when ok is false.
   */
  error?: string;
}
