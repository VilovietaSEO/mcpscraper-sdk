import type { Output as ArtifactDescribeOutput } from './generated/mcp/tools/artifact_describe.js'

/** The delivery alternative from the canonical server contract. */
export type ArtifactDelivery = Extract<ArtifactDescribeOutput, { delivery: { mode: 'artifact' } }>

/** The hosted MCP surface may deliver any convenience call through an artifact. */
export type DeliveredNamespace<Namespace> = {
  [Method in keyof Namespace]: Namespace[Method] extends (...args: infer Args) => Promise<infer Output>
    ? (...args: Args) => Promise<Output | ArtifactDelivery>
    : Namespace[Method]
}
