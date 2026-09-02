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
import * as AddVault from './tools/add-vault.js'
import * as AnswerInboxItemTool from './tools/answerInboxItemTool.js'
import * as ArchiveArtifactTemplate from './tools/archive_artifact_template.js'
import * as ArchiveScheduledRun from './tools/archive_scheduled_run.js'
import * as AssistantContextPacketCreate from './tools/assistant_context_packet_create.js'
import * as AssistantContextPacketGet from './tools/assistant_context_packet_get.js'
import * as AssistantContextPacketLifecycle from './tools/assistant_context_packet_lifecycle.js'
import * as AssistantContextPacketList from './tools/assistant_context_packet_list.js'
import * as AssistantContextPacketShareAccept from './tools/assistant_context_packet_share_accept.js'
import * as AutoOptimizationTool from './tools/autoOptimizationTool.js'
import * as BulkDeleteNotes from './tools/bulk-delete-notes.js'
import * as CostUsage from './tools/cost-usage.js'
import * as CreateArtifactTemplate from './tools/create_artifact_template.js'
import * as CreateChannel from './tools/create-channel.js'
import * as CreateScheduledAction from './tools/create-scheduled-action.js'
import * as CreateSecureVault from './tools/create-secure-vault.js'
import * as CreateWebhook from './tools/create-webhook.js'
import * as TableCreate from './tools/table-create.js'
import * as TableDeleteRows from './tools/table-delete-rows.js'
import * as TableDescribe from './tools/table-describe.js'
import * as TableDrop from './tools/table-drop.js'
import * as TableInsertRows from './tools/table-insert-rows.js'
import * as TableList from './tools/table-list.js'
import * as TableQuery from './tools/table-query.js'
import * as CrmActivityAppend from './tools/crm-activity-append.js'
import * as CrmCounterpartApply from './tools/crm-counterpart-apply.js'
import * as CrmCounterpartPreview from './tools/crm-counterpart-preview.js'
import * as CrmDealTransition from './tools/crm-deal-transition.js'
import * as CrmDealUpsert from './tools/crm-deal-upsert.js'
import * as CrmDuplicateSearch from './tools/crm-duplicate-search.js'
import * as CrmImportApply from './tools/crm-import-apply.js'
import * as CrmImportPreview from './tools/crm-import-preview.js'
import * as CrmMergeApply from './tools/crm-merge-apply.js'
import * as CrmMergePreview from './tools/crm-merge-preview.js'
import * as CrmOrganizationGet from './tools/crm-organization-get.js'
import * as CrmOrganizationSearch from './tools/crm-organization-search.js'
import * as CrmPersonGet from './tools/crm-person-get.js'
import * as CrmPersonSearch from './tools/crm-person-search.js'
import * as CrmPipelineList from './tools/crm-pipeline-list.js'
import * as CrmPipelineUpsert from './tools/crm-pipeline-upsert.js'
import * as CrmQualityList from './tools/crm-quality-list.js'
import * as CrmOrganizationUpsert from './tools/crm-organization-upsert.js'
import * as CrmPersonUpsert from './tools/crm-person-upsert.js'
import * as CrmTaskUpsert from './tools/crm-task-upsert.js'
import * as CrmWorkSearch from './tools/crm-work-search.js'
import * as DeleteNote from './tools/delete-note.js'
import * as DeleteScheduledAction from './tools/delete-scheduled-action.js'
import * as DeleteVault from './tools/delete-vault.js'
import * as MemoryExport from './tools/memory-export.js'
import * as MemoryGet from './tools/memory-get.js'
import * as MemoryGraphPath from './tools/memory-graph-path.js'
import * as MemoryGraphUniverse from './tools/memory-graph-universe.js'
import * as MemoryList from './tools/memory-list.js'
import * as MemoryCapture from './tools/memory-capture.js'
import * as MemoryQuestions from './tools/memory-questions.js'
import * as MemoryBacklinks from './tools/memory-backlinks.js'
import * as MemoryPut from './tools/memory-put.js'
import * as MemorySearch from './tools/memory-search.js'
import * as MemorySuggest from './tools/memory-suggest.js'
import * as MemoryUpload from './tools/memory-upload.js'
import * as FactHistory from './tools/fact-history.js'
import * as FileAssetGet from './tools/file_asset_get.js'
import * as FileAssetSave from './tools/file_asset_save.js'
import * as GetArtifactTemplate from './tools/get_artifact_template.js'
import * as GetScheduledRun from './tools/get_scheduled_run.js'
import * as GetChatLink from './tools/get-chat-link.js'
import * as GetMessageNote from './tools/get-message-note.js'
import * as GetScheduleLink from './tools/get-schedule-link.js'
import * as GetScheduleStatus from './tools/get-schedule-status.js'
import * as GetVaultAppLink from './tools/get-vault-app-link.js'
import * as GetVaultContract from './tools/get-vault-contract.js'
import * as ImageAssetDelete from './tools/image_asset_delete.js'
import * as ImageAssetGet from './tools/image_asset_get.js'
import * as ImageAssetList from './tools/image_asset_list.js'
import * as ImageAssetMove from './tools/image_asset_move.js'
import * as ImageAssetSave from './tools/image_asset_save.js'
import * as ImageAssetSearch from './tools/image_asset_search.js'
import * as ImageFolderCreate from './tools/image_folder_create.js'
import * as ImageFolderList from './tools/image_folder_list.js'
import * as ImageProjectCreate from './tools/image_project_create.js'
import * as ImageProjectList from './tools/image_project_list.js'
import * as LibraryIngest from './tools/library-ingest.js'
import * as ListArtifactTemplates from './tools/list_artifact_templates.js'
import * as ListScheduledRuns from './tools/list_scheduled_runs.js'
import * as ListChannelMembers from './tools/list-channel-members.js'
import * as ListChannelMessages from './tools/list-channel-messages.js'
import * as ListScheduledActions from './tools/list-scheduled-actions.js'
import * as ListSharedWithMe from './tools/list-shared-with-me.js'
import * as ListMemoryTags from './tools/list-memory-tags.js'
import * as ListVaults from './tools/list-vaults.js'
import * as ListWebhooks from './tools/list-webhooks.js'
import * as ListScheduledActionRunsTool from './tools/listScheduledActionRunsTool.js'
import * as MarkScheduledRunOpened from './tools/mark_scheduled_run_opened.js'
import * as MarkScheduledRunUnopened from './tools/mark_scheduled_run_unopened.js'
import * as MergeMemoryTags from './tools/merge-memory-tags.js'
import * as MyMentions from './tools/my-mentions.js'
import * as PauseScheduledAction from './tools/pause-scheduled-action.js'
import * as PollChannel from './tools/poll-channel.js'
import * as PostMessage from './tools/post-message.js'
import * as PrepareMemoryWrite from './tools/prepare-memory-write.js'
import * as ProposeScheduledAction from './tools/propose-scheduled-action.js'
import * as ProvisionDefaults from './tools/provision-defaults.js'
import * as ReactMessage from './tools/react-message.js'
import * as RecordFact from './tools/record-fact.js'
import * as RemoveChannelMember from './tools/remove-channel-member.js'
import * as ReplyMessage from './tools/reply-message.js'
import * as ResearchOrganizationCapture from './tools/research-organization-capture.js'
import * as ResearchOrganizationGet from './tools/research-organization-get.js'
import * as ResearchOrganizationSearch from './tools/research-organization-search.js'
import * as ResearchPersonCapture from './tools/research-person-capture.js'
import * as ResearchPersonGet from './tools/research-person-get.js'
import * as ResearchPersonSearch from './tools/research-person-search.js'
import * as ResolveMemoryTags from './tools/resolve-memory-tags.js'
import * as ResumeScheduledAction from './tools/resume-scheduled-action.js'
import * as RevokeChatLink from './tools/revoke-chat-link.js'
import * as RevokeScheduleLink from './tools/revoke-schedule-link.js'
import * as RevokeVaultAppLink from './tools/revoke-vault-app-link.js'
import * as RevokeWebhook from './tools/revoke-webhook.js'
import * as RouteMemory from './tools/route-memory.js'
import * as SetAgentIdentity from './tools/set-agent-identity.js'
import * as SetScheduleDefaults from './tools/set-schedule-defaults.js'
import * as SetScheduleEntitlement from './tools/set-schedule-entitlement.js'
import * as StorageUsage from './tools/storage-usage.js'
import * as TemporalRecall from './tools/temporal-recall.js'
import * as UpdateArtifactTemplate from './tools/update_artifact_template.js'
import * as UpdateScheduledAction from './tools/update-scheduled-action.js'
import * as UpsertMemoryTag from './tools/upsert-memory-tag.js'
import * as ValidateMemoryWrite from './tools/validate-memory-write.js'
import * as VideoAnalyzeStart from './tools/video-analyze-start.js'
import * as VideoAnalyzeStatus from './tools/video-analyze-status.js'

