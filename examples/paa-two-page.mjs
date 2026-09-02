import { randomUUID } from 'node:crypto'
import { ScraperClient } from 'mcpscraper-sdk'

const apiKey = process.env.MCPSCRAPER_API_KEY
if (!apiKey) throw new Error('Set MCPSCRAPER_API_KEY before running this example.')

const client = new ScraperClient({ apiKey })
const idempotencyKey = randomUUID()

// Omit pages (or pass pages: 1) for the default first-page-only behavior.
const started = await client.tools.other.harvestPaaStart({
  query: 'how to choose a roofing contractor',
  location: 'Denver, CO',
  pages: 2,
  maxQuestions: 10,
  idempotencyKey,
})

let status
do {
  await new Promise(resolve => setTimeout(resolve, started.status.pollAfterSeconds * 1_000))
  status = await client.tools.other.harvestPaaStatus({ jobId: started.jobId })
  console.log(status.status.state, status.progress.pagination)
} while (!status.status.terminal)

if (status.status.state !== 'done' || !status.result) {
  throw new Error(`PAA harvest ended with ${status.status.state}`)
}

// pagination is nullable for saved results produced before this contract.
console.log({
  pagination: status.result.pagination,
  organicResults: status.result.organicResults.length,
  questions: status.result.questions.length,
})

// pages: 2 adds a second organic-results page when available. It never starts a
// second PAA graph: every returned PAA question still comes from page one.
