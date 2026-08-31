import { McpToolsClient } from '../packages/memory/dist/index.js'

const apiKey = process.env.MCP_SCRAPER_API_KEY
if (!apiKey) throw new Error('Set MCP_SCRAPER_API_KEY before running this billed example.')
const query = process.env.PAA_QUERY ?? 'commercial truck insurance'
const client = new McpToolsClient({ apiKey })
const result = await client.search.harvestPaa({ query, pages: 2, maxQuestions: 3, gl: 'us', hl: 'en' })
// An unavailable second page still leaves useful first-page PAA evidence.
console.log(JSON.stringify({
  query: result.query,
  questionCount: result.questionCount,
  pagination: result.pagination,
  questions: result.questions,
}, null, 2))