export class AccessNamespace {
  constructor(private readonly callTool: CallToolFn) {}

  async acceptShare(input: AccessAcceptShare.Input): Promise<AccessAcceptShare.Output> {
    return this.callTool('acceptShareTool', input) as Promise<AccessAcceptShare.Output>
  }

  async approveSender(input: AccessApproveSender.Input): Promise<AccessApproveSender.Output> {
    return this.callTool('approveSenderTool', input) as Promise<AccessApproveSender.Output>
  }

  async declineShare(input: AccessDeclineShare.Input): Promise<AccessDeclineShare.Output> {
    return this.callTool('declineShareTool', input) as Promise<AccessDeclineShare.Output>
  }

  async inboxSettings(input: AccessInboxSettings.Input): Promise<AccessInboxSettings.Output> {
    return this.callTool('inboxSettingsTool', input) as Promise<AccessInboxSettings.Output>
  }

  async inviteAccount(input: AccessInviteAccount.Input): Promise<AccessInviteAccount.Output> {
    return this.callTool('inviteAccountTool', input) as Promise<AccessInviteAccount.Output>
  }

  async issueKey(input: AccessIssueKey.Input): Promise<AccessIssueKey.Output> {
    return this.callTool('issueKeyTool', input) as Promise<AccessIssueKey.Output>
  }

  async listApprovedSenders(input: AccessListApprovedSenders.Input): Promise<AccessListApprovedSenders.Output> {
    return this.callTool('listApprovedSendersTool', input) as Promise<AccessListApprovedSenders.Output>
  }

