/** Public caller labels used for service reporting. These are caller claims, not authentication. */
export interface ClientAttribution {
  /** Defaults to sdk. Wrappers may name their actual transport surface. */
  surface?: 'sdk' | 'rest' | 'mcp-http' | 'mcp-stdio'
  installChannel?: 'npx' | 'npm' | 'mcpb' | 'source'
  aiClient?: 'claude' | 'claude-desktop' | 'claude-code' | 'chatgpt' | 'codex' | 'cursor' | 'gemini' | 'other'
  /** Explicit model identifier, at most 80 characters. */
  aiModel?: string
}

export interface ResponseMetadata {
  requestId?: string
  status: number
}

export interface ClientMetadataOptions {
  clientAttribution?: ClientAttribution
  /** Runs for each HTTP response, including errors, without changing the returned data. */
  onResponse?: (metadata: ResponseMetadata) => void
}

/** Never infer AI, model or install channel from the process or its environment. */
export function clientAttributionHeaders(attribution: ClientAttribution = {}): Record<string, string> {
  const headers: Record<string, string> = { 'x-mcp-client-surface': 'sdk' }
  if (['sdk', 'rest', 'mcp-http', 'mcp-stdio'].includes(attribution.surface ?? '')) {
    headers['x-mcp-client-surface'] = attribution.surface!
  }
  if (['npx', 'npm', 'mcpb', 'source'].includes(attribution.installChannel ?? '')) {
    headers['x-mcp-install-channel'] = attribution.installChannel!
  }
  const aiClient = typeof attribution.aiClient === 'string' ? attribution.aiClient.toLowerCase() : ''
  if (['claude', 'claude-desktop', 'claude-code', 'chatgpt', 'codex', 'cursor', 'gemini', 'other'].includes(aiClient)) {
    headers['x-mcp-ai-client'] = aiClient
  }
  if (typeof attribution.aiModel === 'string' && /^[a-zA-Z0-9][a-zA-Z0-9._:/-]{0,79}$/.test(attribution.aiModel)) {
    headers['x-mcp-ai-model'] = attribution.aiModel
  }
  return headers
}

export function responseMetadata(response: Response): ResponseMetadata {
  const requestId = response.headers?.get('x-mcp-request-id') || undefined
  return { ...(requestId ? { requestId } : {}), status: response.status }
}

/** Observers must not turn completed paid work into a client failure. */
export function notifyResponse(callback: ClientMetadataOptions['onResponse'], metadata: ResponseMetadata): void {
  try { callback?.(metadata) } catch { /* Keep transport success/failure authoritative. */ }
}
