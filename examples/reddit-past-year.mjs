import { randomUUID } from 'node:crypto'
import { pathToFileURL } from 'node:url'
import { ScraperClient } from 'mcpscraper-sdk'

export function findRecentRooferThreads(client, { idempotencyKey, maxThreads = 2 }) {
  return client.tools.reddit.trending({
    topic: 'how to pick a good roofer',
    window: 'year',
    maxThreads,
    includeComments: true,
    maxCommentsPerThread: 20,
    idempotencyKey,
  })
}

// A known thread URL does not require a discovery request first.
export function readKnownThread(client, { url, idempotencyKey }) {
  return client.tools.reddit.thread({ url, maxComments: 20, idempotencyKey })
}

if (process.argv[1] && import.meta.url === pathToFileURL(process.argv[1]).href) {
  const apiKey = process.env.MCPSCRAPER_API_KEY
  if (!apiKey) throw new Error('Set MCPSCRAPER_API_KEY before running this example.')
  // Preserve this key and the exact inputs if the original response is uncertain.
  const idempotencyKey = process.env.MCPSCRAPER_REDDIT_RETRY_KEY ?? randomUUID()
  const client = new ScraperClient({ apiKey })
  console.log({ idempotencyKey })
  const url = process.argv[2]
  const result = url
    ? await readKnownThread(client, { url, idempotencyKey })
    : await findRecentRooferThreads(client, { idempotencyKey })
  // Discovery returns ranked summaries/questions. Use a selected known URL with
  // readKnownThread when the full comment bodies are the requested result.
  // An artifact envelope preserves the complete result through existing readers.
  console.log({
    delivery: result.delivery?.mode ?? 'inline',
    threadsScraped: result.threadsScraped ?? null,
    partial: result.partial ?? null,
  })
}
