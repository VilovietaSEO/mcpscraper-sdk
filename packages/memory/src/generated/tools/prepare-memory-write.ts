export interface Input {
  apiKey?: string;
  sessionId?: string;
  title: string;
  content: string;
  source?: string;
  type?: string;
  vault?: string;
  /**
   * @maxItems 20
   */
  tagCandidates?:
    | []
    | [
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        }
      ]
    | [
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        }
      ]
    | [
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        }
      ]
    | [
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        }
      ]
    | [
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        }
      ]
    | [
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        }
      ]
    | [
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        }
      ]
    | [
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        }
      ]
    | [
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        }
      ]
    | [
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        }
      ]
    | [
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        }
      ]
    | [
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        }
      ]
    | [
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        }
      ]
    | [
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        }
      ]
    | [
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        }
      ]
    | [
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        }
      ]
    | [
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        }
      ]
    | [
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        }
      ]
    | [
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        }
      ]
    | [
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        }
      ];
  maxLinks?: number;
}

export interface Output {
  ok: boolean;
  route?: {
    [k: string]: unknown;
  };
  contract?: {
    [k: string]: unknown;
  };
  tagResolutions?: {
    [k: string]: unknown;
  }[];
  linkOpportunities?: {
    [k: string]: unknown;
  }[];
  instructions?: string[];
  error?: string;
}
