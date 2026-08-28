from typing import Any, Callable

from .direct_models.access_accept_share import AccessAcceptShareInput, AccessAcceptShareOutput
from .direct_models.access_approve_sender import AccessApproveSenderInput, AccessApproveSenderOutput
from .direct_models.access_decline_share import AccessDeclineShareInput, AccessDeclineShareOutput
from .direct_models.access_inbox_settings import AccessInboxSettingsInput, AccessInboxSettingsOutput
from .direct_models.access_invite_account import AccessInviteAccountInput, AccessInviteAccountOutput
from .direct_models.access_issue_key import AccessIssueKeyInput, AccessIssueKeyOutput
from .direct_models.access_list_approved_senders import AccessListApprovedSendersInput, AccessListApprovedSendersOutput
from .direct_models.access_list_keys import AccessListKeysInput, AccessListKeysOutput
from .direct_models.access_note_inbox import AccessNoteInboxInput, AccessNoteInboxOutput
from .direct_models.access_remove_approved_sender import AccessRemoveApprovedSenderInput, AccessRemoveApprovedSenderOutput
from .direct_models.access_revoke_key import AccessRevokeKeyInput, AccessRevokeKeyOutput
from .direct_models.access_revoke_share import AccessRevokeShareInput, AccessRevokeShareOutput
from .direct_models.access_set_scope import AccessSetScopeInput, AccessSetScopeOutput
from .direct_models.access_share_note import AccessShareNoteInput, AccessShareNoteOutput
from .direct_models.access_share_vault import AccessShareVaultInput, AccessShareVaultOutput
from .direct_models.access_swap_vault import AccessSwapVaultInput, AccessSwapVaultOutput
from .direct_models.access_switch_account import AccessSwitchAccountInput, AccessSwitchAccountOutput
from .direct_models.access_unlink_share import AccessUnlinkShareInput, AccessUnlinkShareOutput
from .direct_models.add_vault import AddVaultInput, AddVaultOutput
from .direct_models.answer_inbox_item import AnswerInboxItemInput, AnswerInboxItemOutput
from .direct_models.archive_artifact_template import ArchiveArtifactTemplateInput, ArchiveArtifactTemplateOutput
from .direct_models.archive_scheduled_run import ArchiveScheduledRunInput, ArchiveScheduledRunOutput
from .direct_models.assistant_context_packet_create import AssistantContextPacketCreateInput, AssistantContextPacketCreateOutput
from .direct_models.assistant_context_packet_get import AssistantContextPacketGetInput, AssistantContextPacketGetOutput
from .direct_models.assistant_context_packet_lifecycle import AssistantContextPacketLifecycleInput, AssistantContextPacketLifecycleOutput
from .direct_models.assistant_context_packet_list import AssistantContextPacketListInput, AssistantContextPacketListOutput
from .direct_models.assistant_context_packet_share_accept import AssistantContextPacketShareAcceptInput, AssistantContextPacketShareAcceptOutput
from .direct_models.auto_optimization import AutoOptimizationInput, AutoOptimizationOutput
from .direct_models.bulk_delete_notes import BulkDeleteNotesInput, BulkDeleteNotesOutput
from .direct_models.cost_usage import CostUsageInput, CostUsageOutput
from .direct_models.create_artifact_template import CreateArtifactTemplateInput, CreateArtifactTemplateOutput
from .direct_models.create_channel import CreateChannelInput, CreateChannelOutput
from .direct_models.create_scheduled_action import CreateScheduledActionInput, CreateScheduledActionOutput
from .direct_models.create_secure_vault import CreateSecureVaultInput, CreateSecureVaultOutput
from .direct_models.create_webhook import CreateWebhookInput, CreateWebhookOutput
from .direct_models.delete_note import DeleteNoteInput, DeleteNoteOutput
from .direct_models.delete_scheduled_action import DeleteScheduledActionInput, DeleteScheduledActionOutput
from .direct_models.delete_vault import DeleteVaultInput, DeleteVaultOutput
from .direct_models.fact_history import FactHistoryInput, FactHistoryOutput
from .direct_models.get_artifact_template import GetArtifactTemplateInput, GetArtifactTemplateOutput
from .direct_models.get_chat_link import GetChatLinkInput, GetChatLinkOutput
from .direct_models.get_message_note import GetMessageNoteInput, GetMessageNoteOutput
from .direct_models.get_schedule_link import GetScheduleLinkInput, GetScheduleLinkOutput
from .direct_models.get_schedule_status import GetScheduleStatusInput, GetScheduleStatusOutput
from .direct_models.get_scheduled_run import GetScheduledRunInput, GetScheduledRunOutput
from .direct_models.get_vault_app_link import GetVaultAppLinkInput, GetVaultAppLinkOutput
from .direct_models.get_vault_contract import GetVaultContractInput, GetVaultContractOutput
from .direct_models.library_ingest import LibraryIngestInput, LibraryIngestOutput
from .direct_models.list_artifact_templates import ListArtifactTemplatesInput, ListArtifactTemplatesOutput
from .direct_models.list_channel_members import ListChannelMembersInput, ListChannelMembersOutput
from .direct_models.list_channel_messages import ListChannelMessagesInput, ListChannelMessagesOutput
from .direct_models.list_memory_tags import ListMemoryTagsInput, ListMemoryTagsOutput
from .direct_models.list_scheduled_action_runs import ListScheduledActionRunsInput, ListScheduledActionRunsOutput
from .direct_models.list_scheduled_actions import ListScheduledActionsInput, ListScheduledActionsOutput
from .direct_models.list_scheduled_runs import ListScheduledRunsInput, ListScheduledRunsOutput
from .direct_models.list_shared_with_me import ListSharedWithMeInput, ListSharedWithMeOutput
from .direct_models.list_vaults import ListVaultsInput, ListVaultsOutput
from .direct_models.list_webhooks import ListWebhooksInput, ListWebhooksOutput
from .direct_models.mark_scheduled_run_opened import MarkScheduledRunOpenedInput, MarkScheduledRunOpenedOutput
from .direct_models.mark_scheduled_run_unopened import MarkScheduledRunUnopenedInput, MarkScheduledRunUnopenedOutput
from .direct_models.memory_backlinks import MemoryBacklinksInput, MemoryBacklinksOutput
from .direct_models.memory_capture import MemoryCaptureInput, MemoryCaptureOutput
from .direct_models.memory_export import MemoryExportInput, MemoryExportOutput
from .direct_models.memory_get import MemoryGetInput, MemoryGetOutput
from .direct_models.memory_graph_path import MemoryGraphPathInput, MemoryGraphPathOutput
from .direct_models.memory_graph_universe import MemoryGraphUniverseInput, MemoryGraphUniverseOutput
from .direct_models.memory_list import MemoryListInput, MemoryListOutput
from .direct_models.memory_put import MemoryPutInput, MemoryPutOutput
from .direct_models.memory_questions import MemoryQuestionsInput, MemoryQuestionsOutput
from .direct_models.memory_search import MemorySearchInput, MemorySearchOutput
from .direct_models.memory_suggest import MemorySuggestInput, MemorySuggestOutput
from .direct_models.memory_upload import MemoryUploadInput, MemoryUploadOutput
from .direct_models.merge_memory_tags import MergeMemoryTagsInput, MergeMemoryTagsOutput
from .direct_models.my_mentions import MyMentionsInput, MyMentionsOutput
from .direct_models.pause_scheduled_action import PauseScheduledActionInput, PauseScheduledActionOutput
from .direct_models.poll_channel import PollChannelInput, PollChannelOutput
from .direct_models.post_message import PostMessageInput, PostMessageOutput
from .direct_models.prepare_memory_write import PrepareMemoryWriteInput, PrepareMemoryWriteOutput
from .direct_models.propose_scheduled_action import ProposeScheduledActionInput, ProposeScheduledActionOutput
from .direct_models.provision_defaults import ProvisionDefaultsInput, ProvisionDefaultsOutput
from .direct_models.react_message import ReactMessageInput, ReactMessageOutput
from .direct_models.record_fact import RecordFactInput, RecordFactOutput
from .direct_models.remove_channel_member import RemoveChannelMemberInput, RemoveChannelMemberOutput
from .direct_models.reply_message import ReplyMessageInput, ReplyMessageOutput
from .direct_models.resolve_memory_tags import ResolveMemoryTagsInput, ResolveMemoryTagsOutput
from .direct_models.resume_scheduled_action import ResumeScheduledActionInput, ResumeScheduledActionOutput
from .direct_models.revoke_chat_link import RevokeChatLinkInput, RevokeChatLinkOutput
from .direct_models.revoke_schedule_link import RevokeScheduleLinkInput, RevokeScheduleLinkOutput
from .direct_models.revoke_vault_app_link import RevokeVaultAppLinkInput, RevokeVaultAppLinkOutput
from .direct_models.revoke_webhook import RevokeWebhookInput, RevokeWebhookOutput
from .direct_models.route_memory import RouteMemoryInput, RouteMemoryOutput
from .direct_models.set_agent_identity import SetAgentIdentityInput, SetAgentIdentityOutput
from .direct_models.set_schedule_defaults import SetScheduleDefaultsInput, SetScheduleDefaultsOutput
from .direct_models.set_schedule_entitlement import SetScheduleEntitlementInput, SetScheduleEntitlementOutput
from .direct_models.storage_usage import StorageUsageInput, StorageUsageOutput
from .direct_models.table_create import TableCreateInput, TableCreateOutput
from .direct_models.table_delete_rows import TableDeleteRowsInput, TableDeleteRowsOutput
from .direct_models.table_describe import TableDescribeInput, TableDescribeOutput
from .direct_models.table_drop import TableDropInput, TableDropOutput
from .direct_models.table_insert_rows import TableInsertRowsInput, TableInsertRowsOutput
from .direct_models.table_list import TableListInput, TableListOutput
from .direct_models.table_query import TableQueryInput, TableQueryOutput
from .direct_models.temporal_recall import TemporalRecallInput, TemporalRecallOutput
from .direct_models.update_artifact_template import UpdateArtifactTemplateInput, UpdateArtifactTemplateOutput
from .direct_models.update_scheduled_action import UpdateScheduledActionInput, UpdateScheduledActionOutput
from .direct_models.upsert_memory_tag import UpsertMemoryTagInput, UpsertMemoryTagOutput
from .direct_models.validate_memory_write import ValidateMemoryWriteInput, ValidateMemoryWriteOutput
from .direct_models.video_analyze_start import VideoAnalyzeStartInput, VideoAnalyzeStartOutput
from .direct_models.video_analyze_status import VideoAnalyzeStatusInput, VideoAnalyzeStatusOutput


