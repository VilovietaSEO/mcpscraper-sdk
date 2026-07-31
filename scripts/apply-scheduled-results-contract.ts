import { readFile, writeFile } from 'node:fs/promises'
import { join } from 'node:path'

const ROOT = process.cwd()
const MEMORY_MANIFEST_PATH = join(ROOT, 'contracts/memory.tools.json')
const MCP_MANIFEST_PATH = join(ROOT, 'contracts/mcp.tools.json')
const DRAFT_07 = 'http://json-schema.org/draft-07/schema#'

type JsonSchema = Record<string, any>

interface MemoryTool {
  name: string
  description: string
  category: string
  inputSchema: JsonSchema
  outputSchema: JsonSchema
  legacyId: string
}

interface UnifiedTool {
  name: string
  title: string
  description: string
  category: string
  methodName: string
  inputSchema: JsonSchema
  outputSchema: JsonSchema
  outputSchemaProvided: true
  annotations: Record<string, boolean | string>
}

const stringSchema = (options: JsonSchema = {}): JsonSchema => ({ type: 'string', ...options })
const objectSchema = (
  properties: Record<string, JsonSchema>,
  required: string[] = [],
  options: JsonSchema = {},
): JsonSchema => ({
  type: 'object',
  properties,
  ...(required.length ? { required } : {}),
  additionalProperties: false,
  ...options,
})
const arraySchema = (items: JsonSchema, maxItems?: number): JsonSchema => ({
  type: 'array',
  items,
  ...(maxItems === undefined ? {} : { maxItems }),
})

const uuid = (): JsonSchema => stringSchema({ format: 'uuid' })
const dateTime = (nullable = false): JsonSchema => nullable
  ? { type: ['string', 'null'], format: 'date-time' }
  : stringSchema({ format: 'date-time' })

const scheduledArtifactSelectionSchema = (): JsonSchema => ({
  oneOf: [
    objectSchema({ mode: { const: 'none', type: 'string' } }, ['mode']),
    objectSchema({
      mode: { const: 'saved_template', type: 'string' },
      templateId: uuid(),
      templateVersionId: uuid(),
    }, ['mode', 'templateId', 'templateVersionId']),
  ],
  description: 'No rendered artifact, or one exact immutable saved template version. This does not disable Memory-note output.',
})

const artifactTemplateConfigSchema = (): JsonSchema => objectSchema({
  theme: { type: 'string', enum: ['paper', 'ink', 'warm'] },
  density: { type: 'string', enum: ['comfortable', 'compact'] },
  showSourceRail: { type: 'boolean' },
  showGeneratedAt: { type: 'boolean' },
  brandName: stringSchema({ minLength: 1, maxLength: 80 }),
}, ['theme', 'density', 'showSourceRail', 'showGeneratedAt'])

const artifactTemplateVersionSchema = (): JsonSchema => objectSchema({
  templateVersionId: uuid(),
  templateId: uuid(),
  version: { type: 'integer', minimum: 1 },
  rendererKey: { const: 'editorial_reading_room_v1', type: 'string' },
  rendererVersion: { const: 1, type: 'integer' },
  inputContractVersion: { const: 1, type: 'integer' },
  config: artifactTemplateConfigSchema(),
  authoringInstructions: stringSchema({ maxLength: 4000 }),
  createdAt: dateTime(),
}, [
  'templateVersionId',
  'templateId',
  'version',
  'rendererKey',
  'rendererVersion',
  'inputContractVersion',
  'config',
  'authoringInstructions',
  'createdAt',
])

const artifactTemplateSchema = (): JsonSchema => objectSchema({
  templateId: uuid(),
  name: stringSchema({ minLength: 1, maxLength: 120 }),
  description: stringSchema({ maxLength: 500 }),
  currentVersionId: uuid(),
  status: { type: 'string', enum: ['active', 'archived'] },
  currentVersion: artifactTemplateVersionSchema(),
  versions: arraySchema(artifactTemplateVersionSchema()),
  createdAt: dateTime(),
  updatedAt: dateTime(),
}, ['templateId', 'name', 'description', 'currentVersionId', 'status', 'createdAt', 'updatedAt'])

