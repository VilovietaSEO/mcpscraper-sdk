export type CallToolFn = (name: string, args: unknown) => Promise<unknown>

import * as AccessIssueKey from './tools/access-issue-key.js'
import * as AccessListKeys from './tools/access-list-keys.js'
import * as AccessRevokeKey from './tools/access-revoke-key.js'
import * as AccessSetScope from './tools/access-set-scope.js'
import * as AccessShareVault from './tools/access-share-vault.js'
import * as AccessSwapVault from './tools/access-swap-vault.js'
import * as AccessInviteAccount from './tools/access-invite-account.js'
import * as AccessSwitchAccount from './tools/access-switch-account.js'
import * as AccessApproveSender from './tools/access-approve-sender.js'
import * as AccessRemoveApprovedSender from './tools/access-remove-approved-sender.js'
import * as AccessListApprovedSenders from './tools/access-list-approved-senders.js'
import * as AccessInboxSettings from './tools/access-inbox-settings.js'
import * as AccessShareNote from './tools/access-share-note.js'
import * as AccessNoteInbox from './tools/access-note-inbox.js'
import * as AccessAcceptShare from './tools/access-accept-share.js'
import * as AccessDeclineShare from './tools/access-decline-share.js'
import * as AccessUnlinkShare from './tools/access-unlink-share.js'
import * as AccessRevokeShare from './tools/access-revoke-share.js'
import * as GetChatLink from './tools/get-chat-link.js'
import * as RevokeChatLink from './tools/revoke-chat-link.js'
import * as SetAgentIdentity from './tools/set-agent-identity.js'
import * as ListSharedWithMe from './tools/list-shared-with-me.js'
import * as ListVaults from './tools/list-vaults.js'
import * as AddVault from './tools/add-vault.js'
import * as CreateSecureVault from './tools/create-secure-vault.js'
import * as DeleteVault from './tools/delete-vault.js'
import * as ProvisionDefaults from './tools/provision-defaults.js'
import * as GetVaultContract from './tools/get-vault-contract.js'
import * as RouteMemory from './tools/route-memory.js'
import * as CreateChannel from './tools/create-channel.js'
import * as PostMessage from './tools/post-message.js'
import * as ReplyMessage from './tools/reply-message.js'
import * as ListChannelMessages from './tools/list-channel-messages.js'
import * as ReactMessage from './tools/react-message.js'
import * as MyMentions from './tools/my-mentions.js'
import * as ListChannelMembers from './tools/list-channel-members.js'
import * as RemoveChannelMember from './tools/remove-channel-member.js'
import * as PollChannel from './tools/poll-channel.js'
import * as GetMessageNote from './tools/get-message-note.js'
import * as MemoryQuestions from './tools/memory-questions.js'
import * as PrepareMemoryWrite from './tools/prepare-memory-write.js'
import * as ValidateMemoryWrite from './tools/validate-memory-write.js'
import * as MemoryCapture from './tools/memory-capture.js'
import * as LibraryIngest from './tools/library-ingest.js'
import * as MemoryExport from './tools/memory-export.js'
import * as MemoryGet from './tools/memory-get.js'
import * as MemoryList from './tools/memory-list.js'
import * as MemoryPut from './tools/memory-put.js'
import * as MemorySearch from './tools/memory-search.js'
import * as MemorySuggest from './tools/memory-suggest.js'
import * as MemoryUpload from './tools/memory-upload.js'
import * as DeleteNote from './tools/delete-note.js'
import * as TableCreate from './tools/table-create.js'
import * as TableList from './tools/table-list.js'
import * as TableDescribe from './tools/table-describe.js'
import * as TableInsertRows from './tools/table-insert-rows.js'
import * as TableQuery from './tools/table-query.js'
import * as TableDeleteRows from './tools/table-delete-rows.js'
import * as TableDrop from './tools/table-drop.js'
import * as TemporalRecall from './tools/temporal-recall.js'
import * as ListMemoryTags from './tools/list-memory-tags.js'
import * as ResolveMemoryTags from './tools/resolve-memory-tags.js'
import * as UpsertMemoryTag from './tools/upsert-memory-tag.js'
import * as MemoryBacklinks from './tools/memory-backlinks.js'
import * as MemoryGraphUniverse from './tools/memory-graph-universe.js'
import * as MemoryGraphPath from './tools/memory-graph-path.js'
import * as RecordFact from './tools/record-fact.js'
import * as FactHistory from './tools/fact-history.js'
import * as StorageUsage from './tools/storage-usage.js'
import * as CostUsage from './tools/cost-usage.js'
import * as CreateScheduledAction from './tools/create-scheduled-action.js'
import * as ListScheduledActions from './tools/list-scheduled-actions.js'
import * as PauseScheduledAction from './tools/pause-scheduled-action.js'
import * as ResumeScheduledAction from './tools/resume-scheduled-action.js'
import * as DeleteScheduledAction from './tools/delete-scheduled-action.js'
import * as SetScheduleEntitlement from './tools/set-schedule-entitlement.js'
import * as GetScheduleStatus from './tools/get-schedule-status.js'
import * as ProposeScheduledAction from './tools/propose-scheduled-action.js'
import * as GetScheduleLink from './tools/get-schedule-link.js'
import * as RevokeScheduleLink from './tools/revoke-schedule-link.js'
import * as CreateWebhook from './tools/create-webhook.js'
import * as ListWebhooks from './tools/list-webhooks.js'
import * as RevokeWebhook from './tools/revoke-webhook.js'
import * as VideoAnalyzeStart from './tools/video-analyze-start.js'
import * as VideoAnalyzeStatus from './tools/video-analyze-status.js'

