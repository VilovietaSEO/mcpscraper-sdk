export interface Input {}

export interface Output {
  ok: boolean;
  sites: {
    id: string;
    slug: string;
    name: string;
    timezone: string;
    status: string;
    role: "viewer" | "editor" | "owner";
    pixel_count: number;
    last_event_at: string | null;
  }[];
}
