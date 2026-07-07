export type CallToolFn = (name: string, args: unknown) => Promise<unknown>

import * as AccessAcceptShare from './tools/access-accept-share.js'
import * as AccessApproveSender from './tools/access-approve-sender.js'
import * as AccessDeclineShare from './tools/access-decline-share.js'
import * as AccessInboxSettings from './tools/access-inbox-settings.js'
import * as AccessInviteAccount from './tools/access-invite-account.js'
import * as AccessIssueKey from './tools/access-issue-key.js'
import * as AccessListApprovedSenders from './tools/access-list-approved-senders.js'
import * as AccessListKeys from './tools/access-list-keys.js'
import * as AccessNoteInbox from './tools/access-note-inbox.js'
import * as AccessRemoveApprovedSender from './tools/access-remove-approved-sender.js'
import * as AccessRevokeKey from './tools/access-revoke-key.js'
import * as AccessRevokeShare from './tools/access-revoke-share.js'
import * as AccessSetScope from './tools/access-set-scope.js'
import * as AccessShareNote from './tools/access-share-note.js'
import * as AccessShareVault from './tools/access-share-vault.js'
import * as AccessSwapVault from './tools/access-swap-vault.js'
import * as AccessSwitchAccount from './tools/access-switch-account.js'
import * as AccessUnlinkShare from './tools/access-unlink-share.js'
import * as GetChatLink from './tools/get-chat-link.js'
import * as RevokeChatLink from './tools/revoke-chat-link.js'
import * as SetAgentIdentity from './tools/set-agent-identity.js'
import * as MemoryQuestions from './tools/memory-questions.js'
import * as CreateChannel from './tools/create-channel.js'
import * as GetMessageNote from './tools/get-message-note.js'
import * as ListChannelMembers from './tools/list-channel-members.js'
import * as ListChannelMessages from './tools/list-channel-messages.js'
import * as MyMentions from './tools/my-mentions.js'
import * as PollChannel from './tools/poll-channel.js'
import * as PostMessage from './tools/post-message.js'
import * as ReactMessage from './tools/react-message.js'
import * as RemoveChannelMember from './tools/remove-channel-member.js'
import * as ReplyMessage from './tools/reply-message.js'
import * as FactHistory from './tools/fact-history.js'
import * as RecordFact from './tools/record-fact.js'
import * as LibraryIngest from './tools/library-ingest.js'
import * as DeleteNote from './tools/delete-note.js'
import * as MemoryExport from './tools/memory-export.js'
import * as MemoryGet from './tools/memory-get.js'
import * as MemoryList from './tools/memory-list.js'
import * as MemoryPut from './tools/memory-put.js'
import * as MemorySearch from './tools/memory-search.js'
import * as MemorySuggest from './tools/memory-suggest.js'
import * as MemoryUpload from './tools/memory-upload.js'
import * as TemporalRecall from './tools/temporal-recall.js'
import * as CreateScheduledAction from './tools/create-scheduled-action.js'
import * as DeleteScheduledAction from './tools/delete-scheduled-action.js'
import * as GetScheduleLink from './tools/get-schedule-link.js'
import * as GetScheduleStatus from './tools/get-schedule-status.js'
import * as ListScheduledActions from './tools/list-scheduled-actions.js'
import * as PauseScheduledAction from './tools/pause-scheduled-action.js'
import * as ProposeScheduledAction from './tools/propose-scheduled-action.js'
import * as ResumeScheduledAction from './tools/resume-scheduled-action.js'
import * as RevokeScheduleLink from './tools/revoke-schedule-link.js'
import * as SetScheduleEntitlement from './tools/set-schedule-entitlement.js'
import * as CostUsage from './tools/cost-usage.js'
import * as StorageUsage from './tools/storage-usage.js'
import * as TableCreate from './tools/table-create.js'
import * as TableDeleteRows from './tools/table-delete-rows.js'
import * as TableDescribe from './tools/table-describe.js'
import * as TableDrop from './tools/table-drop.js'
import * as TableInsertRows from './tools/table-insert-rows.js'
import * as TableList from './tools/table-list.js'
import * as TableQuery from './tools/table-query.js'
import * as AddVault from './tools/add-vault.js'
import * as CreateSecureVault from './tools/create-secure-vault.js'
import * as DeleteVault from './tools/delete-vault.js'
import * as ListSharedWithMe from './tools/list-shared-with-me.js'
import * as ListVaults from './tools/list-vaults.js'
import * as ProvisionDefaults from './tools/provision-defaults.js'
import * as VideoAnalyzeStart from './tools/video-analyze-start.js'
import * as VideoAnalyzeStatus from './tools/video-analyze-status.js'
import * as CreateWebhook from './tools/create-webhook.js'
import * as ListWebhooks from './tools/list-webhooks.js'
import * as RevokeWebhook from './tools/revoke-webhook.js'