class AccessNamespace:
    def __init__(self, call_tool):
        self._call_tool = call_tool

    def accept_share(self, **kwargs: Any) -> AccessAcceptShareOutput:
        payload = AccessAcceptShareInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("acceptShareTool", payload)
        return AccessAcceptShareOutput.model_validate(result)

    def approve_sender(self, **kwargs: Any) -> AccessApproveSenderOutput:
        payload = AccessApproveSenderInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("approveSenderTool", payload)
        return AccessApproveSenderOutput.model_validate(result)

    def decline_share(self, **kwargs: Any) -> AccessDeclineShareOutput:
        payload = AccessDeclineShareInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("declineShareTool", payload)
        return AccessDeclineShareOutput.model_validate(result)

    def get_chat_link(self, **kwargs: Any) -> GetChatLinkOutput:
        payload = GetChatLinkInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("getChatLinkTool", payload)
        return GetChatLinkOutput.model_validate(result)

    def get_vault_app_link(self, **kwargs: Any) -> GetVaultAppLinkOutput:
        payload = GetVaultAppLinkInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("getVaultAppLinkTool", payload)
        return GetVaultAppLinkOutput.model_validate(result)

    def inbox_settings(self, **kwargs: Any) -> AccessInboxSettingsOutput:
        payload = AccessInboxSettingsInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("inboxSettingsTool", payload)
        return AccessInboxSettingsOutput.model_validate(result)

    def invite_account(self, **kwargs: Any) -> AccessInviteAccountOutput:
        payload = AccessInviteAccountInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("inviteAccountTool", payload)
        return AccessInviteAccountOutput.model_validate(result)

    def issue_key(self, **kwargs: Any) -> AccessIssueKeyOutput:
        payload = AccessIssueKeyInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("issueKeyTool", payload)
        return AccessIssueKeyOutput.model_validate(result)

    def list_approved_senders(self, **kwargs: Any) -> AccessListApprovedSendersOutput:
        payload = AccessListApprovedSendersInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("listApprovedSendersTool", payload)
        return AccessListApprovedSendersOutput.model_validate(result)

    def list_keys(self, **kwargs: Any) -> AccessListKeysOutput:
        payload = AccessListKeysInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("listKeysTool", payload)
        return AccessListKeysOutput.model_validate(result)

    def note_inbox(self, **kwargs: Any) -> AccessNoteInboxOutput:
        payload = AccessNoteInboxInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("noteInboxTool", payload)
        return AccessNoteInboxOutput.model_validate(result)

    def remove_approved_sender(self, **kwargs: Any) -> AccessRemoveApprovedSenderOutput:
        payload = AccessRemoveApprovedSenderInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("removeApprovedSenderTool", payload)
        return AccessRemoveApprovedSenderOutput.model_validate(result)

    def revoke_chat_link(self, **kwargs: Any) -> RevokeChatLinkOutput:
        payload = RevokeChatLinkInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("revokeChatLinkTool", payload)
        return RevokeChatLinkOutput.model_validate(result)

    def revoke_key(self, **kwargs: Any) -> AccessRevokeKeyOutput:
        payload = AccessRevokeKeyInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("revokeKeyTool", payload)
        return AccessRevokeKeyOutput.model_validate(result)

    def revoke_share(self, **kwargs: Any) -> AccessRevokeShareOutput:
        payload = AccessRevokeShareInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("revokeShareTool", payload)
        return AccessRevokeShareOutput.model_validate(result)

    def revoke_vault_app_link(self, **kwargs: Any) -> RevokeVaultAppLinkOutput:
        payload = RevokeVaultAppLinkInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("revokeVaultAppLinkTool", payload)
        return RevokeVaultAppLinkOutput.model_validate(result)

    def set_agent_identity(self, **kwargs: Any) -> SetAgentIdentityOutput:
        payload = SetAgentIdentityInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("setAgentIdentityTool", payload)
        return SetAgentIdentityOutput.model_validate(result)

    def set_scope(self, **kwargs: Any) -> AccessSetScopeOutput:
        payload = AccessSetScopeInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("setScopeTool", payload)
        return AccessSetScopeOutput.model_validate(result)

    def share_note(self, **kwargs: Any) -> AccessShareNoteOutput:
        payload = AccessShareNoteInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("shareNoteTool", payload)
        return AccessShareNoteOutput.model_validate(result)

    def share_vault(self, **kwargs: Any) -> AccessShareVaultOutput:
        payload = AccessShareVaultInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("shareVaultTool", payload)
        return AccessShareVaultOutput.model_validate(result)

    def swap_vault(self, **kwargs: Any) -> AccessSwapVaultOutput:
        payload = AccessSwapVaultInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("swapVaultTool", payload)
        return AccessSwapVaultOutput.model_validate(result)

    def switch_account(self, **kwargs: Any) -> AccessSwitchAccountOutput:
        payload = AccessSwitchAccountInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("switchAccountTool", payload)
        return AccessSwitchAccountOutput.model_validate(result)

    def unlink_share(self, **kwargs: Any) -> AccessUnlinkShareOutput:
        payload = AccessUnlinkShareInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("unlinkShareTool", payload)
        return AccessUnlinkShareOutput.model_validate(result)


