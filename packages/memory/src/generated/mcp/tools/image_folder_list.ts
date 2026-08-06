export interface Input {
  vault?: string;
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