export class AccessNamespace {
  constructor(private readonly callTool: CallToolFn) {}

  async acceptShare(input: AccessAcceptShare.Input): Promise<AccessAcceptShare.Output> {
    return this.callTool('access-accept-share', input) as Promise<AccessAcceptShare.Output>
  }

  async approveSender(input: AccessApproveSender.Input): Promise<AccessApproveSender.Output> {
    return this.callTool('access-approve-sender', input) as Promise<AccessApproveSender.Output>
  }

  async declineShare(input: AccessDeclineShare.Input): Promise<AccessDeclineShare.Output> {
    return this.callTool('access-decline-share', input) as Promise<AccessDeclineShare.Output>
  }

  async inboxSettings(input: AccessInboxSettings.Input): Promise<AccessInboxSettings.Output> {
    return this.callTool('access-inbox-settings', input) as Promise<AccessInboxSettings.Output>
  }

  async inviteAccount(input: AccessInviteAccount.Input): Promise<AccessInviteAccount.Output> {
    return this.callTool('access-invite-account', input) as Promise<AccessInviteAccount.Output>
  }

  async issueKey(input: AccessIssueKey.Input): Promise<AccessIssueKey.Output> {
    return this.callTool('access-issue-key', input) as Promise<AccessIssueKey.Output>
  }

  async listApprovedSenders(input: AccessListApprovedSenders.Input): Promise<AccessListApprovedSenders.Output> {
    return this.callTool('access-list-approved-senders', input) as Promise<AccessListApprovedSenders.Output>
  }

  async listKeys(input: AccessListKeys.Input): Promise<AccessListKeys.Output> {
    return this.callTool('access-list-keys', input) as Promise<AccessListKeys.Output>
  }

  async noteInbox(input: AccessNoteInbox.Input): Promise<AccessNoteInbox.Output> {
    return this.callTool('access-note-inbox', input) as Promise<AccessNoteInbox.Output>
  }

  async removeApprovedSender(input: AccessRemoveApprovedSender.Input): Promise<AccessRemoveApprovedSender.Output> {
    return this.callTool('access-remove-approved-sender', input) as Promise<AccessRemoveApprovedSender.Output>
  }

  async revokeKey(input: AccessRevokeKey.Input): Promise<AccessRevokeKey.Output> {
    return this.callTool('access-revoke-key', input) as Promise<AccessRevokeKey.Output>
  }

  async revokeShare(input: AccessRevokeShare.Input): Promise<AccessRevokeShare.Output> {
    return this.callTool('access-revoke-share', input) as Promise<AccessRevokeShare.Output>
  }

  async setScope(input: AccessSetScope.Input): Promise<AccessSetScope.Output> {
    return this.callTool('access-set-scope', input) as Promise<AccessSetScope.Output>
  }

  async shareNote(input: AccessShareNote.Input): Promise<AccessShareNote.Output> {
    return this.callTool('access-share-note', input) as Promise<AccessShareNote.Output>
  }

  async shareVault(input: AccessShareVault.Input): Promise<AccessShareVault.Output> {
    return this.callTool('access-share-vault', input) as Promise<AccessShareVault.Output>
  }

  async swapVault(input: AccessSwapVault.Input): Promise<AccessSwapVault.Output> {
    return this.callTool('access-swap-vault', input) as Promise<AccessSwapVault.Output>
  }

