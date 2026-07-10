export interface Input {
  vault: string;
  title: string;
  content: string;
  props: {
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
    [k: string]: unknown;
  };
}

export interface Output {
  ok: boolean;
  valid?: boolean;
  errors?: string[];
  warnings?: string[];
  normalizedTags?: string[];
  error?: string;
}