const scheduledRunNoteOutputSchema = (): JsonSchema => objectSchema({
  vault: stringSchema({ minLength: 1, maxLength: 120 }),
  path: stringSchema({ minLength: 1, maxLength: 1000 }),
  title: stringSchema({ maxLength: 300 }),
  sourceRef: stringSchema({ maxLength: 2000 }),
}, ['vault', 'path'])

const scheduledRunArtifactOutputSchema = (): JsonSchema => objectSchema({
  artifactId: stringSchema({ minLength: 1, maxLength: 1000 }),
  templateId: uuid(),
  templateVersionId: uuid(),
  rendererKey: { const: 'editorial_reading_room_v1', type: 'string' },
  rendererVersion: { const: 1, type: 'integer' },
  mimeType: { const: 'text/html', type: 'string' },
  title: stringSchema({ minLength: 1, maxLength: 300 }),
  bytes: { type: 'integer', minimum: 0, maximum: 2_000_000 },
  sha256: stringSchema({ pattern: '^[a-f0-9]{64}$' }),
  createdAt: dateTime(),
  viewerPath: stringSchema({ pattern: '^/scheduled-actions/runs/' }),
}, [
  'artifactId',
  'templateId',
  'templateVersionId',
  'rendererKey',
  'rendererVersion',
  'mimeType',
  'title',
  'bytes',
  'sha256',
  'createdAt',
  'viewerPath',
])

const scheduledRunResultSchema = (): JsonSchema => objectSchema({
  runId: stringSchema({ minLength: 1, maxLength: 200 }),
  scheduleId: uuid(),
  scheduleDescription: stringSchema({ minLength: 1, maxLength: 20_000 }),
  executionMode: { type: 'string', enum: ['agent', 'connection_sync'] },
  status: {
    type: 'string',
    enum: ['running', 'succeeded', 'no_output', 'partial', 'billing_stopped', 'failed'],
  },
  summary: stringSchema({ maxLength: 2000 }),
  errorCode: { type: ['string', 'null'], maxLength: 120 },
  errorMessage: { type: ['string', 'null'], maxLength: 2000 },
  scheduledFor: dateTime(),
  startedAt: dateTime(),
  completedAt: dateTime(true),
  openedAt: dateTime(true),
  archivedAt: dateTime(true),
  artifactSelection: scheduledArtifactSelectionSchema(),
  noteOutputs: arraySchema(scheduledRunNoteOutputSchema(), 100),
  artifactOutputs: arraySchema(scheduledRunArtifactOutputSchema(), 10),
  createdAt: dateTime(),
  updatedAt: dateTime(),
}, [
  'runId',
  'scheduleId',
  'scheduleDescription',
  'executionMode',
  'status',
  'summary',
  'errorCode',
  'errorMessage',
  'scheduledFor',
  'startedAt',
  'completedAt',
  'openedAt',
  'archivedAt',
  'artifactSelection',
  'noteOutputs',
  'artifactOutputs',
  'createdAt',
  'updatedAt',
])

const apiErrorProperties = (): Record<string, JsonSchema> => ({
  error: stringSchema({ minLength: 1, maxLength: 500 }),
  errorCode: {
    type: 'string',
    enum: [
      'invalid_request',
      'not_found',
      'conflict',
      'template_archived',
      'renderer_unavailable',
      'artifact_unavailable',
      'view_link_unavailable',
      'internal_error',
    ],
  },
  requestId: stringSchema({ maxLength: 200 }),
})

const toolOutputSchema = (
  successProperties: Record<string, JsonSchema>,
  successRequired: string[],
): JsonSchema => ({
  ...objectSchema({
    ok: { type: 'boolean' },
    ...successProperties,
    ...apiErrorProperties(),
  }, ['ok']),
  allOf: [{
    if: { properties: { ok: { const: true } }, required: ['ok'] },
    then: { required: successRequired },
    else: { required: ['error', 'errorCode'] },
  }],
  $schema: DRAFT_07,
})

