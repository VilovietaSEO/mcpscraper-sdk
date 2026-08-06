export interface Input {
  presetKey: "editorial_reading_room_v1" | "personal_authority_v1" | "newsroom_publisher_v1";
}

export interface Output {
  ok: boolean;
  example?: {
    presetKey: "editorial_reading_room_v1" | "personal_authority_v1" | "newsroom_publisher_v1";
    name: string;
    description: string;
    rendererKey: "editorial_reading_room_v1" | "personal_authority_v1" | "newsroom_publisher_v1";
    rendererVersion: 1;
    inputContractVersion: 1;
    defaultConfig:
      | {
          theme: "paper" | "ink" | "warm";
          density: "comfortable" | "compact";
          showSourceRail: boolean;
          showGeneratedAt: boolean;
          brandName?: string;
        }
      | {
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
        }
      | {
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
    recommendedAuthoringInstructions: string;
    /**
     * @minItems 1
     * @maxItems 8
     */
    previewPages:
      | [
          {
            label: string;
            url: string;
            description: string;
          }
        ]
      | [
          {
            label: string;
            url: string;
            description: string;
          },
          {
            label: string;
            url: string;
            description: string;
          }
        ]
      | [
          {
            label: string;
            url: string;
            description: string;
          },
          {
            label: string;
            url: string;
            description: string;
          },
          {
            label: string;
            url: string;
            description: string;
          }
        ]
      | [
          {
            label: string;
            url: string;
            description: string;
          },
          {
            label: string;
            url: string;
            description: string;
          },
          {
            label: string;
            url: string;
            description: string;
          },
          {
            label: string;
            url: string;
            description: string;
          }
        ]
      | [
          {
            label: string;
            url: string;
            description: string;
          },
          {
            label: string;
            url: string;
            description: string;
          },
          {
            label: string;
            url: string;
            description: string;
          },
          {
            label: string;
            url: string;
            description: string;
          },
          {
            label: string;
            url: string;
            description: string;
          }
        ]
      | [
          {
            label: string;
            url: string;
            description: string;
          },
          {
            label: string;
            url: string;
            description: string;
          },
          {
            label: string;
            url: string;
            description: string;
          },
          {
            label: string;
            url: string;
            description: string;
          },
          {
            label: string;
            url: string;
            description: string;
          },
          {
            label: string;
            url: string;
            description: string;
          }
        ]
      | [
          {
            label: string;
            url: string;
            description: string;
          },
          {
            label: string;
            url: string;
            description: string;
          },
          {
            label: string;
            url: string;
            description: string;
          },
          {
            label: string;
            url: string;
            description: string;
          },
          {
            label: string;
            url: string;
            description: string;
          },
          {
            label: string;
            url: string;
            description: string;
          },
          {
            label: string;
            url: string;
            description: string;
          }
        ]
      | [
          {
            label: string;
            url: string;
            description: string;
          },
          {
            label: string;
            url: string;
            description: string;
          },
          {
            label: string;
            url: string;
            description: string;
          },
          {
            label: string;
            url: string;
            description: string;
          },
          {
            label: string;
            url: string;
            description: string;
          },
          {
            label: string;
            url: string;
            description: string;
          },
          {
            label: string;
            url: string;
            description: string;
          },
          {
            label: string;
            url: string;
            description: string;
          }
        ];
    machineReadableExampleUrl: string;
    exampleInput: {
      [k: string]: unknown;
    };
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
