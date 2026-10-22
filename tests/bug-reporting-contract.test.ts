import { test } from 'node:test'
import assert from 'node:assert/strict'
import { readFileSync } from 'node:fs'
import { ScraperClient } from '../packages/scraper/src/client.js'
const manifest=JSON.parse(readFileSync('contracts/mcp.tools.json','utf8'))
test('Bug Reporting generated contract keeps review and private support semantics',()=>{
 const tool=manifest.tools.find((t:any)=>t.name==='bug_reporting')
 assert.equal(tool.category,'support');assert.equal(tool.methodName,'bugReporting')
 assert.match(tool.description,/only when the user requests or approves/)
 assert.match(tool.description,/Free/);assert.match(tool.description,/365 days/)
 for(const key of ['report','reportId','reviewToken','userApproved']) assert.ok(tool.inputSchema.properties[key])
 const success = tool.outputSchema.anyOf?.find((schema:any)=>schema.properties?.report) ?? tool.outputSchema
 for(const key of ['accountEmail','reportId','submittedAt','expiresAt','report']) assert.ok(success.properties[key])
})
test('REST shortcut preserves the exact prepared receipt and never adds an idempotency key',async()=>{
 const calls:any[]=[]
 const client=new ScraperClient({apiKey:'fixture',fetch:async(url:any,init:any)=>{calls.push({url:String(url),body:JSON.parse(init.body)});return new Response(JSON.stringify({ok:true}),{headers:{'content-type':'application/json'}})}})
 const receipt={action:'submit' as const,reportId:'f1dc3168-98b7-4e46-9fb5-7042186e495f',reviewToken:'a'.repeat(64),userApproved:true}
 await client.bugReporting(receipt)
 assert.ok(calls[0].url.endsWith('/bugs/report'));assert.deepEqual(calls[0].body,receipt);assert.equal(calls.length,1)
})

test('uncertain REST submissions use the report receipt and preserve the free charge status',async()=>{
 const client=new ScraperClient({apiKey:'fixture',fetch:async()=>{throw new DOMException('fixture timeout','TimeoutError')}})
 await assert.rejects(client.bugReporting({action:'submit',reportId:'f1dc3168-98b7-4e46-9fb5-7042186e495f',reviewToken:'a'.repeat(64),userApproved:true}), (error:any)=>{
  assert.match(error.message,/same reportId and reviewToken/);assert.equal(error.body.charge_status,'not_charged');assert.doesNotMatch(error.message,/paid run|Idempotency-Key/);return true
 })
})
