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

export type Output =
  | {
      [k: string]: unknown;
    }
  | {
      delivery: {
        mode: "artifact";
        status: "complete" | "partial" | "unavailable";
        retainedRepresentation: "formatted-tool-result";
        sourceIsError: boolean;
        artifacts: {
          artifactId: string;
          filename: string;
          contentType: string;
          bytes: number;
          sha256: string;
          expiresAt: string;
          capabilities: string[];
          downloadUrl: string | null;
          downloadUrlExpiresAt: string | null;
          downloadState: "available" | "local" | "unavailable";
        }[];
        downloadLinksOmitted: boolean;
        scopeOmittedFields: number;
        storageFailure: {
          artifactId: string | null;
          outcome: "unknown" | "bytes-stored-metadata-pending" | "failed";
        } | null;
        nextAction: string;
      };
      preview: string;
      scope: {
        [k: string]: string | number | boolean | null;
      };
      recovery: {
        idempotencyKey?: string;
        operationId?: string;
        runId?: string;
        jobId?: string;
        operation?: {
          runId: string | null;
          idempotencyKey: string;
          state: string;
        };
      };
    };