export class AccessNamespace {
  constructor(private readonly callTool: CallToolFn) {}

  async issueKey(input: AccessIssueKey.Input): Promise<AccessIssueKey.Output> {
    return this.callTool('issueKeyTool', input) as Promise<AccessIssueKey.Output>
  }

  async listKeys(input: AccessListKeys.Input): Promise<AccessListKeys.Output> {
    return this.callTool('listKeysTool', input) as Promise<AccessListKeys.Output>
  }

  async revokeKey(input: AccessRevokeKey.Input): Promise<AccessRevokeKey.Output> {
    return this.callTool('revokeKeyTool', input) as Promise<AccessRevokeKey.Output>
  }

  async setScope(input: AccessSetScope.Input): Promise<AccessSetScope.Output> {
    return this.callTool('setScopeTool', input) as Promise<AccessSetScope.Output>
  }

  async shareVault(input: AccessShareVault.Input): Promise<AccessShareVault.Output> {
    return this.callTool('shareVaultTool', input) as Promise<AccessShareVault.Output>
  }

  async swapVault(input: AccessSwapVault.Input): Promise<AccessSwapVault.Output> {
    return this.callTool('swapVaultTool', input) as Promise<AccessSwapVault.Output>
  }

  async inviteAccount(input: AccessInviteAccount.Input): Promise<AccessInviteAccount.Output> {
    return this.callTool('inviteAccountTool', input) as Promise<AccessInviteAccount.Output>
  }

  async switchAccount(input: AccessSwitchAccount.Input): Promise<AccessSwitchAccount.Output> {
    return this.callTool('switchAccountTool', input) as Promise<AccessSwitchAccount.Output>
  }

  async approveSender(input: AccessApproveSender.Input): Promise<AccessApproveSender.Output> {
    return this.callTool('approveSenderTool', input) as Promise<AccessApproveSender.Output>
  }

  async removeApprovedSender(input: AccessRemoveApprovedSender.Input): Promise<AccessRemoveApprovedSender.Output> {
    return this.callTool('removeApprovedSenderTool', input) as Promise<AccessRemoveApprovedSender.Output>
  }

  async listApprovedSenders(input: AccessListApprovedSenders.Input): Promise<AccessListApprovedSenders.Output> {
    return this.callTool('listApprovedSendersTool', input) as Promise<AccessListApprovedSenders.Output>
  }

