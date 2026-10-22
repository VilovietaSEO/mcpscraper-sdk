export interface Input {
  /**
   * prepare saves a private one-day draft for review; submit sends that exact draft to support; status reads your report receipt.
   */
  action?: "prepare" | "submit" | "status";
  /**
   * Required for prepare. Collect known evidence from the conversation before asking the user for missing details.
   */
  report?: {
    /**
     * Short description of the problem in plain language.
     */
    title: string;
    /**
     * What the user was trying to accomplish, using their words.
     */
    goal: string;
    /**
     * What should have happened.
     */
    expected: string;
    /**
     * What actually happened. Separate observations from suspected causes.
     */
    actual: string;
    /**
     * Ordered reproduction steps, including retries and what changed.
     *
     * @minItems 1
     * @maxItems 30
     */
    steps: [string, ...string[]];
    /**
     * Calls in the order made. Include successful calls that explain the failure.
     *
     * @minItems 1
     * @maxItems 20
     */
    attempts:
      | [
          {
            /**
             * Exact tool name or REST method and path.
             */
            tool: string;
            /**
             * Observed call time with timezone; omit if unknown.
             */
            submittedAt?: string;
            /**
             * Exact submitted arguments as JSON or text. Remove credentials, cookies and unrelated private content first. Do not reconstruct unknown arguments.
             */
            arguments: string;
            /**
             * Observed response or error text, including error codes and retry outcome. Remove secrets.
             */
            result: string;
            /**
             * Returned request ID, when available.
             */
            requestId?: string;
            /**
             * Returned job or run ID, when available.
             */
            jobId?: string;
          }
        ]
      | [
          {
            /**
             * Exact tool name or REST method and path.
             */
            tool: string;
            /**
             * Observed call time with timezone; omit if unknown.
             */
            submittedAt?: string;
            /**
             * Exact submitted arguments as JSON or text. Remove credentials, cookies and unrelated private content first. Do not reconstruct unknown arguments.
             */
            arguments: string;
            /**
             * Observed response or error text, including error codes and retry outcome. Remove secrets.
             */
            result: string;
            /**
             * Returned request ID, when available.
             */
            requestId?: string;
            /**
             * Returned job or run ID, when available.
             */
            jobId?: string;
          },
          {
            /**
             * Exact tool name or REST method and path.
             */
            tool: string;
            /**
             * Observed call time with timezone; omit if unknown.
             */
            submittedAt?: string;
            /**
             * Exact submitted arguments as JSON or text. Remove credentials, cookies and unrelated private content first. Do not reconstruct unknown arguments.
             */
            arguments: string;
            /**
             * Observed response or error text, including error codes and retry outcome. Remove secrets.
             */
            result: string;
            /**
             * Returned request ID, when available.
             */
            requestId?: string;
            /**
             * Returned job or run ID, when available.
             */
            jobId?: string;
          }
        ]
      | [
          {
            /**
             * Exact tool name or REST method and path.
             */
            tool: string;
            /**
             * Observed call time with timezone; omit if unknown.
             */
            submittedAt?: string;
            /**
             * Exact submitted arguments as JSON or text. Remove credentials, cookies and unrelated private content first. Do not reconstruct unknown arguments.
             */
            arguments: string;
            /**
             * Observed response or error text, including error codes and retry outcome. Remove secrets.
             */
            result: string;
            /**
             * Returned request ID, when available.
             */
            requestId?: string;
            /**
             * Returned job or run ID, when available.
             */
            jobId?: string;
          },
          {
            /**
             * Exact tool name or REST method and path.
             */
            tool: string;
            /**
             * Observed call time with timezone; omit if unknown.
             */
            submittedAt?: string;
            /**
             * Exact submitted arguments as JSON or text. Remove credentials, cookies and unrelated private content first. Do not reconstruct unknown arguments.
             */
            arguments: string;
            /**
             * Observed response or error text, including error codes and retry outcome. Remove secrets.
             */
            result: string;
            /**
             * Returned request ID, when available.
             */
            requestId?: string;
            /**
             * Returned job or run ID, when available.
             */
            jobId?: string;
          },
          {
            /**
             * Exact tool name or REST method and path.
             */
            tool: string;
            /**
             * Observed call time with timezone; omit if unknown.
             */
            submittedAt?: string;
            /**
             * Exact submitted arguments as JSON or text. Remove credentials, cookies and unrelated private content first. Do not reconstruct unknown arguments.
             */
            arguments: string;
            /**
             * Observed response or error text, including error codes and retry outcome. Remove secrets.
             */
            result: string;
            /**
             * Returned request ID, when available.
             */
            requestId?: string;
            /**
             * Returned job or run ID, when available.
             */
            jobId?: string;
          }
        ]
      | [
          {
            /**
             * Exact tool name or REST method and path.
             */
            tool: string;
            /**
             * Observed call time with timezone; omit if unknown.
             */
            submittedAt?: string;
            /**
             * Exact submitted arguments as JSON or text. Remove credentials, cookies and unrelated private content first. Do not reconstruct unknown arguments.
             */
            arguments: string;
            /**
             * Observed response or error text, including error codes and retry outcome. Remove secrets.
             */
            result: string;
            /**
             * Returned request ID, when available.
             */
            requestId?: string;
            /**
             * Returned job or run ID, when available.
             */
            jobId?: string;
          },
          {
            /**
             * Exact tool name or REST method and path.
             */
            tool: string;
            /**
             * Observed call time with timezone; omit if unknown.
             */
            submittedAt?: string;
            /**
             * Exact submitted arguments as JSON or text. Remove credentials, cookies and unrelated private content first. Do not reconstruct unknown arguments.
             */
            arguments: string;
            /**
             * Observed response or error text, including error codes and retry outcome. Remove secrets.
             */
            result: string;
            /**
             * Returned request ID, when available.
             */
            requestId?: string;
            /**
             * Returned job or run ID, when available.
             */
            jobId?: string;
          },
          {
            /**
             * Exact tool name or REST method and path.
             */
            tool: string;
            /**
             * Observed call time with timezone; omit if unknown.
             */
            submittedAt?: string;
            /**
             * Exact submitted arguments as JSON or text. Remove credentials, cookies and unrelated private content first. Do not reconstruct unknown arguments.
             */
            arguments: string;
            /**
             * Observed response or error text, including error codes and retry outcome. Remove secrets.
             */
            result: string;
            /**
             * Returned request ID, when available.
             */
            requestId?: string;
            /**
             * Returned job or run ID, when available.
             */
            jobId?: string;
          },
          {
            /**
             * Exact tool name or REST method and path.
             */
            tool: string;
            /**
             * Observed call time with timezone; omit if unknown.
             */
            submittedAt?: string;
            /**
             * Exact submitted arguments as JSON or text. Remove credentials, cookies and unrelated private content first. Do not reconstruct unknown arguments.
             */
            arguments: string;
            /**
             * Observed response or error text, including error codes and retry outcome. Remove secrets.
             */
            result: string;
            /**
             * Returned request ID, when available.
             */
            requestId?: string;
            /**
             * Returned job or run ID, when available.
             */
            jobId?: string;
          }
        ]
      | [
          {
            /**
             * Exact tool name or REST method and path.
             */
            tool: string;
            /**
             * Observed call time with timezone; omit if unknown.
             */
            submittedAt?: string;
            /**
             * Exact submitted arguments as JSON or text. Remove credentials, cookies and unrelated private content first. Do not reconstruct unknown arguments.
             */
            arguments: string;
            /**
             * Observed response or error text, including error codes and retry outcome. Remove secrets.
             */
            result: string;
            /**
             * Returned request ID, when available.
             */
            requestId?: string;
            /**
             * Returned job or run ID, when available.
             */
            jobId?: string;
          },
          {
            /**
             * Exact tool name or REST method and path.
             */
            tool: string;
            /**
             * Observed call time with timezone; omit if unknown.
             */
            submittedAt?: string;
            /**
             * Exact submitted arguments as JSON or text. Remove credentials, cookies and unrelated private content first. Do not reconstruct unknown arguments.
             */
            arguments: string;
            /**
             * Observed response or error text, including error codes and retry outcome. Remove secrets.
             */
            result: string;
            /**
             * Returned request ID, when available.
             */
            requestId?: string;
            /**
             * Returned job or run ID, when available.
             */
            jobId?: string;
          },
          {
            /**
             * Exact tool name or REST method and path.
             */
            tool: string;
            /**
             * Observed call time with timezone; omit if unknown.
             */
            submittedAt?: string;
            /**
             * Exact submitted arguments as JSON or text. Remove credentials, cookies and unrelated private content first. Do not reconstruct unknown arguments.
             */
            arguments: string;
            /**
             * Observed response or error text, including error codes and retry outcome. Remove secrets.
             */
            result: string;
            /**
             * Returned request ID, when available.
             */
            requestId?: string;
            /**
             * Returned job or run ID, when available.
             */
            jobId?: string;
          },
          {
            /**
             * Exact tool name or REST method and path.
             */
            tool: string;
            /**
             * Observed call time with timezone; omit if unknown.
             */
            submittedAt?: string;
            /**
             * Exact submitted arguments as JSON or text. Remove credentials, cookies and unrelated private content first. Do not reconstruct unknown arguments.
             */
            arguments: string;
            /**
             * Observed response or error text, including error codes and retry outcome. Remove secrets.
             */
            result: string;
            /**
             * Returned request ID, when available.
             */
            requestId?: string;
            /**
             * Returned job or run ID, when available.
             */
            jobId?: string;
          },
          {
            /**
             * Exact tool name or REST method and path.
             */
            tool: string;
            /**
             * Observed call time with timezone; omit if unknown.
             */
            submittedAt?: string;
            /**
             * Exact submitted arguments as JSON or text. Remove credentials, cookies and unrelated private content first. Do not reconstruct unknown arguments.
             */
            arguments: string;
            /**
             * Observed response or error text, including error codes and retry outcome. Remove secrets.
             */
            result: string;
            /**
             * Returned request ID, when available.
             */
            requestId?: string;
            /**
             * Returned job or run ID, when available.
             */
            jobId?: string;
          }
        ]
      | [
          {
            /**
             * Exact tool name or REST method and path.
             */
            tool: string;
            /**
             * Observed call time with timezone; omit if unknown.
             */
            submittedAt?: string;
            /**
             * Exact submitted arguments as JSON or text. Remove credentials, cookies and unrelated private content first. Do not reconstruct unknown arguments.
             */
            arguments: string;
            /**
             * Observed response or error text, including error codes and retry outcome. Remove secrets.
             */
            result: string;
            /**
             * Returned request ID, when available.
             */
            requestId?: string;
            /**
             * Returned job or run ID, when available.
             */
            jobId?: string;
          },
          {
            /**
             * Exact tool name or REST method and path.
             */
            tool: string;
            /**
             * Observed call time with timezone; omit if unknown.
             */
            submittedAt?: string;
            /**
             * Exact submitted arguments as JSON or text. Remove credentials, cookies and unrelated private content first. Do not reconstruct unknown arguments.
             */
            arguments: string;
            /**
             * Observed response or error text, including error codes and retry outcome. Remove secrets.
             */
            result: string;
            /**
             * Returned request ID, when available.
             */
            requestId?: string;
            /**
             * Returned job or run ID, when available.
             */
            jobId?: string;
          },
          {
            /**
             * Exact tool name or REST method and path.
             */
            tool: string;
            /**
             * Observed call time with timezone; omit if unknown.
             */
            submittedAt?: string;
            /**
             * Exact submitted arguments as JSON or text. Remove credentials, cookies and unrelated private content first. Do not reconstruct unknown arguments.
             */
            arguments: string;
            /**
             * Observed response or error text, including error codes and retry outcome. Remove secrets.
             */
            result: string;
            /**
             * Returned request ID, when available.
             */
            requestId?: string;
            /**
             * Returned job or run ID, when available.
             */
            jobId?: string;
          },
          {
            /**
             * Exact tool name or REST method and path.
             */
            tool: string;
            /**
             * Observed call time with timezone; omit if unknown.
             */
            submittedAt?: string;
            /**
             * Exact submitted arguments as JSON or text. Remove credentials, cookies and unrelated private content first. Do not reconstruct unknown arguments.
             */
            arguments: string;
            /**
             * Observed response or error text, including error codes and retry outcome. Remove secrets.
             */
            result: string;
            /**
             * Returned request ID, when available.
             */
            requestId?: string;
            /**
             * Returned job or run ID, when available.
             */
            jobId?: string;
          },
          {
            /**
             * Exact tool name or REST method and path.
             */
            tool: string;
            /**
             * Observed call time with timezone; omit if unknown.
             */
            submittedAt?: string;
            /**
             * Exact submitted arguments as JSON or text. Remove credentials, cookies and unrelated private content first. Do not reconstruct unknown arguments.
             */
            arguments: string;
            /**
             * Observed response or error text, including error codes and retry outcome. Remove secrets.
             */
            result: string;
            /**
             * Returned request ID, when available.
             */
            requestId?: string;
            /**
             * Returned job or run ID, when available.
             */
            jobId?: string;
          },
          {
            /**
             * Exact tool name or REST method and path.
             */
            tool: string;
            /**
             * Observed call time with timezone; omit if unknown.
             */
            submittedAt?: string;
            /**
             * Exact submitted arguments as JSON or text. Remove credentials, cookies and unrelated private content first. Do not reconstruct unknown arguments.
             */
            arguments: string;
            /**
             * Observed response or error text, including error codes and retry outcome. Remove secrets.
             */
            result: string;
            /**
             * Returned request ID, when available.
             */
            requestId?: string;
            /**
             * Returned job or run ID, when available.
             */
            jobId?: string;
          }
        ]
      | [
          {
            /**
             * Exact tool name or REST method and path.
             */
            tool: string;
            /**
             * Observed call time with timezone; omit if unknown.
             */
            submittedAt?: string;
            /**
             * Exact submitted arguments as JSON or text. Remove credentials, cookies and unrelated private content first. Do not reconstruct unknown arguments.
             */
            arguments: string;
            /**
             * Observed response or error text, including error codes and retry outcome. Remove secrets.
             */
            result: string;
            /**
             * Returned request ID, when available.
             */
            requestId?: string;
            /**
             * Returned job or run ID, when available.
             */
            jobId?: string;
          },
          {
            /**
             * Exact tool name or REST method and path.
             */
            tool: string;
            /**
             * Observed call time with timezone; omit if unknown.
             */
            submittedAt?: string;
            /**
             * Exact submitted arguments as JSON or text. Remove credentials, cookies and unrelated private content first. Do not reconstruct unknown arguments.
             */
            arguments: string;
            /**
             * Observed response or error text, including error codes and retry outcome. Remove secrets.
             */
            result: string;
            /**
             * Returned request ID, when available.
             */
            requestId?: string;
            /**
             * Returned job or run ID, when available.
             */
            jobId?: string;
          },
          {
            /**
             * Exact tool name or REST method and path.
             */
            tool: string;
            /**
             * Observed call time with timezone; omit if unknown.
             */
            submittedAt?: string;
            /**
             * Exact submitted arguments as JSON or text. Remove credentials, cookies and unrelated private content first. Do not reconstruct unknown arguments.
             */
            arguments: string;
            /**
             * Observed response or error text, including error codes and retry outcome. Remove secrets.
             */
            result: string;
            /**
             * Returned request ID, when available.
             */
            requestId?: string;
            /**
             * Returned job or run ID, when available.
             */
            jobId?: string;
          },
          {
            /**
             * Exact tool name or REST method and path.
             */
            tool: string;
            /**
             * Observed call time with timezone; omit if unknown.
             */
            submittedAt?: string;
            /**
             * Exact submitted arguments as JSON or text. Remove credentials, cookies and unrelated private content first. Do not reconstruct unknown arguments.
             */
            arguments: string;
            /**
             * Observed response or error text, including error codes and retry outcome. Remove secrets.
             */
            result: string;
            /**
             * Returned request ID, when available.
             */
            requestId?: string;
            /**
             * Returned job or run ID, when available.
             */
            jobId?: string;
          },
          {
            /**
             * Exact tool name or REST method and path.
             */
            tool: string;
            /**
             * Observed call time with timezone; omit if unknown.
             */
            submittedAt?: string;
            /**
             * Exact submitted arguments as JSON or text. Remove credentials, cookies and unrelated private content first. Do not reconstruct unknown arguments.
             */
            arguments: string;
            /**
             * Observed response or error text, including error codes and retry outcome. Remove secrets.
             */
            result: string;
            /**
             * Returned request ID, when available.
             */
            requestId?: string;
            /**
             * Returned job or run ID, when available.
             */
            jobId?: string;
          },
          {
            /**
             * Exact tool name or REST method and path.
             */
            tool: string;
            /**
             * Observed call time with timezone; omit if unknown.
             */
            submittedAt?: string;
            /**
             * Exact submitted arguments as JSON or text. Remove credentials, cookies and unrelated private content first. Do not reconstruct unknown arguments.
             */
            arguments: string;
            /**
             * Observed response or error text, including error codes and retry outcome. Remove secrets.
             */
            result: string;
            /**
             * Returned request ID, when available.
             */
            requestId?: string;
            /**
             * Returned job or run ID, when available.
             */
            jobId?: string;
          },
          {
            /**
             * Exact tool name or REST method and path.
             */
            tool: string;
            /**
             * Observed call time with timezone; omit if unknown.
             */
            submittedAt?: string;
            /**
             * Exact submitted arguments as JSON or text. Remove credentials, cookies and unrelated private content first. Do not reconstruct unknown arguments.
             */
            arguments: string;
            /**
             * Observed response or error text, including error codes and retry outcome. Remove secrets.
             */
            result: string;
            /**
             * Returned request ID, when available.
             */
            requestId?: string;
            /**
             * Returned job or run ID, when available.
             */
            jobId?: string;
          }
        ]
      | [
          {
            /**
             * Exact tool name or REST method and path.
             */
            tool: string;
            /**
             * Observed call time with timezone; omit if unknown.
             */
            submittedAt?: string;
            /**
             * Exact submitted arguments as JSON or text. Remove credentials, cookies and unrelated private content first. Do not reconstruct unknown arguments.
             */
            arguments: string;
            /**
             * Observed response or error text, including error codes and retry outcome. Remove secrets.
             */
            result: string;
            /**
             * Returned request ID, when available.
             */
            requestId?: string;
            /**
             * Returned job or run ID, when available.
             */
            jobId?: string;
          },
          {
            /**
             * Exact tool name or REST method and path.
             */
            tool: string;
            /**
             * Observed call time with timezone; omit if unknown.
             */
            submittedAt?: string;
            /**
             * Exact submitted arguments as JSON or text. Remove credentials, cookies and unrelated private content first. Do not reconstruct unknown arguments.
             */
            arguments: string;
            /**
             * Observed response or error text, including error codes and retry outcome. Remove secrets.
             */
            result: string;
            /**
             * Returned request ID, when available.
             */
            requestId?: string;
            /**
             * Returned job or run ID, when available.
             */
            jobId?: string;
          },
          {
            /**
             * Exact tool name or REST method and path.
             */
            tool: string;
            /**
             * Observed call time with timezone; omit if unknown.
             */
            submittedAt?: string;
            /**
             * Exact submitted arguments as JSON or text. Remove credentials, cookies and unrelated private content first. Do not reconstruct unknown arguments.
             */
            arguments: string;
            /**
             * Observed response or error text, including error codes and retry outcome. Remove secrets.
             */
            result: string;
            /**
             * Returned request ID, when available.
             */
            requestId?: string;
            /**
             * Returned job or run ID, when available.
             */
            jobId?: string;
          },
          {
            /**
             * Exact tool name or REST method and path.
             */
            tool: string;
            /**
             * Observed call time with timezone; omit if unknown.
             */
            submittedAt?: string;
            /**
             * Exact submitted arguments as JSON or text. Remove credentials, cookies and unrelated private content first. Do not reconstruct unknown arguments.
             */
            arguments: string;
            /**
             * Observed response or error text, including error codes and retry outcome. Remove secrets.
             */
            result: string;
            /**
             * Returned request ID, when available.
             */
            requestId?: string;
            /**
             * Returned job or run ID, when available.
             */
            jobId?: string;
          },
          {
            /**
             * Exact tool name or REST method and path.
             */
            tool: string;
            /**
             * Observed call time with timezone; omit if unknown.
             */
            submittedAt?: string;
            /**
             * Exact submitted arguments as JSON or text. Remove credentials, cookies and unrelated private content first. Do not reconstruct unknown arguments.
             */
            arguments: string;
            /**
             * Observed response or error text, including error codes and retry outcome. Remove secrets.
             */
            result: string;
            /**
             * Returned request ID, when available.
             */
            requestId?: string;
            /**
             * Returned job or run ID, when available.
             */
            jobId?: string;
          },
          {
            /**
             * Exact tool name or REST method and path.
             */
            tool: string;
            /**
             * Observed call time with timezone; omit if unknown.
             */
            submittedAt?: string;
            /**
             * Exact submitted arguments as JSON or text. Remove credentials, cookies and unrelated private content first. Do not reconstruct unknown arguments.
             */
            arguments: string;
            /**
             * Observed response or error text, including error codes and retry outcome. Remove secrets.
             */
            result: string;
            /**
             * Returned request ID, when available.
             */
            requestId?: string;
            /**
             * Returned job or run ID, when available.
             */
            jobId?: string;
          },
          {
            /**
             * Exact tool name or REST method and path.
             */
            tool: string;
            /**
             * Observed call time with timezone; omit if unknown.
             */
            submittedAt?: string;
            /**
             * Exact submitted arguments as JSON or text. Remove credentials, cookies and unrelated private content first. Do not reconstruct unknown arguments.
             */
            arguments: string;
            /**
             * Observed response or error text, including error codes and retry outcome. Remove secrets.
             */
            result: string;
            /**
             * Returned request ID, when available.
             */
            requestId?: string;
            /**
             * Returned job or run ID, when available.
             */
            jobId?: string;
          },
          {
            /**
             * Exact tool name or REST method and path.
             */
            tool: string;
            /**
             * Observed call time with timezone; omit if unknown.
             */
            submittedAt?: string;
            /**
             * Exact submitted arguments as JSON or text. Remove credentials, cookies and unrelated private content first. Do not reconstruct unknown arguments.
             */
            arguments: string;
            /**
             * Observed response or error text, including error codes and retry outcome. Remove secrets.
             */
            result: string;
            /**
             * Returned request ID, when available.
             */
            requestId?: string;
            /**
             * Returned job or run ID, when available.
             */
            jobId?: string;
          }
        ]
      | [
          {
            /**
             * Exact tool name or REST method and path.
             */
            tool: string;
            /**
             * Observed call time with timezone; omit if unknown.
             */
            submittedAt?: string;
            /**
             * Exact submitted arguments as JSON or text. Remove credentials, cookies and unrelated private content first. Do not reconstruct unknown arguments.
             */
            arguments: string;
            /**
             * Observed response or error text, including error codes and retry outcome. Remove secrets.
             */
            result: string;
            /**
             * Returned request ID, when available.
             */
            requestId?: string;
            /**
             * Returned job or run ID, when available.
             */
            jobId?: string;
          },
          {
            /**
             * Exact tool name or REST method and path.
             */
            tool: string;
            /**
             * Observed call time with timezone; omit if unknown.
             */
            submittedAt?: string;
            /**
             * Exact submitted arguments as JSON or text. Remove credentials, cookies and unrelated private content first. Do not reconstruct unknown arguments.
             */
            arguments: string;
            /**
             * Observed response or error text, including error codes and retry outcome. Remove secrets.
             */
            result: string;
            /**
             * Returned request ID, when available.
             */
            requestId?: string;
            /**
             * Returned job or run ID, when available.
             */
            jobId?: string;
          },
          {
            /**
             * Exact tool name or REST method and path.
             */
            tool: string;
            /**
             * Observed call time with timezone; omit if unknown.
             */
            submittedAt?: string;
            /**
             * Exact submitted arguments as JSON or text. Remove credentials, cookies and unrelated private content first. Do not reconstruct unknown arguments.
             */
            arguments: string;
            /**
             * Observed response or error text, including error codes and retry outcome. Remove secrets.
             */
            result: string;
            /**
             * Returned request ID, when available.
             */
            requestId?: string;
            /**
             * Returned job or run ID, when available.
             */
            jobId?: string;
          },
          {
            /**
             * Exact tool name or REST method and path.
             */
            tool: string;
            /**
             * Observed call time with timezone; omit if unknown.
             */
            submittedAt?: string;
            /**
             * Exact submitted arguments as JSON or text. Remove credentials, cookies and unrelated private content first. Do not reconstruct unknown arguments.
             */
            arguments: string;
            /**
             * Observed response or error text, including error codes and retry outcome. Remove secrets.
             */
            result: string;
            /**
             * Returned request ID, when available.
             */
            requestId?: string;
            /**
             * Returned job or run ID, when available.
             */
            jobId?: string;
          },
          {
            /**
             * Exact tool name or REST method and path.
             */
            tool: string;
            /**
             * Observed call time with timezone; omit if unknown.
             */
            submittedAt?: string;
            /**
             * Exact submitted arguments as JSON or text. Remove credentials, cookies and unrelated private content first. Do not reconstruct unknown arguments.
             */
            arguments: string;
            /**
             * Observed response or error text, including error codes and retry outcome. Remove secrets.
             */
            result: string;
            /**
             * Returned request ID, when available.
             */
            requestId?: string;
            /**
             * Returned job or run ID, when available.
             */
            jobId?: string;
          },
          {
            /**
             * Exact tool name or REST method and path.
             */
            tool: string;
            /**
             * Observed call time with timezone; omit if unknown.
             */
            submittedAt?: string;
            /**
             * Exact submitted arguments as JSON or text. Remove credentials, cookies and unrelated private content first. Do not reconstruct unknown arguments.
             */
            arguments: string;
            /**
             * Observed response or error text, including error codes and retry outcome. Remove secrets.
             */
            result: string;
            /**
             * Returned request ID, when available.
             */
            requestId?: string;
            /**
             * Returned job or run ID, when available.
             */
            jobId?: string;
          },
          {
            /**
             * Exact tool name or REST method and path.
             */
            tool: string;
            /**
             * Observed call time with timezone; omit if unknown.
             */
            submittedAt?: string;
            /**
             * Exact submitted arguments as JSON or text. Remove credentials, cookies and unrelated private content first. Do not reconstruct unknown arguments.
             */
            arguments: string;
            /**
             * Observed response or error text, including error codes and retry outcome. Remove secrets.
             */
            result: string;
            /**
             * Returned request ID, when available.
             */
            requestId?: string;
            /**
             * Returned job or run ID, when available.
             */
            jobId?: string;
          },
          {
            /**
             * Exact tool name or REST method and path.
             */
            tool: string;
            /**
             * Observed call time with timezone; omit if unknown.
             */
            submittedAt?: string;
            /**
             * Exact submitted arguments as JSON or text. Remove credentials, cookies and unrelated private content first. Do not reconstruct unknown arguments.
             */
            arguments: string;
            /**
             * Observed response or error text, including error codes and retry outcome. Remove secrets.
             */
            result: string;
            /**
             * Returned request ID, when available.
             */
            requestId?: string;
            /**
             * Returned job or run ID, when available.
             */
            jobId?: string;
          },
          {
            /**
             * Exact tool name or REST method and path.
             */
            tool: string;
            /**
             * Observed call time with timezone; omit if unknown.
             */
            submittedAt?: string;
            /**
             * Exact submitted arguments as JSON or text. Remove credentials, cookies and unrelated private content first. Do not reconstruct unknown arguments.
             */
            arguments: string;
            /**
             * Observed response or error text, including error codes and retry outcome. Remove secrets.
             */
            result: string;
            /**
             * Returned request ID, when available.
             */
            requestId?: string;
            /**
             * Returned job or run ID, when available.
             */
            jobId?: string;
          }
        ]
      | [
          {
            /**
             * Exact tool name or REST method and path.
             */
            tool: string;
            /**
             * Observed call time with timezone; omit if unknown.
             */
            submittedAt?: string;
            /**
             * Exact submitted arguments as JSON or text. Remove credentials, cookies and unrelated private content first. Do not reconstruct unknown arguments.
             */
            arguments: string;
            /**
             * Observed response or error text, including error codes and retry outcome. Remove secrets.
             */
            result: string;
            /**
             * Returned request ID, when available.
             */
            requestId?: string;
            /**
             * Returned job or run ID, when available.
             */
            jobId?: string;
          },
          {
            /**
             * Exact tool name or REST method and path.
             */
            tool: string;
            /**
             * Observed call time with timezone; omit if unknown.
             */
            submittedAt?: string;
            /**
             * Exact submitted arguments as JSON or text. Remove credentials, cookies and unrelated private content first. Do not reconstruct unknown arguments.
             */
            arguments: string;
            /**
             * Observed response or error text, including error codes and retry outcome. Remove secrets.
             */
            result: string;
            /**
             * Returned request ID, when available.
             */
            requestId?: string;
            /**
             * Returned job or run ID, when available.
             */
            jobId?: string;
          },
          {
            /**
             * Exact tool name or REST method and path.
             */
            tool: string;
            /**
             * Observed call time with timezone; omit if unknown.
             */
            submittedAt?: string;
            /**
             * Exact submitted arguments as JSON or text. Remove credentials, cookies and unrelated private content first. Do not reconstruct unknown arguments.
             */
            arguments: string;
            /**
             * Observed response or error text, including error codes and retry outcome. Remove secrets.
             */
            result: string;
            /**
             * Returned request ID, when available.
             */
            requestId?: string;
            /**
             * Returned job or run ID, when available.
             */
            jobId?: string;
          },
          {
            /**
             * Exact tool name or REST method and path.
             */
            tool: string;
            /**
             * Observed call time with timezone; omit if unknown.
             */
            submittedAt?: string;
            /**
             * Exact submitted arguments as JSON or text. Remove credentials, cookies and unrelated private content first. Do not reconstruct unknown arguments.
             */
            arguments: string;
            /**
             * Observed response or error text, including error codes and retry outcome. Remove secrets.
             */
            result: string;
            /**
             * Returned request ID, when available.
             */
            requestId?: string;
            /**
             * Returned job or run ID, when available.
             */
            jobId?: string;
          },
          {
            /**
             * Exact tool name or REST method and path.
             */
            tool: string;
            /**
             * Observed call time with timezone; omit if unknown.
             */
            submittedAt?: string;
            /**
             * Exact submitted arguments as JSON or text. Remove credentials, cookies and unrelated private content first. Do not reconstruct unknown arguments.
             */
            arguments: string;
            /**
             * Observed response or error text, including error codes and retry outcome. Remove secrets.
             */
            result: string;
            /**
             * Returned request ID, when available.
             */
            requestId?: string;
            /**
             * Returned job or run ID, when available.
             */
            jobId?: string;
          },
          {
            /**
             * Exact tool name or REST method and path.
             */
            tool: string;
            /**
             * Observed call time with timezone; omit if unknown.
             */
            submittedAt?: string;
            /**
             * Exact submitted arguments as JSON or text. Remove credentials, cookies and unrelated private content first. Do not reconstruct unknown arguments.
             */
            arguments: string;
            /**
             * Observed response or error text, including error codes and retry outcome. Remove secrets.
             */
            result: string;
            /**
             * Returned request ID, when available.
             */
            requestId?: string;
            /**
             * Returned job or run ID, when available.
             */
            jobId?: string;
          },
          {
            /**
             * Exact tool name or REST method and path.
             */
            tool: string;
            /**
             * Observed call time with timezone; omit if unknown.
             */
            submittedAt?: string;
            /**
             * Exact submitted arguments as JSON or text. Remove credentials, cookies and unrelated private content first. Do not reconstruct unknown arguments.
             */
            arguments: string;
            /**
             * Observed response or error text, including error codes and retry outcome. Remove secrets.
             */
            result: string;
            /**
             * Returned request ID, when available.
             */
            requestId?: string;
            /**
             * Returned job or run ID, when available.
             */
            jobId?: string;
          },
          {
            /**
             * Exact tool name or REST method and path.
             */
            tool: string;
            /**
             * Observed call time with timezone; omit if unknown.
             */
            submittedAt?: string;
            /**
             * Exact submitted arguments as JSON or text. Remove credentials, cookies and unrelated private content first. Do not reconstruct unknown arguments.
             */
            arguments: string;
            /**
             * Observed response or error text, including error codes and retry outcome. Remove secrets.
             */
            result: string;
            /**
             * Returned request ID, when available.
             */
            requestId?: string;
            /**
             * Returned job or run ID, when available.
             */
            jobId?: string;
          },
          {
            /**
             * Exact tool name or REST method and path.
             */
            tool: string;
            /**
             * Observed call time with timezone; omit if unknown.
             */
            submittedAt?: string;
            /**
             * Exact submitted arguments as JSON or text. Remove credentials, cookies and unrelated private content first. Do not reconstruct unknown arguments.
             */
            arguments: string;
            /**
             * Observed response or error text, including error codes and retry outcome. Remove secrets.
             */
            result: string;
            /**
             * Returned request ID, when available.
             */
            requestId?: string;
            /**
             * Returned job or run ID, when available.
             */
            jobId?: string;
          },
          {
            /**
             * Exact tool name or REST method and path.
             */
            tool: string;
            /**
             * Observed call time with timezone; omit if unknown.
             */
            submittedAt?: string;
            /**
             * Exact submitted arguments as JSON or text. Remove credentials, cookies and unrelated private content first. Do not reconstruct unknown arguments.
             */
            arguments: string;
            /**
             * Observed response or error text, including error codes and retry outcome. Remove secrets.
             */
            result: string;
            /**
             * Returned request ID, when available.
             */
            requestId?: string;
            /**
             * Returned job or run ID, when available.
             */
            jobId?: string;
          }
        ]
      | [
          {
            /**
             * Exact tool name or REST method and path.
             */
            tool: string;
            /**
             * Observed call time with timezone; omit if unknown.
             */
            submittedAt?: string;
            /**
             * Exact submitted arguments as JSON or text. Remove credentials, cookies and unrelated private content first. Do not reconstruct unknown arguments.
             */
            arguments: string;
            /**
             * Observed response or error text, including error codes and retry outcome. Remove secrets.
             */
            result: string;
            /**
             * Returned request ID, when available.
             */
            requestId?: string;
            /**
             * Returned job or run ID, when available.
             */
            jobId?: string;
          },
          {
            /**
             * Exact tool name or REST method and path.
             */
            tool: string;
            /**
             * Observed call time with timezone; omit if unknown.
             */
            submittedAt?: string;
            /**
             * Exact submitted arguments as JSON or text. Remove credentials, cookies and unrelated private content first. Do not reconstruct unknown arguments.
             */
            arguments: string;
            /**
             * Observed response or error text, including error codes and retry outcome. Remove secrets.
             */
            result: string;
            /**
             * Returned request ID, when available.
             */
            requestId?: string;
            /**
             * Returned job or run ID, when available.
             */
            jobId?: string;
          },
          {
            /**
             * Exact tool name or REST method and path.
             */
            tool: string;
            /**
             * Observed call time with timezone; omit if unknown.
             */
            submittedAt?: string;
            /**
             * Exact submitted arguments as JSON or text. Remove credentials, cookies and unrelated private content first. Do not reconstruct unknown arguments.
             */
            arguments: string;
            /**
             * Observed response or error text, including error codes and retry outcome. Remove secrets.
             */
            result: string;
            /**
             * Returned request ID, when available.
             */
            requestId?: string;
            /**
             * Returned job or run ID, when available.
             */
            jobId?: string;
          },
          {
            /**
             * Exact tool name or REST method and path.
             */
            tool: string;
            /**
             * Observed call time with timezone; omit if unknown.
             */
            submittedAt?: string;
            /**
             * Exact submitted arguments as JSON or text. Remove credentials, cookies and unrelated private content first. Do not reconstruct unknown arguments.
             */
            arguments: string;
            /**
             * Observed response or error text, including error codes and retry outcome. Remove secrets.
             */
            result: string;
            /**
             * Returned request ID, when available.
             */
            requestId?: string;
            /**
             * Returned job or run ID, when available.
             */
            jobId?: string;
          },
          {
            /**
             * Exact tool name or REST method and path.
             */
            tool: string;
            /**
             * Observed call time with timezone; omit if unknown.
             */
            submittedAt?: string;
            /**
             * Exact submitted arguments as JSON or text. Remove credentials, cookies and unrelated private content first. Do not reconstruct unknown arguments.
             */
            arguments: string;
            /**
             * Observed response or error text, including error codes and retry outcome. Remove secrets.
             */
            result: string;
            /**
             * Returned request ID, when available.
             */
            requestId?: string;
            /**
             * Returned job or run ID, when available.
             */
            jobId?: string;
          },
          {
            /**
             * Exact tool name or REST method and path.
             */
            tool: string;
            /**
             * Observed call time with timezone; omit if unknown.
             */
            submittedAt?: string;
            /**
             * Exact submitted arguments as JSON or text. Remove credentials, cookies and unrelated private content first. Do not reconstruct unknown arguments.
             */
            arguments: string;
            /**
             * Observed response or error text, including error codes and retry outcome. Remove secrets.
             */
            result: string;
            /**
             * Returned request ID, when available.
             */
            requestId?: string;
            /**
             * Returned job or run ID, when available.
             */
            jobId?: string;
          },
          {
            /**
             * Exact tool name or REST method and path.
             */
            tool: string;
            /**
             * Observed call time with timezone; omit if unknown.
             */
            submittedAt?: string;
            /**
             * Exact submitted arguments as JSON or text. Remove credentials, cookies and unrelated private content first. Do not reconstruct unknown arguments.
             */
            arguments: string;
            /**
             * Observed response or error text, including error codes and retry outcome. Remove secrets.
             */
            result: string;
            /**
             * Returned request ID, when available.
             */
            requestId?: string;
            /**
             * Returned job or run ID, when available.
             */
            jobId?: string;
          },
          {
            /**
             * Exact tool name or REST method and path.
             */
            tool: string;
            /**
             * Observed call time with timezone; omit if unknown.
             */
            submittedAt?: string;
            /**
             * Exact submitted arguments as JSON or text. Remove credentials, cookies and unrelated private content first. Do not reconstruct unknown arguments.
             */
            arguments: string;
            /**
             * Observed response or error text, including error codes and retry outcome. Remove secrets.
             */
            result: string;
            /**
             * Returned request ID, when available.
             */
            requestId?: string;
            /**
             * Returned job or run ID, when available.
             */
            jobId?: string;
          },
          {
            /**
             * Exact tool name or REST method and path.
             */
            tool: string;
            /**
             * Observed call time with timezone; omit if unknown.
             */
            submittedAt?: string;
            /**
             * Exact submitted arguments as JSON or text. Remove credentials, cookies and unrelated private content first. Do not reconstruct unknown arguments.
             */
            arguments: string;
            /**
             * Observed response or error text, including error codes and retry outcome. Remove secrets.
             */
            result: string;
            /**
             * Returned request ID, when available.
             */
            requestId?: string;
            /**
             * Returned job or run ID, when available.
             */
            jobId?: string;
          },
          {
            /**
             * Exact tool name or REST method and path.
             */
            tool: string;
            /**
             * Observed call time with timezone; omit if unknown.
             */
            submittedAt?: string;
            /**
             * Exact submitted arguments as JSON or text. Remove credentials, cookies and unrelated private content first. Do not reconstruct unknown arguments.
             */
            arguments: string;
            /**
             * Observed response or error text, including error codes and retry outcome. Remove secrets.
             */
            result: string;
            /**
             * Returned request ID, when available.
             */
            requestId?: string;
            /**
             * Returned job or run ID, when available.
             */
            jobId?: string;
          },
          {
            /**
             * Exact tool name or REST method and path.
             */
            tool: string;
            /**
             * Observed call time with timezone; omit if unknown.
             */
            submittedAt?: string;
            /**
             * Exact submitted arguments as JSON or text. Remove credentials, cookies and unrelated private content first. Do not reconstruct unknown arguments.
             */
            arguments: string;
            /**
             * Observed response or error text, including error codes and retry outcome. Remove secrets.
             */
            result: string;
            /**
             * Returned request ID, when available.
             */
            requestId?: string;
            /**
             * Returned job or run ID, when available.
             */
            jobId?: string;
          }
        ]
      | [
          {
            /**
             * Exact tool name or REST method and path.
             */
            tool: string;
            /**
             * Observed call time with timezone; omit if unknown.
             */
            submittedAt?: string;
            /**
             * Exact submitted arguments as JSON or text. Remove credentials, cookies and unrelated private content first. Do not reconstruct unknown arguments.
             */
            arguments: string;
            /**
             * Observed response or error text, including error codes and retry outcome. Remove secrets.
             */
            result: string;
            /**
             * Returned request ID, when available.
             */
            requestId?: string;
            /**
             * Returned job or run ID, when available.
             */
            jobId?: string;
          },
          {
            /**
             * Exact tool name or REST method and path.
             */
            tool: string;
            /**
             * Observed call time with timezone; omit if unknown.
             */
            submittedAt?: string;
            /**
             * Exact submitted arguments as JSON or text. Remove credentials, cookies and unrelated private content first. Do not reconstruct unknown arguments.
             */
            arguments: string;
            /**
             * Observed response or error text, including error codes and retry outcome. Remove secrets.
             */
            result: string;
            /**
             * Returned request ID, when available.
             */
            requestId?: string;
            /**
             * Returned job or run ID, when available.
             */
            jobId?: string;
          },
          {
            /**
             * Exact tool name or REST method and path.
             */
            tool: string;
            /**
             * Observed call time with timezone; omit if unknown.
             */
            submittedAt?: string;
            /**
             * Exact submitted arguments as JSON or text. Remove credentials, cookies and unrelated private content first. Do not reconstruct unknown arguments.
             */
            arguments: string;
            /**
             * Observed response or error text, including error codes and retry outcome. Remove secrets.
             */
            result: string;
            /**
             * Returned request ID, when available.
             */
            requestId?: string;
            /**
             * Returned job or run ID, when available.
             */
            jobId?: string;
          },
          {
            /**
             * Exact tool name or REST method and path.
             */
            tool: string;
            /**
             * Observed call time with timezone; omit if unknown.
             */
            submittedAt?: string;
            /**
             * Exact submitted arguments as JSON or text. Remove credentials, cookies and unrelated private content first. Do not reconstruct unknown arguments.
             */
            arguments: string;
            /**
             * Observed response or error text, including error codes and retry outcome. Remove secrets.
             */
            result: string;
            /**
             * Returned request ID, when available.
             */
            requestId?: string;
            /**
             * Returned job or run ID, when available.
             */
            jobId?: string;
          },
          {
            /**
             * Exact tool name or REST method and path.
             */
            tool: string;
            /**
             * Observed call time with timezone; omit if unknown.
             */
            submittedAt?: string;
            /**
             * Exact submitted arguments as JSON or text. Remove credentials, cookies and unrelated private content first. Do not reconstruct unknown arguments.
             */
            arguments: string;
            /**
             * Observed response or error text, including error codes and retry outcome. Remove secrets.
             */
            result: string;
            /**
             * Returned request ID, when available.
             */
            requestId?: string;
            /**
             * Returned job or run ID, when available.
             */
            jobId?: string;
          },
          {
            /**
             * Exact tool name or REST method and path.
             */
            tool: string;
            /**
             * Observed call time with timezone; omit if unknown.
             */
            submittedAt?: string;
            /**
             * Exact submitted arguments as JSON or text. Remove credentials, cookies and unrelated private content first. Do not reconstruct unknown arguments.
             */
            arguments: string;
            /**
             * Observed response or error text, including error codes and retry outcome. Remove secrets.
             */
            result: string;
            /**
             * Returned request ID, when available.
             */
            requestId?: string;
            /**
             * Returned job or run ID, when available.
             */
            jobId?: string;
          },
          {
            /**
             * Exact tool name or REST method and path.
             */
            tool: string;
            /**
             * Observed call time with timezone; omit if unknown.
             */
            submittedAt?: string;
            /**
             * Exact submitted arguments as JSON or text. Remove credentials, cookies and unrelated private content first. Do not reconstruct unknown arguments.
             */
            arguments: string;
            /**
             * Observed response or error text, including error codes and retry outcome. Remove secrets.
             */
            result: string;
            /**
             * Returned request ID, when available.
             */
            requestId?: string;
            /**
             * Returned job or run ID, when available.
             */
            jobId?: string;
          },
          {
            /**
             * Exact tool name or REST method and path.
             */
            tool: string;
            /**
             * Observed call time with timezone; omit if unknown.
             */
            submittedAt?: string;
            /**
             * Exact submitted arguments as JSON or text. Remove credentials, cookies and unrelated private content first. Do not reconstruct unknown arguments.
             */
            arguments: string;
            /**
             * Observed response or error text, including error codes and retry outcome. Remove secrets.
             */
            result: string;
            /**
             * Returned request ID, when available.
             */
            requestId?: string;
            /**
             * Returned job or run ID, when available.
             */
            jobId?: string;
          },
          {
            /**
             * Exact tool name or REST method and path.
             */
            tool: string;
            /**
             * Observed call time with timezone; omit if unknown.
             */
            submittedAt?: string;
            /**
             * Exact submitted arguments as JSON or text. Remove credentials, cookies and unrelated private content first. Do not reconstruct unknown arguments.
             */
            arguments: string;
            /**
             * Observed response or error text, including error codes and retry outcome. Remove secrets.
             */
            result: string;
            /**
             * Returned request ID, when available.
             */
            requestId?: string;
            /**
             * Returned job or run ID, when available.
             */
            jobId?: string;
          },
          {
            /**
             * Exact tool name or REST method and path.
             */
            tool: string;
            /**
             * Observed call time with timezone; omit if unknown.
             */
            submittedAt?: string;
            /**
             * Exact submitted arguments as JSON or text. Remove credentials, cookies and unrelated private content first. Do not reconstruct unknown arguments.
             */
            arguments: string;
            /**
             * Observed response or error text, including error codes and retry outcome. Remove secrets.
             */
            result: string;
            /**
             * Returned request ID, when available.
             */
            requestId?: string;
            /**
             * Returned job or run ID, when available.
             */
            jobId?: string;
          },
          {
            /**
             * Exact tool name or REST method and path.
             */
            tool: string;
            /**
             * Observed call time with timezone; omit if unknown.
             */
            submittedAt?: string;
            /**
             * Exact submitted arguments as JSON or text. Remove credentials, cookies and unrelated private content first. Do not reconstruct unknown arguments.
             */
            arguments: string;
            /**
             * Observed response or error text, including error codes and retry outcome. Remove secrets.
             */
            result: string;
            /**
             * Returned request ID, when available.
             */
            requestId?: string;
            /**
             * Returned job or run ID, when available.
             */
            jobId?: string;
          },
          {
            /**
             * Exact tool name or REST method and path.
             */
            tool: string;
            /**
             * Observed call time with timezone; omit if unknown.
             */
            submittedAt?: string;
            /**
             * Exact submitted arguments as JSON or text. Remove credentials, cookies and unrelated private content first. Do not reconstruct unknown arguments.
             */
            arguments: string;
            /**
             * Observed response or error text, including error codes and retry outcome. Remove secrets.
             */
            result: string;
            /**
             * Returned request ID, when available.
             */
            requestId?: string;
            /**
             * Returned job or run ID, when available.
             */
            jobId?: string;
          }
        ]
      | [
          {
            /**
             * Exact tool name or REST method and path.
             */
            tool: string;
            /**
             * Observed call time with timezone; omit if unknown.
             */
            submittedAt?: string;
            /**
             * Exact submitted arguments as JSON or text. Remove credentials, cookies and unrelated private content first. Do not reconstruct unknown arguments.
             */
            arguments: string;
            /**
             * Observed response or error text, including error codes and retry outcome. Remove secrets.
             */
            result: string;
            /**
             * Returned request ID, when available.
             */
            requestId?: string;
            /**
             * Returned job or run ID, when available.
             */
            jobId?: string;
          },
          {
            /**
             * Exact tool name or REST method and path.
             */
            tool: string;
            /**
             * Observed call time with timezone; omit if unknown.
             */
            submittedAt?: string;
            /**
             * Exact submitted arguments as JSON or text. Remove credentials, cookies and unrelated private content first. Do not reconstruct unknown arguments.
             */
            arguments: string;
            /**
             * Observed response or error text, including error codes and retry outcome. Remove secrets.
             */
            result: string;
            /**
             * Returned request ID, when available.
             */
            requestId?: string;
            /**
             * Returned job or run ID, when available.
             */
            jobId?: string;
          },
          {
            /**
             * Exact tool name or REST method and path.
             */
            tool: string;
            /**
             * Observed call time with timezone; omit if unknown.
             */
            submittedAt?: string;
            /**
             * Exact submitted arguments as JSON or text. Remove credentials, cookies and unrelated private content first. Do not reconstruct unknown arguments.
             */
            arguments: string;
            /**
             * Observed response or error text, including error codes and retry outcome. Remove secrets.
             */
            result: string;
            /**
             * Returned request ID, when available.
             */
            requestId?: string;
            /**
             * Returned job or run ID, when available.
             */
            jobId?: string;
          },
          {
            /**
             * Exact tool name or REST method and path.
             */
            tool: string;
            /**
             * Observed call time with timezone; omit if unknown.
             */
            submittedAt?: string;
            /**
             * Exact submitted arguments as JSON or text. Remove credentials, cookies and unrelated private content first. Do not reconstruct unknown arguments.
             */
            arguments: string;
            /**
             * Observed response or error text, including error codes and retry outcome. Remove secrets.
             */
            result: string;
            /**
             * Returned request ID, when available.
             */
            requestId?: string;
            /**
             * Returned job or run ID, when available.
             */
            jobId?: string;
          },
          {
            /**
             * Exact tool name or REST method and path.
             */
            tool: string;
            /**
             * Observed call time with timezone; omit if unknown.
             */
            submittedAt?: string;
            /**
             * Exact submitted arguments as JSON or text. Remove credentials, cookies and unrelated private content first. Do not reconstruct unknown arguments.
             */
            arguments: string;
            /**
             * Observed response or error text, including error codes and retry outcome. Remove secrets.
             */
            result: string;
            /**
             * Returned request ID, when available.
             */
            requestId?: string;
            /**
             * Returned job or run ID, when available.
             */
            jobId?: string;
          },
          {
            /**
             * Exact tool name or REST method and path.
             */
            tool: string;
            /**
             * Observed call time with timezone; omit if unknown.
             */
            submittedAt?: string;
            /**
             * Exact submitted arguments as JSON or text. Remove credentials, cookies and unrelated private content first. Do not reconstruct unknown arguments.
             */
            arguments: string;
            /**
             * Observed response or error text, including error codes and retry outcome. Remove secrets.
             */
            result: string;
            /**
             * Returned request ID, when available.
             */
            requestId?: string;
            /**
             * Returned job or run ID, when available.
             */
            jobId?: string;
          },
          {
            /**
             * Exact tool name or REST method and path.
             */
            tool: string;
            /**
             * Observed call time with timezone; omit if unknown.
             */
            submittedAt?: string;
            /**
             * Exact submitted arguments as JSON or text. Remove credentials, cookies and unrelated private content first. Do not reconstruct unknown arguments.
             */
            arguments: string;
            /**
             * Observed response or error text, including error codes and retry outcome. Remove secrets.
             */
            result: string;
            /**
             * Returned request ID, when available.
             */
            requestId?: string;
            /**
             * Returned job or run ID, when available.
             */
            jobId?: string;
          },
          {
            /**
             * Exact tool name or REST method and path.
             */
            tool: string;
            /**
             * Observed call time with timezone; omit if unknown.
             */
            submittedAt?: string;
            /**
             * Exact submitted arguments as JSON or text. Remove credentials, cookies and unrelated private content first. Do not reconstruct unknown arguments.
             */
            arguments: string;
            /**
             * Observed response or error text, including error codes and retry outcome. Remove secrets.
             */
            result: string;
            /**
             * Returned request ID, when available.
             */
            requestId?: string;
            /**
             * Returned job or run ID, when available.
             */
            jobId?: string;
          },
          {
            /**
             * Exact tool name or REST method and path.
             */
            tool: string;
            /**
             * Observed call time with timezone; omit if unknown.
             */
            submittedAt?: string;
            /**
             * Exact submitted arguments as JSON or text. Remove credentials, cookies and unrelated private content first. Do not reconstruct unknown arguments.
             */
            arguments: string;
            /**
             * Observed response or error text, including error codes and retry outcome. Remove secrets.
             */
            result: string;
            /**
             * Returned request ID, when available.
             */
            requestId?: string;
            /**
             * Returned job or run ID, when available.
             */
            jobId?: string;
          },
          {
            /**
             * Exact tool name or REST method and path.
             */
            tool: string;
            /**
             * Observed call time with timezone; omit if unknown.
             */
            submittedAt?: string;
            /**
             * Exact submitted arguments as JSON or text. Remove credentials, cookies and unrelated private content first. Do not reconstruct unknown arguments.
             */
            arguments: string;
            /**
             * Observed response or error text, including error codes and retry outcome. Remove secrets.
             */
            result: string;
            /**
             * Returned request ID, when available.
             */
            requestId?: string;
            /**
             * Returned job or run ID, when available.
             */
            jobId?: string;
          },
          {
            /**
             * Exact tool name or REST method and path.
             */
            tool: string;
            /**
             * Observed call time with timezone; omit if unknown.
             */
            submittedAt?: string;
            /**
             * Exact submitted arguments as JSON or text. Remove credentials, cookies and unrelated private content first. Do not reconstruct unknown arguments.
             */
            arguments: string;
            /**
             * Observed response or error text, including error codes and retry outcome. Remove secrets.
             */
            result: string;
            /**
             * Returned request ID, when available.
             */
            requestId?: string;
            /**
             * Returned job or run ID, when available.
             */
            jobId?: string;
          },
          {
            /**
             * Exact tool name or REST method and path.
             */
            tool: string;
            /**
             * Observed call time with timezone; omit if unknown.
             */
            submittedAt?: string;
            /**
             * Exact submitted arguments as JSON or text. Remove credentials, cookies and unrelated private content first. Do not reconstruct unknown arguments.
             */
            arguments: string;
            /**
             * Observed response or error text, including error codes and retry outcome. Remove secrets.
             */
            result: string;
            /**
             * Returned request ID, when available.
             */
            requestId?: string;
            /**
             * Returned job or run ID, when available.
             */
            jobId?: string;
          },
          {
            /**
             * Exact tool name or REST method and path.
             */
            tool: string;
            /**
             * Observed call time with timezone; omit if unknown.
             */
            submittedAt?: string;
            /**
             * Exact submitted arguments as JSON or text. Remove credentials, cookies and unrelated private content first. Do not reconstruct unknown arguments.
             */
            arguments: string;
            /**
             * Observed response or error text, including error codes and retry outcome. Remove secrets.
             */
            result: string;
            /**
             * Returned request ID, when available.
             */
            requestId?: string;
            /**
             * Returned job or run ID, when available.
             */
            jobId?: string;
          }
        ]
      | [
          {
            /**
             * Exact tool name or REST method and path.
             */
            tool: string;
            /**
             * Observed call time with timezone; omit if unknown.
             */
            submittedAt?: string;
            /**
             * Exact submitted arguments as JSON or text. Remove credentials, cookies and unrelated private content first. Do not reconstruct unknown arguments.
             */
            arguments: string;
            /**
             * Observed response or error text, including error codes and retry outcome. Remove secrets.
             */
            result: string;
            /**
             * Returned request ID, when available.
             */
            requestId?: string;
            /**
             * Returned job or run ID, when available.
             */
            jobId?: string;
          },
          {
            /**
             * Exact tool name or REST method and path.
             */
            tool: string;
            /**
             * Observed call time with timezone; omit if unknown.
             */
            submittedAt?: string;
            /**
             * Exact submitted arguments as JSON or text. Remove credentials, cookies and unrelated private content first. Do not reconstruct unknown arguments.
             */
            arguments: string;
            /**
             * Observed response or error text, including error codes and retry outcome. Remove secrets.
             */
            result: string;
            /**
             * Returned request ID, when available.
             */
            requestId?: string;
            /**
             * Returned job or run ID, when available.
             */
            jobId?: string;
          },
          {
            /**
             * Exact tool name or REST method and path.
             */
            tool: string;
            /**
             * Observed call time with timezone; omit if unknown.
             */
            submittedAt?: string;
            /**
             * Exact submitted arguments as JSON or text. Remove credentials, cookies and unrelated private content first. Do not reconstruct unknown arguments.
             */
            arguments: string;
            /**
             * Observed response or error text, including error codes and retry outcome. Remove secrets.
             */
            result: string;
            /**
             * Returned request ID, when available.
             */
            requestId?: string;
            /**
             * Returned job or run ID, when available.
             */
            jobId?: string;
          },
          {
            /**
             * Exact tool name or REST method and path.
             */
            tool: string;
            /**
             * Observed call time with timezone; omit if unknown.
             */
            submittedAt?: string;
            /**
             * Exact submitted arguments as JSON or text. Remove credentials, cookies and unrelated private content first. Do not reconstruct unknown arguments.
             */
            arguments: string;
            /**
             * Observed response or error text, including error codes and retry outcome. Remove secrets.
             */
            result: string;
            /**
             * Returned request ID, when available.
             */
            requestId?: string;
            /**
             * Returned job or run ID, when available.
             */
            jobId?: string;
          },
          {
            /**
             * Exact tool name or REST method and path.
             */
            tool: string;
            /**
             * Observed call time with timezone; omit if unknown.
             */
            submittedAt?: string;
            /**
             * Exact submitted arguments as JSON or text. Remove credentials, cookies and unrelated private content first. Do not reconstruct unknown arguments.
             */
            arguments: string;
            /**
             * Observed response or error text, including error codes and retry outcome. Remove secrets.
             */
            result: string;
            /**
             * Returned request ID, when available.
             */
            requestId?: string;
            /**
             * Returned job or run ID, when available.
             */
            jobId?: string;
          },
          {
            /**
             * Exact tool name or REST method and path.
             */
            tool: string;
            /**
             * Observed call time with timezone; omit if unknown.
             */
            submittedAt?: string;
            /**
             * Exact submitted arguments as JSON or text. Remove credentials, cookies and unrelated private content first. Do not reconstruct unknown arguments.
             */
            arguments: string;
            /**
             * Observed response or error text, including error codes and retry outcome. Remove secrets.
             */
            result: string;
            /**
             * Returned request ID, when available.
             */
            requestId?: string;
            /**
             * Returned job or run ID, when available.
             */
            jobId?: string;
          },
          {
            /**
             * Exact tool name or REST method and path.
             */
            tool: string;
            /**
             * Observed call time with timezone; omit if unknown.
             */
            submittedAt?: string;
            /**
             * Exact submitted arguments as JSON or text. Remove credentials, cookies and unrelated private content first. Do not reconstruct unknown arguments.
             */
            arguments: string;
            /**
             * Observed response or error text, including error codes and retry outcome. Remove secrets.
             */
            result: string;
            /**
             * Returned request ID, when available.
             */
            requestId?: string;
            /**
             * Returned job or run ID, when available.
             */
            jobId?: string;
          },
          {
            /**
             * Exact tool name or REST method and path.
             */
            tool: string;
            /**
             * Observed call time with timezone; omit if unknown.
             */
            submittedAt?: string;
            /**
             * Exact submitted arguments as JSON or text. Remove credentials, cookies and unrelated private content first. Do not reconstruct unknown arguments.
             */
            arguments: string;
            /**
             * Observed response or error text, including error codes and retry outcome. Remove secrets.
             */
            result: string;
            /**
             * Returned request ID, when available.
             */
            requestId?: string;
            /**
             * Returned job or run ID, when available.
             */
            jobId?: string;
          },
          {
            /**
             * Exact tool name or REST method and path.
             */
            tool: string;
            /**
             * Observed call time with timezone; omit if unknown.
             */
            submittedAt?: string;
            /**
             * Exact submitted arguments as JSON or text. Remove credentials, cookies and unrelated private content first. Do not reconstruct unknown arguments.
             */
            arguments: string;
            /**
             * Observed response or error text, including error codes and retry outcome. Remove secrets.
             */
            result: string;
            /**
             * Returned request ID, when available.
             */
            requestId?: string;
            /**
             * Returned job or run ID, when available.
             */
            jobId?: string;
          },
          {
            /**
             * Exact tool name or REST method and path.
             */
            tool: string;
            /**
             * Observed call time with timezone; omit if unknown.
             */
            submittedAt?: string;
            /**
             * Exact submitted arguments as JSON or text. Remove credentials, cookies and unrelated private content first. Do not reconstruct unknown arguments.
             */
            arguments: string;
            /**
             * Observed response or error text, including error codes and retry outcome. Remove secrets.
             */
            result: string;
            /**
             * Returned request ID, when available.
             */
            requestId?: string;
            /**
             * Returned job or run ID, when available.
             */
            jobId?: string;
          },
          {
            /**
             * Exact tool name or REST method and path.
             */
            tool: string;
            /**
             * Observed call time with timezone; omit if unknown.
             */
            submittedAt?: string;
            /**
             * Exact submitted arguments as JSON or text. Remove credentials, cookies and unrelated private content first. Do not reconstruct unknown arguments.
             */
            arguments: string;
            /**
             * Observed response or error text, including error codes and retry outcome. Remove secrets.
             */
            result: string;
            /**
             * Returned request ID, when available.
             */
            requestId?: string;
            /**
             * Returned job or run ID, when available.
             */
            jobId?: string;
          },
          {
            /**
             * Exact tool name or REST method and path.
             */
            tool: string;
            /**
             * Observed call time with timezone; omit if unknown.
             */
            submittedAt?: string;
            /**
             * Exact submitted arguments as JSON or text. Remove credentials, cookies and unrelated private content first. Do not reconstruct unknown arguments.
             */
            arguments: string;
            /**
             * Observed response or error text, including error codes and retry outcome. Remove secrets.
             */
            result: string;
            /**
             * Returned request ID, when available.
             */
            requestId?: string;
            /**
             * Returned job or run ID, when available.
             */
            jobId?: string;
          },
          {
            /**
             * Exact tool name or REST method and path.
             */
            tool: string;
            /**
             * Observed call time with timezone; omit if unknown.
             */
            submittedAt?: string;
            /**
             * Exact submitted arguments as JSON or text. Remove credentials, cookies and unrelated private content first. Do not reconstruct unknown arguments.
             */
            arguments: string;
            /**
             * Observed response or error text, including error codes and retry outcome. Remove secrets.
             */
            result: string;
            /**
             * Returned request ID, when available.
             */
            requestId?: string;
            /**
             * Returned job or run ID, when available.
             */
            jobId?: string;
          },
          {
            /**
             * Exact tool name or REST method and path.
             */
            tool: string;
            /**
             * Observed call time with timezone; omit if unknown.
             */
            submittedAt?: string;
            /**
             * Exact submitted arguments as JSON or text. Remove credentials, cookies and unrelated private content first. Do not reconstruct unknown arguments.
             */
            arguments: string;
            /**
             * Observed response or error text, including error codes and retry outcome. Remove secrets.
             */
            result: string;
            /**
             * Returned request ID, when available.
             */
            requestId?: string;
            /**
             * Returned job or run ID, when available.
             */
            jobId?: string;
          }
        ]
      | [
          {
            /**
             * Exact tool name or REST method and path.
             */
            tool: string;
            /**
             * Observed call time with timezone; omit if unknown.
             */
            submittedAt?: string;
            /**
             * Exact submitted arguments as JSON or text. Remove credentials, cookies and unrelated private content first. Do not reconstruct unknown arguments.
             */
            arguments: string;
            /**
             * Observed response or error text, including error codes and retry outcome. Remove secrets.
             */
            result: string;
            /**
             * Returned request ID, when available.
             */
            requestId?: string;
            /**
             * Returned job or run ID, when available.
             */
            jobId?: string;
          },
          {
            /**
             * Exact tool name or REST method and path.
             */
            tool: string;
            /**
             * Observed call time with timezone; omit if unknown.
             */
            submittedAt?: string;
            /**
             * Exact submitted arguments as JSON or text. Remove credentials, cookies and unrelated private content first. Do not reconstruct unknown arguments.
             */
            arguments: string;
            /**
             * Observed response or error text, including error codes and retry outcome. Remove secrets.
             */
            result: string;
            /**
             * Returned request ID, when available.
             */
            requestId?: string;
            /**
             * Returned job or run ID, when available.
             */
            jobId?: string;
          },
          {
            /**
             * Exact tool name or REST method and path.
             */
            tool: string;
            /**
             * Observed call time with timezone; omit if unknown.
             */
            submittedAt?: string;
            /**
             * Exact submitted arguments as JSON or text. Remove credentials, cookies and unrelated private content first. Do not reconstruct unknown arguments.
             */
            arguments: string;
            /**
             * Observed response or error text, including error codes and retry outcome. Remove secrets.
             */
            result: string;
            /**
             * Returned request ID, when available.
             */
            requestId?: string;
            /**
             * Returned job or run ID, when available.
             */
            jobId?: string;
          },
          {
            /**
             * Exact tool name or REST method and path.
             */
            tool: string;
            /**
             * Observed call time with timezone; omit if unknown.
             */
            submittedAt?: string;
            /**
             * Exact submitted arguments as JSON or text. Remove credentials, cookies and unrelated private content first. Do not reconstruct unknown arguments.
             */
            arguments: string;
            /**
             * Observed response or error text, including error codes and retry outcome. Remove secrets.
             */
            result: string;
            /**
             * Returned request ID, when available.
             */
            requestId?: string;
            /**
             * Returned job or run ID, when available.
             */
            jobId?: string;
          },
          {
            /**
             * Exact tool name or REST method and path.
             */
            tool: string;
            /**
             * Observed call time with timezone; omit if unknown.
             */
            submittedAt?: string;
            /**
             * Exact submitted arguments as JSON or text. Remove credentials, cookies and unrelated private content first. Do not reconstruct unknown arguments.
             */
            arguments: string;
            /**
             * Observed response or error text, including error codes and retry outcome. Remove secrets.
             */
            result: string;
            /**
             * Returned request ID, when available.
             */
            requestId?: string;
            /**
             * Returned job or run ID, when available.
             */
            jobId?: string;
          },
          {
            /**
             * Exact tool name or REST method and path.
             */
            tool: string;
            /**
             * Observed call time with timezone; omit if unknown.
             */
            submittedAt?: string;
            /**
             * Exact submitted arguments as JSON or text. Remove credentials, cookies and unrelated private content first. Do not reconstruct unknown arguments.
             */
            arguments: string;
            /**
             * Observed response or error text, including error codes and retry outcome. Remove secrets.
             */
            result: string;
            /**
             * Returned request ID, when available.
             */
            requestId?: string;
            /**
             * Returned job or run ID, when available.
             */
            jobId?: string;
          },
          {
            /**
             * Exact tool name or REST method and path.
             */
            tool: string;
            /**
             * Observed call time with timezone; omit if unknown.
             */
            submittedAt?: string;
            /**
             * Exact submitted arguments as JSON or text. Remove credentials, cookies and unrelated private content first. Do not reconstruct unknown arguments.
             */
            arguments: string;
            /**
             * Observed response or error text, including error codes and retry outcome. Remove secrets.
             */
            result: string;
            /**
             * Returned request ID, when available.
             */
            requestId?: string;
            /**
             * Returned job or run ID, when available.
             */
            jobId?: string;
          },
          {
            /**
             * Exact tool name or REST method and path.
             */
            tool: string;
            /**
             * Observed call time with timezone; omit if unknown.
             */
            submittedAt?: string;
            /**
             * Exact submitted arguments as JSON or text. Remove credentials, cookies and unrelated private content first. Do not reconstruct unknown arguments.
             */
            arguments: string;
            /**
             * Observed response or error text, including error codes and retry outcome. Remove secrets.
             */
            result: string;
            /**
             * Returned request ID, when available.
             */
            requestId?: string;
            /**
             * Returned job or run ID, when available.
             */
            jobId?: string;
          },
          {
            /**
             * Exact tool name or REST method and path.
             */
            tool: string;
            /**
             * Observed call time with timezone; omit if unknown.
             */
            submittedAt?: string;
            /**
             * Exact submitted arguments as JSON or text. Remove credentials, cookies and unrelated private content first. Do not reconstruct unknown arguments.
             */
            arguments: string;
            /**
             * Observed response or error text, including error codes and retry outcome. Remove secrets.
             */
            result: string;
            /**
             * Returned request ID, when available.
             */
            requestId?: string;
            /**
             * Returned job or run ID, when available.
             */
            jobId?: string;
          },
          {
            /**
             * Exact tool name or REST method and path.
             */
            tool: string;
            /**
             * Observed call time with timezone; omit if unknown.
             */
            submittedAt?: string;
            /**
             * Exact submitted arguments as JSON or text. Remove credentials, cookies and unrelated private content first. Do not reconstruct unknown arguments.
             */
            arguments: string;
            /**
             * Observed response or error text, including error codes and retry outcome. Remove secrets.
             */
            result: string;
            /**
             * Returned request ID, when available.
             */
            requestId?: string;
            /**
             * Returned job or run ID, when available.
             */
            jobId?: string;
          },
          {
            /**
             * Exact tool name or REST method and path.
             */
            tool: string;
            /**
             * Observed call time with timezone; omit if unknown.
             */
            submittedAt?: string;
            /**
             * Exact submitted arguments as JSON or text. Remove credentials, cookies and unrelated private content first. Do not reconstruct unknown arguments.
             */
            arguments: string;
            /**
             * Observed response or error text, including error codes and retry outcome. Remove secrets.
             */
            result: string;
            /**
             * Returned request ID, when available.
             */
            requestId?: string;
            /**
             * Returned job or run ID, when available.
             */
            jobId?: string;
          },
          {
            /**
             * Exact tool name or REST method and path.
             */
            tool: string;
            /**
             * Observed call time with timezone; omit if unknown.
             */
            submittedAt?: string;
            /**
             * Exact submitted arguments as JSON or text. Remove credentials, cookies and unrelated private content first. Do not reconstruct unknown arguments.
             */
            arguments: string;
            /**
             * Observed response or error text, including error codes and retry outcome. Remove secrets.
             */
            result: string;
            /**
             * Returned request ID, when available.
             */
            requestId?: string;
            /**
             * Returned job or run ID, when available.
             */
            jobId?: string;
          },
          {
            /**
             * Exact tool name or REST method and path.
             */
            tool: string;
            /**
             * Observed call time with timezone; omit if unknown.
             */
            submittedAt?: string;
            /**
             * Exact submitted arguments as JSON or text. Remove credentials, cookies and unrelated private content first. Do not reconstruct unknown arguments.
             */
            arguments: string;
            /**
             * Observed response or error text, including error codes and retry outcome. Remove secrets.
             */
            result: string;
            /**
             * Returned request ID, when available.
             */
            requestId?: string;
            /**
             * Returned job or run ID, when available.
             */
            jobId?: string;
          },
          {
            /**
             * Exact tool name or REST method and path.
             */
            tool: string;
            /**
             * Observed call time with timezone; omit if unknown.
             */
            submittedAt?: string;
            /**
             * Exact submitted arguments as JSON or text. Remove credentials, cookies and unrelated private content first. Do not reconstruct unknown arguments.
             */
            arguments: string;
            /**
             * Observed response or error text, including error codes and retry outcome. Remove secrets.
             */
            result: string;
            /**
             * Returned request ID, when available.
             */
            requestId?: string;
            /**
             * Returned job or run ID, when available.
             */
            jobId?: string;
          },
          {
            /**
             * Exact tool name or REST method and path.
             */
            tool: string;
            /**
             * Observed call time with timezone; omit if unknown.
             */
            submittedAt?: string;
            /**
             * Exact submitted arguments as JSON or text. Remove credentials, cookies and unrelated private content first. Do not reconstruct unknown arguments.
             */
            arguments: string;
            /**
             * Observed response or error text, including error codes and retry outcome. Remove secrets.
             */
            result: string;
            /**
             * Returned request ID, when available.
             */
            requestId?: string;
            /**
             * Returned job or run ID, when available.
             */
            jobId?: string;
          }
        ]
      | [
          {
            /**
             * Exact tool name or REST method and path.
             */
            tool: string;
            /**
             * Observed call time with timezone; omit if unknown.
             */
            submittedAt?: string;
            /**
             * Exact submitted arguments as JSON or text. Remove credentials, cookies and unrelated private content first. Do not reconstruct unknown arguments.
             */
            arguments: string;
            /**
             * Observed response or error text, including error codes and retry outcome. Remove secrets.
             */
            result: string;
            /**
             * Returned request ID, when available.
             */
            requestId?: string;
            /**
             * Returned job or run ID, when available.
             */
            jobId?: string;
          },
          {
            /**
             * Exact tool name or REST method and path.
             */
            tool: string;
            /**
             * Observed call time with timezone; omit if unknown.
             */
            submittedAt?: string;
            /**
             * Exact submitted arguments as JSON or text. Remove credentials, cookies and unrelated private content first. Do not reconstruct unknown arguments.
             */
            arguments: string;
            /**
             * Observed response or error text, including error codes and retry outcome. Remove secrets.
             */
            result: string;
            /**
             * Returned request ID, when available.
             */
            requestId?: string;
            /**
             * Returned job or run ID, when available.
             */
            jobId?: string;
          },
          {
            /**
             * Exact tool name or REST method and path.
             */
            tool: string;
            /**
             * Observed call time with timezone; omit if unknown.
             */
            submittedAt?: string;
            /**
             * Exact submitted arguments as JSON or text. Remove credentials, cookies and unrelated private content first. Do not reconstruct unknown arguments.
             */
            arguments: string;
            /**
             * Observed response or error text, including error codes and retry outcome. Remove secrets.
             */
            result: string;
            /**
             * Returned request ID, when available.
             */
            requestId?: string;
            /**
             * Returned job or run ID, when available.
             */
            jobId?: string;
          },
          {
            /**
             * Exact tool name or REST method and path.
             */
            tool: string;
            /**
             * Observed call time with timezone; omit if unknown.
             */
            submittedAt?: string;
            /**
             * Exact submitted arguments as JSON or text. Remove credentials, cookies and unrelated private content first. Do not reconstruct unknown arguments.
             */
            arguments: string;
            /**
             * Observed response or error text, including error codes and retry outcome. Remove secrets.
             */
            result: string;
            /**
             * Returned request ID, when available.
             */
            requestId?: string;
            /**
             * Returned job or run ID, when available.
             */
            jobId?: string;
          },
          {
            /**
             * Exact tool name or REST method and path.
             */
            tool: string;
            /**
             * Observed call time with timezone; omit if unknown.
             */
            submittedAt?: string;
            /**
             * Exact submitted arguments as JSON or text. Remove credentials, cookies and unrelated private content first. Do not reconstruct unknown arguments.
             */
            arguments: string;
            /**
             * Observed response or error text, including error codes and retry outcome. Remove secrets.
             */
            result: string;
            /**
             * Returned request ID, when available.
             */
            requestId?: string;
            /**
             * Returned job or run ID, when available.
             */
            jobId?: string;
          },
          {
            /**
             * Exact tool name or REST method and path.
             */
            tool: string;
            /**
             * Observed call time with timezone; omit if unknown.
             */
            submittedAt?: string;
            /**
             * Exact submitted arguments as JSON or text. Remove credentials, cookies and unrelated private content first. Do not reconstruct unknown arguments.
             */
            arguments: string;
            /**
             * Observed response or error text, including error codes and retry outcome. Remove secrets.
             */
            result: string;
            /**
             * Returned request ID, when available.
             */
            requestId?: string;
            /**
             * Returned job or run ID, when available.
             */
            jobId?: string;
          },
          {
            /**
             * Exact tool name or REST method and path.
             */
            tool: string;
            /**
             * Observed call time with timezone; omit if unknown.
             */
            submittedAt?: string;
            /**
             * Exact submitted arguments as JSON or text. Remove credentials, cookies and unrelated private content first. Do not reconstruct unknown arguments.
             */
            arguments: string;
            /**
             * Observed response or error text, including error codes and retry outcome. Remove secrets.
             */
            result: string;
            /**
             * Returned request ID, when available.
             */
            requestId?: string;
            /**
             * Returned job or run ID, when available.
             */
            jobId?: string;
          },
          {
            /**
             * Exact tool name or REST method and path.
             */
            tool: string;
            /**
             * Observed call time with timezone; omit if unknown.
             */
            submittedAt?: string;
            /**
             * Exact submitted arguments as JSON or text. Remove credentials, cookies and unrelated private content first. Do not reconstruct unknown arguments.
             */
            arguments: string;
            /**
             * Observed response or error text, including error codes and retry outcome. Remove secrets.
             */
            result: string;
            /**
             * Returned request ID, when available.
             */
            requestId?: string;
            /**
             * Returned job or run ID, when available.
             */
            jobId?: string;
          },
          {
            /**
             * Exact tool name or REST method and path.
             */
            tool: string;
            /**
             * Observed call time with timezone; omit if unknown.
             */
            submittedAt?: string;
            /**
             * Exact submitted arguments as JSON or text. Remove credentials, cookies and unrelated private content first. Do not reconstruct unknown arguments.
             */
            arguments: string;
            /**
             * Observed response or error text, including error codes and retry outcome. Remove secrets.
             */
            result: string;
            /**
             * Returned request ID, when available.
             */
            requestId?: string;
            /**
             * Returned job or run ID, when available.
             */
            jobId?: string;
          },
          {
            /**
             * Exact tool name or REST method and path.
             */
            tool: string;
            /**
             * Observed call time with timezone; omit if unknown.
             */
            submittedAt?: string;
            /**
             * Exact submitted arguments as JSON or text. Remove credentials, cookies and unrelated private content first. Do not reconstruct unknown arguments.
             */
            arguments: string;
            /**
             * Observed response or error text, including error codes and retry outcome. Remove secrets.
             */
            result: string;
            /**
             * Returned request ID, when available.
             */
            requestId?: string;
            /**
             * Returned job or run ID, when available.
             */
            jobId?: string;
          },
          {
            /**
             * Exact tool name or REST method and path.
             */
            tool: string;
            /**
             * Observed call time with timezone; omit if unknown.
             */
            submittedAt?: string;
            /**
             * Exact submitted arguments as JSON or text. Remove credentials, cookies and unrelated private content first. Do not reconstruct unknown arguments.
             */
            arguments: string;
            /**
             * Observed response or error text, including error codes and retry outcome. Remove secrets.
             */
            result: string;
            /**
             * Returned request ID, when available.
             */
            requestId?: string;
            /**
             * Returned job or run ID, when available.
             */
            jobId?: string;
          },
          {
            /**
             * Exact tool name or REST method and path.
             */
            tool: string;
            /**
             * Observed call time with timezone; omit if unknown.
             */
            submittedAt?: string;
            /**
             * Exact submitted arguments as JSON or text. Remove credentials, cookies and unrelated private content first. Do not reconstruct unknown arguments.
             */
            arguments: string;
            /**
             * Observed response or error text, including error codes and retry outcome. Remove secrets.
             */
            result: string;
            /**
             * Returned request ID, when available.
             */
            requestId?: string;
            /**
             * Returned job or run ID, when available.
             */
            jobId?: string;
          },
          {
            /**
             * Exact tool name or REST method and path.
             */
            tool: string;
            /**
             * Observed call time with timezone; omit if unknown.
             */
            submittedAt?: string;
            /**
             * Exact submitted arguments as JSON or text. Remove credentials, cookies and unrelated private content first. Do not reconstruct unknown arguments.
             */
            arguments: string;
            /**
             * Observed response or error text, including error codes and retry outcome. Remove secrets.
             */
            result: string;
            /**
             * Returned request ID, when available.
             */
            requestId?: string;
            /**
             * Returned job or run ID, when available.
             */
            jobId?: string;
          },
          {
            /**
             * Exact tool name or REST method and path.
             */
            tool: string;
            /**
             * Observed call time with timezone; omit if unknown.
             */
            submittedAt?: string;
            /**
             * Exact submitted arguments as JSON or text. Remove credentials, cookies and unrelated private content first. Do not reconstruct unknown arguments.
             */
            arguments: string;
            /**
             * Observed response or error text, including error codes and retry outcome. Remove secrets.
             */
            result: string;
            /**
             * Returned request ID, when available.
             */
            requestId?: string;
            /**
             * Returned job or run ID, when available.
             */
            jobId?: string;
          },
          {
            /**
             * Exact tool name or REST method and path.
             */
            tool: string;
            /**
             * Observed call time with timezone; omit if unknown.
             */
            submittedAt?: string;
            /**
             * Exact submitted arguments as JSON or text. Remove credentials, cookies and unrelated private content first. Do not reconstruct unknown arguments.
             */
            arguments: string;
            /**
             * Observed response or error text, including error codes and retry outcome. Remove secrets.
             */
            result: string;
            /**
             * Returned request ID, when available.
             */
            requestId?: string;
            /**
             * Returned job or run ID, when available.
             */
            jobId?: string;
          },
          {
            /**
             * Exact tool name or REST method and path.
             */
            tool: string;
            /**
             * Observed call time with timezone; omit if unknown.
             */
            submittedAt?: string;
            /**
             * Exact submitted arguments as JSON or text. Remove credentials, cookies and unrelated private content first. Do not reconstruct unknown arguments.
             */
            arguments: string;
            /**
             * Observed response or error text, including error codes and retry outcome. Remove secrets.
             */
            result: string;
            /**
             * Returned request ID, when available.
             */
            requestId?: string;
            /**
             * Returned job or run ID, when available.
             */
            jobId?: string;
          }
        ]
      | [
          {
            /**
             * Exact tool name or REST method and path.
             */
            tool: string;
            /**
             * Observed call time with timezone; omit if unknown.
             */
            submittedAt?: string;
            /**
             * Exact submitted arguments as JSON or text. Remove credentials, cookies and unrelated private content first. Do not reconstruct unknown arguments.
             */
            arguments: string;
            /**
             * Observed response or error text, including error codes and retry outcome. Remove secrets.
             */
            result: string;
            /**
             * Returned request ID, when available.
             */
            requestId?: string;
            /**
             * Returned job or run ID, when available.
             */
            jobId?: string;
          },
          {
            /**
             * Exact tool name or REST method and path.
             */
            tool: string;
            /**
             * Observed call time with timezone; omit if unknown.
             */
            submittedAt?: string;
            /**
             * Exact submitted arguments as JSON or text. Remove credentials, cookies and unrelated private content first. Do not reconstruct unknown arguments.
             */
            arguments: string;
            /**
             * Observed response or error text, including error codes and retry outcome. Remove secrets.
             */
            result: string;
            /**
             * Returned request ID, when available.
             */
            requestId?: string;
            /**
             * Returned job or run ID, when available.
             */
            jobId?: string;
          },
          {
            /**
             * Exact tool name or REST method and path.
             */
            tool: string;
            /**
             * Observed call time with timezone; omit if unknown.
             */
            submittedAt?: string;
            /**
             * Exact submitted arguments as JSON or text. Remove credentials, cookies and unrelated private content first. Do not reconstruct unknown arguments.
             */
            arguments: string;
            /**
             * Observed response or error text, including error codes and retry outcome. Remove secrets.
             */
            result: string;
            /**
             * Returned request ID, when available.
             */
            requestId?: string;
            /**
             * Returned job or run ID, when available.
             */
            jobId?: string;
          },
          {
            /**
             * Exact tool name or REST method and path.
             */
            tool: string;
            /**
             * Observed call time with timezone; omit if unknown.
             */
            submittedAt?: string;
            /**
             * Exact submitted arguments as JSON or text. Remove credentials, cookies and unrelated private content first. Do not reconstruct unknown arguments.
             */
            arguments: string;
            /**
             * Observed response or error text, including error codes and retry outcome. Remove secrets.
             */
            result: string;
            /**
             * Returned request ID, when available.
             */
            requestId?: string;
            /**
             * Returned job or run ID, when available.
             */
            jobId?: string;
          },
          {
            /**
             * Exact tool name or REST method and path.
             */
            tool: string;
            /**
             * Observed call time with timezone; omit if unknown.
             */
            submittedAt?: string;
            /**
             * Exact submitted arguments as JSON or text. Remove credentials, cookies and unrelated private content first. Do not reconstruct unknown arguments.
             */
            arguments: string;
            /**
             * Observed response or error text, including error codes and retry outcome. Remove secrets.
             */
            result: string;
            /**
             * Returned request ID, when available.
             */
            requestId?: string;
            /**
             * Returned job or run ID, when available.
             */
            jobId?: string;
          },
          {
            /**
             * Exact tool name or REST method and path.
             */
            tool: string;
            /**
             * Observed call time with timezone; omit if unknown.
             */
            submittedAt?: string;
            /**
             * Exact submitted arguments as JSON or text. Remove credentials, cookies and unrelated private content first. Do not reconstruct unknown arguments.
             */
            arguments: string;
            /**
             * Observed response or error text, including error codes and retry outcome. Remove secrets.
             */
            result: string;
            /**
             * Returned request ID, when available.
             */
            requestId?: string;
            /**
             * Returned job or run ID, when available.
             */
            jobId?: string;
          },
          {
            /**
             * Exact tool name or REST method and path.
             */
            tool: string;
            /**
             * Observed call time with timezone; omit if unknown.
             */
            submittedAt?: string;
            /**
             * Exact submitted arguments as JSON or text. Remove credentials, cookies and unrelated private content first. Do not reconstruct unknown arguments.
             */
            arguments: string;
            /**
             * Observed response or error text, including error codes and retry outcome. Remove secrets.
             */
            result: string;
            /**
             * Returned request ID, when available.
             */
            requestId?: string;
            /**
             * Returned job or run ID, when available.
             */
            jobId?: string;
          },
          {
            /**
             * Exact tool name or REST method and path.
             */
            tool: string;
            /**
             * Observed call time with timezone; omit if unknown.
             */
            submittedAt?: string;
            /**
             * Exact submitted arguments as JSON or text. Remove credentials, cookies and unrelated private content first. Do not reconstruct unknown arguments.
             */
            arguments: string;
            /**
             * Observed response or error text, including error codes and retry outcome. Remove secrets.
             */
            result: string;
            /**
             * Returned request ID, when available.
             */
            requestId?: string;
            /**
             * Returned job or run ID, when available.
             */
            jobId?: string;
          },
          {
            /**
             * Exact tool name or REST method and path.
             */
            tool: string;
            /**
             * Observed call time with timezone; omit if unknown.
             */
            submittedAt?: string;
            /**
             * Exact submitted arguments as JSON or text. Remove credentials, cookies and unrelated private content first. Do not reconstruct unknown arguments.
             */
            arguments: string;
            /**
             * Observed response or error text, including error codes and retry outcome. Remove secrets.
             */
            result: string;
            /**
             * Returned request ID, when available.
             */
            requestId?: string;
            /**
             * Returned job or run ID, when available.
             */
            jobId?: string;
          },
          {
            /**
             * Exact tool name or REST method and path.
             */
            tool: string;
            /**
             * Observed call time with timezone; omit if unknown.
             */
            submittedAt?: string;
            /**
             * Exact submitted arguments as JSON or text. Remove credentials, cookies and unrelated private content first. Do not reconstruct unknown arguments.
             */
            arguments: string;
            /**
             * Observed response or error text, including error codes and retry outcome. Remove secrets.
             */
            result: string;
            /**
             * Returned request ID, when available.
             */
            requestId?: string;
            /**
             * Returned job or run ID, when available.
             */
            jobId?: string;
          },
          {
            /**
             * Exact tool name or REST method and path.
             */
            tool: string;
            /**
             * Observed call time with timezone; omit if unknown.
             */
            submittedAt?: string;
            /**
             * Exact submitted arguments as JSON or text. Remove credentials, cookies and unrelated private content first. Do not reconstruct unknown arguments.
             */
            arguments: string;
            /**
             * Observed response or error text, including error codes and retry outcome. Remove secrets.
             */
            result: string;
            /**
             * Returned request ID, when available.
             */
            requestId?: string;
            /**
             * Returned job or run ID, when available.
             */
            jobId?: string;
          },
          {
            /**
             * Exact tool name or REST method and path.
             */
            tool: string;
            /**
             * Observed call time with timezone; omit if unknown.
             */
            submittedAt?: string;
            /**
             * Exact submitted arguments as JSON or text. Remove credentials, cookies and unrelated private content first. Do not reconstruct unknown arguments.
             */
            arguments: string;
            /**
             * Observed response or error text, including error codes and retry outcome. Remove secrets.
             */
            result: string;
            /**
             * Returned request ID, when available.
             */
            requestId?: string;
            /**
             * Returned job or run ID, when available.
             */
            jobId?: string;
          },
          {
            /**
             * Exact tool name or REST method and path.
             */
            tool: string;
            /**
             * Observed call time with timezone; omit if unknown.
             */
            submittedAt?: string;
            /**
             * Exact submitted arguments as JSON or text. Remove credentials, cookies and unrelated private content first. Do not reconstruct unknown arguments.
             */
            arguments: string;
            /**
             * Observed response or error text, including error codes and retry outcome. Remove secrets.
             */
            result: string;
            /**
             * Returned request ID, when available.
             */
            requestId?: string;
            /**
             * Returned job or run ID, when available.
             */
            jobId?: string;
          },
          {
            /**
             * Exact tool name or REST method and path.
             */
            tool: string;
            /**
             * Observed call time with timezone; omit if unknown.
             */
            submittedAt?: string;
            /**
             * Exact submitted arguments as JSON or text. Remove credentials, cookies and unrelated private content first. Do not reconstruct unknown arguments.
             */
            arguments: string;
            /**
             * Observed response or error text, including error codes and retry outcome. Remove secrets.
             */
            result: string;
            /**
             * Returned request ID, when available.
             */
            requestId?: string;
            /**
             * Returned job or run ID, when available.
             */
            jobId?: string;
          },
          {
            /**
             * Exact tool name or REST method and path.
             */
            tool: string;
            /**
             * Observed call time with timezone; omit if unknown.
             */
            submittedAt?: string;
            /**
             * Exact submitted arguments as JSON or text. Remove credentials, cookies and unrelated private content first. Do not reconstruct unknown arguments.
             */
            arguments: string;
            /**
             * Observed response or error text, including error codes and retry outcome. Remove secrets.
             */
            result: string;
            /**
             * Returned request ID, when available.
             */
            requestId?: string;
            /**
             * Returned job or run ID, when available.
             */
            jobId?: string;
          },
          {
            /**
             * Exact tool name or REST method and path.
             */
            tool: string;
            /**
             * Observed call time with timezone; omit if unknown.
             */
            submittedAt?: string;
            /**
             * Exact submitted arguments as JSON or text. Remove credentials, cookies and unrelated private content first. Do not reconstruct unknown arguments.
             */
            arguments: string;
            /**
             * Observed response or error text, including error codes and retry outcome. Remove secrets.
             */
            result: string;
            /**
             * Returned request ID, when available.
             */
            requestId?: string;
            /**
             * Returned job or run ID, when available.
             */
            jobId?: string;
          },
          {
            /**
             * Exact tool name or REST method and path.
             */
            tool: string;
            /**
             * Observed call time with timezone; omit if unknown.
             */
            submittedAt?: string;
            /**
             * Exact submitted arguments as JSON or text. Remove credentials, cookies and unrelated private content first. Do not reconstruct unknown arguments.
             */
            arguments: string;
            /**
             * Observed response or error text, including error codes and retry outcome. Remove secrets.
             */
            result: string;
            /**
             * Returned request ID, when available.
             */
            requestId?: string;
            /**
             * Returned job or run ID, when available.
             */
            jobId?: string;
          }
        ]
      | [
          {
            /**
             * Exact tool name or REST method and path.
             */
            tool: string;
            /**
             * Observed call time with timezone; omit if unknown.
             */
            submittedAt?: string;
            /**
             * Exact submitted arguments as JSON or text. Remove credentials, cookies and unrelated private content first. Do not reconstruct unknown arguments.
             */
            arguments: string;
            /**
             * Observed response or error text, including error codes and retry outcome. Remove secrets.
             */
            result: string;
            /**
             * Returned request ID, when available.
             */
            requestId?: string;
            /**
             * Returned job or run ID, when available.
             */
            jobId?: string;
          },
          {
            /**
             * Exact tool name or REST method and path.
             */
            tool: string;
            /**
             * Observed call time with timezone; omit if unknown.
             */
            submittedAt?: string;
            /**
             * Exact submitted arguments as JSON or text. Remove credentials, cookies and unrelated private content first. Do not reconstruct unknown arguments.
             */
            arguments: string;
            /**
             * Observed response or error text, including error codes and retry outcome. Remove secrets.
             */
            result: string;
            /**
             * Returned request ID, when available.
             */
            requestId?: string;
            /**
             * Returned job or run ID, when available.
             */
            jobId?: string;
          },
          {
            /**
             * Exact tool name or REST method and path.
             */
            tool: string;
            /**
             * Observed call time with timezone; omit if unknown.
             */
            submittedAt?: string;
            /**
             * Exact submitted arguments as JSON or text. Remove credentials, cookies and unrelated private content first. Do not reconstruct unknown arguments.
             */
            arguments: string;
            /**
             * Observed response or error text, including error codes and retry outcome. Remove secrets.
             */
            result: string;
            /**
             * Returned request ID, when available.
             */
            requestId?: string;
            /**
             * Returned job or run ID, when available.
             */
            jobId?: string;
          },
          {
            /**
             * Exact tool name or REST method and path.
             */
            tool: string;
            /**
             * Observed call time with timezone; omit if unknown.
             */
            submittedAt?: string;
            /**
             * Exact submitted arguments as JSON or text. Remove credentials, cookies and unrelated private content first. Do not reconstruct unknown arguments.
             */
            arguments: string;
            /**
             * Observed response or error text, including error codes and retry outcome. Remove secrets.
             */
            result: string;
            /**
             * Returned request ID, when available.
             */
            requestId?: string;
            /**
             * Returned job or run ID, when available.
             */
            jobId?: string;
          },
          {
            /**
             * Exact tool name or REST method and path.
             */
            tool: string;
            /**
             * Observed call time with timezone; omit if unknown.
             */
            submittedAt?: string;
            /**
             * Exact submitted arguments as JSON or text. Remove credentials, cookies and unrelated private content first. Do not reconstruct unknown arguments.
             */
            arguments: string;
            /**
             * Observed response or error text, including error codes and retry outcome. Remove secrets.
             */
            result: string;
            /**
             * Returned request ID, when available.
             */
            requestId?: string;
            /**
             * Returned job or run ID, when available.
             */
            jobId?: string;
          },
          {
            /**
             * Exact tool name or REST method and path.
             */
            tool: string;
            /**
             * Observed call time with timezone; omit if unknown.
             */
            submittedAt?: string;
            /**
             * Exact submitted arguments as JSON or text. Remove credentials, cookies and unrelated private content first. Do not reconstruct unknown arguments.
             */
            arguments: string;
            /**
             * Observed response or error text, including error codes and retry outcome. Remove secrets.
             */
            result: string;
            /**
             * Returned request ID, when available.
             */
            requestId?: string;
            /**
             * Returned job or run ID, when available.
             */
            jobId?: string;
          },
          {
            /**
             * Exact tool name or REST method and path.
             */
            tool: string;
            /**
             * Observed call time with timezone; omit if unknown.
             */
            submittedAt?: string;
            /**
             * Exact submitted arguments as JSON or text. Remove credentials, cookies and unrelated private content first. Do not reconstruct unknown arguments.
             */
            arguments: string;
            /**
             * Observed response or error text, including error codes and retry outcome. Remove secrets.
             */
            result: string;
            /**
             * Returned request ID, when available.
             */
            requestId?: string;
            /**
             * Returned job or run ID, when available.
             */
            jobId?: string;
          },
          {
            /**
             * Exact tool name or REST method and path.
             */
            tool: string;
            /**
             * Observed call time with timezone; omit if unknown.
             */
            submittedAt?: string;
            /**
             * Exact submitted arguments as JSON or text. Remove credentials, cookies and unrelated private content first. Do not reconstruct unknown arguments.
             */
            arguments: string;
            /**
             * Observed response or error text, including error codes and retry outcome. Remove secrets.
             */
            result: string;
            /**
             * Returned request ID, when available.
             */
            requestId?: string;
            /**
             * Returned job or run ID, when available.
             */
            jobId?: string;
          },
          {
            /**
             * Exact tool name or REST method and path.
             */
            tool: string;
            /**
             * Observed call time with timezone; omit if unknown.
             */
            submittedAt?: string;
            /**
             * Exact submitted arguments as JSON or text. Remove credentials, cookies and unrelated private content first. Do not reconstruct unknown arguments.
             */
            arguments: string;
            /**
             * Observed response or error text, including error codes and retry outcome. Remove secrets.
             */
            result: string;
            /**
             * Returned request ID, when available.
             */
            requestId?: string;
            /**
             * Returned job or run ID, when available.
             */
            jobId?: string;
          },
          {
            /**
             * Exact tool name or REST method and path.
             */
            tool: string;
            /**
             * Observed call time with timezone; omit if unknown.
             */
            submittedAt?: string;
            /**
             * Exact submitted arguments as JSON or text. Remove credentials, cookies and unrelated private content first. Do not reconstruct unknown arguments.
             */
            arguments: string;
            /**
             * Observed response or error text, including error codes and retry outcome. Remove secrets.
             */
            result: string;
            /**
             * Returned request ID, when available.
             */
            requestId?: string;
            /**
             * Returned job or run ID, when available.
             */
            jobId?: string;
          },
          {
            /**
             * Exact tool name or REST method and path.
             */
            tool: string;
            /**
             * Observed call time with timezone; omit if unknown.
             */
            submittedAt?: string;
            /**
             * Exact submitted arguments as JSON or text. Remove credentials, cookies and unrelated private content first. Do not reconstruct unknown arguments.
             */
            arguments: string;
            /**
             * Observed response or error text, including error codes and retry outcome. Remove secrets.
             */
            result: string;
            /**
             * Returned request ID, when available.
             */
            requestId?: string;
            /**
             * Returned job or run ID, when available.
             */
            jobId?: string;
          },
          {
            /**
             * Exact tool name or REST method and path.
             */
            tool: string;
            /**
             * Observed call time with timezone; omit if unknown.
             */
            submittedAt?: string;
            /**
             * Exact submitted arguments as JSON or text. Remove credentials, cookies and unrelated private content first. Do not reconstruct unknown arguments.
             */
            arguments: string;
            /**
             * Observed response or error text, including error codes and retry outcome. Remove secrets.
             */
            result: string;
            /**
             * Returned request ID, when available.
             */
            requestId?: string;
            /**
             * Returned job or run ID, when available.
             */
            jobId?: string;
          },
          {
            /**
             * Exact tool name or REST method and path.
             */
            tool: string;
            /**
             * Observed call time with timezone; omit if unknown.
             */
            submittedAt?: string;
            /**
             * Exact submitted arguments as JSON or text. Remove credentials, cookies and unrelated private content first. Do not reconstruct unknown arguments.
             */
            arguments: string;
            /**
             * Observed response or error text, including error codes and retry outcome. Remove secrets.
             */
            result: string;
            /**
             * Returned request ID, when available.
             */
            requestId?: string;
            /**
             * Returned job or run ID, when available.
             */
            jobId?: string;
          },
          {
            /**
             * Exact tool name or REST method and path.
             */
            tool: string;
            /**
             * Observed call time with timezone; omit if unknown.
             */
            submittedAt?: string;
            /**
             * Exact submitted arguments as JSON or text. Remove credentials, cookies and unrelated private content first. Do not reconstruct unknown arguments.
             */
            arguments: string;
            /**
             * Observed response or error text, including error codes and retry outcome. Remove secrets.
             */
            result: string;
            /**
             * Returned request ID, when available.
             */
            requestId?: string;
            /**
             * Returned job or run ID, when available.
             */
            jobId?: string;
          },
          {
            /**
             * Exact tool name or REST method and path.
             */
            tool: string;
            /**
             * Observed call time with timezone; omit if unknown.
             */
            submittedAt?: string;
            /**
             * Exact submitted arguments as JSON or text. Remove credentials, cookies and unrelated private content first. Do not reconstruct unknown arguments.
             */
            arguments: string;
            /**
             * Observed response or error text, including error codes and retry outcome. Remove secrets.
             */
            result: string;
            /**
             * Returned request ID, when available.
             */
            requestId?: string;
            /**
             * Returned job or run ID, when available.
             */
            jobId?: string;
          },
          {
            /**
             * Exact tool name or REST method and path.
             */
            tool: string;
            /**
             * Observed call time with timezone; omit if unknown.
             */
            submittedAt?: string;
            /**
             * Exact submitted arguments as JSON or text. Remove credentials, cookies and unrelated private content first. Do not reconstruct unknown arguments.
             */
            arguments: string;
            /**
             * Observed response or error text, including error codes and retry outcome. Remove secrets.
             */
            result: string;
            /**
             * Returned request ID, when available.
             */
            requestId?: string;
            /**
             * Returned job or run ID, when available.
             */
            jobId?: string;
          },
          {
            /**
             * Exact tool name or REST method and path.
             */
            tool: string;
            /**
             * Observed call time with timezone; omit if unknown.
             */
            submittedAt?: string;
            /**
             * Exact submitted arguments as JSON or text. Remove credentials, cookies and unrelated private content first. Do not reconstruct unknown arguments.
             */
            arguments: string;
            /**
             * Observed response or error text, including error codes and retry outcome. Remove secrets.
             */
            result: string;
            /**
             * Returned request ID, when available.
             */
            requestId?: string;
            /**
             * Returned job or run ID, when available.
             */
            jobId?: string;
          },
          {
            /**
             * Exact tool name or REST method and path.
             */
            tool: string;
            /**
             * Observed call time with timezone; omit if unknown.
             */
            submittedAt?: string;
            /**
             * Exact submitted arguments as JSON or text. Remove credentials, cookies and unrelated private content first. Do not reconstruct unknown arguments.
             */
            arguments: string;
            /**
             * Observed response or error text, including error codes and retry outcome. Remove secrets.
             */
            result: string;
            /**
             * Returned request ID, when available.
             */
            requestId?: string;
            /**
             * Returned job or run ID, when available.
             */
            jobId?: string;
          }
        ]
      | [
          {
            /**
             * Exact tool name or REST method and path.
             */
            tool: string;
            /**
             * Observed call time with timezone; omit if unknown.
             */
            submittedAt?: string;
            /**
             * Exact submitted arguments as JSON or text. Remove credentials, cookies and unrelated private content first. Do not reconstruct unknown arguments.
             */
            arguments: string;
            /**
             * Observed response or error text, including error codes and retry outcome. Remove secrets.
             */
            result: string;
            /**
             * Returned request ID, when available.
             */
            requestId?: string;
            /**
             * Returned job or run ID, when available.
             */
            jobId?: string;
          },
          {
            /**
             * Exact tool name or REST method and path.
             */
            tool: string;
            /**
             * Observed call time with timezone; omit if unknown.
             */
            submittedAt?: string;
            /**
             * Exact submitted arguments as JSON or text. Remove credentials, cookies and unrelated private content first. Do not reconstruct unknown arguments.
             */
            arguments: string;
            /**
             * Observed response or error text, including error codes and retry outcome. Remove secrets.
             */
            result: string;
            /**
             * Returned request ID, when available.
             */
            requestId?: string;
            /**
             * Returned job or run ID, when available.
             */
            jobId?: string;
          },
          {
            /**
             * Exact tool name or REST method and path.
             */
            tool: string;
            /**
             * Observed call time with timezone; omit if unknown.
             */
            submittedAt?: string;
            /**
             * Exact submitted arguments as JSON or text. Remove credentials, cookies and unrelated private content first. Do not reconstruct unknown arguments.
             */
            arguments: string;
            /**
             * Observed response or error text, including error codes and retry outcome. Remove secrets.
             */
            result: string;
            /**
             * Returned request ID, when available.
             */
            requestId?: string;
            /**
             * Returned job or run ID, when available.
             */
            jobId?: string;
          },
          {
            /**
             * Exact tool name or REST method and path.
             */
            tool: string;
            /**
             * Observed call time with timezone; omit if unknown.
             */
            submittedAt?: string;
            /**
             * Exact submitted arguments as JSON or text. Remove credentials, cookies and unrelated private content first. Do not reconstruct unknown arguments.
             */
            arguments: string;
            /**
             * Observed response or error text, including error codes and retry outcome. Remove secrets.
             */
            result: string;
            /**
             * Returned request ID, when available.
             */
            requestId?: string;
            /**
             * Returned job or run ID, when available.
             */
            jobId?: string;
          },
          {
            /**
             * Exact tool name or REST method and path.
             */
            tool: string;
            /**
             * Observed call time with timezone; omit if unknown.
             */
            submittedAt?: string;
            /**
             * Exact submitted arguments as JSON or text. Remove credentials, cookies and unrelated private content first. Do not reconstruct unknown arguments.
             */
            arguments: string;
            /**
             * Observed response or error text, including error codes and retry outcome. Remove secrets.
             */
            result: string;
            /**
             * Returned request ID, when available.
             */
            requestId?: string;
            /**
             * Returned job or run ID, when available.
             */
            jobId?: string;
          },
          {
            /**
             * Exact tool name or REST method and path.
             */
            tool: string;
            /**
             * Observed call time with timezone; omit if unknown.
             */
            submittedAt?: string;
            /**
             * Exact submitted arguments as JSON or text. Remove credentials, cookies and unrelated private content first. Do not reconstruct unknown arguments.
             */
            arguments: string;
            /**
             * Observed response or error text, including error codes and retry outcome. Remove secrets.
             */
            result: string;
            /**
             * Returned request ID, when available.
             */
            requestId?: string;
            /**
             * Returned job or run ID, when available.
             */
            jobId?: string;
          },
          {
            /**
             * Exact tool name or REST method and path.
             */
            tool: string;
            /**
             * Observed call time with timezone; omit if unknown.
             */
            submittedAt?: string;
            /**
             * Exact submitted arguments as JSON or text. Remove credentials, cookies and unrelated private content first. Do not reconstruct unknown arguments.
             */
            arguments: string;
            /**
             * Observed response or error text, including error codes and retry outcome. Remove secrets.
             */
            result: string;
            /**
             * Returned request ID, when available.
             */
            requestId?: string;
            /**
             * Returned job or run ID, when available.
             */
            jobId?: string;
          },
          {
            /**
             * Exact tool name or REST method and path.
             */
            tool: string;
            /**
             * Observed call time with timezone; omit if unknown.
             */
            submittedAt?: string;
            /**
             * Exact submitted arguments as JSON or text. Remove credentials, cookies and unrelated private content first. Do not reconstruct unknown arguments.
             */
            arguments: string;
            /**
             * Observed response or error text, including error codes and retry outcome. Remove secrets.
             */
            result: string;
            /**
             * Returned request ID, when available.
             */
            requestId?: string;
            /**
             * Returned job or run ID, when available.
             */
            jobId?: string;
          },
          {
            /**
             * Exact tool name or REST method and path.
             */
            tool: string;
            /**
             * Observed call time with timezone; omit if unknown.
             */
            submittedAt?: string;
            /**
             * Exact submitted arguments as JSON or text. Remove credentials, cookies and unrelated private content first. Do not reconstruct unknown arguments.
             */
            arguments: string;
            /**
             * Observed response or error text, including error codes and retry outcome. Remove secrets.
             */
            result: string;
            /**
             * Returned request ID, when available.
             */
            requestId?: string;
            /**
             * Returned job or run ID, when available.
             */
            jobId?: string;
          },
          {
            /**
             * Exact tool name or REST method and path.
             */
            tool: string;
            /**
             * Observed call time with timezone; omit if unknown.
             */
            submittedAt?: string;
            /**
             * Exact submitted arguments as JSON or text. Remove credentials, cookies and unrelated private content first. Do not reconstruct unknown arguments.
             */
            arguments: string;
            /**
             * Observed response or error text, including error codes and retry outcome. Remove secrets.
             */
            result: string;
            /**
             * Returned request ID, when available.
             */
            requestId?: string;
            /**
             * Returned job or run ID, when available.
             */
            jobId?: string;
          },
          {
            /**
             * Exact tool name or REST method and path.
             */
            tool: string;
            /**
             * Observed call time with timezone; omit if unknown.
             */
            submittedAt?: string;
            /**
             * Exact submitted arguments as JSON or text. Remove credentials, cookies and unrelated private content first. Do not reconstruct unknown arguments.
             */
            arguments: string;
            /**
             * Observed response or error text, including error codes and retry outcome. Remove secrets.
             */
            result: string;
            /**
             * Returned request ID, when available.
             */
            requestId?: string;
            /**
             * Returned job or run ID, when available.
             */
            jobId?: string;
          },
          {
            /**
             * Exact tool name or REST method and path.
             */
            tool: string;
            /**
             * Observed call time with timezone; omit if unknown.
             */
            submittedAt?: string;
            /**
             * Exact submitted arguments as JSON or text. Remove credentials, cookies and unrelated private content first. Do not reconstruct unknown arguments.
             */
            arguments: string;
            /**
             * Observed response or error text, including error codes and retry outcome. Remove secrets.
             */
            result: string;
            /**
             * Returned request ID, when available.
             */
            requestId?: string;
            /**
             * Returned job or run ID, when available.
             */
            jobId?: string;
          },
          {
            /**
             * Exact tool name or REST method and path.
             */
            tool: string;
            /**
             * Observed call time with timezone; omit if unknown.
             */
            submittedAt?: string;
            /**
             * Exact submitted arguments as JSON or text. Remove credentials, cookies and unrelated private content first. Do not reconstruct unknown arguments.
             */
            arguments: string;
            /**
             * Observed response or error text, including error codes and retry outcome. Remove secrets.
             */
            result: string;
            /**
             * Returned request ID, when available.
             */
            requestId?: string;
            /**
             * Returned job or run ID, when available.
             */
            jobId?: string;
          },
          {
            /**
             * Exact tool name or REST method and path.
             */
            tool: string;
            /**
             * Observed call time with timezone; omit if unknown.
             */
            submittedAt?: string;
            /**
             * Exact submitted arguments as JSON or text. Remove credentials, cookies and unrelated private content first. Do not reconstruct unknown arguments.
             */
            arguments: string;
            /**
             * Observed response or error text, including error codes and retry outcome. Remove secrets.
             */
            result: string;
            /**
             * Returned request ID, when available.
             */
            requestId?: string;
            /**
             * Returned job or run ID, when available.
             */
            jobId?: string;
          },
          {
            /**
             * Exact tool name or REST method and path.
             */
            tool: string;
            /**
             * Observed call time with timezone; omit if unknown.
             */
            submittedAt?: string;
            /**
             * Exact submitted arguments as JSON or text. Remove credentials, cookies and unrelated private content first. Do not reconstruct unknown arguments.
             */
            arguments: string;
            /**
             * Observed response or error text, including error codes and retry outcome. Remove secrets.
             */
            result: string;
            /**
             * Returned request ID, when available.
             */
            requestId?: string;
            /**
             * Returned job or run ID, when available.
             */
            jobId?: string;
          },
          {
            /**
             * Exact tool name or REST method and path.
             */
            tool: string;
            /**
             * Observed call time with timezone; omit if unknown.
             */
            submittedAt?: string;
            /**
             * Exact submitted arguments as JSON or text. Remove credentials, cookies and unrelated private content first. Do not reconstruct unknown arguments.
             */
            arguments: string;
            /**
             * Observed response or error text, including error codes and retry outcome. Remove secrets.
             */
            result: string;
            /**
             * Returned request ID, when available.
             */
            requestId?: string;
            /**
             * Returned job or run ID, when available.
             */
            jobId?: string;
          },
          {
            /**
             * Exact tool name or REST method and path.
             */
            tool: string;
            /**
             * Observed call time with timezone; omit if unknown.
             */
            submittedAt?: string;
            /**
             * Exact submitted arguments as JSON or text. Remove credentials, cookies and unrelated private content first. Do not reconstruct unknown arguments.
             */
            arguments: string;
            /**
             * Observed response or error text, including error codes and retry outcome. Remove secrets.
             */
            result: string;
            /**
             * Returned request ID, when available.
             */
            requestId?: string;
            /**
             * Returned job or run ID, when available.
             */
            jobId?: string;
          },
          {
            /**
             * Exact tool name or REST method and path.
             */
            tool: string;
            /**
             * Observed call time with timezone; omit if unknown.
             */
            submittedAt?: string;
            /**
             * Exact submitted arguments as JSON or text. Remove credentials, cookies and unrelated private content first. Do not reconstruct unknown arguments.
             */
            arguments: string;
            /**
             * Observed response or error text, including error codes and retry outcome. Remove secrets.
             */
            result: string;
            /**
             * Returned request ID, when available.
             */
            requestId?: string;
            /**
             * Returned job or run ID, when available.
             */
            jobId?: string;
          },
          {
            /**
             * Exact tool name or REST method and path.
             */
            tool: string;
            /**
             * Observed call time with timezone; omit if unknown.
             */
            submittedAt?: string;
            /**
             * Exact submitted arguments as JSON or text. Remove credentials, cookies and unrelated private content first. Do not reconstruct unknown arguments.
             */
            arguments: string;
            /**
             * Observed response or error text, including error codes and retry outcome. Remove secrets.
             */
            result: string;
            /**
             * Returned request ID, when available.
             */
            requestId?: string;
            /**
             * Returned job or run ID, when available.
             */
            jobId?: string;
          }
        ]
      | [
          {
            /**
             * Exact tool name or REST method and path.
             */
            tool: string;
            /**
             * Observed call time with timezone; omit if unknown.
             */
            submittedAt?: string;
            /**
             * Exact submitted arguments as JSON or text. Remove credentials, cookies and unrelated private content first. Do not reconstruct unknown arguments.
             */
            arguments: string;
            /**
             * Observed response or error text, including error codes and retry outcome. Remove secrets.
             */
            result: string;
            /**
             * Returned request ID, when available.
             */
            requestId?: string;
            /**
             * Returned job or run ID, when available.
             */
            jobId?: string;
          },
          {
            /**
             * Exact tool name or REST method and path.
             */
            tool: string;
            /**
             * Observed call time with timezone; omit if unknown.
             */
            submittedAt?: string;
            /**
             * Exact submitted arguments as JSON or text. Remove credentials, cookies and unrelated private content first. Do not reconstruct unknown arguments.
             */
            arguments: string;
            /**
             * Observed response or error text, including error codes and retry outcome. Remove secrets.
             */
            result: string;
            /**
             * Returned request ID, when available.
             */
            requestId?: string;
            /**
             * Returned job or run ID, when available.
             */
            jobId?: string;
          },
          {
            /**
             * Exact tool name or REST method and path.
             */
            tool: string;
            /**
             * Observed call time with timezone; omit if unknown.
             */
            submittedAt?: string;
            /**
             * Exact submitted arguments as JSON or text. Remove credentials, cookies and unrelated private content first. Do not reconstruct unknown arguments.
             */
            arguments: string;
            /**
             * Observed response or error text, including error codes and retry outcome. Remove secrets.
             */
            result: string;
            /**
             * Returned request ID, when available.
             */
            requestId?: string;
            /**
             * Returned job or run ID, when available.
             */
            jobId?: string;
          },
          {
            /**
             * Exact tool name or REST method and path.
             */
            tool: string;
            /**
             * Observed call time with timezone; omit if unknown.
             */
            submittedAt?: string;
            /**
             * Exact submitted arguments as JSON or text. Remove credentials, cookies and unrelated private content first. Do not reconstruct unknown arguments.
             */
            arguments: string;
            /**
             * Observed response or error text, including error codes and retry outcome. Remove secrets.
             */
            result: string;
            /**
             * Returned request ID, when available.
             */
            requestId?: string;
            /**
             * Returned job or run ID, when available.
             */
            jobId?: string;
          },
          {
            /**
             * Exact tool name or REST method and path.
             */
            tool: string;
            /**
             * Observed call time with timezone; omit if unknown.
             */
            submittedAt?: string;
            /**
             * Exact submitted arguments as JSON or text. Remove credentials, cookies and unrelated private content first. Do not reconstruct unknown arguments.
             */
            arguments: string;
            /**
             * Observed response or error text, including error codes and retry outcome. Remove secrets.
             */
            result: string;
            /**
             * Returned request ID, when available.
             */
            requestId?: string;
            /**
             * Returned job or run ID, when available.
             */
            jobId?: string;
          },
          {
            /**
             * Exact tool name or REST method and path.
             */
            tool: string;
            /**
             * Observed call time with timezone; omit if unknown.
             */
            submittedAt?: string;
            /**
             * Exact submitted arguments as JSON or text. Remove credentials, cookies and unrelated private content first. Do not reconstruct unknown arguments.
             */
            arguments: string;
            /**
             * Observed response or error text, including error codes and retry outcome. Remove secrets.
             */
            result: string;
            /**
             * Returned request ID, when available.
             */
            requestId?: string;
            /**
             * Returned job or run ID, when available.
             */
            jobId?: string;
          },
          {
            /**
             * Exact tool name or REST method and path.
             */
            tool: string;
            /**
             * Observed call time with timezone; omit if unknown.
             */
            submittedAt?: string;
            /**
             * Exact submitted arguments as JSON or text. Remove credentials, cookies and unrelated private content first. Do not reconstruct unknown arguments.
             */
            arguments: string;
            /**
             * Observed response or error text, including error codes and retry outcome. Remove secrets.
             */
            result: string;
            /**
             * Returned request ID, when available.
             */
            requestId?: string;
            /**
             * Returned job or run ID, when available.
             */
            jobId?: string;
          },
          {
            /**
             * Exact tool name or REST method and path.
             */
            tool: string;
            /**
             * Observed call time with timezone; omit if unknown.
             */
            submittedAt?: string;
            /**
             * Exact submitted arguments as JSON or text. Remove credentials, cookies and unrelated private content first. Do not reconstruct unknown arguments.
             */
            arguments: string;
            /**
             * Observed response or error text, including error codes and retry outcome. Remove secrets.
             */
            result: string;
            /**
             * Returned request ID, when available.
             */
            requestId?: string;
            /**
             * Returned job or run ID, when available.
             */
            jobId?: string;
          },
          {
            /**
             * Exact tool name or REST method and path.
             */
            tool: string;
            /**
             * Observed call time with timezone; omit if unknown.
             */
            submittedAt?: string;
            /**
             * Exact submitted arguments as JSON or text. Remove credentials, cookies and unrelated private content first. Do not reconstruct unknown arguments.
             */
            arguments: string;
            /**
             * Observed response or error text, including error codes and retry outcome. Remove secrets.
             */
            result: string;
            /**
             * Returned request ID, when available.
             */
            requestId?: string;
            /**
             * Returned job or run ID, when available.
             */
            jobId?: string;
          },
          {
            /**
             * Exact tool name or REST method and path.
             */
            tool: string;
            /**
             * Observed call time with timezone; omit if unknown.
             */
            submittedAt?: string;
            /**
             * Exact submitted arguments as JSON or text. Remove credentials, cookies and unrelated private content first. Do not reconstruct unknown arguments.
             */
            arguments: string;
            /**
             * Observed response or error text, including error codes and retry outcome. Remove secrets.
             */
            result: string;
            /**
             * Returned request ID, when available.
             */
            requestId?: string;
            /**
             * Returned job or run ID, when available.
             */
            jobId?: string;
          },
          {
            /**
             * Exact tool name or REST method and path.
             */
            tool: string;
            /**
             * Observed call time with timezone; omit if unknown.
             */
            submittedAt?: string;
            /**
             * Exact submitted arguments as JSON or text. Remove credentials, cookies and unrelated private content first. Do not reconstruct unknown arguments.
             */
            arguments: string;
            /**
             * Observed response or error text, including error codes and retry outcome. Remove secrets.
             */
            result: string;
            /**
             * Returned request ID, when available.
             */
            requestId?: string;
            /**
             * Returned job or run ID, when available.
             */
            jobId?: string;
          },
          {
            /**
             * Exact tool name or REST method and path.
             */
            tool: string;
            /**
             * Observed call time with timezone; omit if unknown.
             */
            submittedAt?: string;
            /**
             * Exact submitted arguments as JSON or text. Remove credentials, cookies and unrelated private content first. Do not reconstruct unknown arguments.
             */
            arguments: string;
            /**
             * Observed response or error text, including error codes and retry outcome. Remove secrets.
             */
            result: string;
            /**
             * Returned request ID, when available.
             */
            requestId?: string;
            /**
             * Returned job or run ID, when available.
             */
            jobId?: string;
          },
          {
            /**
             * Exact tool name or REST method and path.
             */
            tool: string;
            /**
             * Observed call time with timezone; omit if unknown.
             */
            submittedAt?: string;
            /**
             * Exact submitted arguments as JSON or text. Remove credentials, cookies and unrelated private content first. Do not reconstruct unknown arguments.
             */
            arguments: string;
            /**
             * Observed response or error text, including error codes and retry outcome. Remove secrets.
             */
            result: string;
            /**
             * Returned request ID, when available.
             */
            requestId?: string;
            /**
             * Returned job or run ID, when available.
             */
            jobId?: string;
          },
          {
            /**
             * Exact tool name or REST method and path.
             */
            tool: string;
            /**
             * Observed call time with timezone; omit if unknown.
             */
            submittedAt?: string;
            /**
             * Exact submitted arguments as JSON or text. Remove credentials, cookies and unrelated private content first. Do not reconstruct unknown arguments.
             */
            arguments: string;
            /**
             * Observed response or error text, including error codes and retry outcome. Remove secrets.
             */
            result: string;
            /**
             * Returned request ID, when available.
             */
            requestId?: string;
            /**
             * Returned job or run ID, when available.
             */
            jobId?: string;
          },
          {
            /**
             * Exact tool name or REST method and path.
             */
            tool: string;
            /**
             * Observed call time with timezone; omit if unknown.
             */
            submittedAt?: string;
            /**
             * Exact submitted arguments as JSON or text. Remove credentials, cookies and unrelated private content first. Do not reconstruct unknown arguments.
             */
            arguments: string;
            /**
             * Observed response or error text, including error codes and retry outcome. Remove secrets.
             */
            result: string;
            /**
             * Returned request ID, when available.
             */
            requestId?: string;
            /**
             * Returned job or run ID, when available.
             */
            jobId?: string;
          },
          {
            /**
             * Exact tool name or REST method and path.
             */
            tool: string;
            /**
             * Observed call time with timezone; omit if unknown.
             */
            submittedAt?: string;
            /**
             * Exact submitted arguments as JSON or text. Remove credentials, cookies and unrelated private content first. Do not reconstruct unknown arguments.
             */
            arguments: string;
            /**
             * Observed response or error text, including error codes and retry outcome. Remove secrets.
             */
            result: string;
            /**
             * Returned request ID, when available.
             */
            requestId?: string;
            /**
             * Returned job or run ID, when available.
             */
            jobId?: string;
          },
          {
            /**
             * Exact tool name or REST method and path.
             */
            tool: string;
            /**
             * Observed call time with timezone; omit if unknown.
             */
            submittedAt?: string;
            /**
             * Exact submitted arguments as JSON or text. Remove credentials, cookies and unrelated private content first. Do not reconstruct unknown arguments.
             */
            arguments: string;
            /**
             * Observed response or error text, including error codes and retry outcome. Remove secrets.
             */
            result: string;
            /**
             * Returned request ID, when available.
             */
            requestId?: string;
            /**
             * Returned job or run ID, when available.
             */
            jobId?: string;
          },
          {
            /**
             * Exact tool name or REST method and path.
             */
            tool: string;
            /**
             * Observed call time with timezone; omit if unknown.
             */
            submittedAt?: string;
            /**
             * Exact submitted arguments as JSON or text. Remove credentials, cookies and unrelated private content first. Do not reconstruct unknown arguments.
             */
            arguments: string;
            /**
             * Observed response or error text, including error codes and retry outcome. Remove secrets.
             */
            result: string;
            /**
             * Returned request ID, when available.
             */
            requestId?: string;
            /**
             * Returned job or run ID, when available.
             */
            jobId?: string;
          },
          {
            /**
             * Exact tool name or REST method and path.
             */
            tool: string;
            /**
             * Observed call time with timezone; omit if unknown.
             */
            submittedAt?: string;
            /**
             * Exact submitted arguments as JSON or text. Remove credentials, cookies and unrelated private content first. Do not reconstruct unknown arguments.
             */
            arguments: string;
            /**
             * Observed response or error text, including error codes and retry outcome. Remove secrets.
             */
            result: string;
            /**
             * Returned request ID, when available.
             */
            requestId?: string;
            /**
             * Returned job or run ID, when available.
             */
            jobId?: string;
          },
          {
            /**
             * Exact tool name or REST method and path.
             */
            tool: string;
            /**
             * Observed call time with timezone; omit if unknown.
             */
            submittedAt?: string;
            /**
             * Exact submitted arguments as JSON or text. Remove credentials, cookies and unrelated private content first. Do not reconstruct unknown arguments.
             */
            arguments: string;
            /**
             * Observed response or error text, including error codes and retry outcome. Remove secrets.
             */
            result: string;
            /**
             * Returned request ID, when available.
             */
            requestId?: string;
            /**
             * Returned job or run ID, when available.
             */
            jobId?: string;
          }
        ];
    /**
     * Observed client environment; use unknown rather than guessing.
     */
    client: {
      /**
       * Observed application or SDK name.
       */
      name: string;
      /**
       * Observed application or package version; omit if unknown.
       */
      version?: string;
      /**
       * Connection or install route used for the failed calls.
       */
      transport: "oauth" | "api-key" | "npx" | "npm" | "sdk" | "mcpb" | "rest" | "unknown";
      /**
       * Observed operating system; omit if unknown.
       */
      operatingSystem?: string;
      /**
       * Observed AI model; omit if unknown.
       */
      model?: string;
    };
    /**
     * Impact, frequency, useful prior context, and suspected cause clearly labeled as a guess. No full conversation dump.
     */
    context?: string;
    /**
     * Evidence that is unknown or unavailable; do not invent it.
     *
     * @maxItems 20
     */
    missing?:
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
      | [string, string, string, string, string, string, string, string, string, string, string, string]
      | [string, string, string, string, string, string, string, string, string, string, string, string, string]
      | [string, string, string, string, string, string, string, string, string, string, string, string, string, string]
      | [
          string,
          string,
          string,
          string,
          string,
          string,
          string,
          string,
          string,
          string,
          string,
          string,
          string,
          string,
          string
        ]
      | [
          string,
          string,
          string,
          string,
          string,
          string,
          string,
          string,
          string,
          string,
          string,
          string,
          string,
          string,
          string,
          string
        ]
      | [
          string,
          string,
          string,
          string,
          string,
          string,
          string,
          string,
          string,
          string,
          string,
          string,
          string,
          string,
          string,
          string,
          string
        ]
      | [
          string,
          string,
          string,
          string,
          string,
          string,
          string,
          string,
          string,
          string,
          string,
          string,
          string,
          string,
          string,
          string,
          string,
          string
        ]
      | [
          string,
          string,
          string,
          string,
          string,
          string,
          string,
          string,
          string,
          string,
          string,
          string,
          string,
          string,
          string,
          string,
          string,
          string,
          string
        ]
      | [
          string,
          string,
          string,
          string,
          string,
          string,
          string,
          string,
          string,
          string,
          string,
          string,
          string,
          string,
          string,
          string,
          string,
          string,
          string,
          string
        ];
  };
  /**
   * ID returned by prepare; required for submit or status.
   */
  reportId?: string;
  /**
   * Exact token returned by prepare; required for submit. A changed report requires a new prepare.
   */
  reviewToken?: string;
  /**
   * Set true only when the user has asked to submit this bug or approved the reviewed draft. Repeated errors alone do not authorize submission.
   */
  userApproved?: boolean;
}