class AssistantNamespace:
    def __init__(self, call_tool):
        self._call_tool = call_tool

    def context_packet_create(self, **kwargs: Any) -> AssistantContextPacketCreateOutput:
        payload = AssistantContextPacketCreateInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("assistant_context_packet_create", payload)
        return AssistantContextPacketCreateOutput.model_validate(result)

    def context_packet_get(self, **kwargs: Any) -> AssistantContextPacketGetOutput:
        payload = AssistantContextPacketGetInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("assistant_context_packet_get", payload)
        return AssistantContextPacketGetOutput.model_validate(result)

    def context_packet_lifecycle(self, **kwargs: Any) -> AssistantContextPacketLifecycleOutput:
        payload = AssistantContextPacketLifecycleInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("assistant_context_packet_lifecycle", payload)
        return AssistantContextPacketLifecycleOutput.model_validate(result)

    def context_packet_list(self, **kwargs: Any) -> AssistantContextPacketListOutput:
        payload = AssistantContextPacketListInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("assistant_context_packet_list", payload)
        return AssistantContextPacketListOutput.model_validate(result)

    def context_packet_share_accept(self, **kwargs: Any) -> AssistantContextPacketShareAcceptOutput:
        payload = AssistantContextPacketShareAcceptInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("assistant_context_packet_share_accept", payload)
        return AssistantContextPacketShareAcceptOutput.model_validate(result)


