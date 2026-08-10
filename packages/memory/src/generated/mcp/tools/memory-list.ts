export interface Input {
  /**
   * Vault to list. Optional; defaults to the session active vault, then the first vault the caller is entitled to.
   */
  vault?: string;
  /**
   * Set true for one complete account-wide inventory across every entitled vault. Omit or set false for one vault. When true, vault is ignored and reads run sequentially to avoid backend contention.
   */
  allVaults?: boolean;
  /**
   * Filter to a single note kind. Optional; omit to list every kind in the vault.
   */
  kind?: "note" | "library" | "capture" | "decision";
  /**
   * Filter to notes tagged with any of these tags (matches the note's tags primitive). Optional; omit to not filter by tag.
   */
  tags?: string[];
}

export interface Output {
  /**
   * True when the listing succeeded; false on an auth/scope/lookup error.
   */
  ok: boolean;
  /**
   * Whether the result covers one logical vault or the whole entitled account.
   */
  scope?: "vault" | "account";
  /**
   * Account-wide mode only: true if one vault failed and vaultInventories contains only the completed prefix.
   */
  partial?: boolean;
  /**
   * The vault that was actually listed (after defaulting).
   */
  vault?: string;
  /**
   * The notes in the vault (metadata only, no content). Present when ok is true.
   */
  notes?: {
    /**
     * Vault-relative note path, e.g. projects/q3-plan.
     */
    path: string;
    /**
     * Human-readable note title.
     */
    title: string;
    /**
     * Note kind: note, library, capture, or decision.
     */
    kind: string;
    /**
     * The note's tags, if any.
     */
    tags: string[];
    /**
     * ISO-8601 timestamp of the note last update.
     */
    updatedAt: string;
  }[];
  /**
   * Sorted complete folder inventory derived from note paths, including represented nested parent folders. Present when ok is true.
   */
  folders?: string[];
  /**
   * All vaults the caller is entitled to, for choosing a different vault to list.
   */
  vaults?: string[];
  /**
   * Account-wide mode only: total notes across every completed vault inventory.
   */
  totalNotes?: number;
  /**
   * Account-wide mode only: total represented folder instances across vaults.
   */
  totalFolders?: number;
  /**
   * Account-wide mode only: complete note and folder inventories grouped by vault so paths remain unambiguous.
   */
  vaultInventories?: {
    /**
     * Exact vault handle for every note and folder in this group.
     */
    vault: string;
    noteCount: number;
    folderCount: number;
    /**
     * Every note metadata record in this vault.
     */
    notes: {
      /**
       * Vault-relative note path, e.g. projects/q3-plan.
       */
      path: string;
      /**
       * Human-readable note title.
       */
      title: string;
      /**
       * Note kind: note, library, capture, or decision.
       */
      kind: string;
      /**
       * The note's tags, if any.
       */
      tags: string[];
      /**
       * ISO-8601 timestamp of the note last update.
       */
      updatedAt: string;
    }[];
    /**
     * Every represented folder and nested parent folder in this vault.
     */
    folders: string[];
  }[];
  /**
   * Human-readable failure reason when ok is false.
   */
  error?: string;
}
