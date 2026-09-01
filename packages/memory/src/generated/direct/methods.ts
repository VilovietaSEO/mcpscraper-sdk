export type CallToolFn = (name: string, args: unknown) => Promise<unknown>

import * as AcceptShareTool from './tools/acceptShareTool.js'
import * as AddVaultTool from './tools/addVaultTool.js'
import * as AnswerInboxItemTool from './tools/answerInboxItemTool.js'
import * as ApproveSenderTool from './tools/approveSenderTool.js'
import * as ArchiveArtifactTemplate from './tools/archive_artifact_template.js'
import * as ArchiveScheduledRun from './tools/archive_scheduled_run.js'
import * as AssistantContextPacketCreate from './tools/assistant_context_packet_create.js'
import * as AssistantContextPacketGet from './tools/assistant_context_packet_get.js'
import * as AssistantContextPacketLifecycle from './tools/assistant_context_packet_lifecycle.js'
import * as AssistantContextPacketList from './tools/assistant_context_packet_list.js'
import * as AssistantContextPacketShareAccept from './tools/assistant_context_packet_share_accept.js'
import * as AutoOptimizationTool from './tools/autoOptimizationTool.js'
import * as BulkDeleteNotesTool from './tools/bulkDeleteNotesTool.js'
import * as CostUsageTool from './tools/costUsageTool.js'
import * as CreateArtifactTemplate from './tools/create_artifact_template.js'
import * as CreateChannelTool from './tools/createChannelTool.js'
import * as CreateScheduledActionTool from './tools/createScheduledActionTool.js'
import * as CreateSecureVaultTool from './tools/createSecureVaultTool.js'
import * as CreateTableTool from './tools/createTableTool.js'
import * as CreateWebhookTool from './tools/createWebhookTool.js'
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
import * as DeclineShareTool from './tools/declineShareTool.js'
import * as DeleteNoteTool from './tools/deleteNoteTool.js'
import * as DeleteScheduledActionTool from './tools/deleteScheduledActionTool.js'
import * as DeleteTableRowsTool from './tools/deleteTableRowsTool.js'
import * as DeleteVaultTool from './tools/deleteVaultTool.js'
import * as DescribeTableTool from './tools/describeTableTool.js'
import * as DropTableTool from './tools/dropTableTool.js'
import * as ExportTool from './tools/exportTool.js'
import * as FactHistoryTool from './tools/factHistoryTool.js'
import * as FileAssetGet from './tools/file_asset_get.js'
import * as FileAssetSave from './tools/file_asset_save.js'
import * as GetArtifactTemplate from './tools/get_artifact_template.js'
import * as GetScheduledRun from './tools/get_scheduled_run.js'
import * as GetChatLinkTool from './tools/getChatLinkTool.js'
import * as GetMessageNoteTool from './tools/getMessageNoteTool.js'
import * as GetScheduleLinkTool from './tools/getScheduleLinkTool.js'
import * as GetScheduleStatusTool from './tools/getScheduleStatusTool.js'
import * as GetTool from './tools/getTool.js'
import * as GetVaultAppLinkTool from './tools/getVaultAppLinkTool.js'
import * as GetVaultContractTool from './tools/getVaultContractTool.js'
import * as GraphPathTool from './tools/graphPathTool.js'
import * as GraphUniverseTool from './tools/graphUniverseTool.js'
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
import * as InboxSettingsTool from './tools/inboxSettingsTool.js'
import * as InsertTableRowsTool from './tools/insertTableRowsTool.js'
import * as InviteAccountTool from './tools/inviteAccountTool.js'
import * as IssueKeyTool from './tools/issueKeyTool.js'
import * as LibraryIngestTool from './tools/libraryIngestTool.js'
import * as ListArtifactTemplates from './tools/list_artifact_templates.js'
import * as ListScheduledRuns from './tools/list_scheduled_runs.js'
import * as ListApprovedSendersTool from './tools/listApprovedSendersTool.js'
import * as ListChannelMembersTool from './tools/listChannelMembersTool.js'
import * as ListChannelMessagesTool from './tools/listChannelMessagesTool.js'
import * as ListKeysTool from './tools/listKeysTool.js'
import * as ListScheduledActionRunsTool from './tools/listScheduledActionRunsTool.js'
import * as ListScheduledActionsTool from './tools/listScheduledActionsTool.js'
import * as ListSharedWithMeTool from './tools/listSharedWithMeTool.js'
import * as ListTablesTool from './tools/listTablesTool.js'
import * as ListTagsTool from './tools/listTagsTool.js'
import * as ListTool from './tools/listTool.js'
import * as ListVaultsTool from './tools/listVaultsTool.js'
import * as ListWebhooksTool from './tools/listWebhooksTool.js'
import * as MarkScheduledRunOpened from './tools/mark_scheduled_run_opened.js'
import * as MarkScheduledRunUnopened from './tools/mark_scheduled_run_unopened.js'
import * as MemoryCaptureTool from './tools/memoryCaptureTool.js'
import * as MemoryQuestionsTool from './tools/memoryQuestionsTool.js'
import * as MergeTagsTool from './tools/mergeTagsTool.js'
import * as MyMentionsTool from './tools/myMentionsTool.js'
import * as NoteBacklinksTool from './tools/noteBacklinksTool.js'
import * as NoteInboxTool from './tools/noteInboxTool.js'
import * as PauseScheduledActionTool from './tools/pauseScheduledActionTool.js'
import * as PollChannelTool from './tools/pollChannelTool.js'
import * as PostMessageTool from './tools/postMessageTool.js'
import * as PrepareMemoryWriteTool from './tools/prepareMemoryWriteTool.js'
import * as ProposeScheduledActionTool from './tools/proposeScheduledActionTool.js'
import * as ProvisionDefaultsTool from './tools/provisionDefaultsTool.js'
import * as PutTool from './tools/putTool.js'
import * as QueryTableTool from './tools/queryTableTool.js'
import * as ReactMessageTool from './tools/reactMessageTool.js'
import * as RecordFactTool from './tools/recordFactTool.js'
import * as RemoveApprovedSenderTool from './tools/removeApprovedSenderTool.js'
import * as RemoveChannelMemberTool from './tools/removeChannelMemberTool.js'
import * as ReplyMessageTool from './tools/replyMessageTool.js'
import * as ResearchOrganizationCapture from './tools/research-organization-capture.js'
import * as ResearchOrganizationGet from './tools/research-organization-get.js'
import * as ResearchOrganizationSearch from './tools/research-organization-search.js'
import * as ResearchPersonCapture from './tools/research-person-capture.js'
import * as ResearchPersonGet from './tools/research-person-get.js'
import * as ResearchPersonSearch from './tools/research-person-search.js'
import * as ResolveTagsTool from './tools/resolveTagsTool.js'
import * as ResumeScheduledActionTool from './tools/resumeScheduledActionTool.js'
import * as RevokeChatLinkTool from './tools/revokeChatLinkTool.js'
import * as RevokeKeyTool from './tools/revokeKeyTool.js'
import * as RevokeScheduleLinkTool from './tools/revokeScheduleLinkTool.js'
import * as RevokeShareTool from './tools/revokeShareTool.js'
import * as RevokeVaultAppLinkTool from './tools/revokeVaultAppLinkTool.js'
import * as RevokeWebhookTool from './tools/revokeWebhookTool.js'
import * as RouteMemoryTool from './tools/routeMemoryTool.js'
import * as SearchTool from './tools/searchTool.js'
import * as SetAgentIdentityTool from './tools/setAgentIdentityTool.js'
import * as SetScheduleDefaultsTool from './tools/setScheduleDefaultsTool.js'
import * as SetScheduleEntitlementTool from './tools/setScheduleEntitlementTool.js'
import * as SetScopeTool from './tools/setScopeTool.js'
import * as ShareNoteTool from './tools/shareNoteTool.js'
import * as ShareVaultTool from './tools/shareVaultTool.js'
import * as StorageUsageTool from './tools/storageUsageTool.js'
import * as SuggestTool from './tools/suggestTool.js'
import * as SwapVaultTool from './tools/swapVaultTool.js'
import * as SwitchAccountTool from './tools/switchAccountTool.js'
import * as TemporalRecallTool from './tools/temporalRecallTool.js'
import * as UnlinkShareTool from './tools/unlinkShareTool.js'
import * as UpdateArtifactTemplate from './tools/update_artifact_template.js'
import * as UpdateScheduledActionTool from './tools/updateScheduledActionTool.js'
import * as UploadTool from './tools/uploadTool.js'
import * as UpsertTagTool from './tools/upsertTagTool.js'
import * as ValidateMemoryWriteTool from './tools/validateMemoryWriteTool.js'
import * as VideoAnalyzeStartTool from './tools/videoAnalyzeStartTool.js'
import * as VideoAnalyzeStatusTool from './tools/videoAnalyzeStatusTool.js'