class CaptureNamespace:
    def __init__(self, call_tool):
        self._call_tool = call_tool

    def memory_capture(self, **kwargs: Any) -> MemoryCaptureOutput:
        payload = MemoryCaptureInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("memoryCaptureTool", payload)
        return MemoryCaptureOutput.model_validate(result)

    def memory_questions(self, **kwargs: Any) -> MemoryQuestionsOutput:
        payload = MemoryQuestionsInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("memoryQuestionsTool", payload)
        return MemoryQuestionsOutput.model_validate(result)

    def prepare_memory_write(self, **kwargs: Any) -> PrepareMemoryWriteOutput:
        payload = PrepareMemoryWriteInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("prepareMemoryWriteTool", payload)
        return PrepareMemoryWriteOutput.model_validate(result)

    def validate_memory_write(self, **kwargs: Any) -> ValidateMemoryWriteOutput:
        payload = ValidateMemoryWriteInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("validateMemoryWriteTool", payload)
        return ValidateMemoryWriteOutput.model_validate(result)


class ChannelsNamespace:
    def __init__(self, call_tool):
        self._call_tool = call_tool

    def create_channel(self, **kwargs: Any) -> CreateChannelOutput:
        payload = CreateChannelInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("createChannelTool", payload)
        return CreateChannelOutput.model_validate(result)

    def get_message_note(self, **kwargs: Any) -> GetMessageNoteOutput:
        payload = GetMessageNoteInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("getMessageNoteTool", payload)
        return GetMessageNoteOutput.model_validate(result)

    def list_channel_members(self, **kwargs: Any) -> ListChannelMembersOutput:
        payload = ListChannelMembersInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("listChannelMembersTool", payload)
        return ListChannelMembersOutput.model_validate(result)

    def list_channel_messages(self, **kwargs: Any) -> ListChannelMessagesOutput:
        payload = ListChannelMessagesInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("listChannelMessagesTool", payload)
        return ListChannelMessagesOutput.model_validate(result)

    def my_mentions(self, **kwargs: Any) -> MyMentionsOutput:
        payload = MyMentionsInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("myMentionsTool", payload)
        return MyMentionsOutput.model_validate(result)

    def poll_channel(self, **kwargs: Any) -> PollChannelOutput:
        payload = PollChannelInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("pollChannelTool", payload)
        return PollChannelOutput.model_validate(result)

    def post_message(self, **kwargs: Any) -> PostMessageOutput:
        payload = PostMessageInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("postMessageTool", payload)
        return PostMessageOutput.model_validate(result)

    def react_message(self, **kwargs: Any) -> ReactMessageOutput:
        payload = ReactMessageInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("reactMessageTool", payload)
        return ReactMessageOutput.model_validate(result)

    def remove_channel_member(self, **kwargs: Any) -> RemoveChannelMemberOutput:
        payload = RemoveChannelMemberInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("removeChannelMemberTool", payload)
        return RemoveChannelMemberOutput.model_validate(result)

    def reply_message(self, **kwargs: Any) -> ReplyMessageOutput:
        payload = ReplyMessageInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("replyMessageTool", payload)
        return ReplyMessageOutput.model_validate(result)


