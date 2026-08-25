import assert from 'node:assert/strict'
import test from 'node:test'
import { stripInternalTelemetry } from '../scripts/mcp-contract-telemetry.js'

test('removes internal attempt telemetry from properties and required recursively', () => {
  const projected = stripInternalTelemetry({
    type: 'object',
    properties: {
      results: { type: 'array' },
      attempts: {
        type: 'array',
        items: {
          type: 'object',
          properties: {
            attemptNumber: { type: 'integer' },
            outcome: { type: 'string' },
          },
          required: ['attemptNumber', 'outcome'],
        },
      },
      nested: {
        type: 'object',
        properties: {
          observedIp: { type: 'string' },
          publicStatus: { type: 'string' },
        },
        required: ['observedIp', 'publicStatus'],
      },
    },
    required: ['results', 'attempts', 'nested'],
  })

  assert.deepEqual(projected, {
    type: 'object',
    properties: {
      results: { type: 'array' },
      nested: {
        type: 'object',
        properties: { publicStatus: { type: 'string' } },
        required: ['publicStatus'],
      },
    },
    required: ['results', 'nested'],
  })
})
