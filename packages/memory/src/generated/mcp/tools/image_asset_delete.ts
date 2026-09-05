export interface Input {
  /**
   * Exact accessible Memory vault name; omit only when this tool documents a safe active-vault default.
   */
  vault?: string;
  /**
   * Opaque image asset identifier returned by an image asset tool.
   */
  assetId: string;
  /**
   * Must be true after the caller has confirmed deletion.
   */
  confirmDelete: true;
}

export interface Output {
  ok: boolean;
  deleted?: boolean;
  assetId?: string;
  code?: string;
  error?: string;
}
