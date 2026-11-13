import type { MemoryClient, MemoryNamespace, ArtifactDelivery } from '../../src/index.js'
import type { CrmNamespace, ResearchNamespace } from '../../src/generated/direct/methods.js'

type Expect<Condition extends true> = Condition
type Equal<Left, Right> = (<T>() => T extends Left ? 1 : 2) extends (<T>() => T extends Right ? 1 : 2) ? true : false

type SearchResult = Awaited<ReturnType<MemoryClient['memory']['search']>>
type PersonCaptureResult = Awaited<ReturnType<MemoryClient['research']['personCapture']>>
type PersonUpsertResult = Awaited<ReturnType<MemoryClient['crm']['personUpsert']>>
type SearchSupportsDelivery = Expect<ArtifactDelivery extends SearchResult ? true : false>
type ResearchSupportsDelivery = Expect<ArtifactDelivery extends PersonCaptureResult ? true : false>
type CrmSupportsDelivery = Expect<ArtifactDelivery extends PersonUpsertResult ? true : false>
type SearchInputUnchanged = Expect<Equal<Parameters<MemoryClient['memory']['search']>, Parameters<MemoryNamespace['search']>>>
type ResearchInputUnchanged = Expect<Equal<Parameters<MemoryClient['research']['personCapture']>, Parameters<ResearchNamespace['personCapture']>>>
type CrmInputUnchanged = Expect<Equal<Parameters<MemoryClient['crm']['personUpsert']>, Parameters<CrmNamespace['personUpsert']>>>

function inspectSearch(result: SearchResult): string | undefined {
  if ('delivery' in result) return result.delivery.nextAction
  return result.results?.[0]?.text
}

export type { SearchSupportsDelivery, ResearchSupportsDelivery, CrmSupportsDelivery, SearchInputUnchanged, ResearchInputUnchanged, CrmInputUnchanged }
export { inspectSearch }
