export interface Input {
  apiKey?: string;
  sessionId?: string;
  note: string;
  vault?: string;
}

export interface Output {
  ok: boolean;
  nodes?: {
    id: string;
    vault: string;
    path: string;
    title: string;
    resolved: boolean;
  }[];
  edges?: {
    source: string;
    target: string;
    type: string;
    evidence: string;
    sourceField: string;
    resolved: boolean;
  }[];
  error?: string;
}
