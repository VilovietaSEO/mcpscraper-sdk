export interface Input {}

export interface Output {
  ok: boolean;
  webhooks?: {
    id: string;
    vault: string;
    label: string | null;
    createdAt: string;
  }[];
  error?: string;
}
