export interface Input {
  siteId: string;
  pixelId?: string;
  name: string;
  destinationUrl: string;
  source: string;
  medium: string;
  campaign: string;
  term?: string;
  content?: string;
  adGroup?: string;
  adName?: string;
  creativeId?: string;
}

export interface Output {
  ok: boolean;
}