  async switchAccount(input: AccessSwitchAccount.Input): Promise<AccessSwitchAccount.Output> {
    return this.callTool('access-switch-account', input) as Promise<AccessSwitchAccount.Output>
  }

  async unlinkShare(input: AccessUnlinkShare.Input): Promise<AccessUnlinkShare.Output> {
    return this.callTool('access-unlink-share', input) as Promise<AccessUnlinkShare.Output>
  }

  async getChatLink(input: GetChatLink.Input): Promise<GetChatLink.Output> {
    return this.callTool('get-chat-link', input) as Promise<GetChatLink.Output>
  }

  async revokeChatLink(input: RevokeChatLink.Input): Promise<RevokeChatLink.Output> {
    return this.callTool('revoke-chat-link', input) as Promise<RevokeChatLink.Output>
  }

  async setAgentIdentity(input: SetAgentIdentity.Input): Promise<SetAgentIdentity.Output> {
    return this.callTool('set-agent-identity', input) as Promise<SetAgentIdentity.Output>
  }
}

export class CaptureNamespace {
  constructor(private readonly callTool: CallToolFn) {}

  async memoryQuestions(input: MemoryQuestions.Input): Promise<MemoryQuestions.Output> {
    return this.callTool('memory-questions', input) as Promise<MemoryQuestions.Output>
  }
}

export class ChannelsNamespace {
  constructor(private readonly callTool: CallToolFn) {}

  async createChannel(input: CreateChannel.Input): Promise<CreateChannel.Output> {
    return this.callTool('create-channel', input) as Promise<CreateChannel.Output>
  }

  async getMessageNote(input: GetMessageNote.Input): Promise<GetMessageNote.Output> {
    return this.callTool('get-message-note', input) as Promise<GetMessageNote.Output>
  }

  async listChannelMembers(input: ListChannelMembers.Input): Promise<ListChannelMembers.Output> {
    return this.callTool('list-channel-members', input) as Promise<ListChannelMembers.Output>
  }

  async listChannelMessages(input: ListChannelMessages.Input): Promise<ListChannelMessages.Output> {
    return this.callTool('list-channel-messages', input) as Promise<ListChannelMessages.Output>
  }

  async myMentions(input: MyMentions.Input): Promise<MyMentions.Output> {
    return this.callTool('my-mentions', input) as Promise<MyMentions.Output>
  }

  async pollChannel(input: PollChannel.Input): Promise<PollChannel.Output> {
    return this.callTool('poll-channel', input) as Promise<PollChannel.Output>
  }

  async postMessage(input: PostMessage.Input): Promise<PostMessage.Output> {
    return this.callTool('post-message', input) as Promise<PostMessage.Output>
  }

  async reactMessage(input: ReactMessage.Input): Promise<ReactMessage.Output> {
    return this.callTool('react-message', input) as Promise<ReactMessage.Output>
  }

  async removeChannelMember(input: RemoveChannelMember.Input): Promise<RemoveChannelMember.Output> {
    return this.callTool('remove-channel-member', input) as Promise<RemoveChannelMember.Output>
  }

  async replyMessage(input: ReplyMessage.Input): Promise<ReplyMessage.Output> {
    return this.callTool('reply-message', input) as Promise<ReplyMessage.Output>
  }
}

export class FactsNamespace {
  constructor(private readonly callTool: CallToolFn) {}

  async history(input: FactHistory.Input): Promise<FactHistory.Output> {
    return this.callTool('fact-history', input) as Promise<FactHistory.Output>
  }

  async recordFact(input: RecordFact.Input): Promise<RecordFact.Output> {
    return this.callTool('record-fact', input) as Promise<RecordFact.Output>
  }
}

export class LibraryNamespace {
  constructor(private readonly callTool: CallToolFn) {}

  async ingest(input: LibraryIngest.Input): Promise<LibraryIngest.Output> {
    return this.callTool('library-ingest', input) as Promise<LibraryIngest.Output>
  }
}

export class MemoryNamespace {
  constructor(private readonly callTool: CallToolFn) {}

