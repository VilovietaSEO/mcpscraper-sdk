export interface Input {
  title: string;
  content: string;
  type?: string;
  source?: string;
}

export interface Output {
  ok: boolean;
  vault?: string;
  folder?: string;
  reason?: string;
  contract?: {
    [k: string]: unknown;
  };
  error?: string;
}
