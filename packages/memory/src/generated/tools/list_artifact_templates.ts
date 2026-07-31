export interface Input {
  /**
   * Caller API key (Bearer secret). Optional when the MCP session is already authenticated.
   */
  apiKey?: string;
  /**
   * Session identifier. Optional; defaults to the current MCP session.
   */
  sessionId?: string;
  status?: "active" | "archived" | "all";
}

export type Output = {
  [k: string]: unknown;
} & {
  ok: boolean;
  presets?: {
    presetKey: "editorial_reading_room_v1";
    name: string;
    description: string;
    defaultConfig: {
      theme: "paper" | "ink" | "warm";
      density: "comfortable" | "compact";
      showSourceRail: boolean;
      showGeneratedAt: boolean;
      brandName?: string;
    };
  }[];
  templates?: {
    templateId: string;
    name: string;
    description: string;
    currentVersionId: string;
    status: "active" | "archived";
    currentVersion?: {
      templateVersionId: string;
      templateId: string;
      version: number;
      rendererKey: "editorial_reading_room_v1";
      rendererVersion: 1;
      inputContractVersion: 1;
      config: {
        theme: "paper" | "ink" | "warm";
        density: "comfortable" | "compact";
        showSourceRail: boolean;
        showGeneratedAt: boolean;
        brandName?: string;
      };
      authoringInstructions: string;
      createdAt: string;
    };
    versions?: {
      templateVersionId: string;
      templateId: string;
      version: number;
      rendererKey: "editorial_reading_room_v1";
      rendererVersion: 1;
      inputContractVersion: 1;
      config: {
        theme: "paper" | "ink" | "warm";
        density: "comfortable" | "compact";
        showSourceRail: boolean;
        showGeneratedAt: boolean;
        brandName?: string;
      };
      authoringInstructions: string;
      createdAt: string;
    }[];
    createdAt: string;
    updatedAt: string;
  }[];
  error?: string;
  errorCode?:
    | "invalid_request"
    | "not_found"
    | "conflict"
    | "template_archived"
    | "renderer_unavailable"
    | "artifact_unavailable"
    | "view_link_unavailable"
    | "internal_error";
  requestId?: string;
};