  async deleteNote(input: DeleteNote.Input): Promise<DeleteNote.Output> {
    return this.callTool('delete-note', input) as Promise<DeleteNote.Output>
  }

  async export(input: MemoryExport.Input): Promise<MemoryExport.Output> {
    return this.callTool('memory-export', input) as Promise<MemoryExport.Output>
  }

  async get(input: MemoryGet.Input): Promise<MemoryGet.Output> {
    return this.callTool('memory-get', input) as Promise<MemoryGet.Output>
  }

  async list(input: MemoryList.Input): Promise<MemoryList.Output> {
    return this.callTool('memory-list', input) as Promise<MemoryList.Output>
  }

  async put(input: MemoryPut.Input): Promise<MemoryPut.Output> {
    return this.callTool('memory-put', input) as Promise<MemoryPut.Output>
  }

  async search(input: MemorySearch.Input): Promise<MemorySearch.Output> {
    return this.callTool('memory-search', input) as Promise<MemorySearch.Output>
  }

  async suggest(input: MemorySuggest.Input): Promise<MemorySuggest.Output> {
    return this.callTool('memory-suggest', input) as Promise<MemorySuggest.Output>
  }

  async upload(input: MemoryUpload.Input): Promise<MemoryUpload.Output> {
    return this.callTool('memory-upload', input) as Promise<MemoryUpload.Output>
  }
}

export class RecallNamespace {
  constructor(private readonly callTool: CallToolFn) {}

  async temporalRecall(input: TemporalRecall.Input): Promise<TemporalRecall.Output> {
    return this.callTool('temporal-recall', input) as Promise<TemporalRecall.Output>
  }
}

export class ScheduleNamespace {
  constructor(private readonly callTool: CallToolFn) {}

  async createScheduledAction(input: CreateScheduledAction.Input): Promise<CreateScheduledAction.Output> {
    return this.callTool('create-scheduled-action', input) as Promise<CreateScheduledAction.Output>
  }

  async deleteScheduledAction(input: DeleteScheduledAction.Input): Promise<DeleteScheduledAction.Output> {
    return this.callTool('delete-scheduled-action', input) as Promise<DeleteScheduledAction.Output>
  }

  async getScheduleLink(input: GetScheduleLink.Input): Promise<GetScheduleLink.Output> {
    return this.callTool('get-schedule-link', input) as Promise<GetScheduleLink.Output>
  }

  async getScheduleStatus(input: GetScheduleStatus.Input): Promise<GetScheduleStatus.Output> {
    return this.callTool('get-schedule-status', input) as Promise<GetScheduleStatus.Output>
  }

  async listScheduledActions(input: ListScheduledActions.Input): Promise<ListScheduledActions.Output> {
    return this.callTool('list-scheduled-actions', input) as Promise<ListScheduledActions.Output>
  }

  async pauseScheduledAction(input: PauseScheduledAction.Input): Promise<PauseScheduledAction.Output> {
    return this.callTool('pause-scheduled-action', input) as Promise<PauseScheduledAction.Output>
  }

  async proposeScheduledAction(input: ProposeScheduledAction.Input): Promise<ProposeScheduledAction.Output> {
    return this.callTool('propose-scheduled-action', input) as Promise<ProposeScheduledAction.Output>
  }

  async resumeScheduledAction(input: ResumeScheduledAction.Input): Promise<ResumeScheduledAction.Output> {
    return this.callTool('resume-scheduled-action', input) as Promise<ResumeScheduledAction.Output>
  }

  async revokeScheduleLink(input: RevokeScheduleLink.Input): Promise<RevokeScheduleLink.Output> {
    return this.callTool('revoke-schedule-link', input) as Promise<RevokeScheduleLink.Output>
  }

  async setScheduleEntitlement(input: SetScheduleEntitlement.Input): Promise<SetScheduleEntitlement.Output> {
    return this.callTool('set-schedule-entitlement', input) as Promise<SetScheduleEntitlement.Output>
  }
}

export class StorageNamespace {
  constructor(private readonly callTool: CallToolFn) {}

