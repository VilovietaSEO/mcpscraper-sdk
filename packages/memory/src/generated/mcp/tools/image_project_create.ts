export interface Input {
  /**
   * Writable logical Memory vault. Defaults to the active vault.
   */
  vault?: string;
  name: string;
  description?: string;
}

export type Output = unknown