  async listKeys(input: AccessListKeys.Input): Promise<AccessListKeys.Output> {
    return this.callTool('listKeysTool', input) as Promise<AccessListKeys.Output>
  }

  async noteInbox(input: AccessNoteInbox.Input): Promise<AccessNoteInbox.Output> {
    return this.callTool('noteInboxTool', input) as Promise<AccessNoteInbox.Output>
  }

  async removeApprovedSender(input: AccessRemoveApprovedSender.Input): Promise<AccessRemoveApprovedSender.Output> {
    return this.callTool('removeApprovedSenderTool', input) as Promise<AccessRemoveApprovedSender.Output>
  }

  async revokeKey(input: AccessRevokeKey.Input): Promise<AccessRevokeKey.Output> {
    return this.callTool('revokeKeyTool', input) as Promise<AccessRevokeKey.Output>
  }

  async revokeShare(input: AccessRevokeShare.Input): Promise<AccessRevokeShare.Output> {
    return this.callTool('revokeShareTool', input) as Promise<AccessRevokeShare.Output>
  }

  async setScope(input: AccessSetScope.Input): Promise<AccessSetScope.Output> {
    return this.callTool('setScopeTool', input) as Promise<AccessSetScope.Output>
  }

  async shareNote(input: AccessShareNote.Input): Promise<AccessShareNote.Output> {
    return this.callTool('shareNoteTool', input) as Promise<AccessShareNote.Output>
  }

  async shareVault(input: AccessShareVault.Input): Promise<AccessShareVault.Output> {
    return this.callTool('shareVaultTool', input) as Promise<AccessShareVault.Output>
  }

  async swapVault(input: AccessSwapVault.Input): Promise<AccessSwapVault.Output> {
    return this.callTool('swapVaultTool', input) as Promise<AccessSwapVault.Output>
  }

  async switchAccount(input: AccessSwitchAccount.Input): Promise<AccessSwitchAccount.Output> {
    return this.callTool('switchAccountTool', input) as Promise<AccessSwitchAccount.Output>
  }

  async unlinkShare(input: AccessUnlinkShare.Input): Promise<AccessUnlinkShare.Output> {
    return this.callTool('unlinkShareTool', input) as Promise<AccessUnlinkShare.Output>
  }
}

export class AddNamespace {
  constructor(private readonly callTool: CallToolFn) {}

  async vault(input: AddVault.Input): Promise<AddVault.Output> {
    return this.callTool('addVaultTool', input) as Promise<AddVault.Output>
  }
}

export class AnswerInboxItemToolNamespace {
  constructor(private readonly callTool: CallToolFn) {}

  async answerInboxItemTool(input: AnswerInboxItemTool.Input): Promise<AnswerInboxItemTool.Output> {
    return this.callTool('answerInboxItemTool', input) as Promise<AnswerInboxItemTool.Output>
  }
}

export class ArchiveNamespace {
  constructor(private readonly callTool: CallToolFn) {}

  async artifactTemplate(input: ArchiveArtifactTemplate.Input): Promise<ArchiveArtifactTemplate.Output> {
    return this.callTool('archive_artifact_template', input) as Promise<ArchiveArtifactTemplate.Output>
  }

  async scheduledRun(input: ArchiveScheduledRun.Input): Promise<ArchiveScheduledRun.Output> {
    return this.callTool('archive_scheduled_run', input) as Promise<ArchiveScheduledRun.Output>
  }
}

export class AssistantNamespace {
  constructor(private readonly callTool: CallToolFn) {}

  async contextPacketCreate(input: AssistantContextPacketCreate.Input): Promise<AssistantContextPacketCreate.Output> {
    return this.callTool('assistant_context_packet_create', input) as Promise<AssistantContextPacketCreate.Output>
  }

  async contextPacketGet(input: AssistantContextPacketGet.Input): Promise<AssistantContextPacketGet.Output> {
    return this.callTool('assistant_context_packet_get', input) as Promise<AssistantContextPacketGet.Output>
  }

  async contextPacketLifecycle(input: AssistantContextPacketLifecycle.Input): Promise<AssistantContextPacketLifecycle.Output> {
    return this.callTool('assistant_context_packet_lifecycle', input) as Promise<AssistantContextPacketLifecycle.Output>
  }

  async contextPacketList(input: AssistantContextPacketList.Input): Promise<AssistantContextPacketList.Output> {
    return this.callTool('assistant_context_packet_list', input) as Promise<AssistantContextPacketList.Output>
  }

  async contextPacketShareAccept(input: AssistantContextPacketShareAccept.Input): Promise<AssistantContextPacketShareAccept.Output> {
    return this.callTool('assistant_context_packet_share_accept', input) as Promise<AssistantContextPacketShareAccept.Output>
  }
}

export class AutoOptimizationToolNamespace {
  constructor(private readonly callTool: CallToolFn) {}

  async autoOptimizationTool(input: AutoOptimizationTool.Input): Promise<AutoOptimizationTool.Output> {
    return this.callTool('autoOptimizationTool', input) as Promise<AutoOptimizationTool.Output>
  }
}

export class BulkNamespace {
  constructor(private readonly callTool: CallToolFn) {}

