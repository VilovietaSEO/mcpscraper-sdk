export interface Input {
  apiKey?: string;
  sessionId?: string;
  from: string;
  to: string;
  fromVault?: string;
  toVault?: string;
  maxDepth?: number;
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
