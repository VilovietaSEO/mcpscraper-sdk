import { ScraperClient } from 'mcpscraper-sdk'

const apiKey = process.env.MCP_SCRAPER_API_KEY
const url = process.env.FACEBOOK_PROFILE_URL
if (!apiKey || !url) throw new Error('Set MCP_SCRAPER_API_KEY and FACEBOOK_PROFILE_URL.')

const client = new ScraperClient({ apiKey })
const inventory = await client.tools.facebook.reelsInventory({ url, maxUrls: 20 })
console.log(JSON.stringify(inventory, null, 2))
// Choose a returned items[].url and pass it to client.tools.facebook.videoTranscribe.
// Inspect complete/stoppedReason; public profile collection is non-exhaustive.
// Pass earlier items[].url values in resumeUrls to retain them during another scan.