  async deleteNotes(input: BulkDeleteNotes.Input): Promise<BulkDeleteNotes.Output> {
    return this.callTool('bulkDeleteNotesTool', input) as Promise<BulkDeleteNotes.Output>
  }
}

export class CostNamespace {
  constructor(private readonly callTool: CallToolFn) {}

  async usage(input: CostUsage.Input): Promise<CostUsage.Output> {
    return this.callTool('costUsageTool', input) as Promise<CostUsage.Output>
  }
}

export class CreateNamespace {
  constructor(private readonly callTool: CallToolFn) {}

  async artifactTemplate(input: CreateArtifactTemplate.Input): Promise<CreateArtifactTemplate.Output> {
    return this.callTool('create_artifact_template', input) as Promise<CreateArtifactTemplate.Output>
  }

  async channel(input: CreateChannel.Input): Promise<CreateChannel.Output> {
    return this.callTool('createChannelTool', input) as Promise<CreateChannel.Output>
  }

  async scheduledAction(input: CreateScheduledAction.Input): Promise<CreateScheduledAction.Output> {
    return this.callTool('createScheduledActionTool', input) as Promise<CreateScheduledAction.Output>
  }

  async secureVault(input: CreateSecureVault.Input): Promise<CreateSecureVault.Output> {
    return this.callTool('createSecureVaultTool', input) as Promise<CreateSecureVault.Output>
  }

  async webhook(input: CreateWebhook.Input): Promise<CreateWebhook.Output> {
    return this.callTool('createWebhookTool', input) as Promise<CreateWebhook.Output>
  }
}

export class TableNamespace {
  constructor(private readonly callTool: CallToolFn) {}

  async create(input: TableCreate.Input): Promise<TableCreate.Output> {
    return this.callTool('createTableTool', input) as Promise<TableCreate.Output>
  }

  async deleteRows(input: TableDeleteRows.Input): Promise<TableDeleteRows.Output> {
    return this.callTool('deleteTableRowsTool', input) as Promise<TableDeleteRows.Output>
  }

  async describe(input: TableDescribe.Input): Promise<TableDescribe.Output> {
    return this.callTool('describeTableTool', input) as Promise<TableDescribe.Output>
  }

  async drop(input: TableDrop.Input): Promise<TableDrop.Output> {
    return this.callTool('dropTableTool', input) as Promise<TableDrop.Output>
  }

  async insertRows(input: TableInsertRows.Input): Promise<TableInsertRows.Output> {
    return this.callTool('insertTableRowsTool', input) as Promise<TableInsertRows.Output>
  }

  async list(input: TableList.Input): Promise<TableList.Output> {
    return this.callTool('listTablesTool', input) as Promise<TableList.Output>
  }

  async query(input: TableQuery.Input): Promise<TableQuery.Output> {
    return this.callTool('queryTableTool', input) as Promise<TableQuery.Output>
  }
}

export class CrmNamespace {
  constructor(private readonly callTool: CallToolFn) {}

  async activityAppend(input: CrmActivityAppend.Input): Promise<CrmActivityAppend.Output> {
    return this.callTool('crmAppendCommunicationTool', input) as Promise<CrmActivityAppend.Output>
  }

  async counterpartApply(input: CrmCounterpartApply.Input): Promise<CrmCounterpartApply.Output> {
    return this.callTool('crmCounterpartApplyTool', input) as Promise<CrmCounterpartApply.Output>
  }

  async counterpartPreview(input: CrmCounterpartPreview.Input): Promise<CrmCounterpartPreview.Output> {
    return this.callTool('crmCounterpartPreviewTool', input) as Promise<CrmCounterpartPreview.Output>
  }

  async dealTransition(input: CrmDealTransition.Input): Promise<CrmDealTransition.Output> {
    return this.callTool('crmDealTransitionTool', input) as Promise<CrmDealTransition.Output>
  }

  async dealUpsert(input: CrmDealUpsert.Input): Promise<CrmDealUpsert.Output> {
    return this.callTool('crmDealUpsertTool', input) as Promise<CrmDealUpsert.Output>
  }

  async duplicateSearch(input: CrmDuplicateSearch.Input): Promise<CrmDuplicateSearch.Output> {
    return this.callTool('crmDuplicateSearchTool', input) as Promise<CrmDuplicateSearch.Output>
  }

  async importApply(input: CrmImportApply.Input): Promise<CrmImportApply.Output> {
    return this.callTool('crmImportApplyTool', input) as Promise<CrmImportApply.Output>
  }

  async importPreview(input: CrmImportPreview.Input): Promise<CrmImportPreview.Output> {
    return this.callTool('crmImportPreviewTool', input) as Promise<CrmImportPreview.Output>
  }

  async mergeApply(input: CrmMergeApply.Input): Promise<CrmMergeApply.Output> {
    return this.callTool('crmMergeApplyTool', input) as Promise<CrmMergeApply.Output>
  }

  async mergePreview(input: CrmMergePreview.Input): Promise<CrmMergePreview.Output> {
    return this.callTool('crmMergePreviewTool', input) as Promise<CrmMergePreview.Output>
  }

  async organizationGet(input: CrmOrganizationGet.Input): Promise<CrmOrganizationGet.Output> {
    return this.callTool('crmOrganizationGetTool', input) as Promise<CrmOrganizationGet.Output>
  }

