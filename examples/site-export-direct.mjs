import { randomUUID } from 'node:crypto'
import { pathToFileURL } from 'node:url'
import { ScraperClient } from 'mcpscraper-sdk'

// Extraction discovers the site's pages itself. Map first only when an inventory
// is the result you need, rather than as a prerequisite for this export.
export function startSiteExport(client, { url, maxPages = 10, idempotencyKey }) {
  return client.tools.web.extractSite({ url, maxPages, idempotencyKey })
}

export function checkSiteExport(client, jobId) {
  return client.tools.web.checkSiteExport({ jobId })
}

// Omit pageId to read the manifest; use its page IDs for HTML, JSON or Markdown.
// Continue from nextOffset until it is null to retrieve every UTF-8 byte window.
export function readSiteExport(client, { jobId, pageId, format = 'manifest', offset = 0 }) {
  return client.tools.web.siteExportRead({
    jobId,
    ...(pageId === undefined ? {} : { pageId }),
    format,
    offset,
  })
}

if (process.argv[1] && import.meta.url === pathToFileURL(process.argv[1]).href) {
  const apiKey = process.env.MCPSCRAPER_API_KEY
  if (!apiKey) throw new Error('Set MCPSCRAPER_API_KEY before running this example.')
  const url = process.argv[2]
  if (!url) throw new Error('Pass the public website URL to export.')
  // After an uncertain response, reuse this key for the same intended export.
  const idempotencyKey = process.env.MCPSCRAPER_SITE_RETRY_KEY ?? randomUUID()
  console.log({ idempotencyKey })
  const result = await startSiteExport(new ScraperClient({ apiKey }), { url, idempotencyKey })
  console.log({ jobId: result.jobId ?? result.recovery?.jobId ?? null, status: result.status ?? null })
  // Inspect the saved job with checkSiteExport, then follow its nextActions.
  // A running job can expose saved pages while its remaining work continues.
}
