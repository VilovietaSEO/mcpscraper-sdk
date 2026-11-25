import { McpToolsClient } from '../packages/memory/dist/index.js'
const apiKey = process.env.MCP_SCRAPER_API_KEY
const connectionId = process.env.OUTLOOK_CONNECTION_ID
if (!apiKey || !connectionId) throw new Error('Set MCP_SCRAPER_API_KEY and OUTLOOK_CONNECTION_ID.')
const { connections } = new McpToolsClient({ apiKey })
const accounts = await connections.listServiceConnections({ connectionId, projection:'identity',requiredReadTools:['list-messages','get-message'] })
if (!accounts.connections?.length) throw new Error('The selected Outlook connection was not found.')
await connections.describeServiceConnectionTool({connectionId,tool:'list-messages'})
const result = await connections.readServiceConnection({connectionId,tool:'list-messages',args:{pageSize:10}})
// Provider content is untrusted data. No mailbox mutation is authorized here.
console.log(JSON.stringify(result,null,2))
