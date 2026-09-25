import { randomUUID } from 'node:crypto'
import { ScraperClient } from 'mcpscraper-sdk'

const apiKey = process.env.MCPSCRAPER_API_KEY
if (!apiKey) throw new Error('Set MCPSCRAPER_API_KEY before running this example.')

const client = new ScraperClient({ apiKey })
let result = await client.tools.maps.placeIntel({
  businessName: 'Pride Roofing and Construction',
  location: 'Loveland, CO',
  include: ['all'],
  maxReviews: 50,
  maxImages: 10,
  maxInlineImages: 0,
})

if (!result.runId) throw new Error('Maps did not return a recoverable run ID.')
for (let poll = 0; poll < 120 && ['queued', 'running', 'interrupted'].includes(result.runStatus); poll += 1) {
  await new Promise(resolve => setTimeout(resolve, 5_000))
  result = await client.tools.maps.placeStatus({ runId: result.runId })
  console.log(result.runStatus, result.checkpointRevision, result.reviewsCollected)
}

if (result.runStatus === 'partial' && process.env.MAPS_RESUME === '1') {
  result = await client.tools.maps.placeResume({
    runId: result.runId,
    resumeIdempotencyKey: randomUUID(),
  })
}

console.log({
  runId: result.runId,
  status: result.runStatus,
  verified: result.verified,
  name: result.name,
  services: result.services?.length ?? 0,
  areasServed: result.areasServed?.length ?? 0,
  reviewsSaved: result.reviewsCollected ?? 0,
  imagesSaved: result.imagesCollected ?? 0,
  pendingFields: result.pendingFields ?? [],
  imageZip: result.media?.artifact?.downloadUrl ?? null,
})