const createTemplateInputProperties = (): Record<string, JsonSchema> => ({
  presetKey: { const: 'editorial_reading_room_v1', type: 'string' },
  name: stringSchema({ minLength: 1, maxLength: 120 }),
  description: stringSchema({ maxLength: 500, default: '' }),
  config: artifactTemplateConfigSchema(),
  authoringInstructions: stringSchema({ maxLength: 4000 }),
})

const annotations = (title: string, readOnlyHint: boolean): Record<string, boolean | string> => ({
  title,
  readOnlyHint,
  destructiveHint: false,
  idempotentHint: readOnlyHint,
  openWorldHint: false,
})

const toolDefinitions: Array<{
  internalName: string
  name: string
  title: string
  description: string
  methodName: string
  readOnly: boolean
  idempotent?: boolean
  destructive?: boolean
  directMemory?: boolean
  inputSchema: JsonSchema
  outputSchema: JsonSchema
}> = [
  {
    internalName: 'listArtifactTemplatesTool',
    name: 'list_artifact_templates',
    title: 'List Artifact Templates',
    description: 'List approved built-in artifact presets and saved immutable template versions. A preset must be saved before an automation can select it.',
    methodName: 'listArtifactTemplates',
    readOnly: true,
    inputSchema: objectSchema({
      status: { type: 'string', enum: ['active', 'archived', 'all'], default: 'active' },
    }, [], { $schema: DRAFT_07 }),
    outputSchema: toolOutputSchema({
      presets: arraySchema(objectSchema({
        presetKey: { const: 'editorial_reading_room_v1', type: 'string' },
        name: stringSchema(),
        description: stringSchema(),
        defaultConfig: artifactTemplateConfigSchema(),
      }, ['presetKey', 'name', 'description', 'defaultConfig'])),
      templates: arraySchema(artifactTemplateSchema()),
    }, ['ok', 'presets', 'templates']),
  },
  {
    internalName: 'getArtifactTemplateTool',
    name: 'get_artifact_template',
    title: 'Get Artifact Template',
    description: 'Read one saved artifact template and its immutable version history.',
    methodName: 'getArtifactTemplate',
    readOnly: true,
    inputSchema: objectSchema({ templateId: uuid() }, ['templateId'], { $schema: DRAFT_07 }),
    outputSchema: toolOutputSchema({ template: artifactTemplateSchema() }, ['ok', 'template']),
  },
  {
    internalName: 'createArtifactTemplateTool',
    name: 'create_artifact_template',
    title: 'Save Artifact Template',
    description: 'Save the approved Editorial Reading Room preset as a user-owned template version 1. Arbitrary HTML, JavaScript, and executable code are not accepted.',
    methodName: 'createArtifactTemplate',
    readOnly: false,
    inputSchema: objectSchema(
      createTemplateInputProperties(),
      ['presetKey', 'name', 'config', 'authoringInstructions'],
      { $schema: DRAFT_07 },
    ),
    outputSchema: toolOutputSchema({ template: artifactTemplateSchema() }, ['ok', 'template']),
  },
  {
    internalName: 'updateArtifactTemplateTool',
    name: 'update_artifact_template',
    title: 'Create Artifact Template Version',
    description: 'Create the next immutable version of a saved artifact template. Existing automations remain pinned to their exact prior version until explicitly changed.',
    methodName: 'updateArtifactTemplate',
    readOnly: false,
    inputSchema: objectSchema({
      templateId: uuid(),
      name: stringSchema({ minLength: 1, maxLength: 120 }),
      description: stringSchema({ maxLength: 500 }),
      config: artifactTemplateConfigSchema(),
      authoringInstructions: stringSchema({ maxLength: 4000 }),
    }, ['templateId'], {
      minProperties: 2,
      $schema: DRAFT_07,
    }),
    outputSchema: toolOutputSchema({ template: artifactTemplateSchema() }, ['ok', 'template']),
  },
  {
    internalName: 'archiveArtifactTemplateTool',
    name: 'archive_artifact_template',
    title: 'Archive Artifact Template',
    description: 'Archive or restore a caller-owned template identity without deleting immutable versions. Archived templates cannot be selected for a new or changed schedule binding.',
    methodName: 'archiveArtifactTemplate',
    readOnly: false,
    idempotent: true,
    inputSchema: objectSchema({
      templateId: uuid(),
      archived: {
        type: 'boolean',
        description: 'True to archive the template; false to restore it.',
      },
    }, ['templateId', 'archived'], { $schema: DRAFT_07 }),
    outputSchema: toolOutputSchema({ template: artifactTemplateSchema() }, ['ok', 'template']),
  },
  {
    internalName: 'listScheduledRunsTool',
    name: 'list_scheduled_runs',
    title: 'List Scheduled Results',
    description: 'List the scheduled-results inbox, all unarchived results, or archived results. Returns stable opaque run IDs and output pointers without storage-provider URLs.',
    methodName: 'listScheduledRuns',
    readOnly: true,
    inputSchema: objectSchema({
      view: { type: 'string', enum: ['inbox', 'all', 'archived'], default: 'inbox' },
      status: {
        type: 'string',
        enum: ['running', 'succeeded', 'no_output', 'partial', 'billing_stopped', 'failed'],
      },
      scheduleId: uuid(),
      templateId: uuid(),
      from: dateTime(),
      to: dateTime(),
      query: stringSchema({ maxLength: 200 }),
      cursor: stringSchema({ maxLength: 2000 }),
      limit: { type: 'integer', minimum: 1, maximum: 100, default: 30 },
    }, [], { $schema: DRAFT_07 }),
    outputSchema: toolOutputSchema({
      items: arraySchema(scheduledRunResultSchema()),
      nextCursor: { type: ['string', 'null'], maxLength: 2000 },
    }, ['ok', 'items', 'nextCursor']),
  },
  {
    internalName: 'getScheduledRunTool',
    name: 'get_scheduled_run',
    title: 'Get Scheduled Result',
    description: 'Read complete metadata and durable output pointers for one opaque scheduled run ID.',
    methodName: 'getScheduledRun',
    readOnly: true,
    inputSchema: objectSchema({
      runId: stringSchema({ minLength: 1, maxLength: 200 }),
    }, ['runId'], { $schema: DRAFT_07 }),
    outputSchema: toolOutputSchema({ run: scheduledRunResultSchema() }, ['ok', 'run']),
  },
  {
    internalName: 'markScheduledRunOpenedTool',
    name: 'mark_scheduled_run_opened',
    title: 'Mark Scheduled Result Opened',
    description: 'Idempotently mark one owner-scoped scheduled result opened.',
    methodName: 'markScheduledRunOpened',
    readOnly: false,
    idempotent: true,
    inputSchema: objectSchema({
      runId: stringSchema({ minLength: 1, maxLength: 200 }),
    }, ['runId'], { $schema: DRAFT_07 }),
    outputSchema: toolOutputSchema({ run: scheduledRunResultSchema() }, ['ok', 'run']),
  },
  {
    internalName: 'markScheduledRunUnopenedTool',
    name: 'mark_scheduled_run_unopened',
    title: 'Mark Scheduled Result Unopened',
    description: 'Idempotently return one owner-scoped scheduled result to the unopened inbox.',
    methodName: 'markScheduledRunUnopened',
    readOnly: false,
    idempotent: true,
    inputSchema: objectSchema({
      runId: stringSchema({ minLength: 1, maxLength: 200 }),
    }, ['runId'], { $schema: DRAFT_07 }),
    outputSchema: toolOutputSchema({ run: scheduledRunResultSchema() }, ['ok', 'run']),
  },
  {
    internalName: 'archiveScheduledRunTool',
    name: 'archive_scheduled_run',
    title: 'Archive Scheduled Result',
    description: 'Archive or restore one owner-scoped scheduled result without deleting its outputs.',
    methodName: 'archiveScheduledRun',
    readOnly: false,
    idempotent: true,
    inputSchema: objectSchema({
      runId: stringSchema({ minLength: 1, maxLength: 200 }),
      archived: {
        type: 'boolean',
        description: 'True to archive the result; false to restore it.',
      },
    }, ['runId', 'archived'], { $schema: DRAFT_07 }),
    outputSchema: toolOutputSchema({ run: scheduledRunResultSchema() }, ['ok', 'run']),
  },
  {
    internalName: 'createScheduledRunViewLinkTool',
    name: 'create_scheduled_run_view_link',
    title: 'Create Scheduled Result View Link',
    description: 'Create a revocable, read-only bearer URL for exactly one artifact. The URL is returned once. It expires after 7 days by default and at most 30 days. Anyone holding it can view that artifact.',
    methodName: 'createScheduledRunViewLink',
    readOnly: false,
    directMemory: false,
    inputSchema: objectSchema({
      runId: stringSchema({ minLength: 1, maxLength: 200 }),
      artifactId: stringSchema({ minLength: 1, maxLength: 1000 }),
      expiresInDays: { type: 'integer', minimum: 1, maximum: 30, default: 7 },
    }, ['runId', 'artifactId'], { $schema: DRAFT_07 }),
    outputSchema: toolOutputSchema({
      shareId: uuid(),
      runId: stringSchema({ minLength: 1, maxLength: 200 }),
      artifactId: stringSchema({ minLength: 1, maxLength: 1000 }),
      url: stringSchema({ format: 'uri' }),
      expiresAt: dateTime(),
      createdAt: dateTime(),
    }, ['ok', 'shareId', 'runId', 'artifactId', 'url', 'expiresAt', 'createdAt']),
  },
  {
    internalName: 'revokeScheduledRunViewLinkTool',
    name: 'revoke_scheduled_run_view_link',
    title: 'Revoke Scheduled Result View Link',
    description: 'Immediately revoke one view link owned by the caller.',
    methodName: 'revokeScheduledRunViewLink',
    readOnly: false,
    idempotent: true,
    destructive: true,
    directMemory: false,
    inputSchema: objectSchema({
      runId: stringSchema({ minLength: 1, maxLength: 200 }),
      shareId: uuid(),
    }, ['runId', 'shareId'], { $schema: DRAFT_07 }),
    outputSchema: toolOutputSchema({
      revoked: { const: true, type: 'boolean' },
    }, ['ok', 'revoked']),
  },
]

