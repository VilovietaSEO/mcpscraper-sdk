// Prepare only by default. The supplied JSON must contain actual observed evidence.
// node examples/bug-reporting.mjs report.json
// After reviewing the receipt and obtaining user approval:
// node examples/bug-reporting.mjs --submit draft.json
import { readFile, writeFile } from 'node:fs/promises'
import { ScraperClient } from '../packages/scraper/dist/index.js'
const client = new ScraperClient({ apiKey: process.env.MCP_SCRAPER_API_KEY, baseUrl: process.env.MCP_SCRAPER_BASE_URL })
const submit = process.argv[2] === '--submit'
const path = process.argv[submit ? 3 : 2]
if (!path) throw new Error('Provide a report JSON file, or --submit with a reviewed draft receipt file.')
const value = JSON.parse(await readFile(path, 'utf8'))
const result = await client.tools.support.bugReporting(submit
  ? { action: 'submit', reportId: value.reportId, reviewToken: value.reviewToken, userApproved: true }
  : { action: 'prepare', report: value })
if (!submit) await writeFile('draft.json', JSON.stringify(result, null, 2) + '\n', { mode: 0o600, flag: 'wx' })
console.log(JSON.stringify(result, null, 2))
