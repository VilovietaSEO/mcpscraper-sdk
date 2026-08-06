export interface Input {
  /**
   * Writable logical Memory vault. Defaults to the active vault.
   */
  vault?: string;
  name: string;
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
