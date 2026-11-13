import { randomUUID } from 'node:crypto'
import { pathToFileURL } from 'node:url'
import { ScraperClient } from 'mcpscraper-sdk'

// The retained JSON is complete. Request this optional format only when needed;
// the artifact method generates it from saved data without another search.
export async function searchWithOptionalMarkdown(client, { query, idempotencyKey }) {
  const result = await client.tools.search.searchSerp({ query, mode: 'full', idempotencyKey })
  const handle = result.delivery?.availableExports?.find(item => item.contentType === 'text/markdown; charset=utf-8')
  if (!handle) return { result, markdown: null }
  const markdown = await client.tools.artifacts.download({ artifactId: handle.artifactId })
  return { result, markdown }
}

if (process.argv[1] && import.meta.url === pathToFileURL(process.argv[1]).href) {
  const apiKey = process.env.MCPSCRAPER_API_KEY
  if (!apiKey) throw new Error('Set MCPSCRAPER_API_KEY before running this example.')
  // After an uncertain response, run again with this same retry key.
  const idempotencyKey = process.env.MCPSCRAPER_SERP_RETRY_KEY ?? randomUUID()
  console.log({ idempotencyKey })
  const client = new ScraperClient({ apiKey })
  const { result, markdown } = await searchWithOptionalMarkdown(client, {
    query: process.argv[2] ?? 'plumbers in Denver Colorado',
    idempotencyKey,
  })
  // Do not log temporary download URLs. Use markdown.downloadUrl privately while
  // valid, or call the artifact method again for a renewed link.
  console.log({
    delivery: result.delivery?.mode ?? 'inline',
    markdown: markdown && { artifactId: markdown.artifactId, bytes: markdown.bytes, sha256: markdown.sha256 },
  })
}
