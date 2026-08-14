export interface Input {
  /**
   * Exact accessible Memory vault name; omit only when this tool documents a safe active-vault default.
   */
  vault?: string;
  /**
   * Opaque image project identifier returned by an image project tool.
   */
  projectId: string;
  /**
   * Parent image folder identifier; omit to create the folder at the project root.
   */
  parentId?: string;
  /**
   * Human-readable name for the record being created or updated.
   */
  name: string;
}

export interface Output {
  ok: true | false;
  folder?: {
    id: string;
    projectId: string;
    parentId: string | null;
    name: string;
    depth: number;
    createdAt: string;
  };
  code?: string;
  error?: string;
}
