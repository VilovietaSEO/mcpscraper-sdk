import { McpToolsClient } from '../packages/memory/dist/index.js'

const apiKey = process.env.MCP_SCRAPER_API_KEY
const connectionId = process.env.BING_CONNECTION_ID
const siteUrl = process.env.BING_SITE_URL
if (!apiKey || !connectionId || !siteUrl) {
  throw new Error('Set MCP_SCRAPER_API_KEY, BING_CONNECTION_ID and an exact BING_SITE_URL from list-sites.')
}

const tools = new McpToolsClient({ apiKey })
let continuation
for (let invocation = 0; invocation < 3; invocation++) {
  const result = await tools.connections.exportConnectedServiceData({
    connectionId,
    ...(continuation ? { continuation } : {
      dataset: 'bing_webmaster_reports',
      bing: { siteUrls: [siteUrl], reports: ['search-performance'] },
      lastDays: 7,
    }),
    maxItems: 1000,
    delivery: 'artifact',
  })
  if (!result.ok) throw new Error(result.error ?? 'Bing export failed.')
  console.log(JSON.stringify({ status: result.status, counts: result.counts, artifactId: result.artifact?.artifactId }))
  // Keep the original range, report selection and opaque cursor together.
  continuation = result.continuation
  if (!continuation) break
}
if (continuation) throw new Error('Export remains partial. Resume with its unchanged continuation; do not restart acquisition.')
