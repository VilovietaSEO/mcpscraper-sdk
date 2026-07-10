export interface Input {
  /**
   * Vault to delete from. Optional; defaults to the session active vault, then the first vault the caller is entitled to.
   */
  vault?: string;
  /**
   * Exact vault-relative note path to delete, e.g. projects/q3-plan (as returned by memory-list or recall). Required unless shareId is given.
   */
  path?: string;
  /**
   * Destroy a note shared with you and you accepted, by its shareId, instead of vault+path. Requires the share to grant delete permission and baseRevision (mandatory for shared notes).
   */
  shareId?: string;
  /**
   * Revision the delete is based on (from a prior get). When provided, the delete only applies if the note is still at this revision; otherwise it is rejected as a conflict instead of destroying a concurrent edit. Mandatory when shareId is given; optional otherwise (omit to delete unconditionally).
   */
  baseRevision?: number;
}

export interface Output {
  /**
   * True when the delete request was processed; false on an auth/scope/lookup error or a revision conflict.
   */
  ok: boolean;
  /**
   * The vault the delete was applied to (after defaulting). Present when ok is true.
   */
  vault?: string;
  /**
   * True if a note was removed; false if no matching note existed (idempotent). Present when ok is true.
   */
  deleted?: boolean;
  /**
   * True when baseRevision did not match the current revision: someone else changed the note first. Nothing was deleted.
   */
  conflict?: boolean;
  /**
   * Present only when conflict is true: the note as it stands now, so the caller can re-read before deciding whether to still delete.
   */
  current?: {
    /**
     * The note as it currently stands.
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
   * Machine-readable denial code when ok is false: revision_conflict.
   */
  code?: string;
  /**
   * Human-readable failure reason when ok is false.
   */
  error?: string;
}