function addArtifactSelection(tool: MemoryTool | UnifiedTool): void {
  const inputProperties = tool.inputSchema.properties as Record<string, JsonSchema> | undefined
  if (inputProperties) {
    inputProperties.artifactSelection = {
      ...scheduledArtifactSelectionSchema(),
      default: { mode: 'none' },
    }
  }

  const outputProperties = tool.outputSchema.properties as Record<string, JsonSchema> | undefined
  if (!outputProperties) return

  if (tool.name === 'createScheduledActionTool' || tool.name === 'create-scheduled-action') {
    outputProperties.artifactSelection = scheduledArtifactSelectionSchema()
    const required = new Set<string>(tool.outputSchema.required ?? [])
    required.add('artifactSelection')
    tool.outputSchema.required = [...required]
  }

  const actionProperties = outputProperties.action?.properties as Record<string, JsonSchema> | undefined
  if (actionProperties) {
    actionProperties.artifactSelection = scheduledArtifactSelectionSchema()
    const required = new Set<string>(outputProperties.action.required ?? [])
    required.add('artifactSelection')
    outputProperties.action.required = [...required]
  }

  const selectionDescription = 'Artifact selection defaults to No artifact, which disables only rendered HTML and does not disable Memory-note writing; a saved template binding always pins one exact immutable version.'
  if (!tool.description.includes(selectionDescription)) {
    tool.description = `${tool.description} ${selectionDescription}`
  }
}