class FactsNamespace:
    def __init__(self, call_tool):
        self._call_tool = call_tool

    def history(self, **kwargs: Any) -> FactHistoryOutput:
        payload = FactHistoryInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("factHistoryTool", payload)
        return FactHistoryOutput.model_validate(result)

    def record_fact(self, **kwargs: Any) -> RecordFactOutput:
        payload = RecordFactInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("recordFactTool", payload)
        return RecordFactOutput.model_validate(result)


class GraphNamespace:
    def __init__(self, call_tool):
        self._call_tool = call_tool

    def memory_graph_path(self, **kwargs: Any) -> MemoryGraphPathOutput:
        payload = MemoryGraphPathInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("graphPathTool", payload)
        return MemoryGraphPathOutput.model_validate(result)

    def memory_graph_universe(self, **kwargs: Any) -> MemoryGraphUniverseOutput:
        payload = MemoryGraphUniverseInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("graphUniverseTool", payload)
        return MemoryGraphUniverseOutput.model_validate(result)

    def memory_backlinks(self, **kwargs: Any) -> MemoryBacklinksOutput:
        payload = MemoryBacklinksInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("noteBacklinksTool", payload)
        return MemoryBacklinksOutput.model_validate(result)


class LibraryNamespace:
    def __init__(self, call_tool):
        self._call_tool = call_tool

    def ingest(self, **kwargs: Any) -> LibraryIngestOutput:
        payload = LibraryIngestInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("libraryIngestTool", payload)
        return LibraryIngestOutput.model_validate(result)


