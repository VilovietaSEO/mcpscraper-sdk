export interface Input {
  /**
   * Exact accessible Memory vault name; omit only when this tool documents a safe active-vault default.
   */
  vault?: string;
}

export interface Output {
  ok: true | false;
  projects?: {
    id: string;
    name: string;
    description: string | null;
    status: string;
    createdAt: string;
    updatedAt: string;
  }[];
  code?: string;
  error?: string;
}