function upsert<T extends { name: string }>(tools: T[], entry: T): void {
  const index = tools.findIndex(tool => tool.name === entry.name)
  if (index === -1) tools.push(entry)
  else tools[index] = entry
}

async function main(): Promise<void> {
  const check = process.argv.includes('--check')
  const memoryManifest = JSON.parse(await readFile(MEMORY_MANIFEST_PATH, 'utf8'))
  const unifiedManifest = JSON.parse(await readFile(MCP_MANIFEST_PATH, 'utf8'))

  for (const toolName of ['createScheduledActionTool', 'updateScheduledActionTool']) {
    const tool = memoryManifest.tools.find((candidate: MemoryTool) => candidate.name === toolName)
    if (!tool) throw new Error(`Missing direct Memory tool ${toolName}`)
    addArtifactSelection(tool)
  }

  if (!unifiedManifest.tools.some((tool: UnifiedTool) => tool.name === 'update-scheduled-action')) {
    const memoryTool = memoryManifest.tools.find(
      (tool: MemoryTool) => tool.name === 'updateScheduledActionTool',
    ) as MemoryTool | undefined
    if (!memoryTool) throw new Error('Missing direct Memory updateScheduledActionTool')
    const { apiKey: _apiKey, sessionId: _sessionId, ...publicProperties } =
      memoryTool.inputSchema.properties as Record<string, JsonSchema>
    upsert(unifiedManifest.tools, {
      name: 'update-scheduled-action',
      title: 'Update Scheduled Action',
      description: memoryTool.description,
      category: 'schedule',
      methodName: 'updateScheduledAction',
      inputSchema: {
        ...memoryTool.inputSchema,
        properties: publicProperties,
      },
      outputSchema: memoryTool.outputSchema,
      outputSchemaProvided: true,
      annotations: annotations('Update Scheduled Action', false),
    } satisfies UnifiedTool)
  }
  for (const toolName of ['create-scheduled-action', 'update-scheduled-action']) {
    const tool = unifiedManifest.tools.find((candidate: UnifiedTool) => candidate.name === toolName)
    if (tool) addArtifactSelection(tool)
  }

  for (const definition of toolDefinitions) {
    const directMemoryInputSchema = structuredClone(definition.inputSchema)
    directMemoryInputSchema.properties = {
      apiKey: stringSchema({
        description: 'Caller API key (Bearer secret). Optional when the MCP session is already authenticated.',
      }),
      sessionId: stringSchema({
        description: 'Session identifier. Optional; defaults to the current MCP session.',
      }),
      ...directMemoryInputSchema.properties,
    }
    if (definition.directMemory === false) {
      memoryManifest.tools = memoryManifest.tools.filter(
        (tool: MemoryTool) => tool.name !== definition.internalName,
      )
    } else {
      const memoryTool: MemoryTool = {
        name: definition.internalName,
        description: definition.description,
        category: 'schedule',
        inputSchema: directMemoryInputSchema,
        outputSchema: definition.outputSchema,
        legacyId: definition.name,
      }
      upsert(memoryManifest.tools, memoryTool)
    }
    const unifiedTool: UnifiedTool = {
      name: definition.name,
      title: definition.title,
      description: definition.description,
      category: 'schedule',
      methodName: definition.methodName,
      inputSchema: definition.inputSchema,
      outputSchema: definition.outputSchema,
      outputSchemaProvided: true,
      annotations: {
        ...annotations(definition.title, definition.readOnly),
        destructiveHint: definition.destructive ?? false,
        idempotentHint: definition.idempotent ?? definition.readOnly,
      },
    }
    upsert(unifiedManifest.tools, unifiedTool)
  }

  memoryManifest.toolCount = memoryManifest.tools.length
  unifiedManifest.toolCount = unifiedManifest.tools.length

  const nextMemory = `${JSON.stringify(memoryManifest, null, 2)}\n`
  const nextUnified = `${JSON.stringify(unifiedManifest, null, 2)}\n`
  const currentMemory = await readFile(MEMORY_MANIFEST_PATH, 'utf8')
  const currentUnified = await readFile(MCP_MANIFEST_PATH, 'utf8')
  const changed = nextMemory !== currentMemory || nextUnified !== currentUnified

  if (check && changed) {
    throw new Error('Scheduled-results contract drift detected. Run npm run apply:scheduled-results-contract.')
  }
  if (!check) {
    await writeFile(MEMORY_MANIFEST_PATH, nextMemory)
    await writeFile(MCP_MANIFEST_PATH, nextUnified)
  }
  console.log(`${check ? 'Checked' : 'Applied'} 12 scheduled-results tools; direct=${memoryManifest.toolCount}, unified=${unifiedManifest.toolCount}.`)
}

main().catch(error => {
  console.error(error)
  process.exitCode = 1
})