export type Output =
  | {
      ok: true;
      accountEmail: string;
      reportId: string;
      status: "draft" | "submitted";
      receivedAt: string;
      submittedAt: string | null;
      expiresAt: string;
      report: {
        /**
         * Short description of the problem in plain language.
         */
        title: string;
        /**
         * What the user was trying to accomplish, using their words.
         */
        goal: string;
        /**
         * What should have happened.
         */
        expected: string;
        /**
         * What actually happened. Separate observations from suspected causes.
         */
        actual: string;
        /**
         * Ordered reproduction steps, including retries and what changed.
         *
         * @minItems 1
         * @maxItems 30
         */
        steps: [string, ...string[]];
        /**
         * Observed client environment; use unknown rather than guessing.
         */
        client: {
          /**
           * Observed application or SDK name.
           */
          name: string;
          /**
           * Observed application or package version; omit if unknown.
           */
          version?: string;
          /**
           * Connection or install route used for the failed calls.
           */
          transport: "oauth" | "api-key" | "npx" | "npm" | "sdk" | "mcpb" | "rest" | "unknown";
          /**
           * Observed operating system; omit if unknown.
           */
          operatingSystem?: string;
          /**
           * Observed AI model; omit if unknown.
           */
          model?: string;
        };
        /**
         * Impact, frequency, useful prior context, and suspected cause clearly labeled as a guess. No full conversation dump.
         */
        context?: string;
        /**
         * Evidence that is unknown or unavailable; do not invent it.
         *
         * @maxItems 20
         */
        missing:
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
          | [string, string, string, string, string, string, string, string, string, string, string, string]
          | [string, string, string, string, string, string, string, string, string, string, string, string, string]
          | [
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string
            ]
          | [
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string
            ]
          | [
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string
            ]
          | [
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string
            ]
          | [
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string
            ]
          | [
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string
            ]
          | [
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string
            ];
      };
      reviewToken?: string;
      redacted: boolean;
      message: string;
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
