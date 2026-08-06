export interface Input {
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