  async inboxSettings(input: AccessInboxSettings.Input): Promise<AccessInboxSettings.Output> {
    return this.callTool('inboxSettingsTool', input) as Promise<AccessInboxSettings.Output>
  }

  async shareNote(input: AccessShareNote.Input): Promise<AccessShareNote.Output> {
    return this.callTool('shareNoteTool', input) as Promise<AccessShareNote.Output>
  }

  async noteInbox(input: AccessNoteInbox.Input): Promise<AccessNoteInbox.Output> {
    return this.callTool('noteInboxTool', input) as Promise<AccessNoteInbox.Output>
  }

  async acceptShare(input: AccessAcceptShare.Input): Promise<AccessAcceptShare.Output> {
    return this.callTool('acceptShareTool', input) as Promise<AccessAcceptShare.Output>
  }

  async declineShare(input: AccessDeclineShare.Input): Promise<AccessDeclineShare.Output> {
    return this.callTool('declineShareTool', input) as Promise<AccessDeclineShare.Output>
  }

  async unlinkShare(input: AccessUnlinkShare.Input): Promise<AccessUnlinkShare.Output> {
    return this.callTool('unlinkShareTool', input) as Promise<AccessUnlinkShare.Output>
  }

  async revokeShare(input: AccessRevokeShare.Input): Promise<AccessRevokeShare.Output> {
    return this.callTool('revokeShareTool', input) as Promise<AccessRevokeShare.Output>
  }

  async getChatLink(input: GetChatLink.Input): Promise<GetChatLink.Output> {
    return this.callTool('getChatLinkTool', input) as Promise<GetChatLink.Output>
  }

  async revokeChatLink(input: RevokeChatLink.Input): Promise<RevokeChatLink.Output> {
    return this.callTool('revokeChatLinkTool', input) as Promise<RevokeChatLink.Output>
  }

  async setAgentIdentity(input: SetAgentIdentity.Input): Promise<SetAgentIdentity.Output> {
    return this.callTool('setAgentIdentityTool', input) as Promise<SetAgentIdentity.Output>
  }
}

export class VaultsNamespace {
  constructor(private readonly callTool: CallToolFn) {}

  async listSharedWithMe(input: ListSharedWithMe.Input): Promise<ListSharedWithMe.Output> {
    return this.callTool('listSharedWithMeTool', input) as Promise<ListSharedWithMe.Output>
  }

  async listVaults(input: ListVaults.Input): Promise<ListVaults.Output> {
    return this.callTool('listVaultsTool', input) as Promise<ListVaults.Output>
  }

  async addVault(input: AddVault.Input): Promise<AddVault.Output> {
    return this.callTool('addVaultTool', input) as Promise<AddVault.Output>
  }

  async createSecureVault(input: CreateSecureVault.Input): Promise<CreateSecureVault.Output> {
    return this.callTool('createSecureVaultTool', input) as Promise<CreateSecureVault.Output>
  }

  async deleteVault(input: DeleteVault.Input): Promise<DeleteVault.Output> {
    return this.callTool('deleteVaultTool', input) as Promise<DeleteVault.Output>
  }

  async provisionDefaults(input: ProvisionDefaults.Input): Promise<ProvisionDefaults.Output> {
    return this.callTool('provisionDefaultsTool', input) as Promise<ProvisionDefaults.Output>
  }

  async getVaultContract(input: GetVaultContract.Input): Promise<GetVaultContract.Output> {
    return this.callTool('getVaultContractTool', input) as Promise<GetVaultContract.Output>
  }

  async routeMemory(input: RouteMemory.Input): Promise<RouteMemory.Output> {
    return this.callTool('routeMemoryTool', input) as Promise<RouteMemory.Output>
  }
}

export class ChannelsNamespace {
  constructor(private readonly callTool: CallToolFn) {}

  async createChannel(input: CreateChannel.Input): Promise<CreateChannel.Output> {
    return this.callTool('createChannelTool', input) as Promise<CreateChannel.Output>
  }

