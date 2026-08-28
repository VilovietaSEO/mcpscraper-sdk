export { MemoryClient } from './client.js'
export type { MemoryClientOptions } from './client.js'
export type {
  AssistantApprovalDecision,
  AssistantCommand,
  AssistantCursor,
  AssistantIdempotencyKey,
  AssistantPageRequest,
} from './assistant.js'
export { MemoryApiError } from './errors.js'
export type { MemoryApiErrorDetails } from './errors.js'
export {
  AccessNamespace,
  CaptureNamespace,
  ChannelsNamespace,
  FactsNamespace,
  FilesNamespace,
  GraphNamespace,
  LibraryNamespace,
  MemoryNamespace,
  RecallNamespace,
  ScheduleNamespace,
  StorageNamespace,
  TablesNamespace,
  TagsNamespace,
  VaultsNamespace,
  VideoNamespace,
  WebhooksNamespace,
} from './generated/methods.js'
export { AssistantNamespace } from './generated/direct/methods.js'
export type { CallToolFn } from './generated/methods.js'
export { McpToolsClient, McpToolError } from './mcp-client.js'
export type { McpToolsClientOptions, McpToolDescriptor, McpToolErrorDetails, McpContentBlock, McpToolCallResult } from './mcp-client.js'
export {
  MCP_TOOL_BINDINGS,
  MCP_TOOL_COUNT,
  GeneratedMcpToolsClient,
} from './generated/mcp/methods.js'
