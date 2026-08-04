export interface Input {
  vault?: string;
  assetId: string;
  /**
   * Must be true after the caller has confirmed deletion.
   */
  confirmDelete: true;
}

export type Output = unknown