class MemoryNamespace:
    def __init__(self, call_tool):
        self._call_tool = call_tool

    def bulk_delete_notes(self, **kwargs: Any) -> BulkDeleteNotesOutput:
        payload = BulkDeleteNotesInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("bulkDeleteNotesTool", payload)
        return BulkDeleteNotesOutput.model_validate(result)

    def delete_note(self, **kwargs: Any) -> DeleteNoteOutput:
        payload = DeleteNoteInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("deleteNoteTool", payload)
        return DeleteNoteOutput.model_validate(result)

    def export(self, **kwargs: Any) -> MemoryExportOutput:
        payload = MemoryExportInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("exportTool", payload)
        return MemoryExportOutput.model_validate(result)

    def get(self, **kwargs: Any) -> MemoryGetOutput:
        payload = MemoryGetInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("getTool", payload)
        return MemoryGetOutput.model_validate(result)

    def list(self, **kwargs: Any) -> MemoryListOutput:
        payload = MemoryListInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("listTool", payload)
        return MemoryListOutput.model_validate(result)

    def put(self, **kwargs: Any) -> MemoryPutOutput:
        payload = MemoryPutInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("putTool", payload)
        return MemoryPutOutput.model_validate(result)

    def search(self, **kwargs: Any) -> MemorySearchOutput:
        payload = MemorySearchInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("searchTool", payload)
        return MemorySearchOutput.model_validate(result)

    def suggest(self, **kwargs: Any) -> MemorySuggestOutput:
        payload = MemorySuggestInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("suggestTool", payload)
        return MemorySuggestOutput.model_validate(result)

    def upload(self, **kwargs: Any) -> MemoryUploadOutput:
        payload = MemoryUploadInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("uploadTool", payload)
        return MemoryUploadOutput.model_validate(result)


class RecallNamespace:
    def __init__(self, call_tool):
        self._call_tool = call_tool

    def temporal_recall(self, **kwargs: Any) -> TemporalRecallOutput:
        payload = TemporalRecallInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("temporalRecallTool", payload)
        return TemporalRecallOutput.model_validate(result)


