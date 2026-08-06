export interface Input {
  vault?: string;
  assetId: string;
  /**
   * Must be true after the caller has confirmed deletion.
   */
  confirmDelete: true;
}

export interface Output {
  ok: true | false;
  deleted?: boolean;
  assetId?: string;
  code?: string;
  error?: string;
}
