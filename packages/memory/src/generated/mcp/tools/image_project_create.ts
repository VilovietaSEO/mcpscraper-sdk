export interface Input {
  /**
   * Writable logical Memory vault. Defaults to the active vault.
   */
  vault?: string;
  /**
   * Human-readable name for the record being created or updated.
   */
  name: string;
  /**
   * Human-readable summary that distinguishes this record from similarly named records.
   */
  description?: string;
}

export interface Output {
  ok: true | false;
  project?: {
    id: string;
    name: string;
    description: string | null;
    createdAt: string;
  };
  code?: string;
  error?: string;
}