class ScheduleNamespace:
    def __init__(self, call_tool):
        self._call_tool = call_tool

    def answer_inbox_item(self, **kwargs: Any) -> AnswerInboxItemOutput:
        payload = AnswerInboxItemInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("answerInboxItemTool", payload)
        return AnswerInboxItemOutput.model_validate(result)

    def archive_artifact_template(self, **kwargs: Any) -> ArchiveArtifactTemplateOutput:
        payload = ArchiveArtifactTemplateInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("archive_artifact_template", payload)
        return ArchiveArtifactTemplateOutput.model_validate(result)

    def archive_scheduled_run(self, **kwargs: Any) -> ArchiveScheduledRunOutput:
        payload = ArchiveScheduledRunInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("archive_scheduled_run", payload)
        return ArchiveScheduledRunOutput.model_validate(result)

    def auto_optimization(self, **kwargs: Any) -> AutoOptimizationOutput:
        payload = AutoOptimizationInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("autoOptimizationTool", payload)
        return AutoOptimizationOutput.model_validate(result)

    def create_artifact_template(self, **kwargs: Any) -> CreateArtifactTemplateOutput:
        payload = CreateArtifactTemplateInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("create_artifact_template", payload)
        return CreateArtifactTemplateOutput.model_validate(result)

    def create_scheduled_action(self, **kwargs: Any) -> CreateScheduledActionOutput:
        payload = CreateScheduledActionInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("createScheduledActionTool", payload)
        return CreateScheduledActionOutput.model_validate(result)

    def delete_scheduled_action(self, **kwargs: Any) -> DeleteScheduledActionOutput:
        payload = DeleteScheduledActionInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("deleteScheduledActionTool", payload)
        return DeleteScheduledActionOutput.model_validate(result)

    def get_artifact_template(self, **kwargs: Any) -> GetArtifactTemplateOutput:
        payload = GetArtifactTemplateInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("get_artifact_template", payload)
        return GetArtifactTemplateOutput.model_validate(result)

    def get_scheduled_run(self, **kwargs: Any) -> GetScheduledRunOutput:
        payload = GetScheduledRunInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("get_scheduled_run", payload)
        return GetScheduledRunOutput.model_validate(result)

    def get_schedule_link(self, **kwargs: Any) -> GetScheduleLinkOutput:
        payload = GetScheduleLinkInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("getScheduleLinkTool", payload)
        return GetScheduleLinkOutput.model_validate(result)

    def get_schedule_status(self, **kwargs: Any) -> GetScheduleStatusOutput:
        payload = GetScheduleStatusInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("getScheduleStatusTool", payload)
        return GetScheduleStatusOutput.model_validate(result)

    def list_artifact_templates(self, **kwargs: Any) -> ListArtifactTemplatesOutput:
        payload = ListArtifactTemplatesInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("list_artifact_templates", payload)
        return ListArtifactTemplatesOutput.model_validate(result)

    def list_scheduled_runs(self, **kwargs: Any) -> ListScheduledRunsOutput:
        payload = ListScheduledRunsInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("list_scheduled_runs", payload)
        return ListScheduledRunsOutput.model_validate(result)

    def list_scheduled_action_runs(self, **kwargs: Any) -> ListScheduledActionRunsOutput:
        payload = ListScheduledActionRunsInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("listScheduledActionRunsTool", payload)
        return ListScheduledActionRunsOutput.model_validate(result)

    def list_scheduled_actions(self, **kwargs: Any) -> ListScheduledActionsOutput:
        payload = ListScheduledActionsInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("listScheduledActionsTool", payload)
        return ListScheduledActionsOutput.model_validate(result)

    def mark_scheduled_run_opened(self, **kwargs: Any) -> MarkScheduledRunOpenedOutput:
        payload = MarkScheduledRunOpenedInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("mark_scheduled_run_opened", payload)
        return MarkScheduledRunOpenedOutput.model_validate(result)

    def mark_scheduled_run_unopened(self, **kwargs: Any) -> MarkScheduledRunUnopenedOutput:
        payload = MarkScheduledRunUnopenedInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("mark_scheduled_run_unopened", payload)
        return MarkScheduledRunUnopenedOutput.model_validate(result)

    def pause_scheduled_action(self, **kwargs: Any) -> PauseScheduledActionOutput:
        payload = PauseScheduledActionInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("pauseScheduledActionTool", payload)
        return PauseScheduledActionOutput.model_validate(result)

    def propose_scheduled_action(self, **kwargs: Any) -> ProposeScheduledActionOutput:
        payload = ProposeScheduledActionInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("proposeScheduledActionTool", payload)
        return ProposeScheduledActionOutput.model_validate(result)

    def resume_scheduled_action(self, **kwargs: Any) -> ResumeScheduledActionOutput:
        payload = ResumeScheduledActionInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("resumeScheduledActionTool", payload)
        return ResumeScheduledActionOutput.model_validate(result)

    def revoke_schedule_link(self, **kwargs: Any) -> RevokeScheduleLinkOutput:
        payload = RevokeScheduleLinkInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("revokeScheduleLinkTool", payload)
        return RevokeScheduleLinkOutput.model_validate(result)

    def set_schedule_defaults(self, **kwargs: Any) -> SetScheduleDefaultsOutput:
        payload = SetScheduleDefaultsInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("setScheduleDefaultsTool", payload)
        return SetScheduleDefaultsOutput.model_validate(result)

    def set_schedule_entitlement(self, **kwargs: Any) -> SetScheduleEntitlementOutput:
        payload = SetScheduleEntitlementInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("setScheduleEntitlementTool", payload)
        return SetScheduleEntitlementOutput.model_validate(result)

    def update_artifact_template(self, **kwargs: Any) -> UpdateArtifactTemplateOutput:
        payload = UpdateArtifactTemplateInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("update_artifact_template", payload)
        return UpdateArtifactTemplateOutput.model_validate(result)

    def update_scheduled_action(self, **kwargs: Any) -> UpdateScheduledActionOutput:
        payload = UpdateScheduledActionInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("updateScheduledActionTool", payload)
        return UpdateScheduledActionOutput.model_validate(result)


class StorageNamespace:
    def __init__(self, call_tool):
        self._call_tool = call_tool

    def cost_usage(self, **kwargs: Any) -> CostUsageOutput:
        payload = CostUsageInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("costUsageTool", payload)
        return CostUsageOutput.model_validate(result)

    def usage(self, **kwargs: Any) -> StorageUsageOutput:
        payload = StorageUsageInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("storageUsageTool", payload)
        return StorageUsageOutput.model_validate(result)


class TablesNamespace:
    def __init__(self, call_tool):
        self._call_tool = call_tool

    def create(self, **kwargs: Any) -> TableCreateOutput:
        payload = TableCreateInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("createTableTool", payload)
        return TableCreateOutput.model_validate(result)

    def delete_rows(self, **kwargs: Any) -> TableDeleteRowsOutput:
        payload = TableDeleteRowsInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("deleteTableRowsTool", payload)
        return TableDeleteRowsOutput.model_validate(result)

    def describe(self, **kwargs: Any) -> TableDescribeOutput:
        payload = TableDescribeInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("describeTableTool", payload)
        return TableDescribeOutput.model_validate(result)

    def drop(self, **kwargs: Any) -> TableDropOutput:
        payload = TableDropInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("dropTableTool", payload)
        return TableDropOutput.model_validate(result)

    def insert_rows(self, **kwargs: Any) -> TableInsertRowsOutput:
        payload = TableInsertRowsInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("insertTableRowsTool", payload)
        return TableInsertRowsOutput.model_validate(result)

    def list(self, **kwargs: Any) -> TableListOutput:
        payload = TableListInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("listTablesTool", payload)
        return TableListOutput.model_validate(result)

    def query(self, **kwargs: Any) -> TableQueryOutput:
        payload = TableQueryInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("queryTableTool", payload)
        return TableQueryOutput.model_validate(result)


