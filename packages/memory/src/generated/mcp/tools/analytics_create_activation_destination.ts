export interface Input {
  siteId: string;
  platform: "meta" | "google" | "tiktok" | "reddit";
  name: string;
  connectionRef?: string;
  externalDatasetId?: string;
}

export interface Output {
  ok: boolean;
}