  async organizationSearch(input: CrmOrganizationSearch.Input): Promise<CrmOrganizationSearch.Output> {
    return this.callTool('crmOrganizationSearchTool', input) as Promise<CrmOrganizationSearch.Output>
  }

  async personGet(input: CrmPersonGet.Input): Promise<CrmPersonGet.Output> {
    return this.callTool('crmPersonGetTool', input) as Promise<CrmPersonGet.Output>
  }

  async personSearch(input: CrmPersonSearch.Input): Promise<CrmPersonSearch.Output> {
    return this.callTool('crmPersonSearchTool', input) as Promise<CrmPersonSearch.Output>
  }

  async pipelineList(input: CrmPipelineList.Input): Promise<CrmPipelineList.Output> {
    return this.callTool('crmPipelineListTool', input) as Promise<CrmPipelineList.Output>
  }

  async pipelineUpsert(input: CrmPipelineUpsert.Input): Promise<CrmPipelineUpsert.Output> {
    return this.callTool('crmPipelineUpsertTool', input) as Promise<CrmPipelineUpsert.Output>
  }

  async qualityList(input: CrmQualityList.Input): Promise<CrmQualityList.Output> {
    return this.callTool('crmQualityListTool', input) as Promise<CrmQualityList.Output>
  }

  async organizationUpsert(input: CrmOrganizationUpsert.Input): Promise<CrmOrganizationUpsert.Output> {
    return this.callTool('crmUpsertOrganizationTool', input) as Promise<CrmOrganizationUpsert.Output>
  }

  async personUpsert(input: CrmPersonUpsert.Input): Promise<CrmPersonUpsert.Output> {
    return this.callTool('crmUpsertPersonTool', input) as Promise<CrmPersonUpsert.Output>
  }

  async taskUpsert(input: CrmTaskUpsert.Input): Promise<CrmTaskUpsert.Output> {
    return this.callTool('crmUpsertTaskTool', input) as Promise<CrmTaskUpsert.Output>
  }

  async workSearch(input: CrmWorkSearch.Input): Promise<CrmWorkSearch.Output> {
    return this.callTool('crmWorkSearchTool', input) as Promise<CrmWorkSearch.Output>
  }
}

export class DeleteNamespace {
  constructor(private readonly callTool: CallToolFn) {}

  async note(input: DeleteNote.Input): Promise<DeleteNote.Output> {
    return this.callTool('deleteNoteTool', input) as Promise<DeleteNote.Output>
  }

  async scheduledAction(input: DeleteScheduledAction.Input): Promise<DeleteScheduledAction.Output> {
    return this.callTool('deleteScheduledActionTool', input) as Promise<DeleteScheduledAction.Output>
  }