class TagsNamespace:
    def __init__(self, call_tool):
        self._call_tool = call_tool

    def list_memory_tags(self, **kwargs: Any) -> ListMemoryTagsOutput:
        payload = ListMemoryTagsInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("listTagsTool", payload)
        return ListMemoryTagsOutput.model_validate(result)

    def merge_memory_tags(self, **kwargs: Any) -> MergeMemoryTagsOutput:
        payload = MergeMemoryTagsInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("mergeTagsTool", payload)
        return MergeMemoryTagsOutput.model_validate(result)

    def resolve_memory_tags(self, **kwargs: Any) -> ResolveMemoryTagsOutput:
        payload = ResolveMemoryTagsInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("resolveTagsTool", payload)
        return ResolveMemoryTagsOutput.model_validate(result)

    def upsert_memory_tag(self, **kwargs: Any) -> UpsertMemoryTagOutput:
        payload = UpsertMemoryTagInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("upsertTagTool", payload)
        return UpsertMemoryTagOutput.model_validate(result)


class VaultsNamespace:
    def __init__(self, call_tool):
        self._call_tool = call_tool

    def add_vault(self, **kwargs: Any) -> AddVaultOutput:
        payload = AddVaultInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("addVaultTool", payload)
        return AddVaultOutput.model_validate(result)

    def create_secure_vault(self, **kwargs: Any) -> CreateSecureVaultOutput:
        payload = CreateSecureVaultInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("createSecureVaultTool", payload)
        return CreateSecureVaultOutput.model_validate(result)

    def delete_vault(self, **kwargs: Any) -> DeleteVaultOutput:
        payload = DeleteVaultInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("deleteVaultTool", payload)
        return DeleteVaultOutput.model_validate(result)

    def get_vault_contract(self, **kwargs: Any) -> GetVaultContractOutput:
        payload = GetVaultContractInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("getVaultContractTool", payload)
        return GetVaultContractOutput.model_validate(result)

    def list_shared_with_me(self, **kwargs: Any) -> ListSharedWithMeOutput:
        payload = ListSharedWithMeInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("listSharedWithMeTool", payload)
        return ListSharedWithMeOutput.model_validate(result)

    def list_vaults(self, **kwargs: Any) -> ListVaultsOutput:
        payload = ListVaultsInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("listVaultsTool", payload)
        return ListVaultsOutput.model_validate(result)

    def provision_defaults(self, **kwargs: Any) -> ProvisionDefaultsOutput:
        payload = ProvisionDefaultsInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("provisionDefaultsTool", payload)
        return ProvisionDefaultsOutput.model_validate(result)

    def route_memory(self, **kwargs: Any) -> RouteMemoryOutput:
        payload = RouteMemoryInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("routeMemoryTool", payload)
        return RouteMemoryOutput.model_validate(result)


class VideoNamespace:
    def __init__(self, call_tool):
        self._call_tool = call_tool

    def analyze_start(self, **kwargs: Any) -> VideoAnalyzeStartOutput:
        payload = VideoAnalyzeStartInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("videoAnalyzeStartTool", payload)
        return VideoAnalyzeStartOutput.model_validate(result)

    def analyze_status(self, **kwargs: Any) -> VideoAnalyzeStatusOutput:
        payload = VideoAnalyzeStatusInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("videoAnalyzeStatusTool", payload)
        return VideoAnalyzeStatusOutput.model_validate(result)


class WebhooksNamespace:
    def __init__(self, call_tool):
        self._call_tool = call_tool

    def create_webhook(self, **kwargs: Any) -> CreateWebhookOutput:
        payload = CreateWebhookInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("createWebhookTool", payload)
        return CreateWebhookOutput.model_validate(result)

    def list_webhooks(self, **kwargs: Any) -> ListWebhooksOutput:
        payload = ListWebhooksInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("listWebhooksTool", payload)
        return ListWebhooksOutput.model_validate(result)

    def revoke_webhook(self, **kwargs: Any) -> RevokeWebhookOutput:
        payload = RevokeWebhookInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("revokeWebhookTool", payload)
        return RevokeWebhookOutput.model_validate(result)
