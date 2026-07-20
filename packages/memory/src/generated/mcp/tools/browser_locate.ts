export interface Input {
  /**
   * The session id returned by browser_open or browser_list_sessions.
   */
  session_id: string;
  /**
   * DOM targets to locate in the current viewport. Use selectors for exact elements, or text for visible text ranges.
   *
   * @minItems 1
   * @maxItems 20
   */
  targets:
    | [
        {
          /**
           * Optional label for this target, echoed in the result.
           */
          name?: string;
          /**
           * CSS selector for the exact DOM element to locate, for example h1, input[name="q"], or [data-testid="result"].
           */
          selector?: string;
          /**
           * Visible text to locate when a selector is not known. The tool returns the text range bounds when possible.
           */
          text?: string;
          /**
           * How to match text targets. Defaults to contains.
           */
          match?: "contains" | "exact";
          /**
           * Zero-based match index when multiple elements match.
           */
          index?: number;
        }
      ]
    | [
        {
          /**
           * Optional label for this target, echoed in the result.
           */
          name?: string;
          /**
           * CSS selector for the exact DOM element to locate, for example h1, input[name="q"], or [data-testid="result"].
           */
          selector?: string;
          /**
           * Visible text to locate when a selector is not known. The tool returns the text range bounds when possible.
           */
          text?: string;
          /**
           * How to match text targets. Defaults to contains.
           */
          match?: "contains" | "exact";
          /**
           * Zero-based match index when multiple elements match.
           */
          index?: number;
        },
        {
          /**
           * Optional label for this target, echoed in the result.
           */
          name?: string;
          /**
           * CSS selector for the exact DOM element to locate, for example h1, input[name="q"], or [data-testid="result"].
           */
          selector?: string;
          /**
           * Visible text to locate when a selector is not known. The tool returns the text range bounds when possible.
           */
          text?: string;
          /**
           * How to match text targets. Defaults to contains.
           */
          match?: "contains" | "exact";
          /**
           * Zero-based match index when multiple elements match.
           */
          index?: number;
        }
      ]
    | [
        {
          /**
           * Optional label for this target, echoed in the result.
           */
          name?: string;
          /**
           * CSS selector for the exact DOM element to locate, for example h1, input[name="q"], or [data-testid="result"].
           */
          selector?: string;
          /**
           * Visible text to locate when a selector is not known. The tool returns the text range bounds when possible.
           */
          text?: string;
          /**
           * How to match text targets. Defaults to contains.
           */
          match?: "contains" | "exact";
          /**
           * Zero-based match index when multiple elements match.
           */
          index?: number;
        },
        {
          /**
           * Optional label for this target, echoed in the result.
           */
          name?: string;
          /**
           * CSS selector for the exact DOM element to locate, for example h1, input[name="q"], or [data-testid="result"].
           */
          selector?: string;
          /**
           * Visible text to locate when a selector is not known. The tool returns the text range bounds when possible.
           */
          text?: string;
          /**
           * How to match text targets. Defaults to contains.
           */
          match?: "contains" | "exact";
          /**
           * Zero-based match index when multiple elements match.
           */
          index?: number;
        },
        {
          /**
           * Optional label for this target, echoed in the result.
           */
          name?: string;
          /**
           * CSS selector for the exact DOM element to locate, for example h1, input[name="q"], or [data-testid="result"].
           */
          selector?: string;
          /**
           * Visible text to locate when a selector is not known. The tool returns the text range bounds when possible.
           */
          text?: string;
          /**
           * How to match text targets. Defaults to contains.
           */
          match?: "contains" | "exact";
          /**
           * Zero-based match index when multiple elements match.
           */
          index?: number;
        }
      ]
    | [
        {
          /**
           * Optional label for this target, echoed in the result.
           */
          name?: string;
          /**
           * CSS selector for the exact DOM element to locate, for example h1, input[name="q"], or [data-testid="result"].
           */
          selector?: string;
          /**
           * Visible text to locate when a selector is not known. The tool returns the text range bounds when possible.
           */
          text?: string;
          /**
           * How to match text targets. Defaults to contains.
           */
          match?: "contains" | "exact";
          /**
           * Zero-based match index when multiple elements match.
           */
          index?: number;
        },
        {
          /**
           * Optional label for this target, echoed in the result.
           */
          name?: string;
          /**
           * CSS selector for the exact DOM element to locate, for example h1, input[name="q"], or [data-testid="result"].
           */
          selector?: string;
          /**
           * Visible text to locate when a selector is not known. The tool returns the text range bounds when possible.
           */
          text?: string;
          /**
           * How to match text targets. Defaults to contains.
           */
          match?: "contains" | "exact";
          /**
           * Zero-based match index when multiple elements match.
           */
          index?: number;
        },
        {
          /**
           * Optional label for this target, echoed in the result.
           */
          name?: string;
          /**
           * CSS selector for the exact DOM element to locate, for example h1, input[name="q"], or [data-testid="result"].
           */
          selector?: string;
          /**
           * Visible text to locate when a selector is not known. The tool returns the text range bounds when possible.
           */
          text?: string;
          /**
           * How to match text targets. Defaults to contains.
           */
          match?: "contains" | "exact";
          /**
           * Zero-based match index when multiple elements match.
           */
          index?: number;
        },
        {
          /**
           * Optional label for this target, echoed in the result.
           */
          name?: string;
          /**
           * CSS selector for the exact DOM element to locate, for example h1, input[name="q"], or [data-testid="result"].
           */
          selector?: string;
          /**
           * Visible text to locate when a selector is not known. The tool returns the text range bounds when possible.
           */
          text?: string;
          /**
           * How to match text targets. Defaults to contains.
           */
          match?: "contains" | "exact";
          /**
           * Zero-based match index when multiple elements match.
           */
          index?: number;
        }
      ]
    | [
        {
          /**
           * Optional label for this target, echoed in the result.
           */
          name?: string;
          /**
           * CSS selector for the exact DOM element to locate, for example h1, input[name="q"], or [data-testid="result"].
           */
          selector?: string;
          /**
           * Visible text to locate when a selector is not known. The tool returns the text range bounds when possible.
           */
          text?: string;
          /**
           * How to match text targets. Defaults to contains.
           */
          match?: "contains" | "exact";
          /**
           * Zero-based match index when multiple elements match.
           */
          index?: number;
        },
        {
          /**
           * Optional label for this target, echoed in the result.
           */
          name?: string;
          /**
           * CSS selector for the exact DOM element to locate, for example h1, input[name="q"], or [data-testid="result"].
           */
          selector?: string;
          /**
           * Visible text to locate when a selector is not known. The tool returns the text range bounds when possible.
           */
          text?: string;
          /**
           * How to match text targets. Defaults to contains.
           */
          match?: "contains" | "exact";
          /**
           * Zero-based match index when multiple elements match.
           */
          index?: number;
        },
        {
          /**
           * Optional label for this target, echoed in the result.
           */
          name?: string;
          /**
           * CSS selector for the exact DOM element to locate, for example h1, input[name="q"], or [data-testid="result"].
           */
          selector?: string;
          /**
           * Visible text to locate when a selector is not known. The tool returns the text range bounds when possible.
           */
          text?: string;
          /**
           * How to match text targets. Defaults to contains.
           */
          match?: "contains" | "exact";
          /**
           * Zero-based match index when multiple elements match.
           */
          index?: number;
        },
        {
          /**
           * Optional label for this target, echoed in the result.
           */
          name?: string;
          /**
           * CSS selector for the exact DOM element to locate, for example h1, input[name="q"], or [data-testid="result"].
           */
          selector?: string;
          /**
           * Visible text to locate when a selector is not known. The tool returns the text range bounds when possible.
           */
          text?: string;
          /**
           * How to match text targets. Defaults to contains.
           */
          match?: "contains" | "exact";
          /**
           * Zero-based match index when multiple elements match.
           */
          index?: number;
        },
        {
          /**
           * Optional label for this target, echoed in the result.
           */
          name?: string;
          /**
           * CSS selector for the exact DOM element to locate, for example h1, input[name="q"], or [data-testid="result"].
           */
          selector?: string;
          /**
           * Visible text to locate when a selector is not known. The tool returns the text range bounds when possible.
           */
          text?: string;
          /**
           * How to match text targets. Defaults to contains.
           */
          match?: "contains" | "exact";
          /**
           * Zero-based match index when multiple elements match.
           */
          index?: number;
        }
      ]
    | [
        {
          /**
           * Optional label for this target, echoed in the result.
           */
          name?: string;
          /**
           * CSS selector for the exact DOM element to locate, for example h1, input[name="q"], or [data-testid="result"].
           */
          selector?: string;
          /**
           * Visible text to locate when a selector is not known. The tool returns the text range bounds when possible.
           */
          text?: string;
          /**
           * How to match text targets. Defaults to contains.
           */
          match?: "contains" | "exact";
          /**
           * Zero-based match index when multiple elements match.
           */
          index?: number;
        },
        {
          /**
           * Optional label for this target, echoed in the result.
           */
          name?: string;
          /**
           * CSS selector for the exact DOM element to locate, for example h1, input[name="q"], or [data-testid="result"].
           */
          selector?: string;
          /**
           * Visible text to locate when a selector is not known. The tool returns the text range bounds when possible.
           */
          text?: string;
          /**
           * How to match text targets. Defaults to contains.
           */
          match?: "contains" | "exact";
          /**
           * Zero-based match index when multiple elements match.
           */
          index?: number;
        },
        {
          /**
           * Optional label for this target, echoed in the result.
           */
          name?: string;
          /**
           * CSS selector for the exact DOM element to locate, for example h1, input[name="q"], or [data-testid="result"].
           */
          selector?: string;
          /**
           * Visible text to locate when a selector is not known. The tool returns the text range bounds when possible.
           */
          text?: string;
          /**
           * How to match text targets. Defaults to contains.
           */
          match?: "contains" | "exact";
          /**
           * Zero-based match index when multiple elements match.
           */
          index?: number;
        },
        {
          /**
           * Optional label for this target, echoed in the result.
           */
          name?: string;
          /**
           * CSS selector for the exact DOM element to locate, for example h1, input[name="q"], or [data-testid="result"].
           */
          selector?: string;
          /**
           * Visible text to locate when a selector is not known. The tool returns the text range bounds when possible.
           */
          text?: string;
          /**
           * How to match text targets. Defaults to contains.
           */
          match?: "contains" | "exact";
          /**
           * Zero-based match index when multiple elements match.
           */
          index?: number;
        },
        {
          /**
           * Optional label for this target, echoed in the result.
           */
          name?: string;
          /**
           * CSS selector for the exact DOM element to locate, for example h1, input[name="q"], or [data-testid="result"].
           */
          selector?: string;
          /**
           * Visible text to locate when a selector is not known. The tool returns the text range bounds when possible.
           */
          text?: string;
          /**
           * How to match text targets. Defaults to contains.
           */
          match?: "contains" | "exact";
          /**
           * Zero-based match index when multiple elements match.
           */
          index?: number;
        },
        {
          /**
           * Optional label for this target, echoed in the result.
           */
          name?: string;
          /**
           * CSS selector for the exact DOM element to locate, for example h1, input[name="q"], or [data-testid="result"].
           */
          selector?: string;
          /**
           * Visible text to locate when a selector is not known. The tool returns the text range bounds when possible.
           */
          text?: string;
          /**
           * How to match text targets. Defaults to contains.
           */
          match?: "contains" | "exact";
          /**
           * Zero-based match index when multiple elements match.
           */
          index?: number;
        }
      ]
    | [
        {
          /**
           * Optional label for this target, echoed in the result.
           */
          name?: string;
          /**
           * CSS selector for the exact DOM element to locate, for example h1, input[name="q"], or [data-testid="result"].
           */
          selector?: string;
          /**
           * Visible text to locate when a selector is not known. The tool returns the text range bounds when possible.
           */
          text?: string;
          /**
           * How to match text targets. Defaults to contains.
           */
          match?: "contains" | "exact";
          /**
           * Zero-based match index when multiple elements match.
           */
          index?: number;
        },
        {
          /**
           * Optional label for this target, echoed in the result.
           */
          name?: string;
          /**
           * CSS selector for the exact DOM element to locate, for example h1, input[name="q"], or [data-testid="result"].
           */
          selector?: string;
          /**
           * Visible text to locate when a selector is not known. The tool returns the text range bounds when possible.
           */
          text?: string;
          /**
           * How to match text targets. Defaults to contains.
           */
          match?: "contains" | "exact";
          /**
           * Zero-based match index when multiple elements match.
           */
          index?: number;
        },
        {
          /**
           * Optional label for this target, echoed in the result.
           */
          name?: string;
          /**
           * CSS selector for the exact DOM element to locate, for example h1, input[name="q"], or [data-testid="result"].
           */
          selector?: string;
          /**
           * Visible text to locate when a selector is not known. The tool returns the text range bounds when possible.
           */
          text?: string;
          /**
           * How to match text targets. Defaults to contains.
           */
          match?: "contains" | "exact";
          /**
           * Zero-based match index when multiple elements match.
           */
          index?: number;
        },
        {
          /**
           * Optional label for this target, echoed in the result.
           */
          name?: string;
          /**
           * CSS selector for the exact DOM element to locate, for example h1, input[name="q"], or [data-testid="result"].
           */
          selector?: string;
          /**
           * Visible text to locate when a selector is not known. The tool returns the text range bounds when possible.
           */
          text?: string;
          /**
           * How to match text targets. Defaults to contains.
           */
          match?: "contains" | "exact";
          /**
           * Zero-based match index when multiple elements match.
           */
          index?: number;
        },
        {
          /**
           * Optional label for this target, echoed in the result.
           */
          name?: string;
          /**
           * CSS selector for the exact DOM element to locate, for example h1, input[name="q"], or [data-testid="result"].
           */
          selector?: string;
          /**
           * Visible text to locate when a selector is not known. The tool returns the text range bounds when possible.
           */
          text?: string;
          /**
           * How to match text targets. Defaults to contains.
           */
          match?: "contains" | "exact";
          /**
           * Zero-based match index when multiple elements match.
           */
          index?: number;
        },
        {
          /**
           * Optional label for this target, echoed in the result.
           */
          name?: string;
          /**
           * CSS selector for the exact DOM element to locate, for example h1, input[name="q"], or [data-testid="result"].
           */
          selector?: string;
          /**
           * Visible text to locate when a selector is not known. The tool returns the text range bounds when possible.
           */
          text?: string;
          /**
           * How to match text targets. Defaults to contains.
           */
          match?: "contains" | "exact";
          /**
           * Zero-based match index when multiple elements match.
           */
          index?: number;
        },
        {
          /**
           * Optional label for this target, echoed in the result.
           */
          name?: string;
          /**
           * CSS selector for the exact DOM element to locate, for example h1, input[name="q"], or [data-testid="result"].
           */
          selector?: string;
          /**
           * Visible text to locate when a selector is not known. The tool returns the text range bounds when possible.
           */
          text?: string;
          /**
           * How to match text targets. Defaults to contains.
           */
          match?: "contains" | "exact";
          /**
           * Zero-based match index when multiple elements match.
           */
          index?: number;
        }
      ]
    | [
        {
          /**
           * Optional label for this target, echoed in the result.
           */
          name?: string;
          /**
           * CSS selector for the exact DOM element to locate, for example h1, input[name="q"], or [data-testid="result"].
           */
          selector?: string;
          /**
           * Visible text to locate when a selector is not known. The tool returns the text range bounds when possible.
           */
          text?: string;
          /**
           * How to match text targets. Defaults to contains.
           */
          match?: "contains" | "exact";
          /**
           * Zero-based match index when multiple elements match.
           */
          index?: number;
        },
        {
          /**
           * Optional label for this target, echoed in the result.
           */
          name?: string;
          /**
           * CSS selector for the exact DOM element to locate, for example h1, input[name="q"], or [data-testid="result"].
           */
          selector?: string;
          /**
           * Visible text to locate when a selector is not known. The tool returns the text range bounds when possible.
           */
          text?: string;
          /**
           * How to match text targets. Defaults to contains.
           */
          match?: "contains" | "exact";
          /**
           * Zero-based match index when multiple elements match.
           */
          index?: number;
        },
        {
          /**
           * Optional label for this target, echoed in the result.
           */
          name?: string;
          /**
           * CSS selector for the exact DOM element to locate, for example h1, input[name="q"], or [data-testid="result"].
           */
          selector?: string;
          /**
           * Visible text to locate when a selector is not known. The tool returns the text range bounds when possible.
           */
          text?: string;
          /**
           * How to match text targets. Defaults to contains.
           */
          match?: "contains" | "exact";
          /**
           * Zero-based match index when multiple elements match.
           */
          index?: number;
        },
        {
          /**
           * Optional label for this target, echoed in the result.
           */
          name?: string;
          /**
           * CSS selector for the exact DOM element to locate, for example h1, input[name="q"], or [data-testid="result"].
           */
          selector?: string;
          /**
           * Visible text to locate when a selector is not known. The tool returns the text range bounds when possible.
           */
          text?: string;
          /**
           * How to match text targets. Defaults to contains.
           */
          match?: "contains" | "exact";
          /**
           * Zero-based match index when multiple elements match.
           */
          index?: number;
        },
        {
          /**
           * Optional label for this target, echoed in the result.
           */
          name?: string;
          /**
           * CSS selector for the exact DOM element to locate, for example h1, input[name="q"], or [data-testid="result"].
           */
          selector?: string;
          /**
           * Visible text to locate when a selector is not known. The tool returns the text range bounds when possible.
           */
          text?: string;
          /**
           * How to match text targets. Defaults to contains.
           */
          match?: "contains" | "exact";
          /**
           * Zero-based match index when multiple elements match.
           */
          index?: number;
        },
        {
          /**
           * Optional label for this target, echoed in the result.
           */
          name?: string;
          /**
           * CSS selector for the exact DOM element to locate, for example h1, input[name="q"], or [data-testid="result"].
           */
          selector?: string;
          /**
           * Visible text to locate when a selector is not known. The tool returns the text range bounds when possible.
           */
          text?: string;
          /**
           * How to match text targets. Defaults to contains.
           */
          match?: "contains" | "exact";
          /**
           * Zero-based match index when multiple elements match.
           */
          index?: number;
        },
        {
          /**
           * Optional label for this target, echoed in the result.
           */
          name?: string;
          /**
           * CSS selector for the exact DOM element to locate, for example h1, input[name="q"], or [data-testid="result"].
           */
          selector?: string;
          /**
           * Visible text to locate when a selector is not known. The tool returns the text range bounds when possible.
           */
          text?: string;
          /**
           * How to match text targets. Defaults to contains.
           */
          match?: "contains" | "exact";
          /**
           * Zero-based match index when multiple elements match.
           */
          index?: number;
        },
        {
          /**
           * Optional label for this target, echoed in the result.
           */
          name?: string;
          /**
           * CSS selector for the exact DOM element to locate, for example h1, input[name="q"], or [data-testid="result"].
           */
          selector?: string;
          /**
           * Visible text to locate when a selector is not known. The tool returns the text range bounds when possible.
           */
          text?: string;
          /**
           * How to match text targets. Defaults to contains.
           */
          match?: "contains" | "exact";
          /**
           * Zero-based match index when multiple elements match.
           */
          index?: number;
        }
      ]
    | [
        {
          /**
           * Optional label for this target, echoed in the result.
           */
          name?: string;
          /**
           * CSS selector for the exact DOM element to locate, for example h1, input[name="q"], or [data-testid="result"].
           */
          selector?: string;
          /**
           * Visible text to locate when a selector is not known. The tool returns the text range bounds when possible.
           */
          text?: string;
          /**
           * How to match text targets. Defaults to contains.
           */
          match?: "contains" | "exact";
          /**
           * Zero-based match index when multiple elements match.
           */
          index?: number;
        },
        {
          /**
           * Optional label for this target, echoed in the result.
           */
          name?: string;
          /**
           * CSS selector for the exact DOM element to locate, for example h1, input[name="q"], or [data-testid="result"].
           */
          selector?: string;
          /**
           * Visible text to locate when a selector is not known. The tool returns the text range bounds when possible.
           */
          text?: string;
          /**
           * How to match text targets. Defaults to contains.
           */
          match?: "contains" | "exact";
          /**
           * Zero-based match index when multiple elements match.
           */
          index?: number;
        },
        {
          /**
           * Optional label for this target, echoed in the result.
           */
          name?: string;
          /**
           * CSS selector for the exact DOM element to locate, for example h1, input[name="q"], or [data-testid="result"].
           */
          selector?: string;
          /**
           * Visible text to locate when a selector is not known. The tool returns the text range bounds when possible.
           */
          text?: string;
          /**
           * How to match text targets. Defaults to contains.
           */
          match?: "contains" | "exact";
          /**
           * Zero-based match index when multiple elements match.
           */
          index?: number;
        },
        {
          /**
           * Optional label for this target, echoed in the result.
           */
          name?: string;
          /**
           * CSS selector for the exact DOM element to locate, for example h1, input[name="q"], or [data-testid="result"].
           */
          selector?: string;
          /**
           * Visible text to locate when a selector is not known. The tool returns the text range bounds when possible.
           */
          text?: string;
          /**
           * How to match text targets. Defaults to contains.
           */
          match?: "contains" | "exact";
          /**
           * Zero-based match index when multiple elements match.
           */
          index?: number;
        },
        {
          /**
           * Optional label for this target, echoed in the result.
           */
          name?: string;
          /**
           * CSS selector for the exact DOM element to locate, for example h1, input[name="q"], or [data-testid="result"].
           */
          selector?: string;
          /**
           * Visible text to locate when a selector is not known. The tool returns the text range bounds when possible.
           */
          text?: string;
          /**
           * How to match text targets. Defaults to contains.
           */
          match?: "contains" | "exact";
          /**
           * Zero-based match index when multiple elements match.
           */
          index?: number;
        },
        {
          /**
           * Optional label for this target, echoed in the result.
           */
          name?: string;
          /**
           * CSS selector for the exact DOM element to locate, for example h1, input[name="q"], or [data-testid="result"].
           */
          selector?: string;
          /**
           * Visible text to locate when a selector is not known. The tool returns the text range bounds when possible.
           */
          text?: string;
          /**
           * How to match text targets. Defaults to contains.
           */
          match?: "contains" | "exact";
          /**
           * Zero-based match index when multiple elements match.
           */
          index?: number;
        },
        {
          /**
           * Optional label for this target, echoed in the result.
           */
          name?: string;
          /**
           * CSS selector for the exact DOM element to locate, for example h1, input[name="q"], or [data-testid="result"].
           */
          selector?: string;
          /**
           * Visible text to locate when a selector is not known. The tool returns the text range bounds when possible.
           */
          text?: string;
          /**
           * How to match text targets. Defaults to contains.
           */
          match?: "contains" | "exact";
          /**
           * Zero-based match index when multiple elements match.
           */
          index?: number;
        },
        {
          /**
           * Optional label for this target, echoed in the result.
           */
          name?: string;
          /**
           * CSS selector for the exact DOM element to locate, for example h1, input[name="q"], or [data-testid="result"].
           */
          selector?: string;
          /**
           * Visible text to locate when a selector is not known. The tool returns the text range bounds when possible.
           */
          text?: string;
          /**
           * How to match text targets. Defaults to contains.
           */
          match?: "contains" | "exact";
          /**
           * Zero-based match index when multiple elements match.
           */
          index?: number;
        },
        {
          /**
           * Optional label for this target, echoed in the result.
           */
          name?: string;
          /**
           * CSS selector for the exact DOM element to locate, for example h1, input[name="q"], or [data-testid="result"].
           */
          selector?: string;
          /**
           * Visible text to locate when a selector is not known. The tool returns the text range bounds when possible.
           */
          text?: string;
          /**
           * How to match text targets. Defaults to contains.
           */
          match?: "contains" | "exact";
          /**
           * Zero-based match index when multiple elements match.
           */
          index?: number;
        }
      ]
    | [
        {
          /**
           * Optional label for this target, echoed in the result.
           */
          name?: string;
          /**
           * CSS selector for the exact DOM element to locate, for example h1, input[name="q"], or [data-testid="result"].
           */
          selector?: string;
          /**
           * Visible text to locate when a selector is not known. The tool returns the text range bounds when possible.
           */
          text?: string;
          /**
           * How to match text targets. Defaults to contains.
           */
          match?: "contains" | "exact";
          /**
           * Zero-based match index when multiple elements match.
           */
          index?: number;
        },
        {
          /**
           * Optional label for this target, echoed in the result.
           */
          name?: string;
          /**
           * CSS selector for the exact DOM element to locate, for example h1, input[name="q"], or [data-testid="result"].
           */
          selector?: string;
          /**
           * Visible text to locate when a selector is not known. The tool returns the text range bounds when possible.
           */
          text?: string;
          /**
           * How to match text targets. Defaults to contains.
           */
          match?: "contains" | "exact";
          /**
           * Zero-based match index when multiple elements match.
           */
          index?: number;
        },
        {
          /**
           * Optional label for this target, echoed in the result.
           */
          name?: string;
          /**
           * CSS selector for the exact DOM element to locate, for example h1, input[name="q"], or [data-testid="result"].
           */
          selector?: string;
          /**
           * Visible text to locate when a selector is not known. The tool returns the text range bounds when possible.
           */
          text?: string;
          /**
           * How to match text targets. Defaults to contains.
           */
          match?: "contains" | "exact";
          /**
           * Zero-based match index when multiple elements match.
           */
          index?: number;
        },
        {
          /**
           * Optional label for this target, echoed in the result.
           */
          name?: string;
          /**
           * CSS selector for the exact DOM element to locate, for example h1, input[name="q"], or [data-testid="result"].
           */
          selector?: string;
          /**
           * Visible text to locate when a selector is not known. The tool returns the text range bounds when possible.
           */
          text?: string;
          /**
           * How to match text targets. Defaults to contains.
           */
          match?: "contains" | "exact";
          /**
           * Zero-based match index when multiple elements match.
           */
          index?: number;
        },
        {
          /**
           * Optional label for this target, echoed in the result.
           */
          name?: string;
          /**
           * CSS selector for the exact DOM element to locate, for example h1, input[name="q"], or [data-testid="result"].
           */
          selector?: string;
          /**
           * Visible text to locate when a selector is not known. The tool returns the text range bounds when possible.
           */
          text?: string;
          /**
           * How to match text targets. Defaults to contains.
           */
          match?: "contains" | "exact";
          /**
           * Zero-based match index when multiple elements match.
           */
          index?: number;
        },
        {
          /**
           * Optional label for this target, echoed in the result.
           */
          name?: string;
          /**
           * CSS selector for the exact DOM element to locate, for example h1, input[name="q"], or [data-testid="result"].
           */
          selector?: string;
          /**
           * Visible text to locate when a selector is not known. The tool returns the text range bounds when possible.
           */
          text?: string;
          /**
           * How to match text targets. Defaults to contains.
           */
          match?: "contains" | "exact";
          /**
           * Zero-based match index when multiple elements match.
           */
          index?: number;
        },
        {
          /**
           * Optional label for this target, echoed in the result.
           */
          name?: string;
          /**
           * CSS selector for the exact DOM element to locate, for example h1, input[name="q"], or [data-testid="result"].
           */
          selector?: string;
          /**
           * Visible text to locate when a selector is not known. The tool returns the text range bounds when possible.
           */
          text?: string;
          /**
           * How to match text targets. Defaults to contains.
           */
          match?: "contains" | "exact";
          /**
           * Zero-based match index when multiple elements match.
           */
          index?: number;
        },
        {
          /**
           * Optional label for this target, echoed in the result.
           */
          name?: string;
          /**
           * CSS selector for the exact DOM element to locate, for example h1, input[name="q"], or [data-testid="result"].
           */
          selector?: string;
          /**
           * Visible text to locate when a selector is not known. The tool returns the text range bounds when possible.
           */
          text?: string;
          /**
           * How to match text targets. Defaults to contains.
           */
          match?: "contains" | "exact";
          /**
           * Zero-based match index when multiple elements match.
           */
          index?: number;
        },
        {
          /**
           * Optional label for this target, echoed in the result.
           */
          name?: string;
          /**
           * CSS selector for the exact DOM element to locate, for example h1, input[name="q"], or [data-testid="result"].
           */
          selector?: string;
          /**
           * Visible text to locate when a selector is not known. The tool returns the text range bounds when possible.
           */
          text?: string;
          /**
           * How to match text targets. Defaults to contains.
           */
          match?: "contains" | "exact";
          /**
           * Zero-based match index when multiple elements match.
           */
          index?: number;
        },
        {
          /**
           * Optional label for this target, echoed in the result.
           */
          name?: string;
          /**
           * CSS selector for the exact DOM element to locate, for example h1, input[name="q"], or [data-testid="result"].
           */
          selector?: string;
          /**
           * Visible text to locate when a selector is not known. The tool returns the text range bounds when possible.
           */
          text?: string;
          /**
           * How to match text targets. Defaults to contains.
           */
          match?: "contains" | "exact";
          /**
           * Zero-based match index when multiple elements match.
           */
          index?: number;
        }
      ]
    | [
        {
          /**
           * Optional label for this target, echoed in the result.
           */
          name?: string;
          /**
           * CSS selector for the exact DOM element to locate, for example h1, input[name="q"], or [data-testid="result"].
           */
          selector?: string;
          /**
           * Visible text to locate when a selector is not known. The tool returns the text range bounds when possible.
           */
          text?: string;
          /**
           * How to match text targets. Defaults to contains.
           */
          match?: "contains" | "exact";
          /**
           * Zero-based match index when multiple elements match.
           */
          index?: number;
        },
        {
          /**
           * Optional label for this target, echoed in the result.
           */
          name?: string;
          /**
           * CSS selector for the exact DOM element to locate, for example h1, input[name="q"], or [data-testid="result"].
           */
          selector?: string;
          /**
           * Visible text to locate when a selector is not known. The tool returns the text range bounds when possible.
           */
          text?: string;
          /**
           * How to match text targets. Defaults to contains.
           */
          match?: "contains" | "exact";
          /**
           * Zero-based match index when multiple elements match.
           */
          index?: number;
        },
        {
          /**
           * Optional label for this target, echoed in the result.
           */
          name?: string;
          /**
           * CSS selector for the exact DOM element to locate, for example h1, input[name="q"], or [data-testid="result"].
           */
          selector?: string;
          /**
           * Visible text to locate when a selector is not known. The tool returns the text range bounds when possible.
           */
          text?: string;
          /**
           * How to match text targets. Defaults to contains.
           */
          match?: "contains" | "exact";
          /**
           * Zero-based match index when multiple elements match.
           */
          index?: number;
        },
        {
          /**
           * Optional label for this target, echoed in the result.
           */
          name?: string;
          /**
           * CSS selector for the exact DOM element to locate, for example h1, input[name="q"], or [data-testid="result"].
           */
          selector?: string;
          /**
           * Visible text to locate when a selector is not known. The tool returns the text range bounds when possible.
           */
          text?: string;
          /**
           * How to match text targets. Defaults to contains.
           */
          match?: "contains" | "exact";
          /**
           * Zero-based match index when multiple elements match.
           */
          index?: number;
        },
        {
          /**
           * Optional label for this target, echoed in the result.
           */
          name?: string;
          /**
           * CSS selector for the exact DOM element to locate, for example h1, input[name="q"], or [data-testid="result"].
           */
          selector?: string;
          /**
           * Visible text to locate when a selector is not known. The tool returns the text range bounds when possible.
           */
          text?: string;
          /**
           * How to match text targets. Defaults to contains.
           */
          match?: "contains" | "exact";
          /**
           * Zero-based match index when multiple elements match.
           */
          index?: number;
        },
        {
          /**
           * Optional label for this target, echoed in the result.
           */
          name?: string;
          /**
           * CSS selector for the exact DOM element to locate, for example h1, input[name="q"], or [data-testid="result"].
           */
          selector?: string;
          /**
           * Visible text to locate when a selector is not known. The tool returns the text range bounds when possible.
           */
          text?: string;
          /**
           * How to match text targets. Defaults to contains.
           */
          match?: "contains" | "exact";
          /**
           * Zero-based match index when multiple elements match.
           */
          index?: number;
        },
        {
          /**
           * Optional label for this target, echoed in the result.
           */
          name?: string;
          /**
           * CSS selector for the exact DOM element to locate, for example h1, input[name="q"], or [data-testid="result"].
           */
          selector?: string;
          /**
           * Visible text to locate when a selector is not known. The tool returns the text range bounds when possible.
           */
          text?: string;
          /**
           * How to match text targets. Defaults to contains.
           */
          match?: "contains" | "exact";
          /**
           * Zero-based match index when multiple elements match.
           */
          index?: number;
        },
        {
          /**
           * Optional label for this target, echoed in the result.
           */
          name?: string;
          /**
           * CSS selector for the exact DOM element to locate, for example h1, input[name="q"], or [data-testid="result"].
           */
          selector?: string;
          /**
           * Visible text to locate when a selector is not known. The tool returns the text range bounds when possible.
           */
          text?: string;
          /**
           * How to match text targets. Defaults to contains.
           */
          match?: "contains" | "exact";
          /**
           * Zero-based match index when multiple elements match.
           */
          index?: number;
        },
        {
          /**
           * Optional label for this target, echoed in the result.
           */
          name?: string;
          /**
           * CSS selector for the exact DOM element to locate, for example h1, input[name="q"], or [data-testid="result"].
           */
          selector?: string;
          /**
           * Visible text to locate when a selector is not known. The tool returns the text range bounds when possible.
           */
          text?: string;
          /**
           * How to match text targets. Defaults to contains.
           */
          match?: "contains" | "exact";
          /**
           * Zero-based match index when multiple elements match.
           */
          index?: number;
        },
        {
          /**
           * Optional label for this target, echoed in the result.
           */
          name?: string;
          /**
           * CSS selector for the exact DOM element to locate, for example h1, input[name="q"], or [data-testid="result"].
           */
          selector?: string;
          /**
           * Visible text to locate when a selector is not known. The tool returns the text range bounds when possible.
           */
          text?: string;
          /**
           * How to match text targets. Defaults to contains.
           */
          match?: "contains" | "exact";
          /**
           * Zero-based match index when multiple elements match.
           */
          index?: number;
        },
        {
          /**
           * Optional label for this target, echoed in the result.
           */
          name?: string;
          /**
           * CSS selector for the exact DOM element to locate, for example h1, input[name="q"], or [data-testid="result"].
           */
          selector?: string;
          /**
           * Visible text to locate when a selector is not known. The tool returns the text range bounds when possible.
           */
          text?: string;
          /**
           * How to match text targets. Defaults to contains.
           */
          match?: "contains" | "exact";
          /**
           * Zero-based match index when multiple elements match.
           */
          index?: number;
        }
      ]
    | [
        {
          /**
           * Optional label for this target, echoed in the result.
           */
          name?: string;
          /**
           * CSS selector for the exact DOM element to locate, for example h1, input[name="q"], or [data-testid="result"].
           */
          selector?: string;
          /**
           * Visible text to locate when a selector is not known. The tool returns the text range bounds when possible.
           */
          text?: string;
          /**
           * How to match text targets. Defaults to contains.
           */
          match?: "contains" | "exact";
          /**
           * Zero-based match index when multiple elements match.
           */
          index?: number;
        },
        {
          /**
           * Optional label for this target, echoed in the result.
           */
          name?: string;
          /**
           * CSS selector for the exact DOM element to locate, for example h1, input[name="q"], or [data-testid="result"].
           */
          selector?: string;
          /**
           * Visible text to locate when a selector is not known. The tool returns the text range bounds when possible.
           */
          text?: string;
          /**
           * How to match text targets. Defaults to contains.
           */
          match?: "contains" | "exact";
          /**
           * Zero-based match index when multiple elements match.
           */
          index?: number;
        },
        {
          /**
           * Optional label for this target, echoed in the result.
           */
          name?: string;
          /**
           * CSS selector for the exact DOM element to locate, for example h1, input[name="q"], or [data-testid="result"].
           */
          selector?: string;
          /**
           * Visible text to locate when a selector is not known. The tool returns the text range bounds when possible.
           */
          text?: string;
          /**
           * How to match text targets. Defaults to contains.
           */
          match?: "contains" | "exact";
          /**
           * Zero-based match index when multiple elements match.
           */
          index?: number;
        },
        {
          /**
           * Optional label for this target, echoed in the result.
           */
          name?: string;
          /**
           * CSS selector for the exact DOM element to locate, for example h1, input[name="q"], or [data-testid="result"].
           */
          selector?: string;
          /**
           * Visible text to locate when a selector is not known. The tool returns the text range bounds when possible.
           */
          text?: string;
          /**
           * How to match text targets. Defaults to contains.
           */
          match?: "contains" | "exact";
          /**
           * Zero-based match index when multiple elements match.
           */
          index?: number;
        },
        {
          /**
           * Optional label for this target, echoed in the result.
           */
          name?: string;
          /**
           * CSS selector for the exact DOM element to locate, for example h1, input[name="q"], or [data-testid="result"].
           */
          selector?: string;
          /**
           * Visible text to locate when a selector is not known. The tool returns the text range bounds when possible.
           */
          text?: string;
          /**
           * How to match text targets. Defaults to contains.
           */
          match?: "contains" | "exact";
          /**
           * Zero-based match index when multiple elements match.
           */
          index?: number;
        },
        {
          /**
           * Optional label for this target, echoed in the result.
           */
          name?: string;
          /**
           * CSS selector for the exact DOM element to locate, for example h1, input[name="q"], or [data-testid="result"].
           */
          selector?: string;
          /**
           * Visible text to locate when a selector is not known. The tool returns the text range bounds when possible.
           */
          text?: string;
          /**
           * How to match text targets. Defaults to contains.
           */
          match?: "contains" | "exact";
          /**
           * Zero-based match index when multiple elements match.
           */
          index?: number;
        },
        {
          /**
           * Optional label for this target, echoed in the result.
           */
          name?: string;
          /**
           * CSS selector for the exact DOM element to locate, for example h1, input[name="q"], or [data-testid="result"].
           */
          selector?: string;
          /**
           * Visible text to locate when a selector is not known. The tool returns the text range bounds when possible.
           */
          text?: string;
          /**
           * How to match text targets. Defaults to contains.
           */
          match?: "contains" | "exact";
          /**
           * Zero-based match index when multiple elements match.
           */
          index?: number;
        },
        {
          /**
           * Optional label for this target, echoed in the result.
           */
          name?: string;
          /**
           * CSS selector for the exact DOM element to locate, for example h1, input[name="q"], or [data-testid="result"].
           */
          selector?: string;
          /**
           * Visible text to locate when a selector is not known. The tool returns the text range bounds when possible.
           */
          text?: string;
          /**
           * How to match text targets. Defaults to contains.
           */
          match?: "contains" | "exact";
          /**
           * Zero-based match index when multiple elements match.
           */
          index?: number;
        },
        {
          /**
           * Optional label for this target, echoed in the result.
           */
          name?: string;
          /**
           * CSS selector for the exact DOM element to locate, for example h1, input[name="q"], or [data-testid="result"].
           */
          selector?: string;
          /**
           * Visible text to locate when a selector is not known. The tool returns the text range bounds when possible.
           */
          text?: string;
          /**
           * How to match text targets. Defaults to contains.
           */
          match?: "contains" | "exact";
          /**
           * Zero-based match index when multiple elements match.
           */
          index?: number;
        },
        {
          /**
           * Optional label for this target, echoed in the result.
           */
          name?: string;
          /**
           * CSS selector for the exact DOM element to locate, for example h1, input[name="q"], or [data-testid="result"].
           */
          selector?: string;
          /**
           * Visible text to locate when a selector is not known. The tool returns the text range bounds when possible.
           */
          text?: string;
          /**
           * How to match text targets. Defaults to contains.
           */
          match?: "contains" | "exact";
          /**
           * Zero-based match index when multiple elements match.
           */
          index?: number;
        },
        {
          /**
           * Optional label for this target, echoed in the result.
           */
          name?: string;
          /**
           * CSS selector for the exact DOM element to locate, for example h1, input[name="q"], or [data-testid="result"].
           */
          selector?: string;
          /**
           * Visible text to locate when a selector is not known. The tool returns the text range bounds when possible.
           */
          text?: string;
          /**
           * How to match text targets. Defaults to contains.
           */
          match?: "contains" | "exact";
          /**
           * Zero-based match index when multiple elements match.
           */
          index?: number;
        },
        {
          /**
           * Optional label for this target, echoed in the result.
           */
          name?: string;
          /**
           * CSS selector for the exact DOM element to locate, for example h1, input[name="q"], or [data-testid="result"].
           */
          selector?: string;
          /**
           * Visible text to locate when a selector is not known. The tool returns the text range bounds when possible.
           */
          text?: string;
          /**
           * How to match text targets. Defaults to contains.
           */
          match?: "contains" | "exact";
          /**
           * Zero-based match index when multiple elements match.
           */
          index?: number;
        }
      ]
    | [
        {
          /**
           * Optional label for this target, echoed in the result.
           */
          name?: string;
          /**
           * CSS selector for the exact DOM element to locate, for example h1, input[name="q"], or [data-testid="result"].
           */
          selector?: string;
          /**
           * Visible text to locate when a selector is not known. The tool returns the text range bounds when possible.
           */
          text?: string;
          /**
           * How to match text targets. Defaults to contains.
           */
          match?: "contains" | "exact";
          /**
           * Zero-based match index when multiple elements match.
           */
          index?: number;
        },
        {
          /**
           * Optional label for this target, echoed in the result.
           */
          name?: string;
          /**
           * CSS selector for the exact DOM element to locate, for example h1, input[name="q"], or [data-testid="result"].
           */
          selector?: string;
          /**
           * Visible text to locate when a selector is not known. The tool returns the text range bounds when possible.
           */
          text?: string;
          /**
           * How to match text targets. Defaults to contains.
           */
          match?: "contains" | "exact";
          /**
           * Zero-based match index when multiple elements match.
           */
          index?: number;
        },
        {
          /**
           * Optional label for this target, echoed in the result.
           */
          name?: string;
          /**
           * CSS selector for the exact DOM element to locate, for example h1, input[name="q"], or [data-testid="result"].
           */
          selector?: string;
          /**
           * Visible text to locate when a selector is not known. The tool returns the text range bounds when possible.
           */
          text?: string;
          /**
           * How to match text targets. Defaults to contains.
           */
          match?: "contains" | "exact";
          /**
           * Zero-based match index when multiple elements match.
           */
          index?: number;
        },
        {
          /**
           * Optional label for this target, echoed in the result.
           */
          name?: string;
          /**
           * CSS selector for the exact DOM element to locate, for example h1, input[name="q"], or [data-testid="result"].
           */
          selector?: string;
          /**
           * Visible text to locate when a selector is not known. The tool returns the text range bounds when possible.
           */
          text?: string;
          /**
           * How to match text targets. Defaults to contains.
           */
          match?: "contains" | "exact";
          /**
           * Zero-based match index when multiple elements match.
           */
          index?: number;
        },
        {
          /**
           * Optional label for this target, echoed in the result.
           */
          name?: string;
          /**
           * CSS selector for the exact DOM element to locate, for example h1, input[name="q"], or [data-testid="result"].
           */
          selector?: string;
          /**
           * Visible text to locate when a selector is not known. The tool returns the text range bounds when possible.
           */
          text?: string;
          /**
           * How to match text targets. Defaults to contains.
           */
          match?: "contains" | "exact";
          /**
           * Zero-based match index when multiple elements match.
           */
          index?: number;
        },
        {
          /**
           * Optional label for this target, echoed in the result.
           */
          name?: string;
          /**
           * CSS selector for the exact DOM element to locate, for example h1, input[name="q"], or [data-testid="result"].
           */
          selector?: string;
          /**
           * Visible text to locate when a selector is not known. The tool returns the text range bounds when possible.
           */
          text?: string;
          /**
           * How to match text targets. Defaults to contains.
           */
          match?: "contains" | "exact";
          /**
           * Zero-based match index when multiple elements match.
           */
          index?: number;
        },
        {
          /**
           * Optional label for this target, echoed in the result.
           */
          name?: string;
          /**
           * CSS selector for the exact DOM element to locate, for example h1, input[name="q"], or [data-testid="result"].
           */
          selector?: string;
          /**
           * Visible text to locate when a selector is not known. The tool returns the text range bounds when possible.
           */
          text?: string;
          /**
           * How to match text targets. Defaults to contains.
           */
          match?: "contains" | "exact";
          /**
           * Zero-based match index when multiple elements match.
           */
          index?: number;
        },
        {
          /**
           * Optional label for this target, echoed in the result.
           */
          name?: string;
          /**
           * CSS selector for the exact DOM element to locate, for example h1, input[name="q"], or [data-testid="result"].
           */
          selector?: string;
          /**
           * Visible text to locate when a selector is not known. The tool returns the text range bounds when possible.
           */
          text?: string;
          /**
           * How to match text targets. Defaults to contains.
           */
          match?: "contains" | "exact";
          /**
           * Zero-based match index when multiple elements match.
           */
          index?: number;
        },
        {
          /**
           * Optional label for this target, echoed in the result.
           */
          name?: string;
          /**
           * CSS selector for the exact DOM element to locate, for example h1, input[name="q"], or [data-testid="result"].
           */
          selector?: string;
          /**
           * Visible text to locate when a selector is not known. The tool returns the text range bounds when possible.
           */
          text?: string;
          /**
           * How to match text targets. Defaults to contains.
           */
          match?: "contains" | "exact";
          /**
           * Zero-based match index when multiple elements match.
           */
          index?: number;
        },
        {
          /**
           * Optional label for this target, echoed in the result.
           */
          name?: string;
          /**
           * CSS selector for the exact DOM element to locate, for example h1, input[name="q"], or [data-testid="result"].
           */
          selector?: string;
          /**
           * Visible text to locate when a selector is not known. The tool returns the text range bounds when possible.
           */
          text?: string;
          /**
           * How to match text targets. Defaults to contains.
           */
          match?: "contains" | "exact";
          /**
           * Zero-based match index when multiple elements match.
           */
          index?: number;
        },
        {
          /**
           * Optional label for this target, echoed in the result.
           */
          name?: string;
          /**
           * CSS selector for the exact DOM element to locate, for example h1, input[name="q"], or [data-testid="result"].
           */
          selector?: string;
          /**
           * Visible text to locate when a selector is not known. The tool returns the text range bounds when possible.
           */
          text?: string;
          /**
           * How to match text targets. Defaults to contains.
           */
          match?: "contains" | "exact";
          /**
           * Zero-based match index when multiple elements match.
           */
          index?: number;
        },
        {
          /**
           * Optional label for this target, echoed in the result.
           */
          name?: string;
          /**
           * CSS selector for the exact DOM element to locate, for example h1, input[name="q"], or [data-testid="result"].
           */
          selector?: string;
          /**
           * Visible text to locate when a selector is not known. The tool returns the text range bounds when possible.
           */
          text?: string;
          /**
           * How to match text targets. Defaults to contains.
           */
          match?: "contains" | "exact";
          /**
           * Zero-based match index when multiple elements match.
           */
          index?: number;
        },
        {
          /**
           * Optional label for this target, echoed in the result.
           */
          name?: string;
          /**
           * CSS selector for the exact DOM element to locate, for example h1, input[name="q"], or [data-testid="result"].
           */
          selector?: string;
          /**
           * Visible text to locate when a selector is not known. The tool returns the text range bounds when possible.
           */
          text?: string;
          /**
           * How to match text targets. Defaults to contains.
           */
          match?: "contains" | "exact";
          /**
           * Zero-based match index when multiple elements match.
           */
          index?: number;
        }
      ]
    | [
        {
          /**
           * Optional label for this target, echoed in the result.
           */
          name?: string;
          /**
           * CSS selector for the exact DOM element to locate, for example h1, input[name="q"], or [data-testid="result"].
           */
          selector?: string;
          /**
           * Visible text to locate when a selector is not known. The tool returns the text range bounds when possible.
           */
          text?: string;
          /**
           * How to match text targets. Defaults to contains.
           */
          match?: "contains" | "exact";
          /**
           * Zero-based match index when multiple elements match.
           */
          index?: number;
        },
        {
          /**
           * Optional label for this target, echoed in the result.
           */
          name?: string;
          /**
           * CSS selector for the exact DOM element to locate, for example h1, input[name="q"], or [data-testid="result"].
           */
          selector?: string;
          /**
           * Visible text to locate when a selector is not known. The tool returns the text range bounds when possible.
           */
          text?: string;
          /**
           * How to match text targets. Defaults to contains.
           */
          match?: "contains" | "exact";
          /**
           * Zero-based match index when multiple elements match.
           */
          index?: number;
        },
        {
          /**
           * Optional label for this target, echoed in the result.
           */
          name?: string;
          /**
           * CSS selector for the exact DOM element to locate, for example h1, input[name="q"], or [data-testid="result"].
           */
          selector?: string;
          /**
           * Visible text to locate when a selector is not known. The tool returns the text range bounds when possible.
           */
          text?: string;
          /**
           * How to match text targets. Defaults to contains.
           */
          match?: "contains" | "exact";
          /**
           * Zero-based match index when multiple elements match.
           */
          index?: number;
        },
        {
          /**
           * Optional label for this target, echoed in the result.
           */
          name?: string;
          /**
           * CSS selector for the exact DOM element to locate, for example h1, input[name="q"], or [data-testid="result"].
           */
          selector?: string;
          /**
           * Visible text to locate when a selector is not known. The tool returns the text range bounds when possible.
           */
          text?: string;
          /**
           * How to match text targets. Defaults to contains.
           */
          match?: "contains" | "exact";
          /**
           * Zero-based match index when multiple elements match.
           */
          index?: number;
        },
        {
          /**
           * Optional label for this target, echoed in the result.
           */
          name?: string;
          /**
           * CSS selector for the exact DOM element to locate, for example h1, input[name="q"], or [data-testid="result"].
           */
          selector?: string;
          /**
           * Visible text to locate when a selector is not known. The tool returns the text range bounds when possible.
           */
          text?: string;
          /**
           * How to match text targets. Defaults to contains.
           */
          match?: "contains" | "exact";
          /**
           * Zero-based match index when multiple elements match.
           */
          index?: number;
        },
        {
          /**
           * Optional label for this target, echoed in the result.
           */
          name?: string;
          /**
           * CSS selector for the exact DOM element to locate, for example h1, input[name="q"], or [data-testid="result"].
           */
          selector?: string;
          /**
           * Visible text to locate when a selector is not known. The tool returns the text range bounds when possible.
           */
          text?: string;
          /**
           * How to match text targets. Defaults to contains.
           */
          match?: "contains" | "exact";
          /**
           * Zero-based match index when multiple elements match.
           */
          index?: number;
        },
        {
          /**
           * Optional label for this target, echoed in the result.
           */
          name?: string;
          /**
           * CSS selector for the exact DOM element to locate, for example h1, input[name="q"], or [data-testid="result"].
           */
          selector?: string;
          /**
           * Visible text to locate when a selector is not known. The tool returns the text range bounds when possible.
           */
          text?: string;
          /**
           * How to match text targets. Defaults to contains.
           */
          match?: "contains" | "exact";
          /**
           * Zero-based match index when multiple elements match.
           */
          index?: number;
        },
        {
          /**
           * Optional label for this target, echoed in the result.
           */
          name?: string;
          /**
           * CSS selector for the exact DOM element to locate, for example h1, input[name="q"], or [data-testid="result"].
           */
          selector?: string;
          /**
           * Visible text to locate when a selector is not known. The tool returns the text range bounds when possible.
           */
          text?: string;
          /**
           * How to match text targets. Defaults to contains.
           */
          match?: "contains" | "exact";
          /**
           * Zero-based match index when multiple elements match.
           */
          index?: number;
        },
        {
          /**
           * Optional label for this target, echoed in the result.
           */
          name?: string;
          /**
           * CSS selector for the exact DOM element to locate, for example h1, input[name="q"], or [data-testid="result"].
           */
          selector?: string;
          /**
           * Visible text to locate when a selector is not known. The tool returns the text range bounds when possible.
           */
          text?: string;
          /**
           * How to match text targets. Defaults to contains.
           */
          match?: "contains" | "exact";
          /**
           * Zero-based match index when multiple elements match.
           */
          index?: number;
        },
        {
          /**
           * Optional label for this target, echoed in the result.
           */
          name?: string;
          /**
           * CSS selector for the exact DOM element to locate, for example h1, input[name="q"], or [data-testid="result"].
           */
          selector?: string;
          /**
           * Visible text to locate when a selector is not known. The tool returns the text range bounds when possible.
           */
          text?: string;
          /**
           * How to match text targets. Defaults to contains.
           */
          match?: "contains" | "exact";
          /**
           * Zero-based match index when multiple elements match.
           */
          index?: number;
        },
        {
          /**
           * Optional label for this target, echoed in the result.
           */
          name?: string;
          /**
           * CSS selector for the exact DOM element to locate, for example h1, input[name="q"], or [data-testid="result"].
           */
          selector?: string;
          /**
           * Visible text to locate when a selector is not known. The tool returns the text range bounds when possible.
           */
          text?: string;
          /**
           * How to match text targets. Defaults to contains.
           */
          match?: "contains" | "exact";
          /**
           * Zero-based match index when multiple elements match.
           */
          index?: number;
        },
        {
          /**
           * Optional label for this target, echoed in the result.
           */
          name?: string;
          /**
           * CSS selector for the exact DOM element to locate, for example h1, input[name="q"], or [data-testid="result"].
           */
          selector?: string;
          /**
           * Visible text to locate when a selector is not known. The tool returns the text range bounds when possible.
           */
          text?: string;
          /**
           * How to match text targets. Defaults to contains.
           */
          match?: "contains" | "exact";
          /**
           * Zero-based match index when multiple elements match.
           */
          index?: number;
        },
        {
          /**
           * Optional label for this target, echoed in the result.
           */
          name?: string;
          /**
           * CSS selector for the exact DOM element to locate, for example h1, input[name="q"], or [data-testid="result"].
           */
          selector?: string;
          /**
           * Visible text to locate when a selector is not known. The tool returns the text range bounds when possible.
           */
          text?: string;
          /**
           * How to match text targets. Defaults to contains.
           */
          match?: "contains" | "exact";
          /**
           * Zero-based match index when multiple elements match.
           */
          index?: number;
        },
        {
          /**
           * Optional label for this target, echoed in the result.
           */
          name?: string;
          /**
           * CSS selector for the exact DOM element to locate, for example h1, input[name="q"], or [data-testid="result"].
           */
          selector?: string;
          /**
           * Visible text to locate when a selector is not known. The tool returns the text range bounds when possible.
           */
          text?: string;
          /**
           * How to match text targets. Defaults to contains.
           */
          match?: "contains" | "exact";
          /**
           * Zero-based match index when multiple elements match.
           */
          index?: number;
        }
      ]
    | [
        {
          /**
           * Optional label for this target, echoed in the result.
           */
          name?: string;
          /**
           * CSS selector for the exact DOM element to locate, for example h1, input[name="q"], or [data-testid="result"].
           */
          selector?: string;
          /**
           * Visible text to locate when a selector is not known. The tool returns the text range bounds when possible.
           */
          text?: string;
          /**
           * How to match text targets. Defaults to contains.
           */
          match?: "contains" | "exact";
          /**
           * Zero-based match index when multiple elements match.
           */
          index?: number;
        },
        {
          /**
           * Optional label for this target, echoed in the result.
           */
          name?: string;
          /**
           * CSS selector for the exact DOM element to locate, for example h1, input[name="q"], or [data-testid="result"].
           */
          selector?: string;
          /**
           * Visible text to locate when a selector is not known. The tool returns the text range bounds when possible.
           */
          text?: string;
          /**
           * How to match text targets. Defaults to contains.
           */
          match?: "contains" | "exact";
          /**
           * Zero-based match index when multiple elements match.
           */
          index?: number;
        },
        {
          /**
           * Optional label for this target, echoed in the result.
           */
          name?: string;
          /**
           * CSS selector for the exact DOM element to locate, for example h1, input[name="q"], or [data-testid="result"].
           */
          selector?: string;
          /**
           * Visible text to locate when a selector is not known. The tool returns the text range bounds when possible.
           */
          text?: string;
          /**
           * How to match text targets. Defaults to contains.
           */
          match?: "contains" | "exact";
          /**
           * Zero-based match index when multiple elements match.
           */
          index?: number;
        },
        {
          /**
           * Optional label for this target, echoed in the result.
           */
          name?: string;
          /**
           * CSS selector for the exact DOM element to locate, for example h1, input[name="q"], or [data-testid="result"].
           */
          selector?: string;
          /**
           * Visible text to locate when a selector is not known. The tool returns the text range bounds when possible.
           */
          text?: string;
          /**
           * How to match text targets. Defaults to contains.
           */
          match?: "contains" | "exact";
          /**
           * Zero-based match index when multiple elements match.
           */
          index?: number;
        },
        {
          /**
           * Optional label for this target, echoed in the result.
           */
          name?: string;
          /**
           * CSS selector for the exact DOM element to locate, for example h1, input[name="q"], or [data-testid="result"].
           */
          selector?: string;
          /**
           * Visible text to locate when a selector is not known. The tool returns the text range bounds when possible.
           */
          text?: string;
          /**
           * How to match text targets. Defaults to contains.
           */
          match?: "contains" | "exact";
          /**
           * Zero-based match index when multiple elements match.
           */
          index?: number;
        },
        {
          /**
           * Optional label for this target, echoed in the result.
           */
          name?: string;
          /**
           * CSS selector for the exact DOM element to locate, for example h1, input[name="q"], or [data-testid="result"].
           */
          selector?: string;
          /**
           * Visible text to locate when a selector is not known. The tool returns the text range bounds when possible.
           */
          text?: string;
          /**
           * How to match text targets. Defaults to contains.
           */
          match?: "contains" | "exact";
          /**
           * Zero-based match index when multiple elements match.
           */
          index?: number;
        },
        {
          /**
           * Optional label for this target, echoed in the result.
           */
          name?: string;
          /**
           * CSS selector for the exact DOM element to locate, for example h1, input[name="q"], or [data-testid="result"].
           */
          selector?: string;
          /**
           * Visible text to locate when a selector is not known. The tool returns the text range bounds when possible.
           */
          text?: string;
          /**
           * How to match text targets. Defaults to contains.
           */
          match?: "contains" | "exact";
          /**
           * Zero-based match index when multiple elements match.
           */
          index?: number;
        },
        {
          /**
           * Optional label for this target, echoed in the result.
           */
          name?: string;
          /**
           * CSS selector for the exact DOM element to locate, for example h1, input[name="q"], or [data-testid="result"].
           */
          selector?: string;
          /**
           * Visible text to locate when a selector is not known. The tool returns the text range bounds when possible.
           */
          text?: string;
          /**
           * How to match text targets. Defaults to contains.
           */
          match?: "contains" | "exact";
          /**
           * Zero-based match index when multiple elements match.
           */
          index?: number;
        },
        {
          /**
           * Optional label for this target, echoed in the result.
           */
          name?: string;
          /**
           * CSS selector for the exact DOM element to locate, for example h1, input[name="q"], or [data-testid="result"].
           */
          selector?: string;
          /**
           * Visible text to locate when a selector is not known. The tool returns the text range bounds when possible.
           */
          text?: string;
          /**
           * How to match text targets. Defaults to contains.
           */
          match?: "contains" | "exact";
          /**
           * Zero-based match index when multiple elements match.
           */
          index?: number;
        },
        {
          /**
           * Optional label for this target, echoed in the result.
           */
          name?: string;
          /**
           * CSS selector for the exact DOM element to locate, for example h1, input[name="q"], or [data-testid="result"].
           */
          selector?: string;
          /**
           * Visible text to locate when a selector is not known. The tool returns the text range bounds when possible.
           */
          text?: string;
          /**
           * How to match text targets. Defaults to contains.
           */
          match?: "contains" | "exact";
          /**
           * Zero-based match index when multiple elements match.
           */
          index?: number;
        },
        {
          /**
           * Optional label for this target, echoed in the result.
           */
          name?: string;
          /**
           * CSS selector for the exact DOM element to locate, for example h1, input[name="q"], or [data-testid="result"].
           */
          selector?: string;
          /**
           * Visible text to locate when a selector is not known. The tool returns the text range bounds when possible.
           */
          text?: string;
          /**
           * How to match text targets. Defaults to contains.
           */
          match?: "contains" | "exact";
          /**
           * Zero-based match index when multiple elements match.
           */
          index?: number;
        },
        {
          /**
           * Optional label for this target, echoed in the result.
           */
          name?: string;
          /**
           * CSS selector for the exact DOM element to locate, for example h1, input[name="q"], or [data-testid="result"].
           */
          selector?: string;
          /**
           * Visible text to locate when a selector is not known. The tool returns the text range bounds when possible.
           */
          text?: string;
          /**
           * How to match text targets. Defaults to contains.
           */
          match?: "contains" | "exact";
          /**
           * Zero-based match index when multiple elements match.
           */
          index?: number;
        },
        {
          /**
           * Optional label for this target, echoed in the result.
           */
          name?: string;
          /**
           * CSS selector for the exact DOM element to locate, for example h1, input[name="q"], or [data-testid="result"].
           */
          selector?: string;
          /**
           * Visible text to locate when a selector is not known. The tool returns the text range bounds when possible.
           */
          text?: string;
          /**
           * How to match text targets. Defaults to contains.
           */
          match?: "contains" | "exact";
          /**
           * Zero-based match index when multiple elements match.
           */
          index?: number;
        },
        {
          /**
           * Optional label for this target, echoed in the result.
           */
          name?: string;
          /**
           * CSS selector for the exact DOM element to locate, for example h1, input[name="q"], or [data-testid="result"].
           */
          selector?: string;
          /**
           * Visible text to locate when a selector is not known. The tool returns the text range bounds when possible.
           */
          text?: string;
          /**
           * How to match text targets. Defaults to contains.
           */
          match?: "contains" | "exact";
          /**
           * Zero-based match index when multiple elements match.
           */
          index?: number;
        },
        {
          /**
           * Optional label for this target, echoed in the result.
           */
          name?: string;
          /**
           * CSS selector for the exact DOM element to locate, for example h1, input[name="q"], or [data-testid="result"].
           */
          selector?: string;
          /**
           * Visible text to locate when a selector is not known. The tool returns the text range bounds when possible.
           */
          text?: string;
          /**
           * How to match text targets. Defaults to contains.
           */
          match?: "contains" | "exact";
          /**
           * Zero-based match index when multiple elements match.
           */
          index?: number;
        }
      ]
    | [
        {
          /**
           * Optional label for this target, echoed in the result.
           */
          name?: string;
          /**
           * CSS selector for the exact DOM element to locate, for example h1, input[name="q"], or [data-testid="result"].
           */
          selector?: string;
          /**
           * Visible text to locate when a selector is not known. The tool returns the text range bounds when possible.
           */
          text?: string;
          /**
           * How to match text targets. Defaults to contains.
           */
          match?: "contains" | "exact";
          /**
           * Zero-based match index when multiple elements match.
           */
          index?: number;
        },
        {
          /**
           * Optional label for this target, echoed in the result.
           */
          name?: string;
          /**
           * CSS selector for the exact DOM element to locate, for example h1, input[name="q"], or [data-testid="result"].
           */
          selector?: string;
          /**
           * Visible text to locate when a selector is not known. The tool returns the text range bounds when possible.
           */
          text?: string;
          /**
           * How to match text targets. Defaults to contains.
           */
          match?: "contains" | "exact";
          /**
           * Zero-based match index when multiple elements match.
           */
          index?: number;
        },
        {
          /**
           * Optional label for this target, echoed in the result.
           */
          name?: string;
          /**
           * CSS selector for the exact DOM element to locate, for example h1, input[name="q"], or [data-testid="result"].
           */
          selector?: string;
          /**
           * Visible text to locate when a selector is not known. The tool returns the text range bounds when possible.
           */
          text?: string;
          /**
           * How to match text targets. Defaults to contains.
           */
          match?: "contains" | "exact";
          /**
           * Zero-based match index when multiple elements match.
           */
          index?: number;
        },
        {
          /**
           * Optional label for this target, echoed in the result.
           */
          name?: string;
          /**
           * CSS selector for the exact DOM element to locate, for example h1, input[name="q"], or [data-testid="result"].
           */
          selector?: string;
          /**
           * Visible text to locate when a selector is not known. The tool returns the text range bounds when possible.
           */
          text?: string;
          /**
           * How to match text targets. Defaults to contains.
           */
          match?: "contains" | "exact";
          /**
           * Zero-based match index when multiple elements match.
           */
          index?: number;
        },
        {
          /**
           * Optional label for this target, echoed in the result.
           */
          name?: string;
          /**
           * CSS selector for the exact DOM element to locate, for example h1, input[name="q"], or [data-testid="result"].
           */
          selector?: string;
          /**
           * Visible text to locate when a selector is not known. The tool returns the text range bounds when possible.
           */
          text?: string;
          /**
           * How to match text targets. Defaults to contains.
           */
          match?: "contains" | "exact";
          /**
           * Zero-based match index when multiple elements match.
           */
          index?: number;
        },
        {
          /**
           * Optional label for this target, echoed in the result.
           */
          name?: string;
          /**
           * CSS selector for the exact DOM element to locate, for example h1, input[name="q"], or [data-testid="result"].
           */
          selector?: string;
          /**
           * Visible text to locate when a selector is not known. The tool returns the text range bounds when possible.
           */
          text?: string;
          /**
           * How to match text targets. Defaults to contains.
           */
          match?: "contains" | "exact";
          /**
           * Zero-based match index when multiple elements match.
           */
          index?: number;
        },
        {
          /**
           * Optional label for this target, echoed in the result.
           */
          name?: string;
          /**
           * CSS selector for the exact DOM element to locate, for example h1, input[name="q"], or [data-testid="result"].
           */
          selector?: string;
          /**
           * Visible text to locate when a selector is not known. The tool returns the text range bounds when possible.
           */
          text?: string;
          /**
           * How to match text targets. Defaults to contains.
           */
          match?: "contains" | "exact";
          /**
           * Zero-based match index when multiple elements match.
           */
          index?: number;
        },
        {
          /**
           * Optional label for this target, echoed in the result.
           */
          name?: string;
          /**
           * CSS selector for the exact DOM element to locate, for example h1, input[name="q"], or [data-testid="result"].
           */
          selector?: string;
          /**
           * Visible text to locate when a selector is not known. The tool returns the text range bounds when possible.
           */
          text?: string;
          /**
           * How to match text targets. Defaults to contains.
           */
          match?: "contains" | "exact";
          /**
           * Zero-based match index when multiple elements match.
           */
          index?: number;
        },
        {
          /**
           * Optional label for this target, echoed in the result.
           */
          name?: string;
          /**
           * CSS selector for the exact DOM element to locate, for example h1, input[name="q"], or [data-testid="result"].
           */
          selector?: string;
          /**
           * Visible text to locate when a selector is not known. The tool returns the text range bounds when possible.
           */
          text?: string;
          /**
           * How to match text targets. Defaults to contains.
           */
          match?: "contains" | "exact";
          /**
           * Zero-based match index when multiple elements match.
           */
          index?: number;
        },
        {
          /**
           * Optional label for this target, echoed in the result.
           */
          name?: string;
          /**
           * CSS selector for the exact DOM element to locate, for example h1, input[name="q"], or [data-testid="result"].
           */
          selector?: string;
          /**
           * Visible text to locate when a selector is not known. The tool returns the text range bounds when possible.
           */
          text?: string;
          /**
           * How to match text targets. Defaults to contains.
           */
          match?: "contains" | "exact";
          /**
           * Zero-based match index when multiple elements match.
           */
          index?: number;
        },
        {
          /**
           * Optional label for this target, echoed in the result.
           */
          name?: string;
          /**
           * CSS selector for the exact DOM element to locate, for example h1, input[name="q"], or [data-testid="result"].
           */
          selector?: string;
          /**
           * Visible text to locate when a selector is not known. The tool returns the text range bounds when possible.
           */
          text?: string;
          /**
           * How to match text targets. Defaults to contains.
           */
          match?: "contains" | "exact";
          /**
           * Zero-based match index when multiple elements match.
           */
          index?: number;
        },
        {
          /**
           * Optional label for this target, echoed in the result.
           */
          name?: string;
          /**
           * CSS selector for the exact DOM element to locate, for example h1, input[name="q"], or [data-testid="result"].
           */
          selector?: string;
          /**
           * Visible text to locate when a selector is not known. The tool returns the text range bounds when possible.
           */
          text?: string;
          /**
           * How to match text targets. Defaults to contains.
           */
          match?: "contains" | "exact";
          /**
           * Zero-based match index when multiple elements match.
           */
          index?: number;
        },
        {
          /**
           * Optional label for this target, echoed in the result.
           */
          name?: string;
          /**
           * CSS selector for the exact DOM element to locate, for example h1, input[name="q"], or [data-testid="result"].
           */
          selector?: string;
          /**
           * Visible text to locate when a selector is not known. The tool returns the text range bounds when possible.
           */
          text?: string;
          /**
           * How to match text targets. Defaults to contains.
           */
          match?: "contains" | "exact";
          /**
           * Zero-based match index when multiple elements match.
           */
          index?: number;
        },
        {
          /**
           * Optional label for this target, echoed in the result.
           */
          name?: string;
          /**
           * CSS selector for the exact DOM element to locate, for example h1, input[name="q"], or [data-testid="result"].
           */
          selector?: string;
          /**
           * Visible text to locate when a selector is not known. The tool returns the text range bounds when possible.
           */
          text?: string;
          /**
           * How to match text targets. Defaults to contains.
           */
          match?: "contains" | "exact";
          /**
           * Zero-based match index when multiple elements match.
           */
          index?: number;
        },
        {
          /**
           * Optional label for this target, echoed in the result.
           */
          name?: string;
          /**
           * CSS selector for the exact DOM element to locate, for example h1, input[name="q"], or [data-testid="result"].
           */
          selector?: string;
          /**
           * Visible text to locate when a selector is not known. The tool returns the text range bounds when possible.
           */
          text?: string;
          /**
           * How to match text targets. Defaults to contains.
           */
          match?: "contains" | "exact";
          /**
           * Zero-based match index when multiple elements match.
           */
          index?: number;
        },
        {
          /**
           * Optional label for this target, echoed in the result.
           */
          name?: string;
          /**
           * CSS selector for the exact DOM element to locate, for example h1, input[name="q"], or [data-testid="result"].
           */
          selector?: string;
          /**
           * Visible text to locate when a selector is not known. The tool returns the text range bounds when possible.
           */
          text?: string;
          /**
           * How to match text targets. Defaults to contains.
           */
          match?: "contains" | "exact";
          /**
           * Zero-based match index when multiple elements match.
           */
          index?: number;
        }
      ]
    | [
        {
          /**
           * Optional label for this target, echoed in the result.
           */
          name?: string;
          /**
           * CSS selector for the exact DOM element to locate, for example h1, input[name="q"], or [data-testid="result"].
           */
          selector?: string;
          /**
           * Visible text to locate when a selector is not known. The tool returns the text range bounds when possible.
           */
          text?: string;
          /**
           * How to match text targets. Defaults to contains.
           */
          match?: "contains" | "exact";
          /**
           * Zero-based match index when multiple elements match.
           */
          index?: number;
        },
        {
          /**
           * Optional label for this target, echoed in the result.
           */
          name?: string;
          /**
           * CSS selector for the exact DOM element to locate, for example h1, input[name="q"], or [data-testid="result"].
           */
          selector?: string;
          /**
           * Visible text to locate when a selector is not known. The tool returns the text range bounds when possible.
           */
          text?: string;
          /**
           * How to match text targets. Defaults to contains.
           */
          match?: "contains" | "exact";
          /**
           * Zero-based match index when multiple elements match.
           */
          index?: number;
        },
        {
          /**
           * Optional label for this target, echoed in the result.
           */
          name?: string;
          /**
           * CSS selector for the exact DOM element to locate, for example h1, input[name="q"], or [data-testid="result"].
           */
          selector?: string;
          /**
           * Visible text to locate when a selector is not known. The tool returns the text range bounds when possible.
           */
          text?: string;
          /**
           * How to match text targets. Defaults to contains.
           */
          match?: "contains" | "exact";
          /**
           * Zero-based match index when multiple elements match.
           */
          index?: number;
        },
        {
          /**
           * Optional label for this target, echoed in the result.
           */
          name?: string;
          /**
           * CSS selector for the exact DOM element to locate, for example h1, input[name="q"], or [data-testid="result"].
           */
          selector?: string;
          /**
           * Visible text to locate when a selector is not known. The tool returns the text range bounds when possible.
           */
          text?: string;
          /**
           * How to match text targets. Defaults to contains.
           */
          match?: "contains" | "exact";
          /**
           * Zero-based match index when multiple elements match.
           */
          index?: number;
        },
        {
          /**
           * Optional label for this target, echoed in the result.
           */
          name?: string;
          /**
           * CSS selector for the exact DOM element to locate, for example h1, input[name="q"], or [data-testid="result"].
           */
          selector?: string;
          /**
           * Visible text to locate when a selector is not known. The tool returns the text range bounds when possible.
           */
          text?: string;
          /**
           * How to match text targets. Defaults to contains.
           */
          match?: "contains" | "exact";
          /**
           * Zero-based match index when multiple elements match.
           */
          index?: number;
        },
        {
          /**
           * Optional label for this target, echoed in the result.
           */
          name?: string;
          /**
           * CSS selector for the exact DOM element to locate, for example h1, input[name="q"], or [data-testid="result"].
           */
          selector?: string;
          /**
           * Visible text to locate when a selector is not known. The tool returns the text range bounds when possible.
           */
          text?: string;
          /**
           * How to match text targets. Defaults to contains.
           */
          match?: "contains" | "exact";
          /**
           * Zero-based match index when multiple elements match.
           */
          index?: number;
        },
        {
          /**
           * Optional label for this target, echoed in the result.
           */
          name?: string;
          /**
           * CSS selector for the exact DOM element to locate, for example h1, input[name="q"], or [data-testid="result"].
           */
          selector?: string;
          /**
           * Visible text to locate when a selector is not known. The tool returns the text range bounds when possible.
           */
          text?: string;
          /**
           * How to match text targets. Defaults to contains.
           */
          match?: "contains" | "exact";
          /**
           * Zero-based match index when multiple elements match.
           */
          index?: number;
        },
        {
          /**
           * Optional label for this target, echoed in the result.
           */
          name?: string;
          /**
           * CSS selector for the exact DOM element to locate, for example h1, input[name="q"], or [data-testid="result"].
           */
          selector?: string;
          /**
           * Visible text to locate when a selector is not known. The tool returns the text range bounds when possible.
           */
          text?: string;
          /**
           * How to match text targets. Defaults to contains.
           */
          match?: "contains" | "exact";
          /**
           * Zero-based match index when multiple elements match.
           */
          index?: number;
        },
        {
          /**
           * Optional label for this target, echoed in the result.
           */
          name?: string;
          /**
           * CSS selector for the exact DOM element to locate, for example h1, input[name="q"], or [data-testid="result"].
           */
          selector?: string;
          /**
           * Visible text to locate when a selector is not known. The tool returns the text range bounds when possible.
           */
          text?: string;
          /**
           * How to match text targets. Defaults to contains.
           */
          match?: "contains" | "exact";
          /**
           * Zero-based match index when multiple elements match.
           */
          index?: number;
        },
        {
          /**
           * Optional label for this target, echoed in the result.
           */
          name?: string;
          /**
           * CSS selector for the exact DOM element to locate, for example h1, input[name="q"], or [data-testid="result"].
           */
          selector?: string;
          /**
           * Visible text to locate when a selector is not known. The tool returns the text range bounds when possible.
           */
          text?: string;
          /**
           * How to match text targets. Defaults to contains.
           */
          match?: "contains" | "exact";
          /**
           * Zero-based match index when multiple elements match.
           */
          index?: number;
        },
        {
          /**
           * Optional label for this target, echoed in the result.
           */
          name?: string;
          /**
           * CSS selector for the exact DOM element to locate, for example h1, input[name="q"], or [data-testid="result"].
           */
          selector?: string;
          /**
           * Visible text to locate when a selector is not known. The tool returns the text range bounds when possible.
           */
          text?: string;
          /**
           * How to match text targets. Defaults to contains.
           */
          match?: "contains" | "exact";
          /**
           * Zero-based match index when multiple elements match.
           */
          index?: number;
        },
        {
          /**
           * Optional label for this target, echoed in the result.
           */
          name?: string;
          /**
           * CSS selector for the exact DOM element to locate, for example h1, input[name="q"], or [data-testid="result"].
           */
          selector?: string;
          /**
           * Visible text to locate when a selector is not known. The tool returns the text range bounds when possible.
           */
          text?: string;
          /**
           * How to match text targets. Defaults to contains.
           */
          match?: "contains" | "exact";
          /**
           * Zero-based match index when multiple elements match.
           */
          index?: number;
        },
        {
          /**
           * Optional label for this target, echoed in the result.
           */
          name?: string;
          /**
           * CSS selector for the exact DOM element to locate, for example h1, input[name="q"], or [data-testid="result"].
           */
          selector?: string;
          /**
           * Visible text to locate when a selector is not known. The tool returns the text range bounds when possible.
           */
          text?: string;
          /**
           * How to match text targets. Defaults to contains.
           */
          match?: "contains" | "exact";
          /**
           * Zero-based match index when multiple elements match.
           */
          index?: number;
        },
        {
          /**
           * Optional label for this target, echoed in the result.
           */
          name?: string;
          /**
           * CSS selector for the exact DOM element to locate, for example h1, input[name="q"], or [data-testid="result"].
           */
          selector?: string;
          /**
           * Visible text to locate when a selector is not known. The tool returns the text range bounds when possible.
           */
          text?: string;
          /**
           * How to match text targets. Defaults to contains.
           */
          match?: "contains" | "exact";
          /**
           * Zero-based match index when multiple elements match.
           */
          index?: number;
        },
        {
          /**
           * Optional label for this target, echoed in the result.
           */
          name?: string;
          /**
           * CSS selector for the exact DOM element to locate, for example h1, input[name="q"], or [data-testid="result"].
           */
          selector?: string;
          /**
           * Visible text to locate when a selector is not known. The tool returns the text range bounds when possible.
           */
          text?: string;
          /**
           * How to match text targets. Defaults to contains.
           */
          match?: "contains" | "exact";
          /**
           * Zero-based match index when multiple elements match.
           */
          index?: number;
        },
        {
          /**
           * Optional label for this target, echoed in the result.
           */
          name?: string;
          /**
           * CSS selector for the exact DOM element to locate, for example h1, input[name="q"], or [data-testid="result"].
           */
          selector?: string;
          /**
           * Visible text to locate when a selector is not known. The tool returns the text range bounds when possible.
           */
          text?: string;
          /**
           * How to match text targets. Defaults to contains.
           */
          match?: "contains" | "exact";
          /**
           * Zero-based match index when multiple elements match.
           */
          index?: number;
        },
        {
          /**
           * Optional label for this target, echoed in the result.
           */
          name?: string;
          /**
           * CSS selector for the exact DOM element to locate, for example h1, input[name="q"], or [data-testid="result"].
           */
          selector?: string;
          /**
           * Visible text to locate when a selector is not known. The tool returns the text range bounds when possible.
           */
          text?: string;
          /**
           * How to match text targets. Defaults to contains.
           */
          match?: "contains" | "exact";
          /**
           * Zero-based match index when multiple elements match.
           */
          index?: number;
        }
      ]
    | [
        {
          /**
           * Optional label for this target, echoed in the result.
           */
          name?: string;
          /**
           * CSS selector for the exact DOM element to locate, for example h1, input[name="q"], or [data-testid="result"].
           */
          selector?: string;
          /**
           * Visible text to locate when a selector is not known. The tool returns the text range bounds when possible.
           */
          text?: string;
          /**
           * How to match text targets. Defaults to contains.
           */
          match?: "contains" | "exact";
          /**
           * Zero-based match index when multiple elements match.
           */
          index?: number;
        },
        {
          /**
           * Optional label for this target, echoed in the result.
           */
          name?: string;
          /**
           * CSS selector for the exact DOM element to locate, for example h1, input[name="q"], or [data-testid="result"].
           */
          selector?: string;
          /**
           * Visible text to locate when a selector is not known. The tool returns the text range bounds when possible.
           */
          text?: string;
          /**
           * How to match text targets. Defaults to contains.
           */
          match?: "contains" | "exact";
          /**
           * Zero-based match index when multiple elements match.
           */
          index?: number;
        },
        {
          /**
           * Optional label for this target, echoed in the result.
           */
          name?: string;
          /**
           * CSS selector for the exact DOM element to locate, for example h1, input[name="q"], or [data-testid="result"].
           */
          selector?: string;
          /**
           * Visible text to locate when a selector is not known. The tool returns the text range bounds when possible.
           */
          text?: string;
          /**
           * How to match text targets. Defaults to contains.
           */
          match?: "contains" | "exact";
          /**
           * Zero-based match index when multiple elements match.
           */
          index?: number;
        },
        {
          /**
           * Optional label for this target, echoed in the result.
           */
          name?: string;
          /**
           * CSS selector for the exact DOM element to locate, for example h1, input[name="q"], or [data-testid="result"].
           */
          selector?: string;
          /**
           * Visible text to locate when a selector is not known. The tool returns the text range bounds when possible.
           */
          text?: string;
          /**
           * How to match text targets. Defaults to contains.
           */
          match?: "contains" | "exact";
          /**
           * Zero-based match index when multiple elements match.
           */
          index?: number;
        },
        {
          /**
           * Optional label for this target, echoed in the result.
           */
          name?: string;
          /**
           * CSS selector for the exact DOM element to locate, for example h1, input[name="q"], or [data-testid="result"].
           */
          selector?: string;
          /**
           * Visible text to locate when a selector is not known. The tool returns the text range bounds when possible.
           */
          text?: string;
          /**
           * How to match text targets. Defaults to contains.
           */
          match?: "contains" | "exact";
          /**
           * Zero-based match index when multiple elements match.
           */
          index?: number;
        },
        {
          /**
           * Optional label for this target, echoed in the result.
           */
          name?: string;
          /**
           * CSS selector for the exact DOM element to locate, for example h1, input[name="q"], or [data-testid="result"].
           */
          selector?: string;
          /**
           * Visible text to locate when a selector is not known. The tool returns the text range bounds when possible.
           */
          text?: string;
          /**
           * How to match text targets. Defaults to contains.
           */
          match?: "contains" | "exact";
          /**
           * Zero-based match index when multiple elements match.
           */
          index?: number;
        },
        {
          /**
           * Optional label for this target, echoed in the result.
           */
          name?: string;
          /**
           * CSS selector for the exact DOM element to locate, for example h1, input[name="q"], or [data-testid="result"].
           */
          selector?: string;
          /**
           * Visible text to locate when a selector is not known. The tool returns the text range bounds when possible.
           */
          text?: string;
          /**
           * How to match text targets. Defaults to contains.
           */
          match?: "contains" | "exact";
          /**
           * Zero-based match index when multiple elements match.
           */
          index?: number;
        },
        {
          /**
           * Optional label for this target, echoed in the result.
           */
          name?: string;
          /**
           * CSS selector for the exact DOM element to locate, for example h1, input[name="q"], or [data-testid="result"].
           */
          selector?: string;
          /**
           * Visible text to locate when a selector is not known. The tool returns the text range bounds when possible.
           */
          text?: string;
          /**
           * How to match text targets. Defaults to contains.
           */
          match?: "contains" | "exact";
          /**
           * Zero-based match index when multiple elements match.
           */
          index?: number;
        },
        {
          /**
           * Optional label for this target, echoed in the result.
           */
          name?: string;
          /**
           * CSS selector for the exact DOM element to locate, for example h1, input[name="q"], or [data-testid="result"].
           */
          selector?: string;
          /**
           * Visible text to locate when a selector is not known. The tool returns the text range bounds when possible.
           */
          text?: string;
          /**
           * How to match text targets. Defaults to contains.
           */
          match?: "contains" | "exact";
          /**
           * Zero-based match index when multiple elements match.
           */
          index?: number;
        },
        {
          /**
           * Optional label for this target, echoed in the result.
           */
          name?: string;
          /**
           * CSS selector for the exact DOM element to locate, for example h1, input[name="q"], or [data-testid="result"].
           */
          selector?: string;
          /**
           * Visible text to locate when a selector is not known. The tool returns the text range bounds when possible.
           */
          text?: string;
          /**
           * How to match text targets. Defaults to contains.
           */
          match?: "contains" | "exact";
          /**
           * Zero-based match index when multiple elements match.
           */
          index?: number;
        },
        {
          /**
           * Optional label for this target, echoed in the result.
           */
          name?: string;
          /**
           * CSS selector for the exact DOM element to locate, for example h1, input[name="q"], or [data-testid="result"].
           */
          selector?: string;
          /**
           * Visible text to locate when a selector is not known. The tool returns the text range bounds when possible.
           */
          text?: string;
          /**
           * How to match text targets. Defaults to contains.
           */
          match?: "contains" | "exact";
          /**
           * Zero-based match index when multiple elements match.
           */
          index?: number;
        },
        {
          /**
           * Optional label for this target, echoed in the result.
           */
          name?: string;
          /**
           * CSS selector for the exact DOM element to locate, for example h1, input[name="q"], or [data-testid="result"].
           */
          selector?: string;
          /**
           * Visible text to locate when a selector is not known. The tool returns the text range bounds when possible.
           */
          text?: string;
          /**
           * How to match text targets. Defaults to contains.
           */
          match?: "contains" | "exact";
          /**
           * Zero-based match index when multiple elements match.
           */
          index?: number;
        },
        {
          /**
           * Optional label for this target, echoed in the result.
           */
          name?: string;
          /**
           * CSS selector for the exact DOM element to locate, for example h1, input[name="q"], or [data-testid="result"].
           */
          selector?: string;
          /**
           * Visible text to locate when a selector is not known. The tool returns the text range bounds when possible.
           */
          text?: string;
          /**
           * How to match text targets. Defaults to contains.
           */
          match?: "contains" | "exact";
          /**
           * Zero-based match index when multiple elements match.
           */
          index?: number;
        },
        {
          /**
           * Optional label for this target, echoed in the result.
           */
          name?: string;
          /**
           * CSS selector for the exact DOM element to locate, for example h1, input[name="q"], or [data-testid="result"].
           */
          selector?: string;
          /**
           * Visible text to locate when a selector is not known. The tool returns the text range bounds when possible.
           */
          text?: string;
          /**
           * How to match text targets. Defaults to contains.
           */
          match?: "contains" | "exact";
          /**
           * Zero-based match index when multiple elements match.
           */
          index?: number;
        },
        {
          /**
           * Optional label for this target, echoed in the result.
           */
          name?: string;
          /**
           * CSS selector for the exact DOM element to locate, for example h1, input[name="q"], or [data-testid="result"].
           */
          selector?: string;
          /**
           * Visible text to locate when a selector is not known. The tool returns the text range bounds when possible.
           */
          text?: string;
          /**
           * How to match text targets. Defaults to contains.
           */
          match?: "contains" | "exact";
          /**
           * Zero-based match index when multiple elements match.
           */
          index?: number;
        },
        {
          /**
           * Optional label for this target, echoed in the result.
           */
          name?: string;
          /**
           * CSS selector for the exact DOM element to locate, for example h1, input[name="q"], or [data-testid="result"].
           */
          selector?: string;
          /**
           * Visible text to locate when a selector is not known. The tool returns the text range bounds when possible.
           */
          text?: string;
          /**
           * How to match text targets. Defaults to contains.
           */
          match?: "contains" | "exact";
          /**
           * Zero-based match index when multiple elements match.
           */
          index?: number;
        },
        {
          /**
           * Optional label for this target, echoed in the result.
           */
          name?: string;
          /**
           * CSS selector for the exact DOM element to locate, for example h1, input[name="q"], or [data-testid="result"].
           */
          selector?: string;
          /**
           * Visible text to locate when a selector is not known. The tool returns the text range bounds when possible.
           */
          text?: string;
          /**
           * How to match text targets. Defaults to contains.
           */
          match?: "contains" | "exact";
          /**
           * Zero-based match index when multiple elements match.
           */
          index?: number;
        },
        {
          /**
           * Optional label for this target, echoed in the result.
           */
          name?: string;
          /**
           * CSS selector for the exact DOM element to locate, for example h1, input[name="q"], or [data-testid="result"].
           */
          selector?: string;
          /**
           * Visible text to locate when a selector is not known. The tool returns the text range bounds when possible.
           */
          text?: string;
          /**
           * How to match text targets. Defaults to contains.
           */
          match?: "contains" | "exact";
          /**
           * Zero-based match index when multiple elements match.
           */
          index?: number;
        }
      ]
    | [
        {
          /**
           * Optional label for this target, echoed in the result.
           */
          name?: string;
          /**
           * CSS selector for the exact DOM element to locate, for example h1, input[name="q"], or [data-testid="result"].
           */
          selector?: string;
          /**
           * Visible text to locate when a selector is not known. The tool returns the text range bounds when possible.
           */
          text?: string;
          /**
           * How to match text targets. Defaults to contains.
           */
          match?: "contains" | "exact";
          /**
           * Zero-based match index when multiple elements match.
           */
          index?: number;
        },
        {
          /**
           * Optional label for this target, echoed in the result.
           */
          name?: string;
          /**
           * CSS selector for the exact DOM element to locate, for example h1, input[name="q"], or [data-testid="result"].
           */
          selector?: string;
          /**
           * Visible text to locate when a selector is not known. The tool returns the text range bounds when possible.
           */
          text?: string;
          /**
           * How to match text targets. Defaults to contains.
           */
          match?: "contains" | "exact";
          /**
           * Zero-based match index when multiple elements match.
           */
          index?: number;
        },
        {
          /**
           * Optional label for this target, echoed in the result.
           */
          name?: string;
          /**
           * CSS selector for the exact DOM element to locate, for example h1, input[name="q"], or [data-testid="result"].
           */
          selector?: string;
          /**
           * Visible text to locate when a selector is not known. The tool returns the text range bounds when possible.
           */
          text?: string;
          /**
           * How to match text targets. Defaults to contains.
           */
          match?: "contains" | "exact";
          /**
           * Zero-based match index when multiple elements match.
           */
          index?: number;
        },
        {
          /**
           * Optional label for this target, echoed in the result.
           */
          name?: string;
          /**
           * CSS selector for the exact DOM element to locate, for example h1, input[name="q"], or [data-testid="result"].
           */
          selector?: string;
          /**
           * Visible text to locate when a selector is not known. The tool returns the text range bounds when possible.
           */
          text?: string;
          /**
           * How to match text targets. Defaults to contains.
           */
          match?: "contains" | "exact";
          /**
           * Zero-based match index when multiple elements match.
           */
          index?: number;
        },
        {
          /**
           * Optional label for this target, echoed in the result.
           */
          name?: string;
          /**
           * CSS selector for the exact DOM element to locate, for example h1, input[name="q"], or [data-testid="result"].
           */
          selector?: string;
          /**
           * Visible text to locate when a selector is not known. The tool returns the text range bounds when possible.
           */
          text?: string;
          /**
           * How to match text targets. Defaults to contains.
           */
          match?: "contains" | "exact";
          /**
           * Zero-based match index when multiple elements match.
           */
          index?: number;
        },
        {
          /**
           * Optional label for this target, echoed in the result.
           */
          name?: string;
          /**
           * CSS selector for the exact DOM element to locate, for example h1, input[name="q"], or [data-testid="result"].
           */
          selector?: string;
          /**
           * Visible text to locate when a selector is not known. The tool returns the text range bounds when possible.
           */
          text?: string;
          /**
           * How to match text targets. Defaults to contains.
           */
          match?: "contains" | "exact";
          /**
           * Zero-based match index when multiple elements match.
           */
          index?: number;
        },
        {
          /**
           * Optional label for this target, echoed in the result.
           */
          name?: string;
          /**
           * CSS selector for the exact DOM element to locate, for example h1, input[name="q"], or [data-testid="result"].
           */
          selector?: string;
          /**
           * Visible text to locate when a selector is not known. The tool returns the text range bounds when possible.
           */
          text?: string;
          /**
           * How to match text targets. Defaults to contains.
           */
          match?: "contains" | "exact";
          /**
           * Zero-based match index when multiple elements match.
           */
          index?: number;
        },
        {
          /**
           * Optional label for this target, echoed in the result.
           */
          name?: string;
          /**
           * CSS selector for the exact DOM element to locate, for example h1, input[name="q"], or [data-testid="result"].
           */
          selector?: string;
          /**
           * Visible text to locate when a selector is not known. The tool returns the text range bounds when possible.
           */
          text?: string;
          /**
           * How to match text targets. Defaults to contains.
           */
          match?: "contains" | "exact";
          /**
           * Zero-based match index when multiple elements match.
           */
          index?: number;
        },
        {
          /**
           * Optional label for this target, echoed in the result.
           */
          name?: string;
          /**
           * CSS selector for the exact DOM element to locate, for example h1, input[name="q"], or [data-testid="result"].
           */
          selector?: string;
          /**
           * Visible text to locate when a selector is not known. The tool returns the text range bounds when possible.
           */
          text?: string;
          /**
           * How to match text targets. Defaults to contains.
           */
          match?: "contains" | "exact";
          /**
           * Zero-based match index when multiple elements match.
           */
          index?: number;
        },
        {
          /**
           * Optional label for this target, echoed in the result.
           */
          name?: string;
          /**
           * CSS selector for the exact DOM element to locate, for example h1, input[name="q"], or [data-testid="result"].
           */
          selector?: string;
          /**
           * Visible text to locate when a selector is not known. The tool returns the text range bounds when possible.
           */
          text?: string;
          /**
           * How to match text targets. Defaults to contains.
           */
          match?: "contains" | "exact";
          /**
           * Zero-based match index when multiple elements match.
           */
          index?: number;
        },
        {
          /**
           * Optional label for this target, echoed in the result.
           */
          name?: string;
          /**
           * CSS selector for the exact DOM element to locate, for example h1, input[name="q"], or [data-testid="result"].
           */
          selector?: string;
          /**
           * Visible text to locate when a selector is not known. The tool returns the text range bounds when possible.
           */
          text?: string;
          /**
           * How to match text targets. Defaults to contains.
           */
          match?: "contains" | "exact";
          /**
           * Zero-based match index when multiple elements match.
           */
          index?: number;
        },
        {
          /**
           * Optional label for this target, echoed in the result.
           */
          name?: string;
          /**
           * CSS selector for the exact DOM element to locate, for example h1, input[name="q"], or [data-testid="result"].
           */
          selector?: string;
          /**
           * Visible text to locate when a selector is not known. The tool returns the text range bounds when possible.
           */
          text?: string;
          /**
           * How to match text targets. Defaults to contains.
           */
          match?: "contains" | "exact";
          /**
           * Zero-based match index when multiple elements match.
           */
          index?: number;
        },
        {
          /**
           * Optional label for this target, echoed in the result.
           */
          name?: string;
          /**
           * CSS selector for the exact DOM element to locate, for example h1, input[name="q"], or [data-testid="result"].
           */
          selector?: string;
          /**
           * Visible text to locate when a selector is not known. The tool returns the text range bounds when possible.
           */
          text?: string;
          /**
           * How to match text targets. Defaults to contains.
           */
          match?: "contains" | "exact";
          /**
           * Zero-based match index when multiple elements match.
           */
          index?: number;
        },
        {
          /**
           * Optional label for this target, echoed in the result.
           */
          name?: string;
          /**
           * CSS selector for the exact DOM element to locate, for example h1, input[name="q"], or [data-testid="result"].
           */
          selector?: string;
          /**
           * Visible text to locate when a selector is not known. The tool returns the text range bounds when possible.
           */
          text?: string;
          /**
           * How to match text targets. Defaults to contains.
           */
          match?: "contains" | "exact";
          /**
           * Zero-based match index when multiple elements match.
           */
          index?: number;
        },
        {
          /**
           * Optional label for this target, echoed in the result.
           */
          name?: string;
          /**
           * CSS selector for the exact DOM element to locate, for example h1, input[name="q"], or [data-testid="result"].
           */
          selector?: string;
          /**
           * Visible text to locate when a selector is not known. The tool returns the text range bounds when possible.
           */
          text?: string;
          /**
           * How to match text targets. Defaults to contains.
           */
          match?: "contains" | "exact";
          /**
           * Zero-based match index when multiple elements match.
           */
          index?: number;
        },
        {
          /**
           * Optional label for this target, echoed in the result.
           */
          name?: string;
          /**
           * CSS selector for the exact DOM element to locate, for example h1, input[name="q"], or [data-testid="result"].
           */
          selector?: string;
          /**
           * Visible text to locate when a selector is not known. The tool returns the text range bounds when possible.
           */
          text?: string;
          /**
           * How to match text targets. Defaults to contains.
           */
          match?: "contains" | "exact";
          /**
           * Zero-based match index when multiple elements match.
           */
          index?: number;
        },
        {
          /**
           * Optional label for this target, echoed in the result.
           */
          name?: string;
          /**
           * CSS selector for the exact DOM element to locate, for example h1, input[name="q"], or [data-testid="result"].
           */
          selector?: string;
          /**
           * Visible text to locate when a selector is not known. The tool returns the text range bounds when possible.
           */
          text?: string;
          /**
           * How to match text targets. Defaults to contains.
           */
          match?: "contains" | "exact";
          /**
           * Zero-based match index when multiple elements match.
           */
          index?: number;
        },
        {
          /**
           * Optional label for this target, echoed in the result.
           */
          name?: string;
          /**
           * CSS selector for the exact DOM element to locate, for example h1, input[name="q"], or [data-testid="result"].
           */
          selector?: string;
          /**
           * Visible text to locate when a selector is not known. The tool returns the text range bounds when possible.
           */
          text?: string;
          /**
           * How to match text targets. Defaults to contains.
           */
          match?: "contains" | "exact";
          /**
           * Zero-based match index when multiple elements match.
           */
          index?: number;
        },
        {
          /**
           * Optional label for this target, echoed in the result.
           */
          name?: string;
          /**
           * CSS selector for the exact DOM element to locate, for example h1, input[name="q"], or [data-testid="result"].
           */
          selector?: string;
          /**
           * Visible text to locate when a selector is not known. The tool returns the text range bounds when possible.
           */
          text?: string;
          /**
           * How to match text targets. Defaults to contains.
           */
          match?: "contains" | "exact";
          /**
           * Zero-based match index when multiple elements match.
           */
          index?: number;
        }
      ]
    | [
        {
          /**
           * Optional label for this target, echoed in the result.
           */
          name?: string;
          /**
           * CSS selector for the exact DOM element to locate, for example h1, input[name="q"], or [data-testid="result"].
           */
          selector?: string;
          /**
           * Visible text to locate when a selector is not known. The tool returns the text range bounds when possible.
           */
          text?: string;
          /**
           * How to match text targets. Defaults to contains.
           */
          match?: "contains" | "exact";
          /**
           * Zero-based match index when multiple elements match.
           */
          index?: number;
        },
        {
          /**
           * Optional label for this target, echoed in the result.
           */
          name?: string;
          /**
           * CSS selector for the exact DOM element to locate, for example h1, input[name="q"], or [data-testid="result"].
           */
          selector?: string;
          /**
           * Visible text to locate when a selector is not known. The tool returns the text range bounds when possible.
           */
          text?: string;
          /**
           * How to match text targets. Defaults to contains.
           */
          match?: "contains" | "exact";
          /**
           * Zero-based match index when multiple elements match.
           */
          index?: number;
        },
        {
          /**
           * Optional label for this target, echoed in the result.
           */
          name?: string;
          /**
           * CSS selector for the exact DOM element to locate, for example h1, input[name="q"], or [data-testid="result"].
           */
          selector?: string;
          /**
           * Visible text to locate when a selector is not known. The tool returns the text range bounds when possible.
           */
          text?: string;
          /**
           * How to match text targets. Defaults to contains.
           */
          match?: "contains" | "exact";
          /**
           * Zero-based match index when multiple elements match.
           */
          index?: number;
        },
        {
          /**
           * Optional label for this target, echoed in the result.
           */
          name?: string;
          /**
           * CSS selector for the exact DOM element to locate, for example h1, input[name="q"], or [data-testid="result"].
           */
          selector?: string;
          /**
           * Visible text to locate when a selector is not known. The tool returns the text range bounds when possible.
           */
          text?: string;
          /**
           * How to match text targets. Defaults to contains.
           */
          match?: "contains" | "exact";
          /**
           * Zero-based match index when multiple elements match.
           */
          index?: number;
        },
        {
          /**
           * Optional label for this target, echoed in the result.
           */
          name?: string;
          /**
           * CSS selector for the exact DOM element to locate, for example h1, input[name="q"], or [data-testid="result"].
           */
          selector?: string;
          /**
           * Visible text to locate when a selector is not known. The tool returns the text range bounds when possible.
           */
          text?: string;
          /**
           * How to match text targets. Defaults to contains.
           */
          match?: "contains" | "exact";
          /**
           * Zero-based match index when multiple elements match.
           */
          index?: number;
        },
        {
          /**
           * Optional label for this target, echoed in the result.
           */
          name?: string;
          /**
           * CSS selector for the exact DOM element to locate, for example h1, input[name="q"], or [data-testid="result"].
           */
          selector?: string;
          /**
           * Visible text to locate when a selector is not known. The tool returns the text range bounds when possible.
           */
          text?: string;
          /**
           * How to match text targets. Defaults to contains.
           */
          match?: "contains" | "exact";
          /**
           * Zero-based match index when multiple elements match.
           */
          index?: number;
        },
        {
          /**
           * Optional label for this target, echoed in the result.
           */
          name?: string;
          /**
           * CSS selector for the exact DOM element to locate, for example h1, input[name="q"], or [data-testid="result"].
           */
          selector?: string;
          /**
           * Visible text to locate when a selector is not known. The tool returns the text range bounds when possible.
           */
          text?: string;
          /**
           * How to match text targets. Defaults to contains.
           */
          match?: "contains" | "exact";
          /**
           * Zero-based match index when multiple elements match.
           */
          index?: number;
        },
        {
          /**
           * Optional label for this target, echoed in the result.
           */
          name?: string;
          /**
           * CSS selector for the exact DOM element to locate, for example h1, input[name="q"], or [data-testid="result"].
           */
          selector?: string;
          /**
           * Visible text to locate when a selector is not known. The tool returns the text range bounds when possible.
           */
          text?: string;
          /**
           * How to match text targets. Defaults to contains.
           */
          match?: "contains" | "exact";
          /**
           * Zero-based match index when multiple elements match.
           */
          index?: number;
        },
        {
          /**
           * Optional label for this target, echoed in the result.
           */
          name?: string;
          /**
           * CSS selector for the exact DOM element to locate, for example h1, input[name="q"], or [data-testid="result"].
           */
          selector?: string;
          /**
           * Visible text to locate when a selector is not known. The tool returns the text range bounds when possible.
           */
          text?: string;
          /**
           * How to match text targets. Defaults to contains.
           */
          match?: "contains" | "exact";
          /**
           * Zero-based match index when multiple elements match.
           */
          index?: number;
        },
        {
          /**
           * Optional label for this target, echoed in the result.
           */
          name?: string;
          /**
           * CSS selector for the exact DOM element to locate, for example h1, input[name="q"], or [data-testid="result"].
           */
          selector?: string;
          /**
           * Visible text to locate when a selector is not known. The tool returns the text range bounds when possible.
           */
          text?: string;
          /**
           * How to match text targets. Defaults to contains.
           */
          match?: "contains" | "exact";
          /**
           * Zero-based match index when multiple elements match.
           */
          index?: number;
        },
        {
          /**
           * Optional label for this target, echoed in the result.
           */
          name?: string;
          /**
           * CSS selector for the exact DOM element to locate, for example h1, input[name="q"], or [data-testid="result"].
           */
          selector?: string;
          /**
           * Visible text to locate when a selector is not known. The tool returns the text range bounds when possible.
           */
          text?: string;
          /**
           * How to match text targets. Defaults to contains.
           */
          match?: "contains" | "exact";
          /**
           * Zero-based match index when multiple elements match.
           */
          index?: number;
        },
        {
          /**
           * Optional label for this target, echoed in the result.
           */
          name?: string;
          /**
           * CSS selector for the exact DOM element to locate, for example h1, input[name="q"], or [data-testid="result"].
           */
          selector?: string;
          /**
           * Visible text to locate when a selector is not known. The tool returns the text range bounds when possible.
           */
          text?: string;
          /**
           * How to match text targets. Defaults to contains.
           */
          match?: "contains" | "exact";
          /**
           * Zero-based match index when multiple elements match.
           */
          index?: number;
        },
        {
          /**
           * Optional label for this target, echoed in the result.
           */
          name?: string;
          /**
           * CSS selector for the exact DOM element to locate, for example h1, input[name="q"], or [data-testid="result"].
           */
          selector?: string;
          /**
           * Visible text to locate when a selector is not known. The tool returns the text range bounds when possible.
           */
          text?: string;
          /**
           * How to match text targets. Defaults to contains.
           */
          match?: "contains" | "exact";
          /**
           * Zero-based match index when multiple elements match.
           */
          index?: number;
        },
        {
          /**
           * Optional label for this target, echoed in the result.
           */
          name?: string;
          /**
           * CSS selector for the exact DOM element to locate, for example h1, input[name="q"], or [data-testid="result"].
           */
          selector?: string;
          /**
           * Visible text to locate when a selector is not known. The tool returns the text range bounds when possible.
           */
          text?: string;
          /**
           * How to match text targets. Defaults to contains.
           */
          match?: "contains" | "exact";
          /**
           * Zero-based match index when multiple elements match.
           */
          index?: number;
        },
        {
          /**
           * Optional label for this target, echoed in the result.
           */
          name?: string;
          /**
           * CSS selector for the exact DOM element to locate, for example h1, input[name="q"], or [data-testid="result"].
           */
          selector?: string;
          /**
           * Visible text to locate when a selector is not known. The tool returns the text range bounds when possible.
           */
          text?: string;
          /**
           * How to match text targets. Defaults to contains.
           */
          match?: "contains" | "exact";
          /**
           * Zero-based match index when multiple elements match.
           */
          index?: number;
        },
        {
          /**
           * Optional label for this target, echoed in the result.
           */
          name?: string;
          /**
           * CSS selector for the exact DOM element to locate, for example h1, input[name="q"], or [data-testid="result"].
           */
          selector?: string;
          /**
           * Visible text to locate when a selector is not known. The tool returns the text range bounds when possible.
           */
          text?: string;
          /**
           * How to match text targets. Defaults to contains.
           */
          match?: "contains" | "exact";
          /**
           * Zero-based match index when multiple elements match.
           */
          index?: number;
        },
        {
          /**
           * Optional label for this target, echoed in the result.
           */
          name?: string;
          /**
           * CSS selector for the exact DOM element to locate, for example h1, input[name="q"], or [data-testid="result"].
           */
          selector?: string;
          /**
           * Visible text to locate when a selector is not known. The tool returns the text range bounds when possible.
           */
          text?: string;
          /**
           * How to match text targets. Defaults to contains.
           */
          match?: "contains" | "exact";
          /**
           * Zero-based match index when multiple elements match.
           */
          index?: number;
        },
        {
          /**
           * Optional label for this target, echoed in the result.
           */
          name?: string;
          /**
           * CSS selector for the exact DOM element to locate, for example h1, input[name="q"], or [data-testid="result"].
           */
          selector?: string;
          /**
           * Visible text to locate when a selector is not known. The tool returns the text range bounds when possible.
           */
          text?: string;
          /**
           * How to match text targets. Defaults to contains.
           */
          match?: "contains" | "exact";
          /**
           * Zero-based match index when multiple elements match.
           */
          index?: number;
        },
        {
          /**
           * Optional label for this target, echoed in the result.
           */
          name?: string;
          /**
           * CSS selector for the exact DOM element to locate, for example h1, input[name="q"], or [data-testid="result"].
           */
          selector?: string;
          /**
           * Visible text to locate when a selector is not known. The tool returns the text range bounds when possible.
           */
          text?: string;
          /**
           * How to match text targets. Defaults to contains.
           */
          match?: "contains" | "exact";
          /**
           * Zero-based match index when multiple elements match.
           */
          index?: number;
        },
        {
          /**
           * Optional label for this target, echoed in the result.
           */
          name?: string;
          /**
           * CSS selector for the exact DOM element to locate, for example h1, input[name="q"], or [data-testid="result"].
           */
          selector?: string;
          /**
           * Visible text to locate when a selector is not known. The tool returns the text range bounds when possible.
           */
          text?: string;
          /**
           * How to match text targets. Defaults to contains.
           */
          match?: "contains" | "exact";
          /**
           * Zero-based match index when multiple elements match.
           */
          index?: number;
        }
      ];
}

export type Output = unknown