  async postMessage(input: PostMessage.Input): Promise<PostMessage.Output> {
    return this.callTool('postMessageTool', input) as Promise<PostMessage.Output>
  }

  async replyMessage(input: ReplyMessage.Input): Promise<ReplyMessage.Output> {
    return this.callTool('replyMessageTool', input) as Promise<ReplyMessage.Output>
  }

  async listChannelMessages(input: ListChannelMessages.Input): Promise<ListChannelMessages.Output> {
    return this.callTool('listChannelMessagesTool', input) as Promise<ListChannelMessages.Output>
  }

  async reactMessage(input: ReactMessage.Input): Promise<ReactMessage.Output> {
    return this.callTool('reactMessageTool', input) as Promise<ReactMessage.Output>
  }

  async myMentions(input: MyMentions.Input): Promise<MyMentions.Output> {
    return this.callTool('myMentionsTool', input) as Promise<MyMentions.Output>
  }

  async listChannelMembers(input: ListChannelMembers.Input): Promise<ListChannelMembers.Output> {
    return this.callTool('listChannelMembersTool', input) as Promise<ListChannelMembers.Output>
  }

  async removeChannelMember(input: RemoveChannelMember.Input): Promise<RemoveChannelMember.Output> {
    return this.callTool('removeChannelMemberTool', input) as Promise<RemoveChannelMember.Output>
  }

  async pollChannel(input: PollChannel.Input): Promise<PollChannel.Output> {
    return this.callTool('pollChannelTool', input) as Promise<PollChannel.Output>
  }

  async getMessageNote(input: GetMessageNote.Input): Promise<GetMessageNote.Output> {
    return this.callTool('getMessageNoteTool', input) as Promise<GetMessageNote.Output>
  }
}

export class CaptureNamespace {
  constructor(private readonly callTool: CallToolFn) {}

  async memoryQuestions(input: MemoryQuestions.Input): Promise<MemoryQuestions.Output> {
    return this.callTool('memoryQuestionsTool', input) as Promise<MemoryQuestions.Output>
  }

  async prepareMemoryWrite(input: PrepareMemoryWrite.Input): Promise<PrepareMemoryWrite.Output> {
    return this.callTool('prepareMemoryWriteTool', input) as Promise<PrepareMemoryWrite.Output>
  }

  async validateMemoryWrite(input: ValidateMemoryWrite.Input): Promise<ValidateMemoryWrite.Output> {
    return this.callTool('validateMemoryWriteTool', input) as Promise<ValidateMemoryWrite.Output>
  }

  async memoryCapture(input: MemoryCapture.Input): Promise<MemoryCapture.Output> {
    return this.callTool('memoryCaptureTool', input) as Promise<MemoryCapture.Output>
  }
}

export class LibraryNamespace {
  constructor(private readonly callTool: CallToolFn) {}

  async ingest(input: LibraryIngest.Input): Promise<LibraryIngest.Output> {
    return this.callTool('libraryIngestTool', input) as Promise<LibraryIngest.Output>
  }
}

export class MemoryNamespace {
  constructor(private readonly callTool: CallToolFn) {}

  async export(input: MemoryExport.Input): Promise<MemoryExport.Output> {
    return this.callTool('exportTool', input) as Promise<MemoryExport.Output>
  }

  async get(input: MemoryGet.Input): Promise<MemoryGet.Output> {
    return this.callTool('getTool', input) as Promise<MemoryGet.Output>
  }

  async list(input: MemoryList.Input): Promise<MemoryList.Output> {
    return this.callTool('listTool', input) as Promise<MemoryList.Output>
  }

  async put(input: MemoryPut.Input): Promise<MemoryPut.Output> {
    return this.callTool('putTool', input) as Promise<MemoryPut.Output>
  }

  async search(input: MemorySearch.Input): Promise<MemorySearch.Output> {
    return this.callTool('searchTool', input) as Promise<MemorySearch.Output>
  }

  async suggest(input: MemorySuggest.Input): Promise<MemorySuggest.Output> {
    return this.callTool('suggestTool', input) as Promise<MemorySuggest.Output>
  }

