export interface Input {
  vault?: string;
  projectId: string;
  parentId?: string;
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