  async costUsage(input: CostUsage.Input): Promise<CostUsage.Output> {
    return this.callTool('cost-usage', input) as Promise<CostUsage.Output>
  }

  async usage(input: StorageUsage.Input): Promise<StorageUsage.Output> {
    return this.callTool('storage-usage', input) as Promise<StorageUsage.Output>
  }
}

export class TablesNamespace {
  constructor(private readonly callTool: CallToolFn) {}

  async create(input: TableCreate.Input): Promise<TableCreate.Output> {
    return this.callTool('table-create', input) as Promise<TableCreate.Output>
  }

  async deleteRows(input: TableDeleteRows.Input): Promise<TableDeleteRows.Output> {
    return this.callTool('table-delete-rows', input) as Promise<TableDeleteRows.Output>
  }

  async describe(input: TableDescribe.Input): Promise<TableDescribe.Output> {
    return this.callTool('table-describe', input) as Promise<TableDescribe.Output>
  }

  async drop(input: TableDrop.Input): Promise<TableDrop.Output> {
    return this.callTool('table-drop', input) as Promise<TableDrop.Output>
  }

  async insertRows(input: TableInsertRows.Input): Promise<TableInsertRows.Output> {
    return this.callTool('table-insert-rows', input) as Promise<TableInsertRows.Output>
  }

  async list(input: TableList.Input): Promise<TableList.Output> {
    return this.callTool('table-list', input) as Promise<TableList.Output>
  }

  async query(input: TableQuery.Input): Promise<TableQuery.Output> {
    return this.callTool('table-query', input) as Promise<TableQuery.Output>
  }
}

export class VaultsNamespace {
  constructor(private readonly callTool: CallToolFn) {}

  async addVault(input: AddVault.Input): Promise<AddVault.Output> {
    return this.callTool('add-vault', input) as Promise<AddVault.Output>
  }

  async createSecureVault(input: CreateSecureVault.Input): Promise<CreateSecureVault.Output> {
    return this.callTool('create-secure-vault', input) as Promise<CreateSecureVault.Output>
  }

  async deleteVault(input: DeleteVault.Input): Promise<DeleteVault.Output> {
    return this.callTool('delete-vault', input) as Promise<DeleteVault.Output>
  }

  async listSharedWithMe(input: ListSharedWithMe.Input): Promise<ListSharedWithMe.Output> {
    return this.callTool('list-shared-with-me', input) as Promise<ListSharedWithMe.Output>
  }

  async listVaults(input: ListVaults.Input): Promise<ListVaults.Output> {
    return this.callTool('list-vaults', input) as Promise<ListVaults.Output>
  }

  async provisionDefaults(input: ProvisionDefaults.Input): Promise<ProvisionDefaults.Output> {
    return this.callTool('provision-defaults', input) as Promise<ProvisionDefaults.Output>
  }
}

export class VideoNamespace {
  constructor(private readonly callTool: CallToolFn) {}

  async analyzeStart(input: VideoAnalyzeStart.Input): Promise<VideoAnalyzeStart.Output> {
    return this.callTool('video-analyze-start', input) as Promise<VideoAnalyzeStart.Output>
  }

  async analyzeStatus(input: VideoAnalyzeStatus.Input): Promise<VideoAnalyzeStatus.Output> {
    return this.callTool('video-analyze-status', input) as Promise<VideoAnalyzeStatus.Output>
  }
}

export class WebhooksNamespace {
  constructor(private readonly callTool: CallToolFn) {}

  async createWebhook(input: CreateWebhook.Input): Promise<CreateWebhook.Output> {
    return this.callTool('create-webhook', input) as Promise<CreateWebhook.Output>
  }

  async listWebhooks(input: ListWebhooks.Input): Promise<ListWebhooks.Output> {
    return this.callTool('list-webhooks', input) as Promise<ListWebhooks.Output>
  }

  async revokeWebhook(input: RevokeWebhook.Input): Promise<RevokeWebhook.Output> {
    return this.callTool('revoke-webhook', input) as Promise<RevokeWebhook.Output>
  }
}
