export const INTERNAL_TELEMETRY_FIELDS = new Set([
  'attempts', 'observedIp', 'observedCity', 'observedRegion',
  'proxyResolutionSource', 'proxyTargetLevel', 'proxyTargetLocation', 'proxyTargetZip',
  'proxyIdSuffix', 'browserSessionId', 'browserSessionIdSuffix',
  'attemptNumber', 'maxAttempts', 'willRetry',
])

export function stripInternalTelemetry(value: unknown): unknown {
  if (Array.isArray(value)) return value.map(stripInternalTelemetry)
  if (!value || typeof value !== 'object') return value
  const out: Record<string, unknown> = {}
  for (const [key, child] of Object.entries(value as Record<string, unknown>)) {
    if (key === 'properties' && child && typeof child === 'object') {
      const properties: Record<string, unknown> = {}
      for (const [property, propertyValue] of Object.entries(child as Record<string, unknown>)) {
        if (!INTERNAL_TELEMETRY_FIELDS.has(property)) {
          properties[property] = stripInternalTelemetry(propertyValue)
        }
      }
      out[key] = properties
    } else if (key === 'required' && Array.isArray(child)) {
      out[key] = child.filter(name => !INTERNAL_TELEMETRY_FIELDS.has(String(name)))
    } else {
      out[key] = stripInternalTelemetry(child)
    }
  }
  return out
}
