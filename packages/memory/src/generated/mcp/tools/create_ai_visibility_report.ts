export interface Input {
  /**
   * Report title shown at the top of the page.
   */
  title?: string;
  /**
   * The brand this report is about.
   */
  brand: {
    /**
     * The tracked brand, exactly as it was matched in the answers.
     */
    name: string;
    /**
     * The tracked brand's website domain, for example "example.com".
     */
    domain?: string;
    /**
     * The tracked brand's logo. Public https image.
     */
    logoUrl?: string;
    /**
     * Hex colour for the brand in every chart, for example "#1f5fbf". Too-pale colours are darkened.
     */
    accentColor?: string;
  };
  /**
   * Client or team the report is prepared for.
   */
  preparedFor?: string;
  /**
   * Who presents the report (white-label).
   */
  preparedBy?: {
    /**
     * Agency or person presenting the report.
     */
    name: string;
    /**
     * The presenter's logo. Public https image.
     */
    logoUrl?: string;
  };
  /**
   * The period the measures cover.
   */
  period: {
    /**
     * Period shown under the title, for example "1 to 30 September 2026".
     */
    label: string;
    /**
     * First day covered, as an ISO date.
     */
    from?: string;
    /**
     * Last day covered, as an ISO date.
     */
    to?: string;
  };
  /**
   * Headline measures. The only required section.
   */
  summary: {
    /**
     * Successful answers that named the brand, percent 0-100.
     */
    visibilityPct: number;
    /**
     * Number of successful answers that named the brand.
     */
    answersNamed: number;
    /**
     * Successful answers behind the headline. Excludes failed runs.
     */
    answersTotal: number;
    /**
     * Change against the previous period, in points. Omit without a previous period.
     */
    visibilityChangePts?: number;
    /**
     * Brand mentions divided by all tracked brands' mentions, percent 0-100.
     */
    shareOfVoicePct?: number;
    /**
     * Rank by share of voice; 1 is highest.
     */
    shareRank?: number;
    /**
     * Brands tracked, including this one.
     */
    brandsTracked?: number;
    /**
     * Runs that failed and were left out of every figure.
     */
    failedRuns?: number;
  };
  /**
   * Visibility for each assistant.
   *
   * @maxItems 12
   */
  byAssistant?:
    | []
    | [
        {
          /**
           * Assistant name, for example "ChatGPT", "Gemini" or "Claude".
           */
          assistant: string;
          /**
           * This assistant's answers naming the brand, percent 0-100.
           */
          visibilityPct: number;
          /**
           * Successful answers from this assistant.
           */
          answersTotal: number;
        }
      ]
    | [
        {
          /**
           * Assistant name, for example "ChatGPT", "Gemini" or "Claude".
           */
          assistant: string;
          /**
           * This assistant's answers naming the brand, percent 0-100.
           */
          visibilityPct: number;
          /**
           * Successful answers from this assistant.
           */
          answersTotal: number;
        },
        {
          /**
           * Assistant name, for example "ChatGPT", "Gemini" or "Claude".
           */
          assistant: string;
          /**
           * This assistant's answers naming the brand, percent 0-100.
           */
          visibilityPct: number;
          /**
           * Successful answers from this assistant.
           */
          answersTotal: number;
        }
      ]
    | [
        {
          /**
           * Assistant name, for example "ChatGPT", "Gemini" or "Claude".
           */
          assistant: string;
          /**
           * This assistant's answers naming the brand, percent 0-100.
           */
          visibilityPct: number;
          /**
           * Successful answers from this assistant.
           */
          answersTotal: number;
        },
        {
          /**
           * Assistant name, for example "ChatGPT", "Gemini" or "Claude".
           */
          assistant: string;
          /**
           * This assistant's answers naming the brand, percent 0-100.
           */
          visibilityPct: number;
          /**
           * Successful answers from this assistant.
           */
          answersTotal: number;
        },
        {
          /**
           * Assistant name, for example "ChatGPT", "Gemini" or "Claude".
           */
          assistant: string;
          /**
           * This assistant's answers naming the brand, percent 0-100.
           */
          visibilityPct: number;
          /**
           * Successful answers from this assistant.
           */
          answersTotal: number;
        }
      ]
    | [
        {
          /**
           * Assistant name, for example "ChatGPT", "Gemini" or "Claude".
           */
          assistant: string;
          /**
           * This assistant's answers naming the brand, percent 0-100.
           */
          visibilityPct: number;
          /**
           * Successful answers from this assistant.
           */
          answersTotal: number;
        },
        {
          /**
           * Assistant name, for example "ChatGPT", "Gemini" or "Claude".
           */
          assistant: string;
          /**
           * This assistant's answers naming the brand, percent 0-100.
           */
          visibilityPct: number;
          /**
           * Successful answers from this assistant.
           */
          answersTotal: number;
        },
        {
          /**
           * Assistant name, for example "ChatGPT", "Gemini" or "Claude".
           */
          assistant: string;
          /**
           * This assistant's answers naming the brand, percent 0-100.
           */
          visibilityPct: number;
          /**
           * Successful answers from this assistant.
           */
          answersTotal: number;
        },
        {
          /**
           * Assistant name, for example "ChatGPT", "Gemini" or "Claude".
           */
          assistant: string;
          /**
           * This assistant's answers naming the brand, percent 0-100.
           */
          visibilityPct: number;
          /**
           * Successful answers from this assistant.
           */
          answersTotal: number;
        }
      ]
    | [
        {
          /**
           * Assistant name, for example "ChatGPT", "Gemini" or "Claude".
           */
          assistant: string;
          /**
           * This assistant's answers naming the brand, percent 0-100.
           */
          visibilityPct: number;
          /**
           * Successful answers from this assistant.
           */
          answersTotal: number;
        },
        {
          /**
           * Assistant name, for example "ChatGPT", "Gemini" or "Claude".
           */
          assistant: string;
          /**
           * This assistant's answers naming the brand, percent 0-100.
           */
          visibilityPct: number;
          /**
           * Successful answers from this assistant.
           */
          answersTotal: number;
        },
        {
          /**
           * Assistant name, for example "ChatGPT", "Gemini" or "Claude".
           */
          assistant: string;
          /**
           * This assistant's answers naming the brand, percent 0-100.
           */
          visibilityPct: number;
          /**
           * Successful answers from this assistant.
           */
          answersTotal: number;
        },
        {
          /**
           * Assistant name, for example "ChatGPT", "Gemini" or "Claude".
           */
          assistant: string;
          /**
           * This assistant's answers naming the brand, percent 0-100.
           */
          visibilityPct: number;
          /**
           * Successful answers from this assistant.
           */
          answersTotal: number;
        },
        {
          /**
           * Assistant name, for example "ChatGPT", "Gemini" or "Claude".
           */
          assistant: string;
          /**
           * This assistant's answers naming the brand, percent 0-100.
           */
          visibilityPct: number;
          /**
           * Successful answers from this assistant.
           */
          answersTotal: number;
        }
      ]
    | [
        {
          /**
           * Assistant name, for example "ChatGPT", "Gemini" or "Claude".
           */
          assistant: string;
          /**
           * This assistant's answers naming the brand, percent 0-100.
           */
          visibilityPct: number;
          /**
           * Successful answers from this assistant.
           */
          answersTotal: number;
        },
        {
          /**
           * Assistant name, for example "ChatGPT", "Gemini" or "Claude".
           */
          assistant: string;
          /**
           * This assistant's answers naming the brand, percent 0-100.
           */
          visibilityPct: number;
          /**
           * Successful answers from this assistant.
           */
          answersTotal: number;
        },
        {
          /**
           * Assistant name, for example "ChatGPT", "Gemini" or "Claude".
           */
          assistant: string;
          /**
           * This assistant's answers naming the brand, percent 0-100.
           */
          visibilityPct: number;
          /**
           * Successful answers from this assistant.
           */
          answersTotal: number;
        },
        {
          /**
           * Assistant name, for example "ChatGPT", "Gemini" or "Claude".
           */
          assistant: string;
          /**
           * This assistant's answers naming the brand, percent 0-100.
           */
          visibilityPct: number;
          /**
           * Successful answers from this assistant.
           */
          answersTotal: number;
        },
        {
          /**
           * Assistant name, for example "ChatGPT", "Gemini" or "Claude".
           */
          assistant: string;
          /**
           * This assistant's answers naming the brand, percent 0-100.
           */
          visibilityPct: number;
          /**
           * Successful answers from this assistant.
           */
          answersTotal: number;
        },
        {
          /**
           * Assistant name, for example "ChatGPT", "Gemini" or "Claude".
           */
          assistant: string;
          /**
           * This assistant's answers naming the brand, percent 0-100.
           */
          visibilityPct: number;
          /**
           * Successful answers from this assistant.
           */
          answersTotal: number;
        }
      ]
    | [
        {
          /**
           * Assistant name, for example "ChatGPT", "Gemini" or "Claude".
           */
          assistant: string;
          /**
           * This assistant's answers naming the brand, percent 0-100.
           */
          visibilityPct: number;
          /**
           * Successful answers from this assistant.
           */
          answersTotal: number;
        },
        {
          /**
           * Assistant name, for example "ChatGPT", "Gemini" or "Claude".
           */
          assistant: string;
          /**
           * This assistant's answers naming the brand, percent 0-100.
           */
          visibilityPct: number;
          /**
           * Successful answers from this assistant.
           */
          answersTotal: number;
        },
        {
          /**
           * Assistant name, for example "ChatGPT", "Gemini" or "Claude".
           */
          assistant: string;
          /**
           * This assistant's answers naming the brand, percent 0-100.
           */
          visibilityPct: number;
          /**
           * Successful answers from this assistant.
           */
          answersTotal: number;
        },
        {
          /**
           * Assistant name, for example "ChatGPT", "Gemini" or "Claude".
           */
          assistant: string;
          /**
           * This assistant's answers naming the brand, percent 0-100.
           */
          visibilityPct: number;
          /**
           * Successful answers from this assistant.
           */
          answersTotal: number;
        },
        {
          /**
           * Assistant name, for example "ChatGPT", "Gemini" or "Claude".
           */
          assistant: string;
          /**
           * This assistant's answers naming the brand, percent 0-100.
           */
          visibilityPct: number;
          /**
           * Successful answers from this assistant.
           */
          answersTotal: number;
        },
        {
          /**
           * Assistant name, for example "ChatGPT", "Gemini" or "Claude".
           */
          assistant: string;
          /**
           * This assistant's answers naming the brand, percent 0-100.
           */
          visibilityPct: number;
          /**
           * Successful answers from this assistant.
           */
          answersTotal: number;
        },
        {
          /**
           * Assistant name, for example "ChatGPT", "Gemini" or "Claude".
           */
          assistant: string;
          /**
           * This assistant's answers naming the brand, percent 0-100.
           */
          visibilityPct: number;
          /**
           * Successful answers from this assistant.
           */
          answersTotal: number;
        }
      ]
    | [
        {
          /**
           * Assistant name, for example "ChatGPT", "Gemini" or "Claude".
           */
          assistant: string;
          /**
           * This assistant's answers naming the brand, percent 0-100.
           */
          visibilityPct: number;
          /**
           * Successful answers from this assistant.
           */
          answersTotal: number;
        },
        {
          /**
           * Assistant name, for example "ChatGPT", "Gemini" or "Claude".
           */
          assistant: string;
          /**
           * This assistant's answers naming the brand, percent 0-100.
           */
          visibilityPct: number;
          /**
           * Successful answers from this assistant.
           */
          answersTotal: number;
        },
        {
          /**
           * Assistant name, for example "ChatGPT", "Gemini" or "Claude".
           */
          assistant: string;
          /**
           * This assistant's answers naming the brand, percent 0-100.
           */
          visibilityPct: number;
          /**
           * Successful answers from this assistant.
           */
          answersTotal: number;
        },
        {
          /**
           * Assistant name, for example "ChatGPT", "Gemini" or "Claude".
           */
          assistant: string;
          /**
           * This assistant's answers naming the brand, percent 0-100.
           */
          visibilityPct: number;
          /**
           * Successful answers from this assistant.
           */
          answersTotal: number;
        },
        {
          /**
           * Assistant name, for example "ChatGPT", "Gemini" or "Claude".
           */
          assistant: string;
          /**
           * This assistant's answers naming the brand, percent 0-100.
           */
          visibilityPct: number;
          /**
           * Successful answers from this assistant.
           */
          answersTotal: number;
        },
        {
          /**
           * Assistant name, for example "ChatGPT", "Gemini" or "Claude".
           */
          assistant: string;
          /**
           * This assistant's answers naming the brand, percent 0-100.
           */
          visibilityPct: number;
          /**
           * Successful answers from this assistant.
           */
          answersTotal: number;
        },
        {
          /**
           * Assistant name, for example "ChatGPT", "Gemini" or "Claude".
           */
          assistant: string;
          /**
           * This assistant's answers naming the brand, percent 0-100.
           */
          visibilityPct: number;
          /**
           * Successful answers from this assistant.
           */
          answersTotal: number;
        },
        {
          /**
           * Assistant name, for example "ChatGPT", "Gemini" or "Claude".
           */
          assistant: string;
          /**
           * This assistant's answers naming the brand, percent 0-100.
           */
          visibilityPct: number;
          /**
           * Successful answers from this assistant.
           */
          answersTotal: number;
        }
      ]
    | [
        {
          /**
           * Assistant name, for example "ChatGPT", "Gemini" or "Claude".
           */
          assistant: string;
          /**
           * This assistant's answers naming the brand, percent 0-100.
           */
          visibilityPct: number;
          /**
           * Successful answers from this assistant.
           */
          answersTotal: number;
        },
        {
          /**
           * Assistant name, for example "ChatGPT", "Gemini" or "Claude".
           */
          assistant: string;
          /**
           * This assistant's answers naming the brand, percent 0-100.
           */
          visibilityPct: number;
          /**
           * Successful answers from this assistant.
           */
          answersTotal: number;
        },
        {
          /**
           * Assistant name, for example "ChatGPT", "Gemini" or "Claude".
           */
          assistant: string;
          /**
           * This assistant's answers naming the brand, percent 0-100.
           */
          visibilityPct: number;
          /**
           * Successful answers from this assistant.
           */
          answersTotal: number;
        },
        {
          /**
           * Assistant name, for example "ChatGPT", "Gemini" or "Claude".
           */
          assistant: string;
          /**
           * This assistant's answers naming the brand, percent 0-100.
           */
          visibilityPct: number;
          /**
           * Successful answers from this assistant.
           */
          answersTotal: number;
        },
        {
          /**
           * Assistant name, for example "ChatGPT", "Gemini" or "Claude".
           */
          assistant: string;
          /**
           * This assistant's answers naming the brand, percent 0-100.
           */
          visibilityPct: number;
          /**
           * Successful answers from this assistant.
           */
          answersTotal: number;
        },
        {
          /**
           * Assistant name, for example "ChatGPT", "Gemini" or "Claude".
           */
          assistant: string;
          /**
           * This assistant's answers naming the brand, percent 0-100.
           */
          visibilityPct: number;
          /**
           * Successful answers from this assistant.
           */
          answersTotal: number;
        },
        {
          /**
           * Assistant name, for example "ChatGPT", "Gemini" or "Claude".
           */
          assistant: string;
          /**
           * This assistant's answers naming the brand, percent 0-100.
           */
          visibilityPct: number;
          /**
           * Successful answers from this assistant.
           */
          answersTotal: number;
        },
        {
          /**
           * Assistant name, for example "ChatGPT", "Gemini" or "Claude".
           */
          assistant: string;
          /**
           * This assistant's answers naming the brand, percent 0-100.
           */
          visibilityPct: number;
          /**
           * Successful answers from this assistant.
           */
          answersTotal: number;
        },
        {
          /**
           * Assistant name, for example "ChatGPT", "Gemini" or "Claude".
           */
          assistant: string;
          /**
           * This assistant's answers naming the brand, percent 0-100.
           */
          visibilityPct: number;
          /**
           * Successful answers from this assistant.
           */
          answersTotal: number;
        }
      ]
    | [
        {
          /**
           * Assistant name, for example "ChatGPT", "Gemini" or "Claude".
           */
          assistant: string;
          /**
           * This assistant's answers naming the brand, percent 0-100.
           */
          visibilityPct: number;
          /**
           * Successful answers from this assistant.
           */
          answersTotal: number;
        },
        {
          /**
           * Assistant name, for example "ChatGPT", "Gemini" or "Claude".
           */
          assistant: string;
          /**
           * This assistant's answers naming the brand, percent 0-100.
           */
          visibilityPct: number;
          /**
           * Successful answers from this assistant.
           */
          answersTotal: number;
        },
        {
          /**
           * Assistant name, for example "ChatGPT", "Gemini" or "Claude".
           */
          assistant: string;
          /**
           * This assistant's answers naming the brand, percent 0-100.
           */
          visibilityPct: number;
          /**
           * Successful answers from this assistant.
           */
          answersTotal: number;
        },
        {
          /**
           * Assistant name, for example "ChatGPT", "Gemini" or "Claude".
           */
          assistant: string;
          /**
           * This assistant's answers naming the brand, percent 0-100.
           */
          visibilityPct: number;
          /**
           * Successful answers from this assistant.
           */
          answersTotal: number;
        },
        {
          /**
           * Assistant name, for example "ChatGPT", "Gemini" or "Claude".
           */
          assistant: string;
          /**
           * This assistant's answers naming the brand, percent 0-100.
           */
          visibilityPct: number;
          /**
           * Successful answers from this assistant.
           */
          answersTotal: number;
        },
        {
          /**
           * Assistant name, for example "ChatGPT", "Gemini" or "Claude".
           */
          assistant: string;
          /**
           * This assistant's answers naming the brand, percent 0-100.
           */
          visibilityPct: number;
          /**
           * Successful answers from this assistant.
           */
          answersTotal: number;
        },
        {
          /**
           * Assistant name, for example "ChatGPT", "Gemini" or "Claude".
           */
          assistant: string;
          /**
           * This assistant's answers naming the brand, percent 0-100.
           */
          visibilityPct: number;
          /**
           * Successful answers from this assistant.
           */
          answersTotal: number;
        },
        {
          /**
           * Assistant name, for example "ChatGPT", "Gemini" or "Claude".
           */
          assistant: string;
          /**
           * This assistant's answers naming the brand, percent 0-100.
           */
          visibilityPct: number;
          /**
           * Successful answers from this assistant.
           */
          answersTotal: number;
        },
        {
          /**
           * Assistant name, for example "ChatGPT", "Gemini" or "Claude".
           */
          assistant: string;
          /**
           * This assistant's answers naming the brand, percent 0-100.
           */
          visibilityPct: number;
          /**
           * Successful answers from this assistant.
           */
          answersTotal: number;
        },
        {
          /**
           * Assistant name, for example "ChatGPT", "Gemini" or "Claude".
           */
          assistant: string;
          /**
           * This assistant's answers naming the brand, percent 0-100.
           */
          visibilityPct: number;
          /**
           * Successful answers from this assistant.
           */
          answersTotal: number;
        }
      ]
    | [
        {
          /**
           * Assistant name, for example "ChatGPT", "Gemini" or "Claude".
           */
          assistant: string;
          /**
           * This assistant's answers naming the brand, percent 0-100.
           */
          visibilityPct: number;
          /**
           * Successful answers from this assistant.
           */
          answersTotal: number;
        },
        {
          /**
           * Assistant name, for example "ChatGPT", "Gemini" or "Claude".
           */
          assistant: string;
          /**
           * This assistant's answers naming the brand, percent 0-100.
           */
          visibilityPct: number;
          /**
           * Successful answers from this assistant.
           */
          answersTotal: number;
        },
        {
          /**
           * Assistant name, for example "ChatGPT", "Gemini" or "Claude".
           */
          assistant: string;
          /**
           * This assistant's answers naming the brand, percent 0-100.
           */
          visibilityPct: number;
          /**
           * Successful answers from this assistant.
           */
          answersTotal: number;
        },
        {
          /**
           * Assistant name, for example "ChatGPT", "Gemini" or "Claude".
           */
          assistant: string;
          /**
           * This assistant's answers naming the brand, percent 0-100.
           */
          visibilityPct: number;
          /**
           * Successful answers from this assistant.
           */
          answersTotal: number;
        },
        {
          /**
           * Assistant name, for example "ChatGPT", "Gemini" or "Claude".
           */
          assistant: string;
          /**
           * This assistant's answers naming the brand, percent 0-100.
           */
          visibilityPct: number;
          /**
           * Successful answers from this assistant.
           */
          answersTotal: number;
        },
        {
          /**
           * Assistant name, for example "ChatGPT", "Gemini" or "Claude".
           */
          assistant: string;
          /**
           * This assistant's answers naming the brand, percent 0-100.
           */
          visibilityPct: number;
          /**
           * Successful answers from this assistant.
           */
          answersTotal: number;
        },
        {
          /**
           * Assistant name, for example "ChatGPT", "Gemini" or "Claude".
           */
          assistant: string;
          /**
           * This assistant's answers naming the brand, percent 0-100.
           */
          visibilityPct: number;
          /**
           * Successful answers from this assistant.
           */
          answersTotal: number;
        },
        {
          /**
           * Assistant name, for example "ChatGPT", "Gemini" or "Claude".
           */
          assistant: string;
          /**
           * This assistant's answers naming the brand, percent 0-100.
           */
          visibilityPct: number;
          /**
           * Successful answers from this assistant.
           */
          answersTotal: number;
        },
        {
          /**
           * Assistant name, for example "ChatGPT", "Gemini" or "Claude".
           */
          assistant: string;
          /**
           * This assistant's answers naming the brand, percent 0-100.
           */
          visibilityPct: number;
          /**
           * Successful answers from this assistant.
           */
          answersTotal: number;
        },
        {
          /**
           * Assistant name, for example "ChatGPT", "Gemini" or "Claude".
           */
          assistant: string;
          /**
           * This assistant's answers naming the brand, percent 0-100.
           */
          visibilityPct: number;
          /**
           * Successful answers from this assistant.
           */
          answersTotal: number;
        },
        {
          /**
           * Assistant name, for example "ChatGPT", "Gemini" or "Claude".
           */
          assistant: string;
          /**
           * This assistant's answers naming the brand, percent 0-100.
           */
          visibilityPct: number;
          /**
           * Successful answers from this assistant.
           */
          answersTotal: number;
        }
      ]
    | [
        {
          /**
           * Assistant name, for example "ChatGPT", "Gemini" or "Claude".
           */
          assistant: string;
          /**
           * This assistant's answers naming the brand, percent 0-100.
           */
          visibilityPct: number;
          /**
           * Successful answers from this assistant.
           */
          answersTotal: number;
        },
        {
          /**
           * Assistant name, for example "ChatGPT", "Gemini" or "Claude".
           */
          assistant: string;
          /**
           * This assistant's answers naming the brand, percent 0-100.
           */
          visibilityPct: number;
          /**
           * Successful answers from this assistant.
           */
          answersTotal: number;
        },
        {
          /**
           * Assistant name, for example "ChatGPT", "Gemini" or "Claude".
           */
          assistant: string;
          /**
           * This assistant's answers naming the brand, percent 0-100.
           */
          visibilityPct: number;
          /**
           * Successful answers from this assistant.
           */
          answersTotal: number;
        },
        {
          /**
           * Assistant name, for example "ChatGPT", "Gemini" or "Claude".
           */
          assistant: string;
          /**
           * This assistant's answers naming the brand, percent 0-100.
           */
          visibilityPct: number;
          /**
           * Successful answers from this assistant.
           */
          answersTotal: number;
        },
        {
          /**
           * Assistant name, for example "ChatGPT", "Gemini" or "Claude".
           */
          assistant: string;
          /**
           * This assistant's answers naming the brand, percent 0-100.
           */
          visibilityPct: number;
          /**
           * Successful answers from this assistant.
           */
          answersTotal: number;
        },
        {
          /**
           * Assistant name, for example "ChatGPT", "Gemini" or "Claude".
           */
          assistant: string;
          /**
           * This assistant's answers naming the brand, percent 0-100.
           */
          visibilityPct: number;
          /**
           * Successful answers from this assistant.
           */
          answersTotal: number;
        },
        {
          /**
           * Assistant name, for example "ChatGPT", "Gemini" or "Claude".
           */
          assistant: string;
          /**
           * This assistant's answers naming the brand, percent 0-100.
           */
          visibilityPct: number;
          /**
           * Successful answers from this assistant.
           */
          answersTotal: number;
        },
        {
          /**
           * Assistant name, for example "ChatGPT", "Gemini" or "Claude".
           */
          assistant: string;
          /**
           * This assistant's answers naming the brand, percent 0-100.
           */
          visibilityPct: number;
          /**
           * Successful answers from this assistant.
           */
          answersTotal: number;
        },
        {
          /**
           * Assistant name, for example "ChatGPT", "Gemini" or "Claude".
           */
          assistant: string;
          /**
           * This assistant's answers naming the brand, percent 0-100.
           */
          visibilityPct: number;
          /**
           * Successful answers from this assistant.
           */
          answersTotal: number;
        },
        {
          /**
           * Assistant name, for example "ChatGPT", "Gemini" or "Claude".
           */
          assistant: string;
          /**
           * This assistant's answers naming the brand, percent 0-100.
           */
          visibilityPct: number;
          /**
           * Successful answers from this assistant.
           */
          answersTotal: number;
        },
        {
          /**
           * Assistant name, for example "ChatGPT", "Gemini" or "Claude".
           */
          assistant: string;
          /**
           * This assistant's answers naming the brand, percent 0-100.
           */
          visibilityPct: number;
          /**
           * Successful answers from this assistant.
           */
          answersTotal: number;
        },
        {
          /**
           * Assistant name, for example "ChatGPT", "Gemini" or "Claude".
           */
          assistant: string;
          /**
           * This assistant's answers naming the brand, percent 0-100.
           */
          visibilityPct: number;
          /**
           * Successful answers from this assistant.
           */
          answersTotal: number;
        }
      ];
  /**
   * Visibility over time, oldest first; two points minimum.
   *
   * @maxItems 120
   */
  trend?: {
    /**
     * Axis label, for example "7 Sep".
     */
    date: string;
    /**
     * The brand's visibility at this point, percent 0-100.
     */
    brandPct: number;
    /**
     * Successful answers behind this point.
     */
    answersTotal?: number;
    /**
     * Competitor visibility at this point.
     *
     * @maxItems 8
     */
    competitors?:
      | []
      | [
          {
            /**
             * Competitor name, spelled the same everywhere.
             */
            name: string;
            /**
             * Answers naming this competitor, percent 0-100.
             */
            pct: number;
          }
        ]
      | [
          {
            /**
             * Competitor name, spelled the same everywhere.
             */
            name: string;
            /**
             * Answers naming this competitor, percent 0-100.
             */
            pct: number;
          },
          {
            /**
             * Competitor name, spelled the same everywhere.
             */
            name: string;
            /**
             * Answers naming this competitor, percent 0-100.
             */
            pct: number;
          }
        ]
      | [
          {
            /**
             * Competitor name, spelled the same everywhere.
             */
            name: string;
            /**
             * Answers naming this competitor, percent 0-100.
             */
            pct: number;
          },
          {
            /**
             * Competitor name, spelled the same everywhere.
             */
            name: string;
            /**
             * Answers naming this competitor, percent 0-100.
             */
            pct: number;
          },
          {
            /**
             * Competitor name, spelled the same everywhere.
             */
            name: string;
            /**
             * Answers naming this competitor, percent 0-100.
             */
            pct: number;
          }
        ]
      | [
          {
            /**
             * Competitor name, spelled the same everywhere.
             */
            name: string;
            /**
             * Answers naming this competitor, percent 0-100.
             */
            pct: number;
          },
          {
            /**
             * Competitor name, spelled the same everywhere.
             */
            name: string;
            /**
             * Answers naming this competitor, percent 0-100.
             */
            pct: number;
          },
          {
            /**
             * Competitor name, spelled the same everywhere.
             */
            name: string;
            /**
             * Answers naming this competitor, percent 0-100.
             */
            pct: number;
          },
          {
            /**
             * Competitor name, spelled the same everywhere.
             */
            name: string;
            /**
             * Answers naming this competitor, percent 0-100.
             */
            pct: number;
          }
        ]
      | [
          {
            /**
             * Competitor name, spelled the same everywhere.
             */
            name: string;
            /**
             * Answers naming this competitor, percent 0-100.
             */
            pct: number;
          },
          {
            /**
             * Competitor name, spelled the same everywhere.
             */
            name: string;
            /**
             * Answers naming this competitor, percent 0-100.
             */
            pct: number;
          },
          {
            /**
             * Competitor name, spelled the same everywhere.
             */
            name: string;
            /**
             * Answers naming this competitor, percent 0-100.
             */
            pct: number;
          },
          {
            /**
             * Competitor name, spelled the same everywhere.
             */
            name: string;
            /**
             * Answers naming this competitor, percent 0-100.
             */
            pct: number;
          },
          {
            /**
             * Competitor name, spelled the same everywhere.
             */
            name: string;
            /**
             * Answers naming this competitor, percent 0-100.
             */
            pct: number;
          }
        ]
      | [
          {
            /**
             * Competitor name, spelled the same everywhere.
             */
            name: string;
            /**
             * Answers naming this competitor, percent 0-100.
             */
            pct: number;
          },
          {
            /**
             * Competitor name, spelled the same everywhere.
             */
            name: string;
            /**
             * Answers naming this competitor, percent 0-100.
             */
            pct: number;
          },
          {
            /**
             * Competitor name, spelled the same everywhere.
             */
            name: string;
            /**
             * Answers naming this competitor, percent 0-100.
             */
            pct: number;
          },
          {
            /**
             * Competitor name, spelled the same everywhere.
             */
            name: string;
            /**
             * Answers naming this competitor, percent 0-100.
             */
            pct: number;
          },
          {
            /**
             * Competitor name, spelled the same everywhere.
             */
            name: string;
            /**
             * Answers naming this competitor, percent 0-100.
             */
            pct: number;
          },
          {
            /**
             * Competitor name, spelled the same everywhere.
             */
            name: string;
            /**
             * Answers naming this competitor, percent 0-100.
             */
            pct: number;
          }
        ]
      | [
          {
            /**
             * Competitor name, spelled the same everywhere.
             */
            name: string;
            /**
             * Answers naming this competitor, percent 0-100.
             */
            pct: number;
          },
          {
            /**
             * Competitor name, spelled the same everywhere.
             */
            name: string;
            /**
             * Answers naming this competitor, percent 0-100.
             */
            pct: number;
          },
          {
            /**
             * Competitor name, spelled the same everywhere.
             */
            name: string;
            /**
             * Answers naming this competitor, percent 0-100.
             */
            pct: number;
          },
          {
            /**
             * Competitor name, spelled the same everywhere.
             */
            name: string;
            /**
             * Answers naming this competitor, percent 0-100.
             */
            pct: number;
          },
          {
            /**
             * Competitor name, spelled the same everywhere.
             */
            name: string;
            /**
             * Answers naming this competitor, percent 0-100.
             */
            pct: number;
          },
          {
            /**
             * Competitor name, spelled the same everywhere.
             */
            name: string;
            /**
             * Answers naming this competitor, percent 0-100.
             */
            pct: number;
          },
          {
            /**
             * Competitor name, spelled the same everywhere.
             */
            name: string;
            /**
             * Answers naming this competitor, percent 0-100.
             */
            pct: number;
          }
        ]
      | [
          {
            /**
             * Competitor name, spelled the same everywhere.
             */
            name: string;
            /**
             * Answers naming this competitor, percent 0-100.
             */
            pct: number;
          },
          {
            /**
             * Competitor name, spelled the same everywhere.
             */
            name: string;
            /**
             * Answers naming this competitor, percent 0-100.
             */
            pct: number;
          },
          {
            /**
             * Competitor name, spelled the same everywhere.
             */
            name: string;
            /**
             * Answers naming this competitor, percent 0-100.
             */
            pct: number;
          },
          {
            /**
             * Competitor name, spelled the same everywhere.
             */
            name: string;
            /**
             * Answers naming this competitor, percent 0-100.
             */
            pct: number;
          },
          {
            /**
             * Competitor name, spelled the same everywhere.
             */
            name: string;
            /**
             * Answers naming this competitor, percent 0-100.
             */
            pct: number;
          },
          {
            /**
             * Competitor name, spelled the same everywhere.
             */
            name: string;
            /**
             * Answers naming this competitor, percent 0-100.
             */
            pct: number;
          },
          {
            /**
             * Competitor name, spelled the same everywhere.
             */
            name: string;
            /**
             * Answers naming this competitor, percent 0-100.
             */
            pct: number;
          },
          {
            /**
             * Competitor name, spelled the same everywhere.
             */
            name: string;
            /**
             * Answers naming this competitor, percent 0-100.
             */
            pct: number;
          }
        ];
  }[];
  /**
   * Share of voice for every tracked brand, including this one.
   *
   * @maxItems 25
   */
  shareOfVoice?: {
    /**
     * Brand name. Include the tracked brand too.
     */
    name: string;
    /**
     * The brand's website domain.
     */
    domain?: string;
    /**
     * Its mentions divided by all tracked brands' mentions, percent 0-100.
     */
    sharePct: number;
    /**
     * Number of mentions counted for this brand.
     */
    mentions?: number;
    /**
     * Change against the previous period, in points.
     */
    changePts?: number;
  }[];
  /**
   * Each question, per assistant.
   *
   * @maxItems 200
   */
  prompts?: {
    /**
     * The question asked.
     */
    prompt: string;
    /**
     * Topic of this question.
     */
    topic?: string;
    /**
     * One entry per assistant asked.
     *
     * @maxItems 12
     */
    results:
      | []
      | [
          {
            /**
             * Assistant name, matching byAssistant.
             */
            assistant: string;
            /**
             * Successful answers here.
             */
            runs?: number;
            /**
             * Of those, answers naming the brand.
             */
            namedRuns: number;
            /**
             * Of those, answers citing the brand's website.
             */
            citedRuns?: number;
          }
        ]
      | [
          {
            /**
             * Assistant name, matching byAssistant.
             */
            assistant: string;
            /**
             * Successful answers here.
             */
            runs?: number;
            /**
             * Of those, answers naming the brand.
             */
            namedRuns: number;
            /**
             * Of those, answers citing the brand's website.
             */
            citedRuns?: number;
          },
          {
            /**
             * Assistant name, matching byAssistant.
             */
            assistant: string;
            /**
             * Successful answers here.
             */
            runs?: number;
            /**
             * Of those, answers naming the brand.
             */
            namedRuns: number;
            /**
             * Of those, answers citing the brand's website.
             */
            citedRuns?: number;
          }
        ]
      | [
          {
            /**
             * Assistant name, matching byAssistant.
             */
            assistant: string;
            /**
             * Successful answers here.
             */
            runs?: number;
            /**
             * Of those, answers naming the brand.
             */
            namedRuns: number;
            /**
             * Of those, answers citing the brand's website.
             */
            citedRuns?: number;
          },
          {
            /**
             * Assistant name, matching byAssistant.
             */
            assistant: string;
            /**
             * Successful answers here.
             */
            runs?: number;
            /**
             * Of those, answers naming the brand.
             */
            namedRuns: number;
            /**
             * Of those, answers citing the brand's website.
             */
            citedRuns?: number;
          },
          {
            /**
             * Assistant name, matching byAssistant.
             */
            assistant: string;
            /**
             * Successful answers here.
             */
            runs?: number;
            /**
             * Of those, answers naming the brand.
             */
            namedRuns: number;
            /**
             * Of those, answers citing the brand's website.
             */
            citedRuns?: number;
          }
        ]
      | [
          {
            /**
             * Assistant name, matching byAssistant.
             */
            assistant: string;
            /**
             * Successful answers here.
             */
            runs?: number;
            /**
             * Of those, answers naming the brand.
             */
            namedRuns: number;
            /**
             * Of those, answers citing the brand's website.
             */
            citedRuns?: number;
          },
          {
            /**
             * Assistant name, matching byAssistant.
             */
            assistant: string;
            /**
             * Successful answers here.
             */
            runs?: number;
            /**
             * Of those, answers naming the brand.
             */
            namedRuns: number;
            /**
             * Of those, answers citing the brand's website.
             */
            citedRuns?: number;
          },
          {
            /**
             * Assistant name, matching byAssistant.
             */
            assistant: string;
            /**
             * Successful answers here.
             */
            runs?: number;
            /**
             * Of those, answers naming the brand.
             */
            namedRuns: number;
            /**
             * Of those, answers citing the brand's website.
             */
            citedRuns?: number;
          },
          {
            /**
             * Assistant name, matching byAssistant.
             */
            assistant: string;
            /**
             * Successful answers here.
             */
            runs?: number;
            /**
             * Of those, answers naming the brand.
             */
            namedRuns: number;
            /**
             * Of those, answers citing the brand's website.
             */
            citedRuns?: number;
          }
        ]
      | [
          {
            /**
             * Assistant name, matching byAssistant.
             */
            assistant: string;
            /**
             * Successful answers here.
             */
            runs?: number;
            /**
             * Of those, answers naming the brand.
             */
            namedRuns: number;
            /**
             * Of those, answers citing the brand's website.
             */
            citedRuns?: number;
          },
          {
            /**
             * Assistant name, matching byAssistant.
             */
            assistant: string;
            /**
             * Successful answers here.
             */
            runs?: number;
            /**
             * Of those, answers naming the brand.
             */
            namedRuns: number;
            /**
             * Of those, answers citing the brand's website.
             */
            citedRuns?: number;
          },
          {
            /**
             * Assistant name, matching byAssistant.
             */
            assistant: string;
            /**
             * Successful answers here.
             */
            runs?: number;
            /**
             * Of those, answers naming the brand.
             */
            namedRuns: number;
            /**
             * Of those, answers citing the brand's website.
             */
            citedRuns?: number;
          },
          {
            /**
             * Assistant name, matching byAssistant.
             */
            assistant: string;
            /**
             * Successful answers here.
             */
            runs?: number;
            /**
             * Of those, answers naming the brand.
             */
            namedRuns: number;
            /**
             * Of those, answers citing the brand's website.
             */
            citedRuns?: number;
          },
          {
            /**
             * Assistant name, matching byAssistant.
             */
            assistant: string;
            /**
             * Successful answers here.
             */
            runs?: number;
            /**
             * Of those, answers naming the brand.
             */
            namedRuns: number;
            /**
             * Of those, answers citing the brand's website.
             */
            citedRuns?: number;
          }
        ]
      | [
          {
            /**
             * Assistant name, matching byAssistant.
             */
            assistant: string;
            /**
             * Successful answers here.
             */
            runs?: number;
            /**
             * Of those, answers naming the brand.
             */
            namedRuns: number;
            /**
             * Of those, answers citing the brand's website.
             */
            citedRuns?: number;
          },
          {
            /**
             * Assistant name, matching byAssistant.
             */
            assistant: string;
            /**
             * Successful answers here.
             */
            runs?: number;
            /**
             * Of those, answers naming the brand.
             */
            namedRuns: number;
            /**
             * Of those, answers citing the brand's website.
             */
            citedRuns?: number;
          },
          {
            /**
             * Assistant name, matching byAssistant.
             */
            assistant: string;
            /**
             * Successful answers here.
             */
            runs?: number;
            /**
             * Of those, answers naming the brand.
             */
            namedRuns: number;
            /**
             * Of those, answers citing the brand's website.
             */
            citedRuns?: number;
          },
          {
            /**
             * Assistant name, matching byAssistant.
             */
            assistant: string;
            /**
             * Successful answers here.
             */
            runs?: number;
            /**
             * Of those, answers naming the brand.
             */
            namedRuns: number;
            /**
             * Of those, answers citing the brand's website.
             */
            citedRuns?: number;
          },
          {
            /**
             * Assistant name, matching byAssistant.
             */
            assistant: string;
            /**
             * Successful answers here.
             */
            runs?: number;
            /**
             * Of those, answers naming the brand.
             */
            namedRuns: number;
            /**
             * Of those, answers citing the brand's website.
             */
            citedRuns?: number;
          },
          {
            /**
             * Assistant name, matching byAssistant.
             */
            assistant: string;
            /**
             * Successful answers here.
             */
            runs?: number;
            /**
             * Of those, answers naming the brand.
             */
            namedRuns: number;
            /**
             * Of those, answers citing the brand's website.
             */
            citedRuns?: number;
          }
        ]
      | [
          {
            /**
             * Assistant name, matching byAssistant.
             */
            assistant: string;
            /**
             * Successful answers here.
             */
            runs?: number;
            /**
             * Of those, answers naming the brand.
             */
            namedRuns: number;
            /**
             * Of those, answers citing the brand's website.
             */
            citedRuns?: number;
          },
          {
            /**
             * Assistant name, matching byAssistant.
             */
            assistant: string;
            /**
             * Successful answers here.
             */
            runs?: number;
            /**
             * Of those, answers naming the brand.
             */
            namedRuns: number;
            /**
             * Of those, answers citing the brand's website.
             */
            citedRuns?: number;
          },
          {
            /**
             * Assistant name, matching byAssistant.
             */
            assistant: string;
            /**
             * Successful answers here.
             */
            runs?: number;
            /**
             * Of those, answers naming the brand.
             */
            namedRuns: number;
            /**
             * Of those, answers citing the brand's website.
             */
            citedRuns?: number;
          },
          {
            /**
             * Assistant name, matching byAssistant.
             */
            assistant: string;
            /**
             * Successful answers here.
             */
            runs?: number;
            /**
             * Of those, answers naming the brand.
             */
            namedRuns: number;
            /**
             * Of those, answers citing the brand's website.
             */
            citedRuns?: number;
          },
          {
            /**
             * Assistant name, matching byAssistant.
             */
            assistant: string;
            /**
             * Successful answers here.
             */
            runs?: number;
            /**
             * Of those, answers naming the brand.
             */
            namedRuns: number;
            /**
             * Of those, answers citing the brand's website.
             */
            citedRuns?: number;
          },
          {
            /**
             * Assistant name, matching byAssistant.
             */
            assistant: string;
            /**
             * Successful answers here.
             */
            runs?: number;
            /**
             * Of those, answers naming the brand.
             */
            namedRuns: number;
            /**
             * Of those, answers citing the brand's website.
             */
            citedRuns?: number;
          },
          {
            /**
             * Assistant name, matching byAssistant.
             */
            assistant: string;
            /**
             * Successful answers here.
             */
            runs?: number;
            /**
             * Of those, answers naming the brand.
             */
            namedRuns: number;
            /**
             * Of those, answers citing the brand's website.
             */
            citedRuns?: number;
          }
        ]
      | [
          {
            /**
             * Assistant name, matching byAssistant.
             */
            assistant: string;
            /**
             * Successful answers here.
             */
            runs?: number;
            /**
             * Of those, answers naming the brand.
             */
            namedRuns: number;
            /**
             * Of those, answers citing the brand's website.
             */
            citedRuns?: number;
          },
          {
            /**
             * Assistant name, matching byAssistant.
             */
            assistant: string;
            /**
             * Successful answers here.
             */
            runs?: number;
            /**
             * Of those, answers naming the brand.
             */
            namedRuns: number;
            /**
             * Of those, answers citing the brand's website.
             */
            citedRuns?: number;
          },
          {
            /**
             * Assistant name, matching byAssistant.
             */
            assistant: string;
            /**
             * Successful answers here.
             */
            runs?: number;
            /**
             * Of those, answers naming the brand.
             */
            namedRuns: number;
            /**
             * Of those, answers citing the brand's website.
             */
            citedRuns?: number;
          },
          {
            /**
             * Assistant name, matching byAssistant.
             */
            assistant: string;
            /**
             * Successful answers here.
             */
            runs?: number;
            /**
             * Of those, answers naming the brand.
             */
            namedRuns: number;
            /**
             * Of those, answers citing the brand's website.
             */
            citedRuns?: number;
          },
          {
            /**
             * Assistant name, matching byAssistant.
             */
            assistant: string;
            /**
             * Successful answers here.
             */
            runs?: number;
            /**
             * Of those, answers naming the brand.
             */
            namedRuns: number;
            /**
             * Of those, answers citing the brand's website.
             */
            citedRuns?: number;
          },
          {
            /**
             * Assistant name, matching byAssistant.
             */
            assistant: string;
            /**
             * Successful answers here.
             */
            runs?: number;
            /**
             * Of those, answers naming the brand.
             */
            namedRuns: number;
            /**
             * Of those, answers citing the brand's website.
             */
            citedRuns?: number;
          },
          {
            /**
             * Assistant name, matching byAssistant.
             */
            assistant: string;
            /**
             * Successful answers here.
             */
            runs?: number;
            /**
             * Of those, answers naming the brand.
             */
            namedRuns: number;
            /**
             * Of those, answers citing the brand's website.
             */
            citedRuns?: number;
          },
          {
            /**
             * Assistant name, matching byAssistant.
             */
            assistant: string;
            /**
             * Successful answers here.
             */
            runs?: number;
            /**
             * Of those, answers naming the brand.
             */
            namedRuns: number;
            /**
             * Of those, answers citing the brand's website.
             */
            citedRuns?: number;
          }
        ]
      | [
          {
            /**
             * Assistant name, matching byAssistant.
             */
            assistant: string;
            /**
             * Successful answers here.
             */
            runs?: number;
            /**
             * Of those, answers naming the brand.
             */
            namedRuns: number;
            /**
             * Of those, answers citing the brand's website.
             */
            citedRuns?: number;
          },
          {
            /**
             * Assistant name, matching byAssistant.
             */
            assistant: string;
            /**
             * Successful answers here.
             */
            runs?: number;
            /**
             * Of those, answers naming the brand.
             */
            namedRuns: number;
            /**
             * Of those, answers citing the brand's website.
             */
            citedRuns?: number;
          },
          {
            /**
             * Assistant name, matching byAssistant.
             */
            assistant: string;
            /**
             * Successful answers here.
             */
            runs?: number;
            /**
             * Of those, answers naming the brand.
             */
            namedRuns: number;
            /**
             * Of those, answers citing the brand's website.
             */
            citedRuns?: number;
          },
          {
            /**
             * Assistant name, matching byAssistant.
             */
            assistant: string;
            /**
             * Successful answers here.
             */
            runs?: number;
            /**
             * Of those, answers naming the brand.
             */
            namedRuns: number;
            /**
             * Of those, answers citing the brand's website.
             */
            citedRuns?: number;
          },
          {
            /**
             * Assistant name, matching byAssistant.
             */
            assistant: string;
            /**
             * Successful answers here.
             */
            runs?: number;
            /**
             * Of those, answers naming the brand.
             */
            namedRuns: number;
            /**
             * Of those, answers citing the brand's website.
             */
            citedRuns?: number;
          },
          {
            /**
             * Assistant name, matching byAssistant.
             */
            assistant: string;
            /**
             * Successful answers here.
             */
            runs?: number;
            /**
             * Of those, answers naming the brand.
             */
            namedRuns: number;
            /**
             * Of those, answers citing the brand's website.
             */
            citedRuns?: number;
          },
          {
            /**
             * Assistant name, matching byAssistant.
             */
            assistant: string;
            /**
             * Successful answers here.
             */
            runs?: number;
            /**
             * Of those, answers naming the brand.
             */
            namedRuns: number;
            /**
             * Of those, answers citing the brand's website.
             */
            citedRuns?: number;
          },
          {
            /**
             * Assistant name, matching byAssistant.
             */
            assistant: string;
            /**
             * Successful answers here.
             */
            runs?: number;
            /**
             * Of those, answers naming the brand.
             */
            namedRuns: number;
            /**
             * Of those, answers citing the brand's website.
             */
            citedRuns?: number;
          },
          {
            /**
             * Assistant name, matching byAssistant.
             */
            assistant: string;
            /**
             * Successful answers here.
             */
            runs?: number;
            /**
             * Of those, answers naming the brand.
             */
            namedRuns: number;
            /**
             * Of those, answers citing the brand's website.
             */
            citedRuns?: number;
          }
        ]
      | [
          {
            /**
             * Assistant name, matching byAssistant.
             */
            assistant: string;
            /**
             * Successful answers here.
             */
            runs?: number;
            /**
             * Of those, answers naming the brand.
             */
            namedRuns: number;
            /**
             * Of those, answers citing the brand's website.
             */
            citedRuns?: number;
          },
          {
            /**
             * Assistant name, matching byAssistant.
             */
            assistant: string;
            /**
             * Successful answers here.
             */
            runs?: number;
            /**
             * Of those, answers naming the brand.
             */
            namedRuns: number;
            /**
             * Of those, answers citing the brand's website.
             */
            citedRuns?: number;
          },
          {
            /**
             * Assistant name, matching byAssistant.
             */
            assistant: string;
            /**
             * Successful answers here.
             */
            runs?: number;
            /**
             * Of those, answers naming the brand.
             */
            namedRuns: number;
            /**
             * Of those, answers citing the brand's website.
             */
            citedRuns?: number;
          },
          {
            /**
             * Assistant name, matching byAssistant.
             */
            assistant: string;
            /**
             * Successful answers here.
             */
            runs?: number;
            /**
             * Of those, answers naming the brand.
             */
            namedRuns: number;
            /**
             * Of those, answers citing the brand's website.
             */
            citedRuns?: number;
          },
          {
            /**
             * Assistant name, matching byAssistant.
             */
            assistant: string;
            /**
             * Successful answers here.
             */
            runs?: number;
            /**
             * Of those, answers naming the brand.
             */
            namedRuns: number;
            /**
             * Of those, answers citing the brand's website.
             */
            citedRuns?: number;
          },
          {
            /**
             * Assistant name, matching byAssistant.
             */
            assistant: string;
            /**
             * Successful answers here.
             */
            runs?: number;
            /**
             * Of those, answers naming the brand.
             */
            namedRuns: number;
            /**
             * Of those, answers citing the brand's website.
             */
            citedRuns?: number;
          },
          {
            /**
             * Assistant name, matching byAssistant.
             */
            assistant: string;
            /**
             * Successful answers here.
             */
            runs?: number;
            /**
             * Of those, answers naming the brand.
             */
            namedRuns: number;
            /**
             * Of those, answers citing the brand's website.
             */
            citedRuns?: number;
          },
          {
            /**
             * Assistant name, matching byAssistant.
             */
            assistant: string;
            /**
             * Successful answers here.
             */
            runs?: number;
            /**
             * Of those, answers naming the brand.
             */
            namedRuns: number;
            /**
             * Of those, answers citing the brand's website.
             */
            citedRuns?: number;
          },
          {
            /**
             * Assistant name, matching byAssistant.
             */
            assistant: string;
            /**
             * Successful answers here.
             */
            runs?: number;
            /**
             * Of those, answers naming the brand.
             */
            namedRuns: number;
            /**
             * Of those, answers citing the brand's website.
             */
            citedRuns?: number;
          },
          {
            /**
             * Assistant name, matching byAssistant.
             */
            assistant: string;
            /**
             * Successful answers here.
             */
            runs?: number;
            /**
             * Of those, answers naming the brand.
             */
            namedRuns: number;
            /**
             * Of those, answers citing the brand's website.
             */
            citedRuns?: number;
          }
        ]
      | [
          {
            /**
             * Assistant name, matching byAssistant.
             */
            assistant: string;
            /**
             * Successful answers here.
             */
            runs?: number;
            /**
             * Of those, answers naming the brand.
             */
            namedRuns: number;
            /**
             * Of those, answers citing the brand's website.
             */
            citedRuns?: number;
          },
          {
            /**
             * Assistant name, matching byAssistant.
             */
            assistant: string;
            /**
             * Successful answers here.
             */
            runs?: number;
            /**
             * Of those, answers naming the brand.
             */
            namedRuns: number;
            /**
             * Of those, answers citing the brand's website.
             */
            citedRuns?: number;
          },
          {
            /**
             * Assistant name, matching byAssistant.
             */
            assistant: string;
            /**
             * Successful answers here.
             */
            runs?: number;
            /**
             * Of those, answers naming the brand.
             */
            namedRuns: number;
            /**
             * Of those, answers citing the brand's website.
             */
            citedRuns?: number;
          },
          {
            /**
             * Assistant name, matching byAssistant.
             */
            assistant: string;
            /**
             * Successful answers here.
             */
            runs?: number;
            /**
             * Of those, answers naming the brand.
             */
            namedRuns: number;
            /**
             * Of those, answers citing the brand's website.
             */
            citedRuns?: number;
          },
          {
            /**
             * Assistant name, matching byAssistant.
             */
            assistant: string;
            /**
             * Successful answers here.
             */
            runs?: number;
            /**
             * Of those, answers naming the brand.
             */
            namedRuns: number;
            /**
             * Of those, answers citing the brand's website.
             */
            citedRuns?: number;
          },
          {
            /**
             * Assistant name, matching byAssistant.
             */
            assistant: string;
            /**
             * Successful answers here.
             */
            runs?: number;
            /**
             * Of those, answers naming the brand.
             */
            namedRuns: number;
            /**
             * Of those, answers citing the brand's website.
             */
            citedRuns?: number;
          },
          {
            /**
             * Assistant name, matching byAssistant.
             */
            assistant: string;
            /**
             * Successful answers here.
             */
            runs?: number;
            /**
             * Of those, answers naming the brand.
             */
            namedRuns: number;
            /**
             * Of those, answers citing the brand's website.
             */
            citedRuns?: number;
          },
          {
            /**
             * Assistant name, matching byAssistant.
             */
            assistant: string;
            /**
             * Successful answers here.
             */
            runs?: number;
            /**
             * Of those, answers naming the brand.
             */
            namedRuns: number;
            /**
             * Of those, answers citing the brand's website.
             */
            citedRuns?: number;
          },
          {
            /**
             * Assistant name, matching byAssistant.
             */
            assistant: string;
            /**
             * Successful answers here.
             */
            runs?: number;
            /**
             * Of those, answers naming the brand.
             */
            namedRuns: number;
            /**
             * Of those, answers citing the brand's website.
             */
            citedRuns?: number;
          },
          {
            /**
             * Assistant name, matching byAssistant.
             */
            assistant: string;
            /**
             * Successful answers here.
             */
            runs?: number;
            /**
             * Of those, answers naming the brand.
             */
            namedRuns: number;
            /**
             * Of those, answers citing the brand's website.
             */
            citedRuns?: number;
          },
          {
            /**
             * Assistant name, matching byAssistant.
             */
            assistant: string;
            /**
             * Successful answers here.
             */
            runs?: number;
            /**
             * Of those, answers naming the brand.
             */
            namedRuns: number;
            /**
             * Of those, answers citing the brand's website.
             */
            citedRuns?: number;
          }
        ]
      | [
          {
            /**
             * Assistant name, matching byAssistant.
             */
            assistant: string;
            /**
             * Successful answers here.
             */
            runs?: number;
            /**
             * Of those, answers naming the brand.
             */
            namedRuns: number;
            /**
             * Of those, answers citing the brand's website.
             */
            citedRuns?: number;
          },
          {
            /**
             * Assistant name, matching byAssistant.
             */
            assistant: string;
            /**
             * Successful answers here.
             */
            runs?: number;
            /**
             * Of those, answers naming the brand.
             */
            namedRuns: number;
            /**
             * Of those, answers citing the brand's website.
             */
            citedRuns?: number;
          },
          {
            /**
             * Assistant name, matching byAssistant.
             */
            assistant: string;
            /**
             * Successful answers here.
             */
            runs?: number;
            /**
             * Of those, answers naming the brand.
             */
            namedRuns: number;
            /**
             * Of those, answers citing the brand's website.
             */
            citedRuns?: number;
          },
          {
            /**
             * Assistant name, matching byAssistant.
             */
            assistant: string;
            /**
             * Successful answers here.
             */
            runs?: number;
            /**
             * Of those, answers naming the brand.
             */
            namedRuns: number;
            /**
             * Of those, answers citing the brand's website.
             */
            citedRuns?: number;
          },
          {
            /**
             * Assistant name, matching byAssistant.
             */
            assistant: string;
            /**
             * Successful answers here.
             */
            runs?: number;
            /**
             * Of those, answers naming the brand.
             */
            namedRuns: number;
            /**
             * Of those, answers citing the brand's website.
             */
            citedRuns?: number;
          },
          {
            /**
             * Assistant name, matching byAssistant.
             */
            assistant: string;
            /**
             * Successful answers here.
             */
            runs?: number;
            /**
             * Of those, answers naming the brand.
             */
            namedRuns: number;
            /**
             * Of those, answers citing the brand's website.
             */
            citedRuns?: number;
          },
          {
            /**
             * Assistant name, matching byAssistant.
             */
            assistant: string;
            /**
             * Successful answers here.
             */
            runs?: number;
            /**
             * Of those, answers naming the brand.
             */
            namedRuns: number;
            /**
             * Of those, answers citing the brand's website.
             */
            citedRuns?: number;
          },
          {
            /**
             * Assistant name, matching byAssistant.
             */
            assistant: string;
            /**
             * Successful answers here.
             */
            runs?: number;
            /**
             * Of those, answers naming the brand.
             */
            namedRuns: number;
            /**
             * Of those, answers citing the brand's website.
             */
            citedRuns?: number;
          },
          {
            /**
             * Assistant name, matching byAssistant.
             */
            assistant: string;
            /**
             * Successful answers here.
             */
            runs?: number;
            /**
             * Of those, answers naming the brand.
             */
            namedRuns: number;
            /**
             * Of those, answers citing the brand's website.
             */
            citedRuns?: number;
          },
          {
            /**
             * Assistant name, matching byAssistant.
             */
            assistant: string;
            /**
             * Successful answers here.
             */
            runs?: number;
            /**
             * Of those, answers naming the brand.
             */
            namedRuns: number;
            /**
             * Of those, answers citing the brand's website.
             */
            citedRuns?: number;
          },
          {
            /**
             * Assistant name, matching byAssistant.
             */
            assistant: string;
            /**
             * Successful answers here.
             */
            runs?: number;
            /**
             * Of those, answers naming the brand.
             */
            namedRuns: number;
            /**
             * Of those, answers citing the brand's website.
             */
            citedRuns?: number;
          },
          {
            /**
             * Assistant name, matching byAssistant.
             */
            assistant: string;
            /**
             * Successful answers here.
             */
            runs?: number;
            /**
             * Of those, answers naming the brand.
             */
            namedRuns: number;
            /**
             * Of those, answers citing the brand's website.
             */
            citedRuns?: number;
          }
        ];
  }[];
  /**
   * Visibility by topic against competitors.
   *
   * @maxItems 50
   */
  topics?: {
    /**
     * Topic or situation.
     */
    topic: string;
    /**
     * Successful answers in this topic.
     */
    answersTotal?: number;
    /**
     * The brand's visibility in this topic, percent 0-100.
     */
    brandPct: number;
    /**
     * Competitor visibility in this topic.
     *
     * @maxItems 6
     */
    competitors?:
      | []
      | [
          {
            /**
             * Competitor name, spelled the same everywhere.
             */
            name: string;
            /**
             * Answers naming this competitor, percent 0-100.
             */
            pct: number;
          }
        ]
      | [
          {
            /**
             * Competitor name, spelled the same everywhere.
             */
            name: string;
            /**
             * Answers naming this competitor, percent 0-100.
             */
            pct: number;
          },
          {
            /**
             * Competitor name, spelled the same everywhere.
             */
            name: string;
            /**
             * Answers naming this competitor, percent 0-100.
             */
            pct: number;
          }
        ]
      | [
          {
            /**
             * Competitor name, spelled the same everywhere.
             */
            name: string;
            /**
             * Answers naming this competitor, percent 0-100.
             */
            pct: number;
          },
          {
            /**
             * Competitor name, spelled the same everywhere.
             */
            name: string;
            /**
             * Answers naming this competitor, percent 0-100.
             */
            pct: number;
          },
          {
            /**
             * Competitor name, spelled the same everywhere.
             */
            name: string;
            /**
             * Answers naming this competitor, percent 0-100.
             */
            pct: number;
          }
        ]
      | [
          {
            /**
             * Competitor name, spelled the same everywhere.
             */
            name: string;
            /**
             * Answers naming this competitor, percent 0-100.
             */
            pct: number;
          },
          {
            /**
             * Competitor name, spelled the same everywhere.
             */
            name: string;
            /**
             * Answers naming this competitor, percent 0-100.
             */
            pct: number;
          },
          {
            /**
             * Competitor name, spelled the same everywhere.
             */
            name: string;
            /**
             * Answers naming this competitor, percent 0-100.
             */
            pct: number;
          },
          {
            /**
             * Competitor name, spelled the same everywhere.
             */
            name: string;
            /**
             * Answers naming this competitor, percent 0-100.
             */
            pct: number;
          }
        ]
      | [
          {
            /**
             * Competitor name, spelled the same everywhere.
             */
            name: string;
            /**
             * Answers naming this competitor, percent 0-100.
             */
            pct: number;
          },
          {
            /**
             * Competitor name, spelled the same everywhere.
             */
            name: string;
            /**
             * Answers naming this competitor, percent 0-100.
             */
            pct: number;
          },
          {
            /**
             * Competitor name, spelled the same everywhere.
             */
            name: string;
            /**
             * Answers naming this competitor, percent 0-100.
             */
            pct: number;
          },
          {
            /**
             * Competitor name, spelled the same everywhere.
             */
            name: string;
            /**
             * Answers naming this competitor, percent 0-100.
             */
            pct: number;
          },
          {
            /**
             * Competitor name, spelled the same everywhere.
             */
            name: string;
            /**
             * Answers naming this competitor, percent 0-100.
             */
            pct: number;
          }
        ]
      | [
          {
            /**
             * Competitor name, spelled the same everywhere.
             */
            name: string;
            /**
             * Answers naming this competitor, percent 0-100.
             */
            pct: number;
          },
          {
            /**
             * Competitor name, spelled the same everywhere.
             */
            name: string;
            /**
             * Answers naming this competitor, percent 0-100.
             */
            pct: number;
          },
          {
            /**
             * Competitor name, spelled the same everywhere.
             */
            name: string;
            /**
             * Answers naming this competitor, percent 0-100.
             */
            pct: number;
          },
          {
            /**
             * Competitor name, spelled the same everywhere.
             */
            name: string;
            /**
             * Answers naming this competitor, percent 0-100.
             */
            pct: number;
          },
          {
            /**
             * Competitor name, spelled the same everywhere.
             */
            name: string;
            /**
             * Answers naming this competitor, percent 0-100.
             */
            pct: number;
          },
          {
            /**
             * Competitor name, spelled the same everywhere.
             */
            name: string;
            /**
             * Answers naming this competitor, percent 0-100.
             */
            pct: number;
          }
        ];
  }[];
  /**
   * The brand's website across the answers.
   */
  siteOutcome?: {
    /**
     * Answers that cited the brand's website.
     */
    cited: number;
    /**
     * Answers that read the website without citing it.
     */
    researched: number;
    /**
     * Answers where the website did not appear.
     */
    absent: number;
  };
  /**
   * The kinds of site the assistants relied on.
   *
   * @maxItems 20
   */
  siteTypes?:
    | []
    | [
        {
          /**
           * Site type, for example "Review site".
           */
          type: string;
          /**
           * Pages of this type used.
           */
          sources: number;
          /**
           * Of those, pages cited.
           */
          cited?: number;
        }
      ]
    | [
        {
          /**
           * Site type, for example "Review site".
           */
          type: string;
          /**
           * Pages of this type used.
           */
          sources: number;
          /**
           * Of those, pages cited.
           */
          cited?: number;
        },
        {
          /**
           * Site type, for example "Review site".
           */
          type: string;
          /**
           * Pages of this type used.
           */
          sources: number;
          /**
           * Of those, pages cited.
           */
          cited?: number;
        }
      ]
    | [
        {
          /**
           * Site type, for example "Review site".
           */
          type: string;
          /**
           * Pages of this type used.
           */
          sources: number;
          /**
           * Of those, pages cited.
           */
          cited?: number;
        },
        {
          /**
           * Site type, for example "Review site".
           */
          type: string;
          /**
           * Pages of this type used.
           */
          sources: number;
          /**
           * Of those, pages cited.
           */
          cited?: number;
        },
        {
          /**
           * Site type, for example "Review site".
           */
          type: string;
          /**
           * Pages of this type used.
           */
          sources: number;
          /**
           * Of those, pages cited.
           */
          cited?: number;
        }
      ]
    | [
        {
          /**
           * Site type, for example "Review site".
           */
          type: string;
          /**
           * Pages of this type used.
           */
          sources: number;
          /**
           * Of those, pages cited.
           */
          cited?: number;
        },
        {
          /**
           * Site type, for example "Review site".
           */
          type: string;
          /**
           * Pages of this type used.
           */
          sources: number;
          /**
           * Of those, pages cited.
           */
          cited?: number;
        },
        {
          /**
           * Site type, for example "Review site".
           */
          type: string;
          /**
           * Pages of this type used.
           */
          sources: number;
          /**
           * Of those, pages cited.
           */
          cited?: number;
        },
        {
          /**
           * Site type, for example "Review site".
           */
          type: string;
          /**
           * Pages of this type used.
           */
          sources: number;
          /**
           * Of those, pages cited.
           */
          cited?: number;
        }
      ]
    | [
        {
          /**
           * Site type, for example "Review site".
           */
          type: string;
          /**
           * Pages of this type used.
           */
          sources: number;
          /**
           * Of those, pages cited.
           */
          cited?: number;
        },
        {
          /**
           * Site type, for example "Review site".
           */
          type: string;
          /**
           * Pages of this type used.
           */
          sources: number;
          /**
           * Of those, pages cited.
           */
          cited?: number;
        },
        {
          /**
           * Site type, for example "Review site".
           */
          type: string;
          /**
           * Pages of this type used.
           */
          sources: number;
          /**
           * Of those, pages cited.
           */
          cited?: number;
        },
        {
          /**
           * Site type, for example "Review site".
           */
          type: string;
          /**
           * Pages of this type used.
           */
          sources: number;
          /**
           * Of those, pages cited.
           */
          cited?: number;
        },
        {
          /**
           * Site type, for example "Review site".
           */
          type: string;
          /**
           * Pages of this type used.
           */
          sources: number;
          /**
           * Of those, pages cited.
           */
          cited?: number;
        }
      ]
    | [
        {
          /**
           * Site type, for example "Review site".
           */
          type: string;
          /**
           * Pages of this type used.
           */
          sources: number;
          /**
           * Of those, pages cited.
           */
          cited?: number;
        },
        {
          /**
           * Site type, for example "Review site".
           */
          type: string;
          /**
           * Pages of this type used.
           */
          sources: number;
          /**
           * Of those, pages cited.
           */
          cited?: number;
        },
        {
          /**
           * Site type, for example "Review site".
           */
          type: string;
          /**
           * Pages of this type used.
           */
          sources: number;
          /**
           * Of those, pages cited.
           */
          cited?: number;
        },
        {
          /**
           * Site type, for example "Review site".
           */
          type: string;
          /**
           * Pages of this type used.
           */
          sources: number;
          /**
           * Of those, pages cited.
           */
          cited?: number;
        },
        {
          /**
           * Site type, for example "Review site".
           */
          type: string;
          /**
           * Pages of this type used.
           */
          sources: number;
          /**
           * Of those, pages cited.
           */
          cited?: number;
        },
        {
          /**
           * Site type, for example "Review site".
           */
          type: string;
          /**
           * Pages of this type used.
           */
          sources: number;
          /**
           * Of those, pages cited.
           */
          cited?: number;
        }
      ]
    | [
        {
          /**
           * Site type, for example "Review site".
           */
          type: string;
          /**
           * Pages of this type used.
           */
          sources: number;
          /**
           * Of those, pages cited.
           */
          cited?: number;
        },
        {
          /**
           * Site type, for example "Review site".
           */
          type: string;
          /**
           * Pages of this type used.
           */
          sources: number;
          /**
           * Of those, pages cited.
           */
          cited?: number;
        },
        {
          /**
           * Site type, for example "Review site".
           */
          type: string;
          /**
           * Pages of this type used.
           */
          sources: number;
          /**
           * Of those, pages cited.
           */
          cited?: number;
        },
        {
          /**
           * Site type, for example "Review site".
           */
          type: string;
          /**
           * Pages of this type used.
           */
          sources: number;
          /**
           * Of those, pages cited.
           */
          cited?: number;
        },
        {
          /**
           * Site type, for example "Review site".
           */
          type: string;
          /**
           * Pages of this type used.
           */
          sources: number;
          /**
           * Of those, pages cited.
           */
          cited?: number;
        },
        {
          /**
           * Site type, for example "Review site".
           */
          type: string;
          /**
           * Pages of this type used.
           */
          sources: number;
          /**
           * Of those, pages cited.
           */
          cited?: number;
        },
        {
          /**
           * Site type, for example "Review site".
           */
          type: string;
          /**
           * Pages of this type used.
           */
          sources: number;
          /**
           * Of those, pages cited.
           */
          cited?: number;
        }
      ]
    | [
        {
          /**
           * Site type, for example "Review site".
           */
          type: string;
          /**
           * Pages of this type used.
           */
          sources: number;
          /**
           * Of those, pages cited.
           */
          cited?: number;
        },
        {
          /**
           * Site type, for example "Review site".
           */
          type: string;
          /**
           * Pages of this type used.
           */
          sources: number;
          /**
           * Of those, pages cited.
           */
          cited?: number;
        },
        {
          /**
           * Site type, for example "Review site".
           */
          type: string;
          /**
           * Pages of this type used.
           */
          sources: number;
          /**
           * Of those, pages cited.
           */
          cited?: number;
        },
        {
          /**
           * Site type, for example "Review site".
           */
          type: string;
          /**
           * Pages of this type used.
           */
          sources: number;
          /**
           * Of those, pages cited.
           */
          cited?: number;
        },
        {
          /**
           * Site type, for example "Review site".
           */
          type: string;
          /**
           * Pages of this type used.
           */
          sources: number;
          /**
           * Of those, pages cited.
           */
          cited?: number;
        },
        {
          /**
           * Site type, for example "Review site".
           */
          type: string;
          /**
           * Pages of this type used.
           */
          sources: number;
          /**
           * Of those, pages cited.
           */
          cited?: number;
        },
        {
          /**
           * Site type, for example "Review site".
           */
          type: string;
          /**
           * Pages of this type used.
           */
          sources: number;
          /**
           * Of those, pages cited.
           */
          cited?: number;
        },
        {
          /**
           * Site type, for example "Review site".
           */
          type: string;
          /**
           * Pages of this type used.
           */
          sources: number;
          /**
           * Of those, pages cited.
           */
          cited?: number;
        }
      ]
    | [
        {
          /**
           * Site type, for example "Review site".
           */
          type: string;
          /**
           * Pages of this type used.
           */
          sources: number;
          /**
           * Of those, pages cited.
           */
          cited?: number;
        },
        {
          /**
           * Site type, for example "Review site".
           */
          type: string;
          /**
           * Pages of this type used.
           */
          sources: number;
          /**
           * Of those, pages cited.
           */
          cited?: number;
        },
        {
          /**
           * Site type, for example "Review site".
           */
          type: string;
          /**
           * Pages of this type used.
           */
          sources: number;
          /**
           * Of those, pages cited.
           */
          cited?: number;
        },
        {
          /**
           * Site type, for example "Review site".
           */
          type: string;
          /**
           * Pages of this type used.
           */
          sources: number;
          /**
           * Of those, pages cited.
           */
          cited?: number;
        },
        {
          /**
           * Site type, for example "Review site".
           */
          type: string;
          /**
           * Pages of this type used.
           */
          sources: number;
          /**
           * Of those, pages cited.
           */
          cited?: number;
        },
        {
          /**
           * Site type, for example "Review site".
           */
          type: string;
          /**
           * Pages of this type used.
           */
          sources: number;
          /**
           * Of those, pages cited.
           */
          cited?: number;
        },
        {
          /**
           * Site type, for example "Review site".
           */
          type: string;
          /**
           * Pages of this type used.
           */
          sources: number;
          /**
           * Of those, pages cited.
           */
          cited?: number;
        },
        {
          /**
           * Site type, for example "Review site".
           */
          type: string;
          /**
           * Pages of this type used.
           */
          sources: number;
          /**
           * Of those, pages cited.
           */
          cited?: number;
        },
        {
          /**
           * Site type, for example "Review site".
           */
          type: string;
          /**
           * Pages of this type used.
           */
          sources: number;
          /**
           * Of those, pages cited.
           */
          cited?: number;
        }
      ]
    | [
        {
          /**
           * Site type, for example "Review site".
           */
          type: string;
          /**
           * Pages of this type used.
           */
          sources: number;
          /**
           * Of those, pages cited.
           */
          cited?: number;
        },
        {
          /**
           * Site type, for example "Review site".
           */
          type: string;
          /**
           * Pages of this type used.
           */
          sources: number;
          /**
           * Of those, pages cited.
           */
          cited?: number;
        },
        {
          /**
           * Site type, for example "Review site".
           */
          type: string;
          /**
           * Pages of this type used.
           */
          sources: number;
          /**
           * Of those, pages cited.
           */
          cited?: number;
        },
        {
          /**
           * Site type, for example "Review site".
           */
          type: string;
          /**
           * Pages of this type used.
           */
          sources: number;
          /**
           * Of those, pages cited.
           */
          cited?: number;
        },
        {
          /**
           * Site type, for example "Review site".
           */
          type: string;
          /**
           * Pages of this type used.
           */
          sources: number;
          /**
           * Of those, pages cited.
           */
          cited?: number;
        },
        {
          /**
           * Site type, for example "Review site".
           */
          type: string;
          /**
           * Pages of this type used.
           */
          sources: number;
          /**
           * Of those, pages cited.
           */
          cited?: number;
        },
        {
          /**
           * Site type, for example "Review site".
           */
          type: string;
          /**
           * Pages of this type used.
           */
          sources: number;
          /**
           * Of those, pages cited.
           */
          cited?: number;
        },
        {
          /**
           * Site type, for example "Review site".
           */
          type: string;
          /**
           * Pages of this type used.
           */
          sources: number;
          /**
           * Of those, pages cited.
           */
          cited?: number;
        },
        {
          /**
           * Site type, for example "Review site".
           */
          type: string;
          /**
           * Pages of this type used.
           */
          sources: number;
          /**
           * Of those, pages cited.
           */
          cited?: number;
        },
        {
          /**
           * Site type, for example "Review site".
           */
          type: string;
          /**
           * Pages of this type used.
           */
          sources: number;
          /**
           * Of those, pages cited.
           */
          cited?: number;
        }
      ]
    | [
        {
          /**
           * Site type, for example "Review site".
           */
          type: string;
          /**
           * Pages of this type used.
           */
          sources: number;
          /**
           * Of those, pages cited.
           */
          cited?: number;
        },
        {
          /**
           * Site type, for example "Review site".
           */
          type: string;
          /**
           * Pages of this type used.
           */
          sources: number;
          /**
           * Of those, pages cited.
           */
          cited?: number;
        },
        {
          /**
           * Site type, for example "Review site".
           */
          type: string;
          /**
           * Pages of this type used.
           */
          sources: number;
          /**
           * Of those, pages cited.
           */
          cited?: number;
        },
        {
          /**
           * Site type, for example "Review site".
           */
          type: string;
          /**
           * Pages of this type used.
           */
          sources: number;
          /**
           * Of those, pages cited.
           */
          cited?: number;
        },
        {
          /**
           * Site type, for example "Review site".
           */
          type: string;
          /**
           * Pages of this type used.
           */
          sources: number;
          /**
           * Of those, pages cited.
           */
          cited?: number;
        },
        {
          /**
           * Site type, for example "Review site".
           */
          type: string;
          /**
           * Pages of this type used.
           */
          sources: number;
          /**
           * Of those, pages cited.
           */
          cited?: number;
        },
        {
          /**
           * Site type, for example "Review site".
           */
          type: string;
          /**
           * Pages of this type used.
           */
          sources: number;
          /**
           * Of those, pages cited.
           */
          cited?: number;
        },
        {
          /**
           * Site type, for example "Review site".
           */
          type: string;
          /**
           * Pages of this type used.
           */
          sources: number;
          /**
           * Of those, pages cited.
           */
          cited?: number;
        },
        {
          /**
           * Site type, for example "Review site".
           */
          type: string;
          /**
           * Pages of this type used.
           */
          sources: number;
          /**
           * Of those, pages cited.
           */
          cited?: number;
        },
        {
          /**
           * Site type, for example "Review site".
           */
          type: string;
          /**
           * Pages of this type used.
           */
          sources: number;
          /**
           * Of those, pages cited.
           */
          cited?: number;
        },
        {
          /**
           * Site type, for example "Review site".
           */
          type: string;
          /**
           * Pages of this type used.
           */
          sources: number;
          /**
           * Of those, pages cited.
           */
          cited?: number;
        }
      ]
    | [
        {
          /**
           * Site type, for example "Review site".
           */
          type: string;
          /**
           * Pages of this type used.
           */
          sources: number;
          /**
           * Of those, pages cited.
           */
          cited?: number;
        },
        {
          /**
           * Site type, for example "Review site".
           */
          type: string;
          /**
           * Pages of this type used.
           */
          sources: number;
          /**
           * Of those, pages cited.
           */
          cited?: number;
        },
        {
          /**
           * Site type, for example "Review site".
           */
          type: string;
          /**
           * Pages of this type used.
           */
          sources: number;
          /**
           * Of those, pages cited.
           */
          cited?: number;
        },
        {
          /**
           * Site type, for example "Review site".
           */
          type: string;
          /**
           * Pages of this type used.
           */
          sources: number;
          /**
           * Of those, pages cited.
           */
          cited?: number;
        },
        {
          /**
           * Site type, for example "Review site".
           */
          type: string;
          /**
           * Pages of this type used.
           */
          sources: number;
          /**
           * Of those, pages cited.
           */
          cited?: number;
        },
        {
          /**
           * Site type, for example "Review site".
           */
          type: string;
          /**
           * Pages of this type used.
           */
          sources: number;
          /**
           * Of those, pages cited.
           */
          cited?: number;
        },
        {
          /**
           * Site type, for example "Review site".
           */
          type: string;
          /**
           * Pages of this type used.
           */
          sources: number;
          /**
           * Of those, pages cited.
           */
          cited?: number;
        },
        {
          /**
           * Site type, for example "Review site".
           */
          type: string;
          /**
           * Pages of this type used.
           */
          sources: number;
          /**
           * Of those, pages cited.
           */
          cited?: number;
        },
        {
          /**
           * Site type, for example "Review site".
           */
          type: string;
          /**
           * Pages of this type used.
           */
          sources: number;
          /**
           * Of those, pages cited.
           */
          cited?: number;
        },
        {
          /**
           * Site type, for example "Review site".
           */
          type: string;
          /**
           * Pages of this type used.
           */
          sources: number;
          /**
           * Of those, pages cited.
           */
          cited?: number;
        },
        {
          /**
           * Site type, for example "Review site".
           */
          type: string;
          /**
           * Pages of this type used.
           */
          sources: number;
          /**
           * Of those, pages cited.
           */
          cited?: number;
        },
        {
          /**
           * Site type, for example "Review site".
           */
          type: string;
          /**
           * Pages of this type used.
           */
          sources: number;
          /**
           * Of those, pages cited.
           */
          cited?: number;
        }
      ]
    | [
        {
          /**
           * Site type, for example "Review site".
           */
          type: string;
          /**
           * Pages of this type used.
           */
          sources: number;
          /**
           * Of those, pages cited.
           */
          cited?: number;
        },
        {
          /**
           * Site type, for example "Review site".
           */
          type: string;
          /**
           * Pages of this type used.
           */
          sources: number;
          /**
           * Of those, pages cited.
           */
          cited?: number;
        },
        {
          /**
           * Site type, for example "Review site".
           */
          type: string;
          /**
           * Pages of this type used.
           */
          sources: number;
          /**
           * Of those, pages cited.
           */
          cited?: number;
        },
        {
          /**
           * Site type, for example "Review site".
           */
          type: string;
          /**
           * Pages of this type used.
           */
          sources: number;
          /**
           * Of those, pages cited.
           */
          cited?: number;
        },
        {
          /**
           * Site type, for example "Review site".
           */
          type: string;
          /**
           * Pages of this type used.
           */
          sources: number;
          /**
           * Of those, pages cited.
           */
          cited?: number;
        },
        {
          /**
           * Site type, for example "Review site".
           */
          type: string;
          /**
           * Pages of this type used.
           */
          sources: number;
          /**
           * Of those, pages cited.
           */
          cited?: number;
        },
        {
          /**
           * Site type, for example "Review site".
           */
          type: string;
          /**
           * Pages of this type used.
           */
          sources: number;
          /**
           * Of those, pages cited.
           */
          cited?: number;
        },
        {
          /**
           * Site type, for example "Review site".
           */
          type: string;
          /**
           * Pages of this type used.
           */
          sources: number;
          /**
           * Of those, pages cited.
           */
          cited?: number;
        },
        {
          /**
           * Site type, for example "Review site".
           */
          type: string;
          /**
           * Pages of this type used.
           */
          sources: number;
          /**
           * Of those, pages cited.
           */
          cited?: number;
        },
        {
          /**
           * Site type, for example "Review site".
           */
          type: string;
          /**
           * Pages of this type used.
           */
          sources: number;
          /**
           * Of those, pages cited.
           */
          cited?: number;
        },
        {
          /**
           * Site type, for example "Review site".
           */
          type: string;
          /**
           * Pages of this type used.
           */
          sources: number;
          /**
           * Of those, pages cited.
           */
          cited?: number;
        },
        {
          /**
           * Site type, for example "Review site".
           */
          type: string;
          /**
           * Pages of this type used.
           */
          sources: number;
          /**
           * Of those, pages cited.
           */
          cited?: number;
        },
        {
          /**
           * Site type, for example "Review site".
           */
          type: string;
          /**
           * Pages of this type used.
           */
          sources: number;
          /**
           * Of those, pages cited.
           */
          cited?: number;
        }
      ]
    | [
        {
          /**
           * Site type, for example "Review site".
           */
          type: string;
          /**
           * Pages of this type used.
           */
          sources: number;
          /**
           * Of those, pages cited.
           */
          cited?: number;
        },
        {
          /**
           * Site type, for example "Review site".
           */
          type: string;
          /**
           * Pages of this type used.
           */
          sources: number;
          /**
           * Of those, pages cited.
           */
          cited?: number;
        },
        {
          /**
           * Site type, for example "Review site".
           */
          type: string;
          /**
           * Pages of this type used.
           */
          sources: number;
          /**
           * Of those, pages cited.
           */
          cited?: number;
        },
        {
          /**
           * Site type, for example "Review site".
           */
          type: string;
          /**
           * Pages of this type used.
           */
          sources: number;
          /**
           * Of those, pages cited.
           */
          cited?: number;
        },
        {
          /**
           * Site type, for example "Review site".
           */
          type: string;
          /**
           * Pages of this type used.
           */
          sources: number;
          /**
           * Of those, pages cited.
           */
          cited?: number;
        },
        {
          /**
           * Site type, for example "Review site".
           */
          type: string;
          /**
           * Pages of this type used.
           */
          sources: number;
          /**
           * Of those, pages cited.
           */
          cited?: number;
        },
        {
          /**
           * Site type, for example "Review site".
           */
          type: string;
          /**
           * Pages of this type used.
           */
          sources: number;
          /**
           * Of those, pages cited.
           */
          cited?: number;
        },
        {
          /**
           * Site type, for example "Review site".
           */
          type: string;
          /**
           * Pages of this type used.
           */
          sources: number;
          /**
           * Of those, pages cited.
           */
          cited?: number;
        },
        {
          /**
           * Site type, for example "Review site".
           */
          type: string;
          /**
           * Pages of this type used.
           */
          sources: number;
          /**
           * Of those, pages cited.
           */
          cited?: number;
        },
        {
          /**
           * Site type, for example "Review site".
           */
          type: string;
          /**
           * Pages of this type used.
           */
          sources: number;
          /**
           * Of those, pages cited.
           */
          cited?: number;
        },
        {
          /**
           * Site type, for example "Review site".
           */
          type: string;
          /**
           * Pages of this type used.
           */
          sources: number;
          /**
           * Of those, pages cited.
           */
          cited?: number;
        },
        {
          /**
           * Site type, for example "Review site".
           */
          type: string;
          /**
           * Pages of this type used.
           */
          sources: number;
          /**
           * Of those, pages cited.
           */
          cited?: number;
        },
        {
          /**
           * Site type, for example "Review site".
           */
          type: string;
          /**
           * Pages of this type used.
           */
          sources: number;
          /**
           * Of those, pages cited.
           */
          cited?: number;
        },
        {
          /**
           * Site type, for example "Review site".
           */
          type: string;
          /**
           * Pages of this type used.
           */
          sources: number;
          /**
           * Of those, pages cited.
           */
          cited?: number;
        }
      ]
    | [
        {
          /**
           * Site type, for example "Review site".
           */
          type: string;
          /**
           * Pages of this type used.
           */
          sources: number;
          /**
           * Of those, pages cited.
           */
          cited?: number;
        },
        {
          /**
           * Site type, for example "Review site".
           */
          type: string;
          /**
           * Pages of this type used.
           */
          sources: number;
          /**
           * Of those, pages cited.
           */
          cited?: number;
        },
        {
          /**
           * Site type, for example "Review site".
           */
          type: string;
          /**
           * Pages of this type used.
           */
          sources: number;
          /**
           * Of those, pages cited.
           */
          cited?: number;
        },
        {
          /**
           * Site type, for example "Review site".
           */
          type: string;
          /**
           * Pages of this type used.
           */
          sources: number;
          /**
           * Of those, pages cited.
           */
          cited?: number;
        },
        {
          /**
           * Site type, for example "Review site".
           */
          type: string;
          /**
           * Pages of this type used.
           */
          sources: number;
          /**
           * Of those, pages cited.
           */
          cited?: number;
        },
        {
          /**
           * Site type, for example "Review site".
           */
          type: string;
          /**
           * Pages of this type used.
           */
          sources: number;
          /**
           * Of those, pages cited.
           */
          cited?: number;
        },
        {
          /**
           * Site type, for example "Review site".
           */
          type: string;
          /**
           * Pages of this type used.
           */
          sources: number;
          /**
           * Of those, pages cited.
           */
          cited?: number;
        },
        {
          /**
           * Site type, for example "Review site".
           */
          type: string;
          /**
           * Pages of this type used.
           */
          sources: number;
          /**
           * Of those, pages cited.
           */
          cited?: number;
        },
        {
          /**
           * Site type, for example "Review site".
           */
          type: string;
          /**
           * Pages of this type used.
           */
          sources: number;
          /**
           * Of those, pages cited.
           */
          cited?: number;
        },
        {
          /**
           * Site type, for example "Review site".
           */
          type: string;
          /**
           * Pages of this type used.
           */
          sources: number;
          /**
           * Of those, pages cited.
           */
          cited?: number;
        },
        {
          /**
           * Site type, for example "Review site".
           */
          type: string;
          /**
           * Pages of this type used.
           */
          sources: number;
          /**
           * Of those, pages cited.
           */
          cited?: number;
        },
        {
          /**
           * Site type, for example "Review site".
           */
          type: string;
          /**
           * Pages of this type used.
           */
          sources: number;
          /**
           * Of those, pages cited.
           */
          cited?: number;
        },
        {
          /**
           * Site type, for example "Review site".
           */
          type: string;
          /**
           * Pages of this type used.
           */
          sources: number;
          /**
           * Of those, pages cited.
           */
          cited?: number;
        },
        {
          /**
           * Site type, for example "Review site".
           */
          type: string;
          /**
           * Pages of this type used.
           */
          sources: number;
          /**
           * Of those, pages cited.
           */
          cited?: number;
        },
        {
          /**
           * Site type, for example "Review site".
           */
          type: string;
          /**
           * Pages of this type used.
           */
          sources: number;
          /**
           * Of those, pages cited.
           */
          cited?: number;
        }
      ]
    | [
        {
          /**
           * Site type, for example "Review site".
           */
          type: string;
          /**
           * Pages of this type used.
           */
          sources: number;
          /**
           * Of those, pages cited.
           */
          cited?: number;
        },
        {
          /**
           * Site type, for example "Review site".
           */
          type: string;
          /**
           * Pages of this type used.
           */
          sources: number;
          /**
           * Of those, pages cited.
           */
          cited?: number;
        },
        {
          /**
           * Site type, for example "Review site".
           */
          type: string;
          /**
           * Pages of this type used.
           */
          sources: number;
          /**
           * Of those, pages cited.
           */
          cited?: number;
        },
        {
          /**
           * Site type, for example "Review site".
           */
          type: string;
          /**
           * Pages of this type used.
           */
          sources: number;
          /**
           * Of those, pages cited.
           */
          cited?: number;
        },
        {
          /**
           * Site type, for example "Review site".
           */
          type: string;
          /**
           * Pages of this type used.
           */
          sources: number;
          /**
           * Of those, pages cited.
           */
          cited?: number;
        },
        {
          /**
           * Site type, for example "Review site".
           */
          type: string;
          /**
           * Pages of this type used.
           */
          sources: number;
          /**
           * Of those, pages cited.
           */
          cited?: number;
        },
        {
          /**
           * Site type, for example "Review site".
           */
          type: string;
          /**
           * Pages of this type used.
           */
          sources: number;
          /**
           * Of those, pages cited.
           */
          cited?: number;
        },
        {
          /**
           * Site type, for example "Review site".
           */
          type: string;
          /**
           * Pages of this type used.
           */
          sources: number;
          /**
           * Of those, pages cited.
           */
          cited?: number;
        },
        {
          /**
           * Site type, for example "Review site".
           */
          type: string;
          /**
           * Pages of this type used.
           */
          sources: number;
          /**
           * Of those, pages cited.
           */
          cited?: number;
        },
        {
          /**
           * Site type, for example "Review site".
           */
          type: string;
          /**
           * Pages of this type used.
           */
          sources: number;
          /**
           * Of those, pages cited.
           */
          cited?: number;
        },
        {
          /**
           * Site type, for example "Review site".
           */
          type: string;
          /**
           * Pages of this type used.
           */
          sources: number;
          /**
           * Of those, pages cited.
           */
          cited?: number;
        },
        {
          /**
           * Site type, for example "Review site".
           */
          type: string;
          /**
           * Pages of this type used.
           */
          sources: number;
          /**
           * Of those, pages cited.
           */
          cited?: number;
        },
        {
          /**
           * Site type, for example "Review site".
           */
          type: string;
          /**
           * Pages of this type used.
           */
          sources: number;
          /**
           * Of those, pages cited.
           */
          cited?: number;
        },
        {
          /**
           * Site type, for example "Review site".
           */
          type: string;
          /**
           * Pages of this type used.
           */
          sources: number;
          /**
           * Of those, pages cited.
           */
          cited?: number;
        },
        {
          /**
           * Site type, for example "Review site".
           */
          type: string;
          /**
           * Pages of this type used.
           */
          sources: number;
          /**
           * Of those, pages cited.
           */
          cited?: number;
        },
        {
          /**
           * Site type, for example "Review site".
           */
          type: string;
          /**
           * Pages of this type used.
           */
          sources: number;
          /**
           * Of those, pages cited.
           */
          cited?: number;
        }
      ]
    | [
        {
          /**
           * Site type, for example "Review site".
           */
          type: string;
          /**
           * Pages of this type used.
           */
          sources: number;
          /**
           * Of those, pages cited.
           */
          cited?: number;
        },
        {
          /**
           * Site type, for example "Review site".
           */
          type: string;
          /**
           * Pages of this type used.
           */
          sources: number;
          /**
           * Of those, pages cited.
           */
          cited?: number;
        },
        {
          /**
           * Site type, for example "Review site".
           */
          type: string;
          /**
           * Pages of this type used.
           */
          sources: number;
          /**
           * Of those, pages cited.
           */
          cited?: number;
        },
        {
          /**
           * Site type, for example "Review site".
           */
          type: string;
          /**
           * Pages of this type used.
           */
          sources: number;
          /**
           * Of those, pages cited.
           */
          cited?: number;
        },
        {
          /**
           * Site type, for example "Review site".
           */
          type: string;
          /**
           * Pages of this type used.
           */
          sources: number;
          /**
           * Of those, pages cited.
           */
          cited?: number;
        },
        {
          /**
           * Site type, for example "Review site".
           */
          type: string;
          /**
           * Pages of this type used.
           */
          sources: number;
          /**
           * Of those, pages cited.
           */
          cited?: number;
        },
        {
          /**
           * Site type, for example "Review site".
           */
          type: string;
          /**
           * Pages of this type used.
           */
          sources: number;
          /**
           * Of those, pages cited.
           */
          cited?: number;
        },
        {
          /**
           * Site type, for example "Review site".
           */
          type: string;
          /**
           * Pages of this type used.
           */
          sources: number;
          /**
           * Of those, pages cited.
           */
          cited?: number;
        },
        {
          /**
           * Site type, for example "Review site".
           */
          type: string;
          /**
           * Pages of this type used.
           */
          sources: number;
          /**
           * Of those, pages cited.
           */
          cited?: number;
        },
        {
          /**
           * Site type, for example "Review site".
           */
          type: string;
          /**
           * Pages of this type used.
           */
          sources: number;
          /**
           * Of those, pages cited.
           */
          cited?: number;
        },
        {
          /**
           * Site type, for example "Review site".
           */
          type: string;
          /**
           * Pages of this type used.
           */
          sources: number;
          /**
           * Of those, pages cited.
           */
          cited?: number;
        },
        {
          /**
           * Site type, for example "Review site".
           */
          type: string;
          /**
           * Pages of this type used.
           */
          sources: number;
          /**
           * Of those, pages cited.
           */
          cited?: number;
        },
        {
          /**
           * Site type, for example "Review site".
           */
          type: string;
          /**
           * Pages of this type used.
           */
          sources: number;
          /**
           * Of those, pages cited.
           */
          cited?: number;
        },
        {
          /**
           * Site type, for example "Review site".
           */
          type: string;
          /**
           * Pages of this type used.
           */
          sources: number;
          /**
           * Of those, pages cited.
           */
          cited?: number;
        },
        {
          /**
           * Site type, for example "Review site".
           */
          type: string;
          /**
           * Pages of this type used.
           */
          sources: number;
          /**
           * Of those, pages cited.
           */
          cited?: number;
        },
        {
          /**
           * Site type, for example "Review site".
           */
          type: string;
          /**
           * Pages of this type used.
           */
          sources: number;
          /**
           * Of those, pages cited.
           */
          cited?: number;
        },
        {
          /**
           * Site type, for example "Review site".
           */
          type: string;
          /**
           * Pages of this type used.
           */
          sources: number;
          /**
           * Of those, pages cited.
           */
          cited?: number;
        }
      ]
    | [
        {
          /**
           * Site type, for example "Review site".
           */
          type: string;
          /**
           * Pages of this type used.
           */
          sources: number;
          /**
           * Of those, pages cited.
           */
          cited?: number;
        },
        {
          /**
           * Site type, for example "Review site".
           */
          type: string;
          /**
           * Pages of this type used.
           */
          sources: number;
          /**
           * Of those, pages cited.
           */
          cited?: number;
        },
        {
          /**
           * Site type, for example "Review site".
           */
          type: string;
          /**
           * Pages of this type used.
           */
          sources: number;
          /**
           * Of those, pages cited.
           */
          cited?: number;
        },
        {
          /**
           * Site type, for example "Review site".
           */
          type: string;
          /**
           * Pages of this type used.
           */
          sources: number;
          /**
           * Of those, pages cited.
           */
          cited?: number;
        },
        {
          /**
           * Site type, for example "Review site".
           */
          type: string;
          /**
           * Pages of this type used.
           */
          sources: number;
          /**
           * Of those, pages cited.
           */
          cited?: number;
        },
        {
          /**
           * Site type, for example "Review site".
           */
          type: string;
          /**
           * Pages of this type used.
           */
          sources: number;
          /**
           * Of those, pages cited.
           */
          cited?: number;
        },
        {
          /**
           * Site type, for example "Review site".
           */
          type: string;
          /**
           * Pages of this type used.
           */
          sources: number;
          /**
           * Of those, pages cited.
           */
          cited?: number;
        },
        {
          /**
           * Site type, for example "Review site".
           */
          type: string;
          /**
           * Pages of this type used.
           */
          sources: number;
          /**
           * Of those, pages cited.
           */
          cited?: number;
        },
        {
          /**
           * Site type, for example "Review site".
           */
          type: string;
          /**
           * Pages of this type used.
           */
          sources: number;
          /**
           * Of those, pages cited.
           */
          cited?: number;
        },
        {
          /**
           * Site type, for example "Review site".
           */
          type: string;
          /**
           * Pages of this type used.
           */
          sources: number;
          /**
           * Of those, pages cited.
           */
          cited?: number;
        },
        {
          /**
           * Site type, for example "Review site".
           */
          type: string;
          /**
           * Pages of this type used.
           */
          sources: number;
          /**
           * Of those, pages cited.
           */
          cited?: number;
        },
        {
          /**
           * Site type, for example "Review site".
           */
          type: string;
          /**
           * Pages of this type used.
           */
          sources: number;
          /**
           * Of those, pages cited.
           */
          cited?: number;
        },
        {
          /**
           * Site type, for example "Review site".
           */
          type: string;
          /**
           * Pages of this type used.
           */
          sources: number;
          /**
           * Of those, pages cited.
           */
          cited?: number;
        },
        {
          /**
           * Site type, for example "Review site".
           */
          type: string;
          /**
           * Pages of this type used.
           */
          sources: number;
          /**
           * Of those, pages cited.
           */
          cited?: number;
        },
        {
          /**
           * Site type, for example "Review site".
           */
          type: string;
          /**
           * Pages of this type used.
           */
          sources: number;
          /**
           * Of those, pages cited.
           */
          cited?: number;
        },
        {
          /**
           * Site type, for example "Review site".
           */
          type: string;
          /**
           * Pages of this type used.
           */
          sources: number;
          /**
           * Of those, pages cited.
           */
          cited?: number;
        },
        {
          /**
           * Site type, for example "Review site".
           */
          type: string;
          /**
           * Pages of this type used.
           */
          sources: number;
          /**
           * Of those, pages cited.
           */
          cited?: number;
        },
        {
          /**
           * Site type, for example "Review site".
           */
          type: string;
          /**
           * Pages of this type used.
           */
          sources: number;
          /**
           * Of those, pages cited.
           */
          cited?: number;
        }
      ]
    | [
        {
          /**
           * Site type, for example "Review site".
           */
          type: string;
          /**
           * Pages of this type used.
           */
          sources: number;
          /**
           * Of those, pages cited.
           */
          cited?: number;
        },
        {
          /**
           * Site type, for example "Review site".
           */
          type: string;
          /**
           * Pages of this type used.
           */
          sources: number;
          /**
           * Of those, pages cited.
           */
          cited?: number;
        },
        {
          /**
           * Site type, for example "Review site".
           */
          type: string;
          /**
           * Pages of this type used.
           */
          sources: number;
          /**
           * Of those, pages cited.
           */
          cited?: number;
        },
        {
          /**
           * Site type, for example "Review site".
           */
          type: string;
          /**
           * Pages of this type used.
           */
          sources: number;
          /**
           * Of those, pages cited.
           */
          cited?: number;
        },
        {
          /**
           * Site type, for example "Review site".
           */
          type: string;
          /**
           * Pages of this type used.
           */
          sources: number;
          /**
           * Of those, pages cited.
           */
          cited?: number;
        },
        {
          /**
           * Site type, for example "Review site".
           */
          type: string;
          /**
           * Pages of this type used.
           */
          sources: number;
          /**
           * Of those, pages cited.
           */
          cited?: number;
        },
        {
          /**
           * Site type, for example "Review site".
           */
          type: string;
          /**
           * Pages of this type used.
           */
          sources: number;
          /**
           * Of those, pages cited.
           */
          cited?: number;
        },
        {
          /**
           * Site type, for example "Review site".
           */
          type: string;
          /**
           * Pages of this type used.
           */
          sources: number;
          /**
           * Of those, pages cited.
           */
          cited?: number;
        },
        {
          /**
           * Site type, for example "Review site".
           */
          type: string;
          /**
           * Pages of this type used.
           */
          sources: number;
          /**
           * Of those, pages cited.
           */
          cited?: number;
        },
        {
          /**
           * Site type, for example "Review site".
           */
          type: string;
          /**
           * Pages of this type used.
           */
          sources: number;
          /**
           * Of those, pages cited.
           */
          cited?: number;
        },
        {
          /**
           * Site type, for example "Review site".
           */
          type: string;
          /**
           * Pages of this type used.
           */
          sources: number;
          /**
           * Of those, pages cited.
           */
          cited?: number;
        },
        {
          /**
           * Site type, for example "Review site".
           */
          type: string;
          /**
           * Pages of this type used.
           */
          sources: number;
          /**
           * Of those, pages cited.
           */
          cited?: number;
        },
        {
          /**
           * Site type, for example "Review site".
           */
          type: string;
          /**
           * Pages of this type used.
           */
          sources: number;
          /**
           * Of those, pages cited.
           */
          cited?: number;
        },
        {
          /**
           * Site type, for example "Review site".
           */
          type: string;
          /**
           * Pages of this type used.
           */
          sources: number;
          /**
           * Of those, pages cited.
           */
          cited?: number;
        },
        {
          /**
           * Site type, for example "Review site".
           */
          type: string;
          /**
           * Pages of this type used.
           */
          sources: number;
          /**
           * Of those, pages cited.
           */
          cited?: number;
        },
        {
          /**
           * Site type, for example "Review site".
           */
          type: string;
          /**
           * Pages of this type used.
           */
          sources: number;
          /**
           * Of those, pages cited.
           */
          cited?: number;
        },
        {
          /**
           * Site type, for example "Review site".
           */
          type: string;
          /**
           * Pages of this type used.
           */
          sources: number;
          /**
           * Of those, pages cited.
           */
          cited?: number;
        },
        {
          /**
           * Site type, for example "Review site".
           */
          type: string;
          /**
           * Pages of this type used.
           */
          sources: number;
          /**
           * Of those, pages cited.
           */
          cited?: number;
        },
        {
          /**
           * Site type, for example "Review site".
           */
          type: string;
          /**
           * Pages of this type used.
           */
          sources: number;
          /**
           * Of those, pages cited.
           */
          cited?: number;
        }
      ]
    | [
        {
          /**
           * Site type, for example "Review site".
           */
          type: string;
          /**
           * Pages of this type used.
           */
          sources: number;
          /**
           * Of those, pages cited.
           */
          cited?: number;
        },
        {
          /**
           * Site type, for example "Review site".
           */
          type: string;
          /**
           * Pages of this type used.
           */
          sources: number;
          /**
           * Of those, pages cited.
           */
          cited?: number;
        },
        {
          /**
           * Site type, for example "Review site".
           */
          type: string;
          /**
           * Pages of this type used.
           */
          sources: number;
          /**
           * Of those, pages cited.
           */
          cited?: number;
        },
        {
          /**
           * Site type, for example "Review site".
           */
          type: string;
          /**
           * Pages of this type used.
           */
          sources: number;
          /**
           * Of those, pages cited.
           */
          cited?: number;
        },
        {
          /**
           * Site type, for example "Review site".
           */
          type: string;
          /**
           * Pages of this type used.
           */
          sources: number;
          /**
           * Of those, pages cited.
           */
          cited?: number;
        },
        {
          /**
           * Site type, for example "Review site".
           */
          type: string;
          /**
           * Pages of this type used.
           */
          sources: number;
          /**
           * Of those, pages cited.
           */
          cited?: number;
        },
        {
          /**
           * Site type, for example "Review site".
           */
          type: string;
          /**
           * Pages of this type used.
           */
          sources: number;
          /**
           * Of those, pages cited.
           */
          cited?: number;
        },
        {
          /**
           * Site type, for example "Review site".
           */
          type: string;
          /**
           * Pages of this type used.
           */
          sources: number;
          /**
           * Of those, pages cited.
           */
          cited?: number;
        },
        {
          /**
           * Site type, for example "Review site".
           */
          type: string;
          /**
           * Pages of this type used.
           */
          sources: number;
          /**
           * Of those, pages cited.
           */
          cited?: number;
        },
        {
          /**
           * Site type, for example "Review site".
           */
          type: string;
          /**
           * Pages of this type used.
           */
          sources: number;
          /**
           * Of those, pages cited.
           */
          cited?: number;
        },
        {
          /**
           * Site type, for example "Review site".
           */
          type: string;
          /**
           * Pages of this type used.
           */
          sources: number;
          /**
           * Of those, pages cited.
           */
          cited?: number;
        },
        {
          /**
           * Site type, for example "Review site".
           */
          type: string;
          /**
           * Pages of this type used.
           */
          sources: number;
          /**
           * Of those, pages cited.
           */
          cited?: number;
        },
        {
          /**
           * Site type, for example "Review site".
           */
          type: string;
          /**
           * Pages of this type used.
           */
          sources: number;
          /**
           * Of those, pages cited.
           */
          cited?: number;
        },
        {
          /**
           * Site type, for example "Review site".
           */
          type: string;
          /**
           * Pages of this type used.
           */
          sources: number;
          /**
           * Of those, pages cited.
           */
          cited?: number;
        },
        {
          /**
           * Site type, for example "Review site".
           */
          type: string;
          /**
           * Pages of this type used.
           */
          sources: number;
          /**
           * Of those, pages cited.
           */
          cited?: number;
        },
        {
          /**
           * Site type, for example "Review site".
           */
          type: string;
          /**
           * Pages of this type used.
           */
          sources: number;
          /**
           * Of those, pages cited.
           */
          cited?: number;
        },
        {
          /**
           * Site type, for example "Review site".
           */
          type: string;
          /**
           * Pages of this type used.
           */
          sources: number;
          /**
           * Of those, pages cited.
           */
          cited?: number;
        },
        {
          /**
           * Site type, for example "Review site".
           */
          type: string;
          /**
           * Pages of this type used.
           */
          sources: number;
          /**
           * Of those, pages cited.
           */
          cited?: number;
        },
        {
          /**
           * Site type, for example "Review site".
           */
          type: string;
          /**
           * Pages of this type used.
           */
          sources: number;
          /**
           * Of those, pages cited.
           */
          cited?: number;
        },
        {
          /**
           * Site type, for example "Review site".
           */
          type: string;
          /**
           * Pages of this type used.
           */
          sources: number;
          /**
           * Of those, pages cited.
           */
          cited?: number;
        }
      ];
  /**
   * Domains that appeared most often.
   *
   * @maxItems 100
   */
  topSources?: {
    /**
     * Source domain.
     */
    domain: string;
    /**
     * Site type of this domain.
     */
    siteType?: string;
    /**
     * Answers it appeared in.
     */
    answers: number;
    /**
     * Answers that cited it.
     */
    cited?: number;
  }[];
  /**
   * The assistants' own searches, when shown.
   *
   * @maxItems 100
   */
  searchQueries?: {
    /**
     * A search an assistant ran.
     */
    query: string;
    /**
     * How many answers ran this search.
     */
    count?: number;
  }[];
  /**
   * Written analysis. State only what the figures support.
   *
   * @maxItems 12
   */
  writeUps?:
    | []
    | [
        {
          /**
           * Section heading.
           */
          heading: string;
          /**
           * Plain text: blank line = paragraph, "- " = list item, **bold**.
           */
          body: string;
        }
      ]
    | [
        {
          /**
           * Section heading.
           */
          heading: string;
          /**
           * Plain text: blank line = paragraph, "- " = list item, **bold**.
           */
          body: string;
        },
        {
          /**
           * Section heading.
           */
          heading: string;
          /**
           * Plain text: blank line = paragraph, "- " = list item, **bold**.
           */
          body: string;
        }
      ]
    | [
        {
          /**
           * Section heading.
           */
          heading: string;
          /**
           * Plain text: blank line = paragraph, "- " = list item, **bold**.
           */
          body: string;
        },
        {
          /**
           * Section heading.
           */
          heading: string;
          /**
           * Plain text: blank line = paragraph, "- " = list item, **bold**.
           */
          body: string;
        },
        {
          /**
           * Section heading.
           */
          heading: string;
          /**
           * Plain text: blank line = paragraph, "- " = list item, **bold**.
           */
          body: string;
        }
      ]
    | [
        {
          /**
           * Section heading.
           */
          heading: string;
          /**
           * Plain text: blank line = paragraph, "- " = list item, **bold**.
           */
          body: string;
        },
        {
          /**
           * Section heading.
           */
          heading: string;
          /**
           * Plain text: blank line = paragraph, "- " = list item, **bold**.
           */
          body: string;
        },
        {
          /**
           * Section heading.
           */
          heading: string;
          /**
           * Plain text: blank line = paragraph, "- " = list item, **bold**.
           */
          body: string;
        },
        {
          /**
           * Section heading.
           */
          heading: string;
          /**
           * Plain text: blank line = paragraph, "- " = list item, **bold**.
           */
          body: string;
        }
      ]
    | [
        {
          /**
           * Section heading.
           */
          heading: string;
          /**
           * Plain text: blank line = paragraph, "- " = list item, **bold**.
           */
          body: string;
        },
        {
          /**
           * Section heading.
           */
          heading: string;
          /**
           * Plain text: blank line = paragraph, "- " = list item, **bold**.
           */
          body: string;
        },
        {
          /**
           * Section heading.
           */
          heading: string;
          /**
           * Plain text: blank line = paragraph, "- " = list item, **bold**.
           */
          body: string;
        },
        {
          /**
           * Section heading.
           */
          heading: string;
          /**
           * Plain text: blank line = paragraph, "- " = list item, **bold**.
           */
          body: string;
        },
        {
          /**
           * Section heading.
           */
          heading: string;
          /**
           * Plain text: blank line = paragraph, "- " = list item, **bold**.
           */
          body: string;
        }
      ]
    | [
        {
          /**
           * Section heading.
           */
          heading: string;
          /**
           * Plain text: blank line = paragraph, "- " = list item, **bold**.
           */
          body: string;
        },
        {
          /**
           * Section heading.
           */
          heading: string;
          /**
           * Plain text: blank line = paragraph, "- " = list item, **bold**.
           */
          body: string;
        },
        {
          /**
           * Section heading.
           */
          heading: string;
          /**
           * Plain text: blank line = paragraph, "- " = list item, **bold**.
           */
          body: string;
        },
        {
          /**
           * Section heading.
           */
          heading: string;
          /**
           * Plain text: blank line = paragraph, "- " = list item, **bold**.
           */
          body: string;
        },
        {
          /**
           * Section heading.
           */
          heading: string;
          /**
           * Plain text: blank line = paragraph, "- " = list item, **bold**.
           */
          body: string;
        },
        {
          /**
           * Section heading.
           */
          heading: string;
          /**
           * Plain text: blank line = paragraph, "- " = list item, **bold**.
           */
          body: string;
        }
      ]
    | [
        {
          /**
           * Section heading.
           */
          heading: string;
          /**
           * Plain text: blank line = paragraph, "- " = list item, **bold**.
           */
          body: string;
        },
        {
          /**
           * Section heading.
           */
          heading: string;
          /**
           * Plain text: blank line = paragraph, "- " = list item, **bold**.
           */
          body: string;
        },
        {
          /**
           * Section heading.
           */
          heading: string;
          /**
           * Plain text: blank line = paragraph, "- " = list item, **bold**.
           */
          body: string;
        },
        {
          /**
           * Section heading.
           */
          heading: string;
          /**
           * Plain text: blank line = paragraph, "- " = list item, **bold**.
           */
          body: string;
        },
        {
          /**
           * Section heading.
           */
          heading: string;
          /**
           * Plain text: blank line = paragraph, "- " = list item, **bold**.
           */
          body: string;
        },
        {
          /**
           * Section heading.
           */
          heading: string;
          /**
           * Plain text: blank line = paragraph, "- " = list item, **bold**.
           */
          body: string;
        },
        {
          /**
           * Section heading.
           */
          heading: string;
          /**
           * Plain text: blank line = paragraph, "- " = list item, **bold**.
           */
          body: string;
        }
      ]
    | [
        {
          /**
           * Section heading.
           */
          heading: string;
          /**
           * Plain text: blank line = paragraph, "- " = list item, **bold**.
           */
          body: string;
        },
        {
          /**
           * Section heading.
           */
          heading: string;
          /**
           * Plain text: blank line = paragraph, "- " = list item, **bold**.
           */
          body: string;
        },
        {
          /**
           * Section heading.
           */
          heading: string;
          /**
           * Plain text: blank line = paragraph, "- " = list item, **bold**.
           */
          body: string;
        },
        {
          /**
           * Section heading.
           */
          heading: string;
          /**
           * Plain text: blank line = paragraph, "- " = list item, **bold**.
           */
          body: string;
        },
        {
          /**
           * Section heading.
           */
          heading: string;
          /**
           * Plain text: blank line = paragraph, "- " = list item, **bold**.
           */
          body: string;
        },
        {
          /**
           * Section heading.
           */
          heading: string;
          /**
           * Plain text: blank line = paragraph, "- " = list item, **bold**.
           */
          body: string;
        },
        {
          /**
           * Section heading.
           */
          heading: string;
          /**
           * Plain text: blank line = paragraph, "- " = list item, **bold**.
           */
          body: string;
        },
        {
          /**
           * Section heading.
           */
          heading: string;
          /**
           * Plain text: blank line = paragraph, "- " = list item, **bold**.
           */
          body: string;
        }
      ]
    | [
        {
          /**
           * Section heading.
           */
          heading: string;
          /**
           * Plain text: blank line = paragraph, "- " = list item, **bold**.
           */
          body: string;
        },
        {
          /**
           * Section heading.
           */
          heading: string;
          /**
           * Plain text: blank line = paragraph, "- " = list item, **bold**.
           */
          body: string;
        },
        {
          /**
           * Section heading.
           */
          heading: string;
          /**
           * Plain text: blank line = paragraph, "- " = list item, **bold**.
           */
          body: string;
        },
        {
          /**
           * Section heading.
           */
          heading: string;
          /**
           * Plain text: blank line = paragraph, "- " = list item, **bold**.
           */
          body: string;
        },
        {
          /**
           * Section heading.
           */
          heading: string;
          /**
           * Plain text: blank line = paragraph, "- " = list item, **bold**.
           */
          body: string;
        },
        {
          /**
           * Section heading.
           */
          heading: string;
          /**
           * Plain text: blank line = paragraph, "- " = list item, **bold**.
           */
          body: string;
        },
        {
          /**
           * Section heading.
           */
          heading: string;
          /**
           * Plain text: blank line = paragraph, "- " = list item, **bold**.
           */
          body: string;
        },
        {
          /**
           * Section heading.
           */
          heading: string;
          /**
           * Plain text: blank line = paragraph, "- " = list item, **bold**.
           */
          body: string;
        },
        {
          /**
           * Section heading.
           */
          heading: string;
          /**
           * Plain text: blank line = paragraph, "- " = list item, **bold**.
           */
          body: string;
        }
      ]
    | [
        {
          /**
           * Section heading.
           */
          heading: string;
          /**
           * Plain text: blank line = paragraph, "- " = list item, **bold**.
           */
          body: string;
        },
        {
          /**
           * Section heading.
           */
          heading: string;
          /**
           * Plain text: blank line = paragraph, "- " = list item, **bold**.
           */
          body: string;
        },
        {
          /**
           * Section heading.
           */
          heading: string;
          /**
           * Plain text: blank line = paragraph, "- " = list item, **bold**.
           */
          body: string;
        },
        {
          /**
           * Section heading.
           */
          heading: string;
          /**
           * Plain text: blank line = paragraph, "- " = list item, **bold**.
           */
          body: string;
        },
        {
          /**
           * Section heading.
           */
          heading: string;
          /**
           * Plain text: blank line = paragraph, "- " = list item, **bold**.
           */
          body: string;
        },
        {
          /**
           * Section heading.
           */
          heading: string;
          /**
           * Plain text: blank line = paragraph, "- " = list item, **bold**.
           */
          body: string;
        },
        {
          /**
           * Section heading.
           */
          heading: string;
          /**
           * Plain text: blank line = paragraph, "- " = list item, **bold**.
           */
          body: string;
        },
        {
          /**
           * Section heading.
           */
          heading: string;
          /**
           * Plain text: blank line = paragraph, "- " = list item, **bold**.
           */
          body: string;
        },
        {
          /**
           * Section heading.
           */
          heading: string;
          /**
           * Plain text: blank line = paragraph, "- " = list item, **bold**.
           */
          body: string;
        },
        {
          /**
           * Section heading.
           */
          heading: string;
          /**
           * Plain text: blank line = paragraph, "- " = list item, **bold**.
           */
          body: string;
        }
      ]
    | [
        {
          /**
           * Section heading.
           */
          heading: string;
          /**
           * Plain text: blank line = paragraph, "- " = list item, **bold**.
           */
          body: string;
        },
        {
          /**
           * Section heading.
           */
          heading: string;
          /**
           * Plain text: blank line = paragraph, "- " = list item, **bold**.
           */
          body: string;
        },
        {
          /**
           * Section heading.
           */
          heading: string;
          /**
           * Plain text: blank line = paragraph, "- " = list item, **bold**.
           */
          body: string;
        },
        {
          /**
           * Section heading.
           */
          heading: string;
          /**
           * Plain text: blank line = paragraph, "- " = list item, **bold**.
           */
          body: string;
        },
        {
          /**
           * Section heading.
           */
          heading: string;
          /**
           * Plain text: blank line = paragraph, "- " = list item, **bold**.
           */
          body: string;
        },
        {
          /**
           * Section heading.
           */
          heading: string;
          /**
           * Plain text: blank line = paragraph, "- " = list item, **bold**.
           */
          body: string;
        },
        {
          /**
           * Section heading.
           */
          heading: string;
          /**
           * Plain text: blank line = paragraph, "- " = list item, **bold**.
           */
          body: string;
        },
        {
          /**
           * Section heading.
           */
          heading: string;
          /**
           * Plain text: blank line = paragraph, "- " = list item, **bold**.
           */
          body: string;
        },
        {
          /**
           * Section heading.
           */
          heading: string;
          /**
           * Plain text: blank line = paragraph, "- " = list item, **bold**.
           */
          body: string;
        },
        {
          /**
           * Section heading.
           */
          heading: string;
          /**
           * Plain text: blank line = paragraph, "- " = list item, **bold**.
           */
          body: string;
        },
        {
          /**
           * Section heading.
           */
          heading: string;
          /**
           * Plain text: blank line = paragraph, "- " = list item, **bold**.
           */
          body: string;
        }
      ]
    | [
        {
          /**
           * Section heading.
           */
          heading: string;
          /**
           * Plain text: blank line = paragraph, "- " = list item, **bold**.
           */
          body: string;
        },
        {
          /**
           * Section heading.
           */
          heading: string;
          /**
           * Plain text: blank line = paragraph, "- " = list item, **bold**.
           */
          body: string;
        },
        {
          /**
           * Section heading.
           */
          heading: string;
          /**
           * Plain text: blank line = paragraph, "- " = list item, **bold**.
           */
          body: string;
        },
        {
          /**
           * Section heading.
           */
          heading: string;
          /**
           * Plain text: blank line = paragraph, "- " = list item, **bold**.
           */
          body: string;
        },
        {
          /**
           * Section heading.
           */
          heading: string;
          /**
           * Plain text: blank line = paragraph, "- " = list item, **bold**.
           */
          body: string;
        },
        {
          /**
           * Section heading.
           */
          heading: string;
          /**
           * Plain text: blank line = paragraph, "- " = list item, **bold**.
           */
          body: string;
        },
        {
          /**
           * Section heading.
           */
          heading: string;
          /**
           * Plain text: blank line = paragraph, "- " = list item, **bold**.
           */
          body: string;
        },
        {
          /**
           * Section heading.
           */
          heading: string;
          /**
           * Plain text: blank line = paragraph, "- " = list item, **bold**.
           */
          body: string;
        },
        {
          /**
           * Section heading.
           */
          heading: string;
          /**
           * Plain text: blank line = paragraph, "- " = list item, **bold**.
           */
          body: string;
        },
        {
          /**
           * Section heading.
           */
          heading: string;
          /**
           * Plain text: blank line = paragraph, "- " = list item, **bold**.
           */
          body: string;
        },
        {
          /**
           * Section heading.
           */
          heading: string;
          /**
           * Plain text: blank line = paragraph, "- " = list item, **bold**.
           */
          body: string;
        },
        {
          /**
           * Section heading.
           */
          heading: string;
          /**
           * Plain text: blank line = paragraph, "- " = list item, **bold**.
           */
          body: string;
        }
      ];
  /**
   * Recommended next steps, most important first.
   *
   * @maxItems 12
   */
  recommendations?:
    | []
    | [
        {
          /**
           * What to do.
           */
          title: string;
          /**
           * Why, citing evidence in this report.
           */
          detail: string;
        }
      ]
    | [
        {
          /**
           * What to do.
           */
          title: string;
          /**
           * Why, citing evidence in this report.
           */
          detail: string;
        },
        {
          /**
           * What to do.
           */
          title: string;
          /**
           * Why, citing evidence in this report.
           */
          detail: string;
        }
      ]
    | [
        {
          /**
           * What to do.
           */
          title: string;
          /**
           * Why, citing evidence in this report.
           */
          detail: string;
        },
        {
          /**
           * What to do.
           */
          title: string;
          /**
           * Why, citing evidence in this report.
           */
          detail: string;
        },
        {
          /**
           * What to do.
           */
          title: string;
          /**
           * Why, citing evidence in this report.
           */
          detail: string;
        }
      ]
    | [
        {
          /**
           * What to do.
           */
          title: string;
          /**
           * Why, citing evidence in this report.
           */
          detail: string;
        },
        {
          /**
           * What to do.
           */
          title: string;
          /**
           * Why, citing evidence in this report.
           */
          detail: string;
        },
        {
          /**
           * What to do.
           */
          title: string;
          /**
           * Why, citing evidence in this report.
           */
          detail: string;
        },
        {
          /**
           * What to do.
           */
          title: string;
          /**
           * Why, citing evidence in this report.
           */
          detail: string;
        }
      ]
    | [
        {
          /**
           * What to do.
           */
          title: string;
          /**
           * Why, citing evidence in this report.
           */
          detail: string;
        },
        {
          /**
           * What to do.
           */
          title: string;
          /**
           * Why, citing evidence in this report.
           */
          detail: string;
        },
        {
          /**
           * What to do.
           */
          title: string;
          /**
           * Why, citing evidence in this report.
           */
          detail: string;
        },
        {
          /**
           * What to do.
           */
          title: string;
          /**
           * Why, citing evidence in this report.
           */
          detail: string;
        },
        {
          /**
           * What to do.
           */
          title: string;
          /**
           * Why, citing evidence in this report.
           */
          detail: string;
        }
      ]
    | [
        {
          /**
           * What to do.
           */
          title: string;
          /**
           * Why, citing evidence in this report.
           */
          detail: string;
        },
        {
          /**
           * What to do.
           */
          title: string;
          /**
           * Why, citing evidence in this report.
           */
          detail: string;
        },
        {
          /**
           * What to do.
           */
          title: string;
          /**
           * Why, citing evidence in this report.
           */
          detail: string;
        },
        {
          /**
           * What to do.
           */
          title: string;
          /**
           * Why, citing evidence in this report.
           */
          detail: string;
        },
        {
          /**
           * What to do.
           */
          title: string;
          /**
           * Why, citing evidence in this report.
           */
          detail: string;
        },
        {
          /**
           * What to do.
           */
          title: string;
          /**
           * Why, citing evidence in this report.
           */
          detail: string;
        }
      ]
    | [
        {
          /**
           * What to do.
           */
          title: string;
          /**
           * Why, citing evidence in this report.
           */
          detail: string;
        },
        {
          /**
           * What to do.
           */
          title: string;
          /**
           * Why, citing evidence in this report.
           */
          detail: string;
        },
        {
          /**
           * What to do.
           */
          title: string;
          /**
           * Why, citing evidence in this report.
           */
          detail: string;
        },
        {
          /**
           * What to do.
           */
          title: string;
          /**
           * Why, citing evidence in this report.
           */
          detail: string;
        },
        {
          /**
           * What to do.
           */
          title: string;
          /**
           * Why, citing evidence in this report.
           */
          detail: string;
        },
        {
          /**
           * What to do.
           */
          title: string;
          /**
           * Why, citing evidence in this report.
           */
          detail: string;
        },
        {
          /**
           * What to do.
           */
          title: string;
          /**
           * Why, citing evidence in this report.
           */
          detail: string;
        }
      ]
    | [
        {
          /**
           * What to do.
           */
          title: string;
          /**
           * Why, citing evidence in this report.
           */
          detail: string;
        },
        {
          /**
           * What to do.
           */
          title: string;
          /**
           * Why, citing evidence in this report.
           */
          detail: string;
        },
        {
          /**
           * What to do.
           */
          title: string;
          /**
           * Why, citing evidence in this report.
           */
          detail: string;
        },
        {
          /**
           * What to do.
           */
          title: string;
          /**
           * Why, citing evidence in this report.
           */
          detail: string;
        },
        {
          /**
           * What to do.
           */
          title: string;
          /**
           * Why, citing evidence in this report.
           */
          detail: string;
        },
        {
          /**
           * What to do.
           */
          title: string;
          /**
           * Why, citing evidence in this report.
           */
          detail: string;
        },
        {
          /**
           * What to do.
           */
          title: string;
          /**
           * Why, citing evidence in this report.
           */
          detail: string;
        },
        {
          /**
           * What to do.
           */
          title: string;
          /**
           * Why, citing evidence in this report.
           */
          detail: string;
        }
      ]
    | [
        {
          /**
           * What to do.
           */
          title: string;
          /**
           * Why, citing evidence in this report.
           */
          detail: string;
        },
        {
          /**
           * What to do.
           */
          title: string;
          /**
           * Why, citing evidence in this report.
           */
          detail: string;
        },
        {
          /**
           * What to do.
           */
          title: string;
          /**
           * Why, citing evidence in this report.
           */
          detail: string;
        },
        {
          /**
           * What to do.
           */
          title: string;
          /**
           * Why, citing evidence in this report.
           */
          detail: string;
        },
        {
          /**
           * What to do.
           */
          title: string;
          /**
           * Why, citing evidence in this report.
           */
          detail: string;
        },
        {
          /**
           * What to do.
           */
          title: string;
          /**
           * Why, citing evidence in this report.
           */
          detail: string;
        },
        {
          /**
           * What to do.
           */
          title: string;
          /**
           * Why, citing evidence in this report.
           */
          detail: string;
        },
        {
          /**
           * What to do.
           */
          title: string;
          /**
           * Why, citing evidence in this report.
           */
          detail: string;
        },
        {
          /**
           * What to do.
           */
          title: string;
          /**
           * Why, citing evidence in this report.
           */
          detail: string;
        }
      ]
    | [
        {
          /**
           * What to do.
           */
          title: string;
          /**
           * Why, citing evidence in this report.
           */
          detail: string;
        },
        {
          /**
           * What to do.
           */
          title: string;
          /**
           * Why, citing evidence in this report.
           */
          detail: string;
        },
        {
          /**
           * What to do.
           */
          title: string;
          /**
           * Why, citing evidence in this report.
           */
          detail: string;
        },
        {
          /**
           * What to do.
           */
          title: string;
          /**
           * Why, citing evidence in this report.
           */
          detail: string;
        },
        {
          /**
           * What to do.
           */
          title: string;
          /**
           * Why, citing evidence in this report.
           */
          detail: string;
        },
        {
          /**
           * What to do.
           */
          title: string;
          /**
           * Why, citing evidence in this report.
           */
          detail: string;
        },
        {
          /**
           * What to do.
           */
          title: string;
          /**
           * Why, citing evidence in this report.
           */
          detail: string;
        },
        {
          /**
           * What to do.
           */
          title: string;
          /**
           * Why, citing evidence in this report.
           */
          detail: string;
        },
        {
          /**
           * What to do.
           */
          title: string;
          /**
           * Why, citing evidence in this report.
           */
          detail: string;
        },
        {
          /**
           * What to do.
           */
          title: string;
          /**
           * Why, citing evidence in this report.
           */
          detail: string;
        }
      ]
    | [
        {
          /**
           * What to do.
           */
          title: string;
          /**
           * Why, citing evidence in this report.
           */
          detail: string;
        },
        {
          /**
           * What to do.
           */
          title: string;
          /**
           * Why, citing evidence in this report.
           */
          detail: string;
        },
        {
          /**
           * What to do.
           */
          title: string;
          /**
           * Why, citing evidence in this report.
           */
          detail: string;
        },
        {
          /**
           * What to do.
           */
          title: string;
          /**
           * Why, citing evidence in this report.
           */
          detail: string;
        },
        {
          /**
           * What to do.
           */
          title: string;
          /**
           * Why, citing evidence in this report.
           */
          detail: string;
        },
        {
          /**
           * What to do.
           */
          title: string;
          /**
           * Why, citing evidence in this report.
           */
          detail: string;
        },
        {
          /**
           * What to do.
           */
          title: string;
          /**
           * Why, citing evidence in this report.
           */
          detail: string;
        },
        {
          /**
           * What to do.
           */
          title: string;
          /**
           * Why, citing evidence in this report.
           */
          detail: string;
        },
        {
          /**
           * What to do.
           */
          title: string;
          /**
           * Why, citing evidence in this report.
           */
          detail: string;
        },
        {
          /**
           * What to do.
           */
          title: string;
          /**
           * Why, citing evidence in this report.
           */
          detail: string;
        },
        {
          /**
           * What to do.
           */
          title: string;
          /**
           * Why, citing evidence in this report.
           */
          detail: string;
        }
      ]
    | [
        {
          /**
           * What to do.
           */
          title: string;
          /**
           * Why, citing evidence in this report.
           */
          detail: string;
        },
        {
          /**
           * What to do.
           */
          title: string;
          /**
           * Why, citing evidence in this report.
           */
          detail: string;
        },
        {
          /**
           * What to do.
           */
          title: string;
          /**
           * Why, citing evidence in this report.
           */
          detail: string;
        },
        {
          /**
           * What to do.
           */
          title: string;
          /**
           * Why, citing evidence in this report.
           */
          detail: string;
        },
        {
          /**
           * What to do.
           */
          title: string;
          /**
           * Why, citing evidence in this report.
           */
          detail: string;
        },
        {
          /**
           * What to do.
           */
          title: string;
          /**
           * Why, citing evidence in this report.
           */
          detail: string;
        },
        {
          /**
           * What to do.
           */
          title: string;
          /**
           * Why, citing evidence in this report.
           */
          detail: string;
        },
        {
          /**
           * What to do.
           */
          title: string;
          /**
           * Why, citing evidence in this report.
           */
          detail: string;
        },
        {
          /**
           * What to do.
           */
          title: string;
          /**
           * Why, citing evidence in this report.
           */
          detail: string;
        },
        {
          /**
           * What to do.
           */
          title: string;
          /**
           * Why, citing evidence in this report.
           */
          detail: string;
        },
        {
          /**
           * What to do.
           */
          title: string;
          /**
           * Why, citing evidence in this report.
           */
          detail: string;
        },
        {
          /**
           * What to do.
           */
          title: string;
          /**
           * Why, citing evidence in this report.
           */
          detail: string;
        }
      ];
  /**
   * How the data was collected.
   */
  method?: {
    /**
     * Assistants that were asked.
     *
     * @maxItems 12
     */
    assistants?:
      | []
      | [string]
      | [string, string]
      | [string, string, string]
      | [string, string, string, string]
      | [string, string, string, string, string]
      | [string, string, string, string, string, string]
      | [string, string, string, string, string, string, string]
      | [string, string, string, string, string, string, string, string]
      | [string, string, string, string, string, string, string, string, string]
      | [string, string, string, string, string, string, string, string, string, string]
      | [string, string, string, string, string, string, string, string, string, string, string]
      | [string, string, string, string, string, string, string, string, string, string, string, string];
    /**
     * Runs per question per assistant.
     */
    runsPerPrompt?: number;
    /**
     * What a reader needs to judge the figures, such as how names were matched.
     */
    notes?: string;
  };
  /**
   * Optional file name; derived from brand and period when omitted.
   */
  filename?: string;
  /**
   * Fill a missing logo, colour and presenter from the brand profile saved in the Brand vault. Values passed here always win.
   */
  useSavedBrand?: boolean;
  /**
   * Also make a PDF file on A4 or US Letter paper. The PDF is charged; the page is free.
   */
  pdf?: "none" | "a4" | "letter";
}

export type Output =
  | {
      ok: boolean;
      title: string;
      filename: string;
      delivery: "artifact" | "local_file";
      sections: string[];
      bytes: number;
      sha256: string;
      generatedAt: string;
      artifact?: {
        artifactId: string;
        filename: string;
        contentType: "text/html";
        bytes: number;
        sha256: string;
        expiresAt: string;
        downloadUrl: string | null;
        downloadUrlExpiresAt: string | null;
      };
      localPath?: string;
      warnings: string[];
      savedBrand?: {
        status: "applied" | "not_saved" | "not_needed" | "turned_off" | "unavailable";
        applied: string[];
        hint?: string;
      };
      pdf?: {
        ok: boolean;
        paper?: string;
        artifact?: {
          artifactId: string;
          filename: string;
          contentType: "application/pdf";
          bytes: number;
          sha256: string;
          expiresAt: string;
          downloadUrl: string | null;
          downloadUrlExpiresAt: string | null;
        };
        chargedCredits: number;
        error?: string;
      };
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
        availableExports?: {
          artifactId: string;
          sourceArtifactId: string;
          filename: "result.md";
          contentType: "text/markdown; charset=utf-8";
          state: "on-demand";
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
