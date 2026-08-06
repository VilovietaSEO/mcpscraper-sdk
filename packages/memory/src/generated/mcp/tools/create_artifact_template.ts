export type Input =
  | {
      presetKey: "editorial_reading_room_v1";
      name: string;
      description?: string;
      authoringInstructions: string;
      config: {
        theme: "paper" | "ink" | "warm";
        density: "comfortable" | "compact";
        showSourceRail: boolean;
        showGeneratedAt: boolean;
        brandName?: string;
      };
    }
  | {
      presetKey: "personal_authority_v1";
      name: string;
      description?: string;
      authoringInstructions: string;
      config: {
        theme: "blue" | "slate" | "monochrome";
        showGeneratedAt: boolean;
        brandName?: string;
        featureFlags: {
          navigation: boolean;
          socialLinks: boolean;
          authority: boolean;
          consultation: boolean;
          learning: boolean;
          services: boolean;
          proof: boolean;
          finalCta: boolean;
        };
      };
    }
  | {
      presetKey: "newsroom_publisher_v1";
      name: string;
      description?: string;
      authoringInstructions: string;
      config: {
        theme: "daily" | "journal" | "midnight";
        showGeneratedAt: boolean;
        showBylines: boolean;
        brandName?: string;
        featureFlags: {
          breakingTicker: boolean;
          navigation: boolean;
          leadGrid: boolean;
          latestNews: boolean;
          categorySections: boolean;
          newsletter: boolean;
          pressRoom: boolean;
          trustFooter: boolean;
        };
      };
    };

export interface Output {
  ok: boolean;
  template?: {
    templateId: string;
    name: string;
    description: string;
    currentVersionId: string;
    status: "active" | "archived";
    currentVersion?:
      | {
          templateVersionId: string;
          templateId: string;
          version: number;
          rendererVersion: 1;
          inputContractVersion: 1;
          authoringInstructions: string;
          createdAt: string;
          rendererKey: "editorial_reading_room_v1";
          config: {
            theme: "paper" | "ink" | "warm";
            density: "comfortable" | "compact";
            showSourceRail: boolean;
            showGeneratedAt: boolean;
            brandName?: string;
          };
        }
      | {
          templateVersionId: string;
          templateId: string;
          version: number;
          rendererVersion: 1;
          inputContractVersion: 1;
          authoringInstructions: string;
          createdAt: string;
          rendererKey: "personal_authority_v1";
          config: {
            theme: "blue" | "slate" | "monochrome";
            showGeneratedAt: boolean;
            brandName?: string;
            featureFlags: {
              navigation: boolean;
              socialLinks: boolean;
              authority: boolean;
              consultation: boolean;
              learning: boolean;
              services: boolean;
              proof: boolean;
              finalCta: boolean;
            };
          };
        }
      | {
          templateVersionId: string;
          templateId: string;
          version: number;
          rendererVersion: 1;
          inputContractVersion: 1;
          authoringInstructions: string;
          createdAt: string;
          rendererKey: "newsroom_publisher_v1";
          config: {
            theme: "daily" | "journal" | "midnight";
            showGeneratedAt: boolean;
            showBylines: boolean;
            brandName?: string;
            featureFlags: {
              breakingTicker: boolean;
              navigation: boolean;
              leadGrid: boolean;
              latestNews: boolean;
              categorySections: boolean;
              newsletter: boolean;
              pressRoom: boolean;
              trustFooter: boolean;
            };
          };
        };
    versions?: (
      | {
          templateVersionId: string;
          templateId: string;
          version: number;
          rendererVersion: 1;
          inputContractVersion: 1;
          authoringInstructions: string;
          createdAt: string;
          rendererKey: "editorial_reading_room_v1";
          config: {
            theme: "paper" | "ink" | "warm";
            density: "comfortable" | "compact";
            showSourceRail: boolean;
            showGeneratedAt: boolean;
            brandName?: string;
          };
        }
      | {
          templateVersionId: string;
          templateId: string;
          version: number;
          rendererVersion: 1;
          inputContractVersion: 1;
          authoringInstructions: string;
          createdAt: string;
          rendererKey: "personal_authority_v1";
          config: {
            theme: "blue" | "slate" | "monochrome";
            showGeneratedAt: boolean;
            brandName?: string;
            featureFlags: {
              navigation: boolean;
              socialLinks: boolean;
              authority: boolean;
              consultation: boolean;
              learning: boolean;
              services: boolean;
              proof: boolean;
              finalCta: boolean;
            };
          };
        }
      | {
          templateVersionId: string;
          templateId: string;
          version: number;
          rendererVersion: 1;
          inputContractVersion: 1;
          authoringInstructions: string;
          createdAt: string;
          rendererKey: "newsroom_publisher_v1";
          config: {
            theme: "daily" | "journal" | "midnight";
            showGeneratedAt: boolean;
            showBylines: boolean;
            brandName?: string;
            featureFlags: {
              breakingTicker: boolean;
              navigation: boolean;
              leadGrid: boolean;
              latestNews: boolean;
              categorySections: boolean;
              newsletter: boolean;
              pressRoom: boolean;
              trustFooter: boolean;
            };
          };
        }
    )[];
    createdAt: string;
    updatedAt: string;
  };
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
}
