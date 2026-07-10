export interface Input {}

export interface Output {
  /**
   * True on success; false on auth error.
   */
  ok: boolean;
  /**
   * Notes shared with you and accepted. Present when ok is true.
   */
  notes?: {
    /**
     * Pass this as shareId to memory-get/memory-put/delete-note/unlink-share.
     */
    shareId: string;
    /**
     * Identity who shared the note.
     */
    owner: string;
    /**
     * Note title.
     */
    title: string;
    /**
     * Your permissions on this note.
     */
    permissions: {
      read: boolean;
      edit: boolean;
      delete: boolean;
      reshare: boolean;
    };
    /**
     * Current revision (pass as baseRevision when editing).
     */
    revision: number;
    /**
     * Last update timestamp.
     */
    updatedAt: string;
  }[];
  /**
   * Human-readable failure reason when ok is false.
   */
  error?: string;
}
