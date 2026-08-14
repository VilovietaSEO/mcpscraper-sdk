export interface Input {
  /**
   * Exact accessible Memory vault name; omit only when this tool documents a safe active-vault default.
   */
  vault?: string;
  /**
   * Opaque image project identifier returned by an image project tool.
   */
  projectId: string;
}

export interface Output {
  ok: true | false;
  folders?: {
    id: string;
    projectId: string;
    parentId: string | null;
    name: string;
    depth: number;
    createdAt: string;
    updatedAt: string;
  }[];
  code?: string;
  error?: string;
}
