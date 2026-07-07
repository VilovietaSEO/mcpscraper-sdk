export interface Input {
  /**
   * Caller API key (Bearer secret). Optional when the MCP session is already authenticated; the server resolves auth from the session.
   */
  apiKey?: string;
  /**
   * Session identifier used to resolve the active vault and per-session state. Optional; defaults to the current MCP session.
   */
  sessionId?: string;
  /**
   * Vault to write to. Optional; defaults to the session active vault, then the first vault the caller is entitled to. On a default-provisioned account, pick the vault whose job matches the content (see the server instructions for the full 13-vault guide) rather than defaulting blindly — e.g. a lesson learned goes in Knowledge, the raw source it came from goes in Library, a broken feature goes in Issues, a named real-world initiative goes in Projects.
   */
  vault?: string;
  /**
   * Vault-relative note path to create or overwrite, e.g. projects/q3-plan. Writing an existing path replaces it. Required unless shareId is given.
   */
  path?: string;
  /**
   * Edit a note someone individually shared with you and you accepted (accept-share), by its shareId, instead of vault+path. Requires the share to grant edit permission, and baseRevision is mandatory (get the current revision first) since you are editing alongside the owner and possibly others.
   */
  shareId?: string;
  /**
   * Optional human-readable title; defaults are derived from the path when omitted.
   */
  title?: string;
  /**
   * The full note body to store and index for semantic search. Must be non-empty.
   */
  content: string;
  /**
   * Obsidian note primitives (status, summary, tags, pinned, source_type, source_ref, related, related_vault_notes, embed, embed_priority, type, domain, folder). Stored on the note so it round-trips the vault shape; type/domain/folder also steer routing when no vault is given.
   */
  props?: {
    /**
     * Status enum value from the target vault contract.
     */
    status?: string;
    /**
     * Short retrieval-ready description.
     */
    summary?: string;
    /**
     * AI-generated keyword tags, not vault names.
     */
    tags?: string[];
    /**
     * Recall boost for important notes.
     */
    pinned?: boolean;
    /**
     * Attribution kind: user, person, url, file, channel, thread, or note.
     */
    source_type?: string;
    /**
     * Attribution reference (URL, path, channel, thread, or source note).
     */
    source_ref?: string;
    /**
     * Same-vault links (wiki [[ ]] targets).
     */
    related?: string[];
    /**
     * Cross-vault references in "Vault Name::relative/path.md" form.
     */
    related_vault_notes?: string[];
    /**
     * Whether Smart RAG should index the note.
     */
    embed?: boolean;
    /**
     * Embedding priority.
     */
    embed_priority?: "low" | "normal" | "high";
    /**
     * Optional retrieval-specific summary.
     */
    embedding_summary?: string;
    /**
     * Note type from the target vault contract (also used to route the note).
     */
    type?: string;
    /**
     * Domain folder for Library/Knowledge (AI, SEO, Copywriting & Ads, Business, Spirituality).
     */
    domain?: string;
    /**
     * Explicit sub-folder within the vault; overrides routing-derived folder.
     */
    folder?: string;
    /**
     * Channel messages only: the path of the top-level message this is a reply to. Absent on top-level messages.
     */
    parentMessageId?: string;
  };
  /**
   * Revision the edit is based on (from a prior get/put). When provided, the write only applies if the note is still at this revision; otherwise it is rejected as a conflict instead of silently overwriting a concurrent edit. Omit for last-write-wins (fine for solo notes).
   */
  baseRevision?: number;
}

export interface Output {
  /**
   * True when the note was stored; false on auth/scope error, empty content, or a revision conflict.
   */
  ok: boolean;
  /**
   * The stored note metadata. Present when ok is true.
   */
  note?: {
    /**
     * Vault-relative path the note was stored at.
     */
    path: string;
    /**
     * Stored note title.
     */
    title: string;
    /**
     * ISO-8601 timestamp of the write.
     */
    updatedAt: string;
    /**
     * New revision number after this write. Pass this as baseRevision on the next edit.
     */
    revision: number;
  };
  /**
   * Number of search chunks indexed for the content (0 if embedding failed but the note still saved).
   */
  indexed?: number;
  /**
   * True when baseRevision did not match the current revision: someone else changed the note first. No write happened.
   */
  conflict?: boolean;
  /**
   * Present only when conflict is true: the note as it stands now, so the caller can reconcile and retry without another round trip.
   */
  current?: {
    /**
     * The note as it currently stands (so a re-read is unnecessary).
     */
    content: string;
    /**
     * Current revision. Use this as the new baseRevision after reconciling.
     */
    revision: number;
    /**
     * Identity that made the conflicting write.
     */
    updatedBy: string | null;
    /**
     * When the conflicting write happened.
     */
    updatedAt: string;
  };
  /**
   * Machine-readable denial code when ok is false: quota_exceeded, free_cost_cap, or revision_conflict.
   */
  code?: string;
  /**
   * Human-readable failure reason when ok is false.
   */
  error?: string;
}