export class AcceptShareToolNamespace {
  constructor(private readonly callTool: CallToolFn) {}

  async acceptShareTool(input: AcceptShareTool.Input): Promise<AcceptShareTool.Output> {
    return this.callTool('acceptShareTool', input) as Promise<AcceptShareTool.Output>
  }
}

export class AddVaultToolNamespace {
  constructor(private readonly callTool: CallToolFn) {}

  async addVaultTool(input: AddVaultTool.Input): Promise<AddVaultTool.Output> {
    return this.callTool('addVaultTool', input) as Promise<AddVaultTool.Output>
  }
}

export class AnswerInboxItemToolNamespace {
  constructor(private readonly callTool: CallToolFn) {}

  async answerInboxItemTool(input: AnswerInboxItemTool.Input): Promise<AnswerInboxItemTool.Output> {
    return this.callTool('answerInboxItemTool', input) as Promise<AnswerInboxItemTool.Output>
  }
}

export class ApproveSenderToolNamespace {
  constructor(private readonly callTool: CallToolFn) {}

  async approveSenderTool(input: ApproveSenderTool.Input): Promise<ApproveSenderTool.Output> {
    return this.callTool('approveSenderTool', input) as Promise<ApproveSenderTool.Output>
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

export class BulkDeleteNotesToolNamespace {
  constructor(private readonly callTool: CallToolFn) {}

  async bulkDeleteNotesTool(input: BulkDeleteNotesTool.Input): Promise<BulkDeleteNotesTool.Output> {
    return this.callTool('bulkDeleteNotesTool', input) as Promise<BulkDeleteNotesTool.Output>
  }
}

export class CostUsageToolNamespace {
  constructor(private readonly callTool: CallToolFn) {}

  async costUsageTool(input: CostUsageTool.Input): Promise<CostUsageTool.Output> {
    return this.callTool('costUsageTool', input) as Promise<CostUsageTool.Output>
  }
}

export class CreateNamespace {
  constructor(private readonly callTool: CallToolFn) {}

  async artifactTemplate(input: CreateArtifactTemplate.Input): Promise<CreateArtifactTemplate.Output> {
    return this.callTool('create_artifact_template', input) as Promise<CreateArtifactTemplate.Output>
  }
}

export class CreateChannelToolNamespace {
  constructor(private readonly callTool: CallToolFn) {}

  async createChannelTool(input: CreateChannelTool.Input): Promise<CreateChannelTool.Output> {
    return this.callTool('createChannelTool', input) as Promise<CreateChannelTool.Output>
  }
}

export class CreateScheduledActionToolNamespace {
  constructor(private readonly callTool: CallToolFn) {}

  async createScheduledActionTool(input: CreateScheduledActionTool.Input): Promise<CreateScheduledActionTool.Output> {
    return this.callTool('createScheduledActionTool', input) as Promise<CreateScheduledActionTool.Output>
  }
}

export class CreateSecureVaultToolNamespace {
  constructor(private readonly callTool: CallToolFn) {}

  async createSecureVaultTool(input: CreateSecureVaultTool.Input): Promise<CreateSecureVaultTool.Output> {
    return this.callTool('createSecureVaultTool', input) as Promise<CreateSecureVaultTool.Output>
  }
}

export class CreateTableToolNamespace {
  constructor(private readonly callTool: CallToolFn) {}

  async createTableTool(input: CreateTableTool.Input): Promise<CreateTableTool.Output> {
    return this.callTool('createTableTool', input) as Promise<CreateTableTool.Output>
  }
}

export class CreateWebhookToolNamespace {
  constructor(private readonly callTool: CallToolFn) {}

  async createWebhookTool(input: CreateWebhookTool.Input): Promise<CreateWebhookTool.Output> {
    return this.callTool('createWebhookTool', input) as Promise<CreateWebhookTool.Output>
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

export class DeclineShareToolNamespace {
  constructor(private readonly callTool: CallToolFn) {}

  async declineShareTool(input: DeclineShareTool.Input): Promise<DeclineShareTool.Output> {
    return this.callTool('declineShareTool', input) as Promise<DeclineShareTool.Output>
  }
}

export class DeleteNoteToolNamespace {
  constructor(private readonly callTool: CallToolFn) {}

  async deleteNoteTool(input: DeleteNoteTool.Input): Promise<DeleteNoteTool.Output> {
    return this.callTool('deleteNoteTool', input) as Promise<DeleteNoteTool.Output>
  }
}

export class DeleteScheduledActionToolNamespace {
  constructor(private readonly callTool: CallToolFn) {}

  async deleteScheduledActionTool(input: DeleteScheduledActionTool.Input): Promise<DeleteScheduledActionTool.Output> {
    return this.callTool('deleteScheduledActionTool', input) as Promise<DeleteScheduledActionTool.Output>
  }
}

export class DeleteTableRowsToolNamespace {
  constructor(private readonly callTool: CallToolFn) {}

  async deleteTableRowsTool(input: DeleteTableRowsTool.Input): Promise<DeleteTableRowsTool.Output> {
    return this.callTool('deleteTableRowsTool', input) as Promise<DeleteTableRowsTool.Output>
  }
}

export class DeleteVaultToolNamespace {
  constructor(private readonly callTool: CallToolFn) {}

  async deleteVaultTool(input: DeleteVaultTool.Input): Promise<DeleteVaultTool.Output> {
    return this.callTool('deleteVaultTool', input) as Promise<DeleteVaultTool.Output>
  }
}

export class DescribeTableToolNamespace {
  constructor(private readonly callTool: CallToolFn) {}

  async describeTableTool(input: DescribeTableTool.Input): Promise<DescribeTableTool.Output> {
    return this.callTool('describeTableTool', input) as Promise<DescribeTableTool.Output>
  }
}

export class DropTableToolNamespace {
  constructor(private readonly callTool: CallToolFn) {}

  async dropTableTool(input: DropTableTool.Input): Promise<DropTableTool.Output> {
    return this.callTool('dropTableTool', input) as Promise<DropTableTool.Output>
  }
}

export class ExportToolNamespace {
  constructor(private readonly callTool: CallToolFn) {}

  async exportTool(input: ExportTool.Input): Promise<ExportTool.Output> {
    return this.callTool('exportTool', input) as Promise<ExportTool.Output>
  }
}

export class FactHistoryToolNamespace {
  constructor(private readonly callTool: CallToolFn) {}

  async factHistoryTool(input: FactHistoryTool.Input): Promise<FactHistoryTool.Output> {
    return this.callTool('factHistoryTool', input) as Promise<FactHistoryTool.Output>
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
}

export class GetChatLinkToolNamespace {
  constructor(private readonly callTool: CallToolFn) {}

  async getChatLinkTool(input: GetChatLinkTool.Input): Promise<GetChatLinkTool.Output> {
    return this.callTool('getChatLinkTool', input) as Promise<GetChatLinkTool.Output>
  }
}

export class GetMessageNoteToolNamespace {
  constructor(private readonly callTool: CallToolFn) {}

  async getMessageNoteTool(input: GetMessageNoteTool.Input): Promise<GetMessageNoteTool.Output> {
    return this.callTool('getMessageNoteTool', input) as Promise<GetMessageNoteTool.Output>
  }
}

export class GetScheduleLinkToolNamespace {
  constructor(private readonly callTool: CallToolFn) {}

  async getScheduleLinkTool(input: GetScheduleLinkTool.Input): Promise<GetScheduleLinkTool.Output> {
    return this.callTool('getScheduleLinkTool', input) as Promise<GetScheduleLinkTool.Output>
  }
}

export class GetScheduleStatusToolNamespace {
  constructor(private readonly callTool: CallToolFn) {}

  async getScheduleStatusTool(input: GetScheduleStatusTool.Input): Promise<GetScheduleStatusTool.Output> {
    return this.callTool('getScheduleStatusTool', input) as Promise<GetScheduleStatusTool.Output>
  }
}

export class GetToolNamespace {
  constructor(private readonly callTool: CallToolFn) {}

  async getTool(input: GetTool.Input): Promise<GetTool.Output> {
    return this.callTool('getTool', input) as Promise<GetTool.Output>
  }
}

export class GetVaultAppLinkToolNamespace {
  constructor(private readonly callTool: CallToolFn) {}

  async getVaultAppLinkTool(input: GetVaultAppLinkTool.Input): Promise<GetVaultAppLinkTool.Output> {
    return this.callTool('getVaultAppLinkTool', input) as Promise<GetVaultAppLinkTool.Output>
  }
}

export class GetVaultContractToolNamespace {
  constructor(private readonly callTool: CallToolFn) {}

  async getVaultContractTool(input: GetVaultContractTool.Input): Promise<GetVaultContractTool.Output> {
    return this.callTool('getVaultContractTool', input) as Promise<GetVaultContractTool.Output>
  }
}

export class GraphPathToolNamespace {
  constructor(private readonly callTool: CallToolFn) {}

  async graphPathTool(input: GraphPathTool.Input): Promise<GraphPathTool.Output> {
    return this.callTool('graphPathTool', input) as Promise<GraphPathTool.Output>
  }
}

export class GraphUniverseToolNamespace {
  constructor(private readonly callTool: CallToolFn) {}

  async graphUniverseTool(input: GraphUniverseTool.Input): Promise<GraphUniverseTool.Output> {
    return this.callTool('graphUniverseTool', input) as Promise<GraphUniverseTool.Output>
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

export class InboxSettingsToolNamespace {
  constructor(private readonly callTool: CallToolFn) {}

  async inboxSettingsTool(input: InboxSettingsTool.Input): Promise<InboxSettingsTool.Output> {
    return this.callTool('inboxSettingsTool', input) as Promise<InboxSettingsTool.Output>
  }
}

export class InsertTableRowsToolNamespace {
  constructor(private readonly callTool: CallToolFn) {}

  async insertTableRowsTool(input: InsertTableRowsTool.Input): Promise<InsertTableRowsTool.Output> {
    return this.callTool('insertTableRowsTool', input) as Promise<InsertTableRowsTool.Output>
  }
}

export class InviteAccountToolNamespace {
  constructor(private readonly callTool: CallToolFn) {}

  async inviteAccountTool(input: InviteAccountTool.Input): Promise<InviteAccountTool.Output> {
    return this.callTool('inviteAccountTool', input) as Promise<InviteAccountTool.Output>
  }
}

export class IssueKeyToolNamespace {
  constructor(private readonly callTool: CallToolFn) {}

  async issueKeyTool(input: IssueKeyTool.Input): Promise<IssueKeyTool.Output> {
    return this.callTool('issueKeyTool', input) as Promise<IssueKeyTool.Output>
  }
}

export class LibraryIngestToolNamespace {
  constructor(private readonly callTool: CallToolFn) {}

  async libraryIngestTool(input: LibraryIngestTool.Input): Promise<LibraryIngestTool.Output> {
    return this.callTool('libraryIngestTool', input) as Promise<LibraryIngestTool.Output>
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
}

export class ListApprovedSendersToolNamespace {
  constructor(private readonly callTool: CallToolFn) {}

  async listApprovedSendersTool(input: ListApprovedSendersTool.Input): Promise<ListApprovedSendersTool.Output> {
    return this.callTool('listApprovedSendersTool', input) as Promise<ListApprovedSendersTool.Output>
  }
}

export class ListChannelMembersToolNamespace {
  constructor(private readonly callTool: CallToolFn) {}

  async listChannelMembersTool(input: ListChannelMembersTool.Input): Promise<ListChannelMembersTool.Output> {
    return this.callTool('listChannelMembersTool', input) as Promise<ListChannelMembersTool.Output>
  }
}

export class ListChannelMessagesToolNamespace {
  constructor(private readonly callTool: CallToolFn) {}

  async listChannelMessagesTool(input: ListChannelMessagesTool.Input): Promise<ListChannelMessagesTool.Output> {
    return this.callTool('listChannelMessagesTool', input) as Promise<ListChannelMessagesTool.Output>
  }
}

export class ListKeysToolNamespace {
  constructor(private readonly callTool: CallToolFn) {}

  async listKeysTool(input: ListKeysTool.Input): Promise<ListKeysTool.Output> {
    return this.callTool('listKeysTool', input) as Promise<ListKeysTool.Output>
  }
}

export class ListScheduledActionRunsToolNamespace {
  constructor(private readonly callTool: CallToolFn) {}

  async listScheduledActionRunsTool(input: ListScheduledActionRunsTool.Input): Promise<ListScheduledActionRunsTool.Output> {
    return this.callTool('listScheduledActionRunsTool', input) as Promise<ListScheduledActionRunsTool.Output>
  }
}

export class ListScheduledActionsToolNamespace {
  constructor(private readonly callTool: CallToolFn) {}

  async listScheduledActionsTool(input: ListScheduledActionsTool.Input): Promise<ListScheduledActionsTool.Output> {
    return this.callTool('listScheduledActionsTool', input) as Promise<ListScheduledActionsTool.Output>
  }
}

export class ListSharedWithMeToolNamespace {
  constructor(private readonly callTool: CallToolFn) {}

  async listSharedWithMeTool(input: ListSharedWithMeTool.Input): Promise<ListSharedWithMeTool.Output> {
    return this.callTool('listSharedWithMeTool', input) as Promise<ListSharedWithMeTool.Output>
  }
}

export class ListTablesToolNamespace {
  constructor(private readonly callTool: CallToolFn) {}

  async listTablesTool(input: ListTablesTool.Input): Promise<ListTablesTool.Output> {
    return this.callTool('listTablesTool', input) as Promise<ListTablesTool.Output>
  }
}

export class ListTagsToolNamespace {
  constructor(private readonly callTool: CallToolFn) {}

  async listTagsTool(input: ListTagsTool.Input): Promise<ListTagsTool.Output> {
    return this.callTool('listTagsTool', input) as Promise<ListTagsTool.Output>
  }
}

export class ListToolNamespace {
  constructor(private readonly callTool: CallToolFn) {}

  async listTool(input: ListTool.Input): Promise<ListTool.Output> {
    return this.callTool('listTool', input) as Promise<ListTool.Output>
  }
}

export class ListVaultsToolNamespace {
  constructor(private readonly callTool: CallToolFn) {}

  async listVaultsTool(input: ListVaultsTool.Input): Promise<ListVaultsTool.Output> {
    return this.callTool('listVaultsTool', input) as Promise<ListVaultsTool.Output>
  }
}

export class ListWebhooksToolNamespace {
  constructor(private readonly callTool: CallToolFn) {}

  async listWebhooksTool(input: ListWebhooksTool.Input): Promise<ListWebhooksTool.Output> {
    return this.callTool('listWebhooksTool', input) as Promise<ListWebhooksTool.Output>
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

export class MemoryCaptureToolNamespace {
  constructor(private readonly callTool: CallToolFn) {}

  async memoryCaptureTool(input: MemoryCaptureTool.Input): Promise<MemoryCaptureTool.Output> {
    return this.callTool('memoryCaptureTool', input) as Promise<MemoryCaptureTool.Output>
  }
}

export class MemoryQuestionsToolNamespace {
  constructor(private readonly callTool: CallToolFn) {}

  async memoryQuestionsTool(input: MemoryQuestionsTool.Input): Promise<MemoryQuestionsTool.Output> {
    return this.callTool('memoryQuestionsTool', input) as Promise<MemoryQuestionsTool.Output>
  }
}

export class MergeTagsToolNamespace {
  constructor(private readonly callTool: CallToolFn) {}

  async mergeTagsTool(input: MergeTagsTool.Input): Promise<MergeTagsTool.Output> {
    return this.callTool('mergeTagsTool', input) as Promise<MergeTagsTool.Output>
  }
}

export class MyMentionsToolNamespace {
  constructor(private readonly callTool: CallToolFn) {}

  async myMentionsTool(input: MyMentionsTool.Input): Promise<MyMentionsTool.Output> {
    return this.callTool('myMentionsTool', input) as Promise<MyMentionsTool.Output>
  }
}

export class NoteBacklinksToolNamespace {
  constructor(private readonly callTool: CallToolFn) {}

  async noteBacklinksTool(input: NoteBacklinksTool.Input): Promise<NoteBacklinksTool.Output> {
    return this.callTool('noteBacklinksTool', input) as Promise<NoteBacklinksTool.Output>
  }
}

export class NoteInboxToolNamespace {
  constructor(private readonly callTool: CallToolFn) {}

  async noteInboxTool(input: NoteInboxTool.Input): Promise<NoteInboxTool.Output> {
    return this.callTool('noteInboxTool', input) as Promise<NoteInboxTool.Output>
  }
}

export class PauseScheduledActionToolNamespace {
  constructor(private readonly callTool: CallToolFn) {}

  async pauseScheduledActionTool(input: PauseScheduledActionTool.Input): Promise<PauseScheduledActionTool.Output> {
    return this.callTool('pauseScheduledActionTool', input) as Promise<PauseScheduledActionTool.Output>
  }
}

export class PollChannelToolNamespace {
  constructor(private readonly callTool: CallToolFn) {}

  async pollChannelTool(input: PollChannelTool.Input): Promise<PollChannelTool.Output> {
    return this.callTool('pollChannelTool', input) as Promise<PollChannelTool.Output>
  }
}

export class PostMessageToolNamespace {
  constructor(private readonly callTool: CallToolFn) {}

  async postMessageTool(input: PostMessageTool.Input): Promise<PostMessageTool.Output> {
    return this.callTool('postMessageTool', input) as Promise<PostMessageTool.Output>
  }
}

export class PrepareMemoryWriteToolNamespace {
  constructor(private readonly callTool: CallToolFn) {}

  async prepareMemoryWriteTool(input: PrepareMemoryWriteTool.Input): Promise<PrepareMemoryWriteTool.Output> {
    return this.callTool('prepareMemoryWriteTool', input) as Promise<PrepareMemoryWriteTool.Output>
  }
}

export class ProposeScheduledActionToolNamespace {
  constructor(private readonly callTool: CallToolFn) {}

  async proposeScheduledActionTool(input: ProposeScheduledActionTool.Input): Promise<ProposeScheduledActionTool.Output> {
    return this.callTool('proposeScheduledActionTool', input) as Promise<ProposeScheduledActionTool.Output>
  }
}

export class ProvisionDefaultsToolNamespace {
  constructor(private readonly callTool: CallToolFn) {}

  async provisionDefaultsTool(input: ProvisionDefaultsTool.Input): Promise<ProvisionDefaultsTool.Output> {
    return this.callTool('provisionDefaultsTool', input) as Promise<ProvisionDefaultsTool.Output>
  }
}

export class PutToolNamespace {
  constructor(private readonly callTool: CallToolFn) {}

  async putTool(input: PutTool.Input): Promise<PutTool.Output> {
    return this.callTool('putTool', input) as Promise<PutTool.Output>
  }
}

export class QueryTableToolNamespace {
  constructor(private readonly callTool: CallToolFn) {}

  async queryTableTool(input: QueryTableTool.Input): Promise<QueryTableTool.Output> {
    return this.callTool('queryTableTool', input) as Promise<QueryTableTool.Output>
  }
}

export class ReactMessageToolNamespace {
  constructor(private readonly callTool: CallToolFn) {}

  async reactMessageTool(input: ReactMessageTool.Input): Promise<ReactMessageTool.Output> {
    return this.callTool('reactMessageTool', input) as Promise<ReactMessageTool.Output>
  }
}

export class RecordFactToolNamespace {
  constructor(private readonly callTool: CallToolFn) {}

  async recordFactTool(input: RecordFactTool.Input): Promise<RecordFactTool.Output> {
    return this.callTool('recordFactTool', input) as Promise<RecordFactTool.Output>
  }
}

export class RemoveApprovedSenderToolNamespace {
  constructor(private readonly callTool: CallToolFn) {}

  async removeApprovedSenderTool(input: RemoveApprovedSenderTool.Input): Promise<RemoveApprovedSenderTool.Output> {
    return this.callTool('removeApprovedSenderTool', input) as Promise<RemoveApprovedSenderTool.Output>
  }
}

export class RemoveChannelMemberToolNamespace {
  constructor(private readonly callTool: CallToolFn) {}

  async removeChannelMemberTool(input: RemoveChannelMemberTool.Input): Promise<RemoveChannelMemberTool.Output> {
    return this.callTool('removeChannelMemberTool', input) as Promise<RemoveChannelMemberTool.Output>
  }
}

export class ReplyMessageToolNamespace {
  constructor(private readonly callTool: CallToolFn) {}

  async replyMessageTool(input: ReplyMessageTool.Input): Promise<ReplyMessageTool.Output> {
    return this.callTool('replyMessageTool', input) as Promise<ReplyMessageTool.Output>
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

export class ResolveTagsToolNamespace {
  constructor(private readonly callTool: CallToolFn) {}

  async resolveTagsTool(input: ResolveTagsTool.Input): Promise<ResolveTagsTool.Output> {
    return this.callTool('resolveTagsTool', input) as Promise<ResolveTagsTool.Output>
  }
}

export class ResumeScheduledActionToolNamespace {
  constructor(private readonly callTool: CallToolFn) {}

  async resumeScheduledActionTool(input: ResumeScheduledActionTool.Input): Promise<ResumeScheduledActionTool.Output> {
    return this.callTool('resumeScheduledActionTool', input) as Promise<ResumeScheduledActionTool.Output>
  }
}

export class RevokeChatLinkToolNamespace {
  constructor(private readonly callTool: CallToolFn) {}

  async revokeChatLinkTool(input: RevokeChatLinkTool.Input): Promise<RevokeChatLinkTool.Output> {
    return this.callTool('revokeChatLinkTool', input) as Promise<RevokeChatLinkTool.Output>
  }
}

export class RevokeKeyToolNamespace {
  constructor(private readonly callTool: CallToolFn) {}

  async revokeKeyTool(input: RevokeKeyTool.Input): Promise<RevokeKeyTool.Output> {
    return this.callTool('revokeKeyTool', input) as Promise<RevokeKeyTool.Output>
  }
}

export class RevokeScheduleLinkToolNamespace {
  constructor(private readonly callTool: CallToolFn) {}

  async revokeScheduleLinkTool(input: RevokeScheduleLinkTool.Input): Promise<RevokeScheduleLinkTool.Output> {
    return this.callTool('revokeScheduleLinkTool', input) as Promise<RevokeScheduleLinkTool.Output>
  }
}

export class RevokeShareToolNamespace {
  constructor(private readonly callTool: CallToolFn) {}

  async revokeShareTool(input: RevokeShareTool.Input): Promise<RevokeShareTool.Output> {
    return this.callTool('revokeShareTool', input) as Promise<RevokeShareTool.Output>
  }
}

export class RevokeVaultAppLinkToolNamespace {
  constructor(private readonly callTool: CallToolFn) {}

  async revokeVaultAppLinkTool(input: RevokeVaultAppLinkTool.Input): Promise<RevokeVaultAppLinkTool.Output> {
    return this.callTool('revokeVaultAppLinkTool', input) as Promise<RevokeVaultAppLinkTool.Output>
  }
}

export class RevokeWebhookToolNamespace {
  constructor(private readonly callTool: CallToolFn) {}

  async revokeWebhookTool(input: RevokeWebhookTool.Input): Promise<RevokeWebhookTool.Output> {
    return this.callTool('revokeWebhookTool', input) as Promise<RevokeWebhookTool.Output>
  }
}

export class RouteMemoryToolNamespace {
  constructor(private readonly callTool: CallToolFn) {}

  async routeMemoryTool(input: RouteMemoryTool.Input): Promise<RouteMemoryTool.Output> {
    return this.callTool('routeMemoryTool', input) as Promise<RouteMemoryTool.Output>
  }
}

export class SearchToolNamespace {
  constructor(private readonly callTool: CallToolFn) {}

  async searchTool(input: SearchTool.Input): Promise<SearchTool.Output> {
    return this.callTool('searchTool', input) as Promise<SearchTool.Output>
  }
}

export class SetAgentIdentityToolNamespace {
  constructor(private readonly callTool: CallToolFn) {}

  async setAgentIdentityTool(input: SetAgentIdentityTool.Input): Promise<SetAgentIdentityTool.Output> {
    return this.callTool('setAgentIdentityTool', input) as Promise<SetAgentIdentityTool.Output>
  }
}

export class SetScheduleDefaultsToolNamespace {
  constructor(private readonly callTool: CallToolFn) {}

  async setScheduleDefaultsTool(input: SetScheduleDefaultsTool.Input): Promise<SetScheduleDefaultsTool.Output> {
    return this.callTool('setScheduleDefaultsTool', input) as Promise<SetScheduleDefaultsTool.Output>
  }
}

export class SetScheduleEntitlementToolNamespace {
  constructor(private readonly callTool: CallToolFn) {}

  async setScheduleEntitlementTool(input: SetScheduleEntitlementTool.Input): Promise<SetScheduleEntitlementTool.Output> {
    return this.callTool('setScheduleEntitlementTool', input) as Promise<SetScheduleEntitlementTool.Output>
  }
}

export class SetScopeToolNamespace {
  constructor(private readonly callTool: CallToolFn) {}

  async setScopeTool(input: SetScopeTool.Input): Promise<SetScopeTool.Output> {
    return this.callTool('setScopeTool', input) as Promise<SetScopeTool.Output>
  }
}

export class ShareNoteToolNamespace {
  constructor(private readonly callTool: CallToolFn) {}

  async shareNoteTool(input: ShareNoteTool.Input): Promise<ShareNoteTool.Output> {
    return this.callTool('shareNoteTool', input) as Promise<ShareNoteTool.Output>
  }
}

export class ShareVaultToolNamespace {
  constructor(private readonly callTool: CallToolFn) {}

  async shareVaultTool(input: ShareVaultTool.Input): Promise<ShareVaultTool.Output> {
    return this.callTool('shareVaultTool', input) as Promise<ShareVaultTool.Output>
  }
}

export class StorageUsageToolNamespace {
  constructor(private readonly callTool: CallToolFn) {}

  async storageUsageTool(input: StorageUsageTool.Input): Promise<StorageUsageTool.Output> {
    return this.callTool('storageUsageTool', input) as Promise<StorageUsageTool.Output>
  }
}

export class SuggestToolNamespace {
  constructor(private readonly callTool: CallToolFn) {}

  async suggestTool(input: SuggestTool.Input): Promise<SuggestTool.Output> {
    return this.callTool('suggestTool', input) as Promise<SuggestTool.Output>
  }
}

export class SwapVaultToolNamespace {
  constructor(private readonly callTool: CallToolFn) {}

  async swapVaultTool(input: SwapVaultTool.Input): Promise<SwapVaultTool.Output> {
    return this.callTool('swapVaultTool', input) as Promise<SwapVaultTool.Output>
  }
}

export class SwitchAccountToolNamespace {
  constructor(private readonly callTool: CallToolFn) {}

  async switchAccountTool(input: SwitchAccountTool.Input): Promise<SwitchAccountTool.Output> {
    return this.callTool('switchAccountTool', input) as Promise<SwitchAccountTool.Output>
  }
}

export class TemporalRecallToolNamespace {
  constructor(private readonly callTool: CallToolFn) {}

  async temporalRecallTool(input: TemporalRecallTool.Input): Promise<TemporalRecallTool.Output> {
    return this.callTool('temporalRecallTool', input) as Promise<TemporalRecallTool.Output>
  }
}

export class UnlinkShareToolNamespace {
  constructor(private readonly callTool: CallToolFn) {}

  async unlinkShareTool(input: UnlinkShareTool.Input): Promise<UnlinkShareTool.Output> {
    return this.callTool('unlinkShareTool', input) as Promise<UnlinkShareTool.Output>
  }
}

export class UpdateNamespace {
  constructor(private readonly callTool: CallToolFn) {}

  async artifactTemplate(input: UpdateArtifactTemplate.Input): Promise<UpdateArtifactTemplate.Output> {
    return this.callTool('update_artifact_template', input) as Promise<UpdateArtifactTemplate.Output>
  }
}

export class UpdateScheduledActionToolNamespace {
  constructor(private readonly callTool: CallToolFn) {}

  async updateScheduledActionTool(input: UpdateScheduledActionTool.Input): Promise<UpdateScheduledActionTool.Output> {
    return this.callTool('updateScheduledActionTool', input) as Promise<UpdateScheduledActionTool.Output>
  }
}

export class UploadToolNamespace {
  constructor(private readonly callTool: CallToolFn) {}

  async uploadTool(input: UploadTool.Input): Promise<UploadTool.Output> {
    return this.callTool('uploadTool', input) as Promise<UploadTool.Output>
  }
}

export class UpsertTagToolNamespace {
  constructor(private readonly callTool: CallToolFn) {}

  async upsertTagTool(input: UpsertTagTool.Input): Promise<UpsertTagTool.Output> {
    return this.callTool('upsertTagTool', input) as Promise<UpsertTagTool.Output>
  }
}

export class ValidateMemoryWriteToolNamespace {
  constructor(private readonly callTool: CallToolFn) {}

  async validateMemoryWriteTool(input: ValidateMemoryWriteTool.Input): Promise<ValidateMemoryWriteTool.Output> {
    return this.callTool('validateMemoryWriteTool', input) as Promise<ValidateMemoryWriteTool.Output>
  }
}

export class VideoAnalyzeStartToolNamespace {
  constructor(private readonly callTool: CallToolFn) {}

  async videoAnalyzeStartTool(input: VideoAnalyzeStartTool.Input): Promise<VideoAnalyzeStartTool.Output> {
    return this.callTool('videoAnalyzeStartTool', input) as Promise<VideoAnalyzeStartTool.Output>
  }
}

export class VideoAnalyzeStatusToolNamespace {
  constructor(private readonly callTool: CallToolFn) {}

  async videoAnalyzeStatusTool(input: VideoAnalyzeStatusTool.Input): Promise<VideoAnalyzeStatusTool.Output> {
    return this.callTool('videoAnalyzeStatusTool', input) as Promise<VideoAnalyzeStatusTool.Output>
  }
}