  async upload(input: MemoryUpload.Input): Promise<MemoryUpload.Output> {
    return this.callTool('uploadTool', input) as Promise<MemoryUpload.Output>
  }

  async deleteNote(input: DeleteNote.Input): Promise<DeleteNote.Output> {
    return this.callTool('deleteNoteTool', input) as Promise<DeleteNote.Output>
  }
}

export class TablesNamespace {
  constructor(private readonly callTool: CallToolFn) {}

  async create(input: TableCreate.Input): Promise<TableCreate.Output> {
    return this.callTool('createTableTool', input) as Promise<TableCreate.Output>
  }

  async list(input: TableList.Input): Promise<TableList.Output> {
    return this.callTool('listTablesTool', input) as Promise<TableList.Output>
  }

  async describe(input: TableDescribe.Input): Promise<TableDescribe.Output> {
    return this.callTool('describeTableTool', input) as Promise<TableDescribe.Output>
  }

  async insertRows(input: TableInsertRows.Input): Promise<TableInsertRows.Output> {
    return this.callTool('insertTableRowsTool', input) as Promise<TableInsertRows.Output>
  }

  async query(input: TableQuery.Input): Promise<TableQuery.Output> {
    return this.callTool('queryTableTool', input) as Promise<TableQuery.Output>
  }

  async deleteRows(input: TableDeleteRows.Input): Promise<TableDeleteRows.Output> {
    return this.callTool('deleteTableRowsTool', input) as Promise<TableDeleteRows.Output>
  }

  async drop(input: TableDrop.Input): Promise<TableDrop.Output> {
    return this.callTool('dropTableTool', input) as Promise<TableDrop.Output>
  }
}

export class RecallNamespace {
  constructor(private readonly callTool: CallToolFn) {}

  async temporalRecall(input: TemporalRecall.Input): Promise<TemporalRecall.Output> {
    return this.callTool('temporalRecallTool', input) as Promise<TemporalRecall.Output>
  }
}

export class TagsNamespace {
  constructor(private readonly callTool: CallToolFn) {}

  async listMemoryTags(input: ListMemoryTags.Input): Promise<ListMemoryTags.Output> {
    return this.callTool('listTagsTool', input) as Promise<ListMemoryTags.Output>
  }

  async resolveMemoryTags(input: ResolveMemoryTags.Input): Promise<ResolveMemoryTags.Output> {
    return this.callTool('resolveTagsTool', input) as Promise<ResolveMemoryTags.Output>
  }

  async upsertMemoryTag(input: UpsertMemoryTag.Input): Promise<UpsertMemoryTag.Output> {
    return this.callTool('upsertTagTool', input) as Promise<UpsertMemoryTag.Output>
  }
}

export class GraphNamespace {
  constructor(private readonly callTool: CallToolFn) {}

  async memoryBacklinks(input: MemoryBacklinks.Input): Promise<MemoryBacklinks.Output> {
    return this.callTool('noteBacklinksTool', input) as Promise<MemoryBacklinks.Output>
  }

  async memoryGraphUniverse(input: MemoryGraphUniverse.Input): Promise<MemoryGraphUniverse.Output> {
    return this.callTool('graphUniverseTool', input) as Promise<MemoryGraphUniverse.Output>
  }

  async memoryGraphPath(input: MemoryGraphPath.Input): Promise<MemoryGraphPath.Output> {
    return this.callTool('graphPathTool', input) as Promise<MemoryGraphPath.Output>
  }
}

export class FactsNamespace {
  constructor(private readonly callTool: CallToolFn) {}

  async recordFact(input: RecordFact.Input): Promise<RecordFact.Output> {
    return this.callTool('recordFactTool', input) as Promise<RecordFact.Output>
  }

  async history(input: FactHistory.Input): Promise<FactHistory.Output> {
    return this.callTool('factHistoryTool', input) as Promise<FactHistory.Output>
  }
}

export class StorageNamespace {
  constructor(private readonly callTool: CallToolFn) {}

