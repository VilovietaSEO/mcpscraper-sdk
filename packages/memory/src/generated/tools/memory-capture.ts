export interface Input {
  apiKey?: string;
  sessionId?: string;
  vault: string;
  folder?: string;
  path: string;
  title: string;
  content: string;
  props: {
    /**
     * Status enum value from the target vault contract.
     */
    status?: string;
    /**
     * Short retrieval-ready description.
     */
    summary?: string;
    /**
     * AI-generated keyword tags, not vault names.
     */
    tags?: string[];
    /**
     * Recall boost for important notes.
     */
    pinned?: boolean;
    /**
     * Attribution kind: user, person, url, file, channel, thread, or note.
     */
    source_type?: string;
    /**
     * Attribution reference (URL, path, channel, thread, or source note).
     */
    source_ref?: string;
    /**
     * Same-vault links (wiki [[ ]] targets).
     */
    related?: string[];
    /**
     * Cross-vault references in "Vault Name::relative/path.md" form.
     */
    related_vault_notes?: string[];
    /**
     * Whether Smart RAG should index the note.
     */
    embed?: boolean;
    /**
     * Embedding priority.
     */
    embed_priority?: "low" | "normal" | "high";
    /**
     * Optional retrieval-specific summary.
     */
    embedding_summary?: string;
    /**
     * Note type from the target vault contract (also used to route the note).
     */
    type?: string;
    /**
     * Domain folder for Library/Knowledge (AI, SEO, Copywriting & Ads, Business, Spirituality).
     */
    domain?: string;
    /**
     * Explicit sub-folder within the vault; overrides routing-derived folder.
     */
    folder?: string;
    /**
     * Skills only: one or more Obsidian/internal paths under scripts/.
     */
    script_links?: string[];
    /**
     * Skills only: optional Obsidian/internal paths under references/.
     */
    reference_links?: string[];
    /**
     * Skills only: optional Obsidian/internal paths under templates/.
     */
    template_links?: string[];
    /**
     * Channel messages only: the path of the top-level message this is a reply to. Absent on top-level messages.
     */
    parentMessageId?: string;
    [k: string]: unknown;
  };
  baseRevision?: number;
  /**
   * Required justification for any tag that does not already exist. Existing exact/alias/near tags are canonicalized automatically; a new tag is accepted only when its matching decision has central=true and reusable=true.
   *
   * @maxItems 8
   */
  tagDecisions?:
    | []
    | [
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
        }
      ]
    | [
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
        },
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
        }
      ]
    | [
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
        },
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
        },
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
        }
      ]
    | [
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
        },
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
        },
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
        },
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
        }
      ]
    | [
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
        },
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
        },
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
        },
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
        },
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
        }
      ]
    | [
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
        },
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
        },
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
        },
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
        },
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
        },
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
        }
      ]
    | [
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
        },
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
        },
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
        },
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
        },
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
        },
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
        },
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
        }
      ]
    | [
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
        },
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
        },
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
        },
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
        },
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
        },
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
        },
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
        },
        {
          tag: string;
          central: boolean;
          reusable: boolean;
          description?: string;
        }
      ];
}

export interface Output {
  ok: boolean;
  valid?: boolean;
  errors?: string[];
  warnings?: string[];
  tagResolutions?: {
    candidate: string;
    action: "reuse" | "create" | "omit";
    tag?: string;
    reason: string;
  }[];
  note?: {
    path: string;
    title: string;
    updatedAt: string;
    revision: number;
  };
  indexed?: number;
  verified?: {
    contentBytes: number;
    propsPersisted: boolean;
    revision: number;
  };
  conflict?: boolean;
  code?: string;
  error?: string;
}