  async vault(input: DeleteVault.Input): Promise<DeleteVault.Output> {
    return this.callTool('deleteVaultTool', input) as Promise<DeleteVault.Output>
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

  async graphPath(input: MemoryGraphPath.Input): Promise<MemoryGraphPath.Output> {
    return this.callTool('graphPathTool', input) as Promise<MemoryGraphPath.Output>
  }

  async graphUniverse(input: MemoryGraphUniverse.Input): Promise<MemoryGraphUniverse.Output> {
    return this.callTool('graphUniverseTool', input) as Promise<MemoryGraphUniverse.Output>
  }

  async list(input: MemoryList.Input): Promise<MemoryList.Output> {
    return this.callTool('listTool', input) as Promise<MemoryList.Output>
  }

  async capture(input: MemoryCapture.Input): Promise<MemoryCapture.Output> {
    return this.callTool('memoryCaptureTool', input) as Promise<MemoryCapture.Output>
  }

  async questions(input: MemoryQuestions.Input): Promise<MemoryQuestions.Output> {
    return this.callTool('memoryQuestionsTool', input) as Promise<MemoryQuestions.Output>
  }

  async backlinks(input: MemoryBacklinks.Input): Promise<MemoryBacklinks.Output> {
    return this.callTool('noteBacklinksTool', input) as Promise<MemoryBacklinks.Output>
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
}

export class FactNamespace {
  constructor(private readonly callTool: CallToolFn) {}

  async history(input: FactHistory.Input): Promise<FactHistory.Output> {
    return this.callTool('factHistoryTool', input) as Promise<FactHistory.Output>
  }
}

export class FileNamespace {
  constructor(private readonly callTool: CallToolFn) {}

  async assetGet(input: FileAssetGet.Input): Promise<FileAssetGet.Output> {
    return this.callTool('file_asset_get', input) as Promise<FileAssetGet.Output>
  }

  async assetSave(input: FileAssetSave.Input): Promise<FileAssetSave.Output> {
    return this.callTool('file_asset_save', input) as Promise<FileAssetSave.Output>
  }
}

export class GetNamespace {
  constructor(private readonly callTool: CallToolFn) {}

  async artifactTemplate(input: GetArtifactTemplate.Input): Promise<GetArtifactTemplate.Output> {
    return this.callTool('get_artifact_template', input) as Promise<GetArtifactTemplate.Output>
  }

  async scheduledRun(input: GetScheduledRun.Input): Promise<GetScheduledRun.Output> {
    return this.callTool('get_scheduled_run', input) as Promise<GetScheduledRun.Output>
  }

  async chatLink(input: GetChatLink.Input): Promise<GetChatLink.Output> {
    return this.callTool('getChatLinkTool', input) as Promise<GetChatLink.Output>
  }

  async messageNote(input: GetMessageNote.Input): Promise<GetMessageNote.Output> {
    return this.callTool('getMessageNoteTool', input) as Promise<GetMessageNote.Output>
  }

  async scheduleLink(input: GetScheduleLink.Input): Promise<GetScheduleLink.Output> {
    return this.callTool('getScheduleLinkTool', input) as Promise<GetScheduleLink.Output>
  }

  async scheduleStatus(input: GetScheduleStatus.Input): Promise<GetScheduleStatus.Output> {
    return this.callTool('getScheduleStatusTool', input) as Promise<GetScheduleStatus.Output>
  }

  async vaultAppLink(input: GetVaultAppLink.Input): Promise<GetVaultAppLink.Output> {
    return this.callTool('getVaultAppLinkTool', input) as Promise<GetVaultAppLink.Output>
  }

  async vaultContract(input: GetVaultContract.Input): Promise<GetVaultContract.Output> {
    return this.callTool('getVaultContractTool', input) as Promise<GetVaultContract.Output>
  }
}

export class ImageNamespace {
  constructor(private readonly callTool: CallToolFn) {}

  async assetDelete(input: ImageAssetDelete.Input): Promise<ImageAssetDelete.Output> {
    return this.callTool('image_asset_delete', input) as Promise<ImageAssetDelete.Output>
  }

  async assetGet(input: ImageAssetGet.Input): Promise<ImageAssetGet.Output> {
    return this.callTool('image_asset_get', input) as Promise<ImageAssetGet.Output>
  }

  async assetList(input: ImageAssetList.Input): Promise<ImageAssetList.Output> {
    return this.callTool('image_asset_list', input) as Promise<ImageAssetList.Output>
  }

  async assetMove(input: ImageAssetMove.Input): Promise<ImageAssetMove.Output> {
    return this.callTool('image_asset_move', input) as Promise<ImageAssetMove.Output>
  }

  async assetSave(input: ImageAssetSave.Input): Promise<ImageAssetSave.Output> {
    return this.callTool('image_asset_save', input) as Promise<ImageAssetSave.Output>
  }

  async assetSearch(input: ImageAssetSearch.Input): Promise<ImageAssetSearch.Output> {
    return this.callTool('image_asset_search', input) as Promise<ImageAssetSearch.Output>
  }

  async folderCreate(input: ImageFolderCreate.Input): Promise<ImageFolderCreate.Output> {
    return this.callTool('image_folder_create', input) as Promise<ImageFolderCreate.Output>
  }

  async folderList(input: ImageFolderList.Input): Promise<ImageFolderList.Output> {
    return this.callTool('image_folder_list', input) as Promise<ImageFolderList.Output>
  }

  async projectCreate(input: ImageProjectCreate.Input): Promise<ImageProjectCreate.Output> {
    return this.callTool('image_project_create', input) as Promise<ImageProjectCreate.Output>
  }

  async projectList(input: ImageProjectList.Input): Promise<ImageProjectList.Output> {
    return this.callTool('image_project_list', input) as Promise<ImageProjectList.Output>
  }
}

export class LibraryNamespace {
  constructor(private readonly callTool: CallToolFn) {}

  async ingest(input: LibraryIngest.Input): Promise<LibraryIngest.Output> {
    return this.callTool('libraryIngestTool', input) as Promise<LibraryIngest.Output>
  }
}

export class ListNamespace {
  constructor(private readonly callTool: CallToolFn) {}

  async artifactTemplates(input: ListArtifactTemplates.Input): Promise<ListArtifactTemplates.Output> {
    return this.callTool('list_artifact_templates', input) as Promise<ListArtifactTemplates.Output>
  }

  async scheduledRuns(input: ListScheduledRuns.Input): Promise<ListScheduledRuns.Output> {
    return this.callTool('list_scheduled_runs', input) as Promise<ListScheduledRuns.Output>
  }

  async channelMembers(input: ListChannelMembers.Input): Promise<ListChannelMembers.Output> {
    return this.callTool('listChannelMembersTool', input) as Promise<ListChannelMembers.Output>
  }

  async channelMessages(input: ListChannelMessages.Input): Promise<ListChannelMessages.Output> {
    return this.callTool('listChannelMessagesTool', input) as Promise<ListChannelMessages.Output>
  }

  async scheduledActions(input: ListScheduledActions.Input): Promise<ListScheduledActions.Output> {
    return this.callTool('listScheduledActionsTool', input) as Promise<ListScheduledActions.Output>
  }

  async sharedWithMe(input: ListSharedWithMe.Input): Promise<ListSharedWithMe.Output> {
    return this.callTool('listSharedWithMeTool', input) as Promise<ListSharedWithMe.Output>
  }

  async memoryTags(input: ListMemoryTags.Input): Promise<ListMemoryTags.Output> {
    return this.callTool('listTagsTool', input) as Promise<ListMemoryTags.Output>
  }

  async vaults(input: ListVaults.Input): Promise<ListVaults.Output> {
    return this.callTool('listVaultsTool', input) as Promise<ListVaults.Output>
  }

  async webhooks(input: ListWebhooks.Input): Promise<ListWebhooks.Output> {
    return this.callTool('listWebhooksTool', input) as Promise<ListWebhooks.Output>
  }
}

export class ListScheduledActionRunsToolNamespace {
  constructor(private readonly callTool: CallToolFn) {}

  async listScheduledActionRunsTool(input: ListScheduledActionRunsTool.Input): Promise<ListScheduledActionRunsTool.Output> {
    return this.callTool('listScheduledActionRunsTool', input) as Promise<ListScheduledActionRunsTool.Output>
  }
}

export class MarkNamespace {
  constructor(private readonly callTool: CallToolFn) {}

  async scheduledRunOpened(input: MarkScheduledRunOpened.Input): Promise<MarkScheduledRunOpened.Output> {
    return this.callTool('mark_scheduled_run_opened', input) as Promise<MarkScheduledRunOpened.Output>
  }

  async scheduledRunUnopened(input: MarkScheduledRunUnopened.Input): Promise<MarkScheduledRunUnopened.Output> {
    return this.callTool('mark_scheduled_run_unopened', input) as Promise<MarkScheduledRunUnopened.Output>
  }
}

export class MergeNamespace {
  constructor(private readonly callTool: CallToolFn) {}

  async memoryTags(input: MergeMemoryTags.Input): Promise<MergeMemoryTags.Output> {
    return this.callTool('mergeTagsTool', input) as Promise<MergeMemoryTags.Output>
  }
}

export class MyNamespace {
  constructor(private readonly callTool: CallToolFn) {}

  async mentions(input: MyMentions.Input): Promise<MyMentions.Output> {
    return this.callTool('myMentionsTool', input) as Promise<MyMentions.Output>
  }
}

export class PauseNamespace {
  constructor(private readonly callTool: CallToolFn) {}

  async scheduledAction(input: PauseScheduledAction.Input): Promise<PauseScheduledAction.Output> {
    return this.callTool('pauseScheduledActionTool', input) as Promise<PauseScheduledAction.Output>
  }
}

export class PollNamespace {
  constructor(private readonly callTool: CallToolFn) {}

  async channel(input: PollChannel.Input): Promise<PollChannel.Output> {
    return this.callTool('pollChannelTool', input) as Promise<PollChannel.Output>
  }
}

export class PostNamespace {
  constructor(private readonly callTool: CallToolFn) {}

  async message(input: PostMessage.Input): Promise<PostMessage.Output> {
    return this.callTool('postMessageTool', input) as Promise<PostMessage.Output>
  }
}

export class PrepareNamespace {
  constructor(private readonly callTool: CallToolFn) {}

  async memoryWrite(input: PrepareMemoryWrite.Input): Promise<PrepareMemoryWrite.Output> {
    return this.callTool('prepareMemoryWriteTool', input) as Promise<PrepareMemoryWrite.Output>
  }
}

export class ProposeNamespace {
  constructor(private readonly callTool: CallToolFn) {}

  async scheduledAction(input: ProposeScheduledAction.Input): Promise<ProposeScheduledAction.Output> {
    return this.callTool('proposeScheduledActionTool', input) as Promise<ProposeScheduledAction.Output>
  }
}

export class ProvisionNamespace {
  constructor(private readonly callTool: CallToolFn) {}

  async defaults(input: ProvisionDefaults.Input): Promise<ProvisionDefaults.Output> {
    return this.callTool('provisionDefaultsTool', input) as Promise<ProvisionDefaults.Output>
  }
}

export class ReactNamespace {
  constructor(private readonly callTool: CallToolFn) {}

  async message(input: ReactMessage.Input): Promise<ReactMessage.Output> {
    return this.callTool('reactMessageTool', input) as Promise<ReactMessage.Output>
  }
}

export class RecordNamespace {
  constructor(private readonly callTool: CallToolFn) {}

  async fact(input: RecordFact.Input): Promise<RecordFact.Output> {
    return this.callTool('recordFactTool', input) as Promise<RecordFact.Output>
  }
}

export class RemoveNamespace {
  constructor(private readonly callTool: CallToolFn) {}

  async channelMember(input: RemoveChannelMember.Input): Promise<RemoveChannelMember.Output> {
    return this.callTool('removeChannelMemberTool', input) as Promise<RemoveChannelMember.Output>
  }
}

export class ReplyNamespace {
  constructor(private readonly callTool: CallToolFn) {}

  async message(input: ReplyMessage.Input): Promise<ReplyMessage.Output> {
    return this.callTool('replyMessageTool', input) as Promise<ReplyMessage.Output>
  }
}

export class ResearchNamespace {
  constructor(private readonly callTool: CallToolFn) {}

  async organizationCapture(input: ResearchOrganizationCapture.Input): Promise<ResearchOrganizationCapture.Output> {
    return this.callTool('researchOrganizationCaptureTool', input) as Promise<ResearchOrganizationCapture.Output>
  }

  async organizationGet(input: ResearchOrganizationGet.Input): Promise<ResearchOrganizationGet.Output> {
    return this.callTool('researchOrganizationGetTool', input) as Promise<ResearchOrganizationGet.Output>
  }

  async organizationSearch(input: ResearchOrganizationSearch.Input): Promise<ResearchOrganizationSearch.Output> {
    return this.callTool('researchOrganizationSearchTool', input) as Promise<ResearchOrganizationSearch.Output>
  }

  async personCapture(input: ResearchPersonCapture.Input): Promise<ResearchPersonCapture.Output> {
    return this.callTool('researchPersonCaptureTool', input) as Promise<ResearchPersonCapture.Output>
  }

  async personGet(input: ResearchPersonGet.Input): Promise<ResearchPersonGet.Output> {
    return this.callTool('researchPersonGetTool', input) as Promise<ResearchPersonGet.Output>
  }

  async personSearch(input: ResearchPersonSearch.Input): Promise<ResearchPersonSearch.Output> {
    return this.callTool('researchPersonSearchTool', input) as Promise<ResearchPersonSearch.Output>
  }
}

export class ResolveNamespace {
  constructor(private readonly callTool: CallToolFn) {}

  async memoryTags(input: ResolveMemoryTags.Input): Promise<ResolveMemoryTags.Output> {
    return this.callTool('resolveTagsTool', input) as Promise<ResolveMemoryTags.Output>
  }
}

export class ResumeNamespace {
  constructor(private readonly callTool: CallToolFn) {}

  async scheduledAction(input: ResumeScheduledAction.Input): Promise<ResumeScheduledAction.Output> {
    return this.callTool('resumeScheduledActionTool', input) as Promise<ResumeScheduledAction.Output>
  }
}

export class RevokeNamespace {
  constructor(private readonly callTool: CallToolFn) {}

  async chatLink(input: RevokeChatLink.Input): Promise<RevokeChatLink.Output> {
    return this.callTool('revokeChatLinkTool', input) as Promise<RevokeChatLink.Output>
  }

  async scheduleLink(input: RevokeScheduleLink.Input): Promise<RevokeScheduleLink.Output> {
    return this.callTool('revokeScheduleLinkTool', input) as Promise<RevokeScheduleLink.Output>
  }

  async vaultAppLink(input: RevokeVaultAppLink.Input): Promise<RevokeVaultAppLink.Output> {
    return this.callTool('revokeVaultAppLinkTool', input) as Promise<RevokeVaultAppLink.Output>
  }

  async webhook(input: RevokeWebhook.Input): Promise<RevokeWebhook.Output> {
    return this.callTool('revokeWebhookTool', input) as Promise<RevokeWebhook.Output>
  }
}

export class RouteNamespace {
  constructor(private readonly callTool: CallToolFn) {}

  async memory(input: RouteMemory.Input): Promise<RouteMemory.Output> {
    return this.callTool('routeMemoryTool', input) as Promise<RouteMemory.Output>
  }
}

export class SetNamespace {
  constructor(private readonly callTool: CallToolFn) {}

  async agentIdentity(input: SetAgentIdentity.Input): Promise<SetAgentIdentity.Output> {
    return this.callTool('setAgentIdentityTool', input) as Promise<SetAgentIdentity.Output>
  }

  async scheduleDefaults(input: SetScheduleDefaults.Input): Promise<SetScheduleDefaults.Output> {
    return this.callTool('setScheduleDefaultsTool', input) as Promise<SetScheduleDefaults.Output>
  }

  async scheduleEntitlement(input: SetScheduleEntitlement.Input): Promise<SetScheduleEntitlement.Output> {
    return this.callTool('setScheduleEntitlementTool', input) as Promise<SetScheduleEntitlement.Output>
  }
}

export class StorageNamespace {
  constructor(private readonly callTool: CallToolFn) {}

  async usage(input: StorageUsage.Input): Promise<StorageUsage.Output> {
    return this.callTool('storageUsageTool', input) as Promise<StorageUsage.Output>
  }
}

export class TemporalNamespace {
  constructor(private readonly callTool: CallToolFn) {}

  async recall(input: TemporalRecall.Input): Promise<TemporalRecall.Output> {
    return this.callTool('temporalRecallTool', input) as Promise<TemporalRecall.Output>
  }
}

export class UpdateNamespace {
  constructor(private readonly callTool: CallToolFn) {}

  async artifactTemplate(input: UpdateArtifactTemplate.Input): Promise<UpdateArtifactTemplate.Output> {
    return this.callTool('update_artifact_template', input) as Promise<UpdateArtifactTemplate.Output>
  }

  async scheduledAction(input: UpdateScheduledAction.Input): Promise<UpdateScheduledAction.Output> {
    return this.callTool('updateScheduledActionTool', input) as Promise<UpdateScheduledAction.Output>
  }
}

export class UpsertNamespace {
  constructor(private readonly callTool: CallToolFn) {}

  async memoryTag(input: UpsertMemoryTag.Input): Promise<UpsertMemoryTag.Output> {
    return this.callTool('upsertTagTool', input) as Promise<UpsertMemoryTag.Output>
  }
}

export class ValidateNamespace {
  constructor(private readonly callTool: CallToolFn) {}

  async memoryWrite(input: ValidateMemoryWrite.Input): Promise<ValidateMemoryWrite.Output> {
    return this.callTool('validateMemoryWriteTool', input) as Promise<ValidateMemoryWrite.Output>
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