  async usage(input: StorageUsage.Input): Promise<StorageUsage.Output> {
    return this.callTool('storageUsageTool', input) as Promise<StorageUsage.Output>
  }

  async costUsage(input: CostUsage.Input): Promise<CostUsage.Output> {
    return this.callTool('costUsageTool', input) as Promise<CostUsage.Output>
  }
}

export class ScheduleNamespace {
  constructor(private readonly callTool: CallToolFn) {}

  async createScheduledAction(input: CreateScheduledAction.Input): Promise<CreateScheduledAction.Output> {
    return this.callTool('createScheduledActionTool', input) as Promise<CreateScheduledAction.Output>
  }

  async listScheduledActions(input: ListScheduledActions.Input): Promise<ListScheduledActions.Output> {
    return this.callTool('listScheduledActionsTool', input) as Promise<ListScheduledActions.Output>
  }

  async pauseScheduledAction(input: PauseScheduledAction.Input): Promise<PauseScheduledAction.Output> {
    return this.callTool('pauseScheduledActionTool', input) as Promise<PauseScheduledAction.Output>
  }

  async resumeScheduledAction(input: ResumeScheduledAction.Input): Promise<ResumeScheduledAction.Output> {
    return this.callTool('resumeScheduledActionTool', input) as Promise<ResumeScheduledAction.Output>
  }

  async deleteScheduledAction(input: DeleteScheduledAction.Input): Promise<DeleteScheduledAction.Output> {
    return this.callTool('deleteScheduledActionTool', input) as Promise<DeleteScheduledAction.Output>
  }

  async setScheduleEntitlement(input: SetScheduleEntitlement.Input): Promise<SetScheduleEntitlement.Output> {
    return this.callTool('setScheduleEntitlementTool', input) as Promise<SetScheduleEntitlement.Output>
  }

  async getScheduleStatus(input: GetScheduleStatus.Input): Promise<GetScheduleStatus.Output> {
    return this.callTool('getScheduleStatusTool', input) as Promise<GetScheduleStatus.Output>
  }

  async proposeScheduledAction(input: ProposeScheduledAction.Input): Promise<ProposeScheduledAction.Output> {
    return this.callTool('proposeScheduledActionTool', input) as Promise<ProposeScheduledAction.Output>
  }

  async getScheduleLink(input: GetScheduleLink.Input): Promise<GetScheduleLink.Output> {
    return this.callTool('getScheduleLinkTool', input) as Promise<GetScheduleLink.Output>
  }

  async revokeScheduleLink(input: RevokeScheduleLink.Input): Promise<RevokeScheduleLink.Output> {
    return this.callTool('revokeScheduleLinkTool', input) as Promise<RevokeScheduleLink.Output>
  }
}

export class WebhooksNamespace {
  constructor(private readonly callTool: CallToolFn) {}

  async createWebhook(input: CreateWebhook.Input): Promise<CreateWebhook.Output> {
    return this.callTool('createWebhookTool', input) as Promise<CreateWebhook.Output>
  }

  async listWebhooks(input: ListWebhooks.Input): Promise<ListWebhooks.Output> {
    return this.callTool('listWebhooksTool', input) as Promise<ListWebhooks.Output>
  }

  async revokeWebhook(input: RevokeWebhook.Input): Promise<RevokeWebhook.Output> {
    return this.callTool('revokeWebhookTool', input) as Promise<RevokeWebhook.Output>
  }
}

export class VideoNamespace {
  constructor(private readonly callTool: CallToolFn) {}

  async analyzeStart(input: VideoAnalyzeStart.Input): Promise<VideoAnalyzeStart.Output> {
    return this.callTool('videoAnalyzeStartTool', input) as Promise<VideoAnalyzeStart.Output>
  }

  async analyzeStatus(input: VideoAnalyzeStatus.Input): Promise<VideoAnalyzeStatus.Output> {
    return this.callTool('videoAnalyzeStatusTool', input) as Promise<VideoAnalyzeStatus.Output>
  }
}
