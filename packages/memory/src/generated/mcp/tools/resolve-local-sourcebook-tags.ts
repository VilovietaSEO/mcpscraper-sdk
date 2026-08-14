export interface Input {
  /**
   * Proposed reusable directory concepts to resolve against the live vocabulary.
   *
   * @minItems 1
   * @maxItems 20
   */
  candidates:
    | [
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central?: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable?: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
        }
      ]
    | [
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central?: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable?: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
        },
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central?: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable?: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
        }
      ]
    | [
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central?: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable?: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
        },
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central?: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable?: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
        },
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central?: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable?: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
        }
      ]
    | [
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central?: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable?: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
        },
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central?: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable?: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
        },
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central?: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable?: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
        },
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central?: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable?: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
        }
      ]
    | [
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central?: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable?: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
        },
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central?: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable?: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
        },
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central?: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable?: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
        },
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central?: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable?: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
        },
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central?: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable?: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
        }
      ]
    | [
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central?: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable?: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
        },
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central?: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable?: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
        },
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central?: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable?: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
        },
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central?: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable?: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
        },
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central?: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable?: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
        },
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central?: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable?: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
        }
      ]
    | [
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central?: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable?: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
        },
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central?: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable?: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
        },
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central?: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable?: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
        },
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central?: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable?: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
        },
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central?: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable?: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
        },
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central?: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable?: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
        },
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central?: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable?: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
        }
      ]
    | [
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central?: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable?: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
        },
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central?: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable?: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
        },
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central?: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable?: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
        },
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central?: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable?: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
        },
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central?: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable?: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
        },
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central?: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable?: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
        },
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central?: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable?: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
        },
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central?: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable?: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
        }
      ]
    | [
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central?: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable?: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
        },
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central?: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable?: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
        },
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central?: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable?: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
        },
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central?: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable?: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
        },
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central?: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable?: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
        },
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central?: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable?: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
        },
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central?: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable?: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
        },
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central?: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable?: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
        },
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central?: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable?: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
        }
      ]
    | [
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central?: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable?: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
        },
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central?: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable?: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
        },
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central?: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable?: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
        },
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central?: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable?: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
        },
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central?: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable?: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
        },
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central?: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable?: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
        },
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central?: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable?: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
        },
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central?: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable?: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
        },
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central?: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable?: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
        },
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central?: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable?: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
        }
      ]
    | [
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central?: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable?: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
        },
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central?: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable?: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
        },
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central?: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable?: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
        },
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central?: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable?: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
        },
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central?: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable?: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
        },
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central?: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable?: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
        },
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central?: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable?: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
        },
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central?: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable?: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
        },
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central?: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable?: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
        },
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central?: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable?: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
        },
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central?: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable?: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
        }
      ]
    | [
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central?: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable?: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
        },
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central?: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable?: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
        },
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central?: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable?: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
        },
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central?: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable?: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
        },
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central?: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable?: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
        },
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central?: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable?: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
        },
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central?: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable?: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
        },
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central?: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable?: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
        },
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central?: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable?: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
        },
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central?: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable?: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
        },
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central?: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable?: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
        },
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central?: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable?: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
        }
      ]
    | [
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central?: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable?: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
        },
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central?: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable?: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
        },
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central?: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable?: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
        },
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central?: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable?: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
        },
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central?: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable?: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
        },
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central?: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable?: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
        },
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central?: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable?: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
        },
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central?: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable?: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
        },
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central?: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable?: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
        },
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central?: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable?: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
        },
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central?: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable?: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
        },
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central?: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable?: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
        },
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central?: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable?: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
        }
      ]
    | [
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central?: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable?: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
        },
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central?: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable?: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
        },
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central?: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable?: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
        },
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central?: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable?: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
        },
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central?: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable?: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
        },
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central?: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable?: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
        },
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central?: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable?: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
        },
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central?: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable?: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
        },
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central?: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable?: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
        },
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central?: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable?: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
        },
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central?: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable?: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
        },
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central?: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable?: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
        },
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central?: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable?: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
        },
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central?: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable?: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
        }
      ]
    | [
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central?: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable?: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
        },
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central?: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable?: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
        },
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central?: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable?: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
        },
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central?: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable?: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
        },
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central?: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable?: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
        },
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central?: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable?: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
        },
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central?: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable?: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
        },
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central?: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable?: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
        },
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central?: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable?: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
        },
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central?: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable?: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
        },
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central?: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable?: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
        },
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central?: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable?: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
        },
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central?: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable?: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
        },
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central?: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable?: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
        },
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central?: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable?: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
        }
      ]
    | [
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central?: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable?: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
        },
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central?: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable?: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
        },
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central?: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable?: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
        },
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central?: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable?: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
        },
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central?: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable?: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
        },
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central?: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable?: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
        },
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central?: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable?: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
        },
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central?: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable?: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
        },
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central?: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable?: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
        },
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central?: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable?: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
        },
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central?: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable?: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
        },
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central?: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable?: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
        },
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central?: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable?: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
        },
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central?: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable?: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
        },
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central?: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable?: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
        },
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central?: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable?: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
        }
      ]
    | [
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central?: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable?: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
        },
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central?: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable?: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
        },
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central?: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable?: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
        },
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central?: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable?: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
        },
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central?: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable?: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
        },
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central?: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable?: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
        },
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central?: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable?: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
        },
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central?: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable?: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
        },
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central?: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable?: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
        },
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central?: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable?: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
        },
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central?: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable?: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
        },
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central?: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable?: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
        },
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central?: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable?: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
        },
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central?: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable?: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
        },
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central?: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable?: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
        },
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central?: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable?: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
        },
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central?: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable?: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
        }
      ]
    | [
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central?: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable?: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
        },
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central?: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable?: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
        },
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central?: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable?: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
        },
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central?: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable?: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
        },
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central?: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable?: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
        },
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central?: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable?: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
        },
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central?: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable?: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
        },
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central?: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable?: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
        },
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central?: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable?: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
        },
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central?: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable?: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
        },
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central?: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable?: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
        },
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central?: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable?: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
        },
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central?: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable?: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
        },
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central?: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable?: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
        },
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central?: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable?: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
        },
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central?: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable?: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
        },
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central?: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable?: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
        },
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central?: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable?: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
        }
      ]
    | [
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central?: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable?: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
        },
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central?: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable?: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
        },
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central?: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable?: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
        },
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central?: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable?: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
        },
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central?: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable?: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
        },
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central?: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable?: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
        },
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central?: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable?: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
        },
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central?: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable?: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
        },
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central?: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable?: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
        },
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central?: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable?: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
        },
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central?: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable?: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
        },
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central?: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable?: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
        },
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central?: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable?: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
        },
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central?: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable?: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
        },
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central?: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable?: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
        },
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central?: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable?: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
        },
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central?: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable?: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
        },
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central?: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable?: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
        },
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central?: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable?: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
        }
      ]
    | [
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central?: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable?: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
        },
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central?: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable?: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
        },
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central?: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable?: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
        },
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central?: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable?: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
        },
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central?: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable?: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
        },
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central?: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable?: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
        },
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central?: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable?: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
        },
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central?: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable?: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
        },
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central?: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable?: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
        },
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central?: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable?: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
        },
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central?: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable?: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
        },
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central?: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable?: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
        },
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central?: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable?: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
        },
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central?: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable?: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
        },
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central?: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable?: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
        },
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central?: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable?: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
        },
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central?: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable?: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
        },
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central?: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable?: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
        },
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central?: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable?: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
        },
        {
          /**
           * Canonical tag name to create or curate.
           */
          tag: string;
          /**
           * Whether the proposed tag is central to the record rather than incidental.
           */
          central?: boolean;
          /**
           * Whether the proposed tag is useful across multiple future records.
           */
          reusable?: boolean;
          /**
           * Human-readable summary that distinguishes this record from similarly named records.
           */
          description?: string;
        }
      ];
}

export interface Output {
  [k: string]: unknown;
}
