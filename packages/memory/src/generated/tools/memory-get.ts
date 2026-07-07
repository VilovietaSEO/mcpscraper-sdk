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
   * Vault to read from. Optional; defaults to the session active vault, then the first vault the caller is entitled to. Ignored when shareId is given.
   */
  vault?: string;
  /**
   * Exact vault-relative note path to read, e.g. projects/q3-plan (as returned by memory-list or recall). Required unless shareId is given.
   */
  path?: string;
  /**
   * Read a note shared with you and accepted, by its shareId (from note-inbox or list-shared-with-me), instead of vault+path.
   */
  shareId?: string;
}

export interface Output {
  /**
   * True when the note was found and returned; false on error or not-found.
   */
  ok: boolean;
  /**
   * The full note. Present when ok is true.
   */
  note?: {
    /**
     * Vault-relative note path that was read.
     */
    path: string;
    /**
     * Human-readable note title.
     */
    title: string;
    /**
     * Full note body text. Wrapped as untrusted content when read via shareId; internal [[wikilinks]] to notes you have not also been given access to are rewritten to [[private note]].
     */
    content: string;
    /**
     * Note kind: note, library, capture, or decision.
     */
    kind: string;
    /**
     * Origin tag recorded when the note was created (e.g. put, upload, library:...).
     */
    source: string;
    /**
     * ISO-8601 timestamp of the note last update.
     */
    updatedAt: string;
    /**
     * ISO-8601 timestamp of when the note was first captured.
     */
    capturedAt: string;
    /**
     * Current revision number. Pass this as baseRevision when editing, so a concurrent edit by someone else is detected instead of silently overwritten.
     */
    revision: number;
    /**
     * Identity that made the last write, if known.
     */
    updatedBy: string | null;
    /**
     * Present only when read via shareId: the identity who owns and shared this note.
     */
    sharedBy?: string;
    /**
     * Advisory only, not a lock: identities who read this same note within the last ~2 minutes and may be about to edit it. Worth a heads-up to the human before you write; the real safety net is still baseRevision on the write itself.
     */
    othersEditing?: string[];
  };
  /**
   * Human-readable failure reason when ok is false (e.g. "note not found").
   */
  error?: string;
}
