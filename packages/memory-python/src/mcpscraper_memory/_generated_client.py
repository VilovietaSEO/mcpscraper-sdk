from typing import Any, Callable

from .models.access_accept_share import AccessAcceptShareInput, AccessAcceptShareOutput
from .models.access_approve_sender import AccessApproveSenderInput, AccessApproveSenderOutput
from .models.access_decline_share import AccessDeclineShareInput, AccessDeclineShareOutput
from .models.access_inbox_settings import AccessInboxSettingsInput, AccessInboxSettingsOutput
from .models.access_invite_account import AccessInviteAccountInput, AccessInviteAccountOutput
from .models.access_issue_key import AccessIssueKeyInput, AccessIssueKeyOutput
from .models.access_list_approved_senders import AccessListApprovedSendersInput, AccessListApprovedSendersOutput
from .models.access_list_keys import AccessListKeysInput, AccessListKeysOutput
from .models.access_note_inbox import AccessNoteInboxInput, AccessNoteInboxOutput
from .models.access_remove_approved_sender import AccessRemoveApprovedSenderInput, AccessRemoveApprovedSenderOutput
from .models.access_revoke_key import AccessRevokeKeyInput, AccessRevokeKeyOutput
from .models.access_revoke_share import AccessRevokeShareInput, AccessRevokeShareOutput
from .models.access_set_scope import AccessSetScopeInput, AccessSetScopeOutput
from .models.access_share_note import AccessShareNoteInput, AccessShareNoteOutput
from .models.access_share_vault import AccessShareVaultInput, AccessShareVaultOutput
from .models.access_swap_vault import AccessSwapVaultInput, AccessSwapVaultOutput
from .models.access_switch_account import AccessSwitchAccountInput, AccessSwitchAccountOutput
from .models.access_unlink_share import AccessUnlinkShareInput, AccessUnlinkShareOutput
from .models.add_vault import AddVaultInput, AddVaultOutput
from .models.cost_usage import CostUsageInput, CostUsageOutput
from .models.create_channel import CreateChannelInput, CreateChannelOutput
from .models.create_scheduled_action import CreateScheduledActionInput, CreateScheduledActionOutput
from .models.create_secure_vault import CreateSecureVaultInput, CreateSecureVaultOutput
from .models.create_webhook import CreateWebhookInput, CreateWebhookOutput
from .models.delete_note import DeleteNoteInput, DeleteNoteOutput
from .models.delete_scheduled_action import DeleteScheduledActionInput, DeleteScheduledActionOutput
from .models.delete_vault import DeleteVaultInput, DeleteVaultOutput
from .models.fact_history import FactHistoryInput, FactHistoryOutput
from .models.get_chat_link import GetChatLinkInput, GetChatLinkOutput
from .models.get_message_note import GetMessageNoteInput, GetMessageNoteOutput
from .models.get_schedule_link import GetScheduleLinkInput, GetScheduleLinkOutput
from .models.get_schedule_status import GetScheduleStatusInput, GetScheduleStatusOutput
from .models.library_ingest import LibraryIngestInput, LibraryIngestOutput
from .models.list_channel_members import ListChannelMembersInput, ListChannelMembersOutput
from .models.list_channel_messages import ListChannelMessagesInput, ListChannelMessagesOutput
from .models.list_scheduled_actions import ListScheduledActionsInput, ListScheduledActionsOutput
from .models.list_shared_with_me import ListSharedWithMeInput, ListSharedWithMeOutput
from .models.list_vaults import ListVaultsInput, ListVaultsOutput
from .models.list_webhooks import ListWebhooksInput, ListWebhooksOutput
from .models.memory_export import MemoryExportInput, MemoryExportOutput
from .models.memory_get import MemoryGetInput, MemoryGetOutput
from .models.memory_list import MemoryListInput, MemoryListOutput
from .models.memory_put import MemoryPutInput, MemoryPutOutput
from .models.memory_questions import MemoryQuestionsInput, MemoryQuestionsOutput
from .models.memory_search import MemorySearchInput, MemorySearchOutput
from .models.memory_suggest import MemorySuggestInput, MemorySuggestOutput
from .models.memory_upload import MemoryUploadInput, MemoryUploadOutput
from .models.my_mentions import MyMentionsInput, MyMentionsOutput
from .models.pause_scheduled_action import PauseScheduledActionInput, PauseScheduledActionOutput
from .models.poll_channel import PollChannelInput, PollChannelOutput
from .models.post_message import PostMessageInput, PostMessageOutput
from .models.propose_scheduled_action import ProposeScheduledActionInput, ProposeScheduledActionOutput
from .models.provision_defaults import ProvisionDefaultsInput, ProvisionDefaultsOutput
from .models.react_message import ReactMessageInput, ReactMessageOutput
from .models.record_fact import RecordFactInput, RecordFactOutput
from .models.remove_channel_member import RemoveChannelMemberInput, RemoveChannelMemberOutput
from .models.reply_message import ReplyMessageInput, ReplyMessageOutput
from .models.resume_scheduled_action import ResumeScheduledActionInput, ResumeScheduledActionOutput
from .models.revoke_chat_link import RevokeChatLinkInput, RevokeChatLinkOutput
from .models.revoke_schedule_link import RevokeScheduleLinkInput, RevokeScheduleLinkOutput
from .models.revoke_webhook import RevokeWebhookInput, RevokeWebhookOutput
from .models.set_agent_identity import SetAgentIdentityInput, SetAgentIdentityOutput
from .models.set_schedule_entitlement import SetScheduleEntitlementInput, SetScheduleEntitlementOutput
from .models.storage_usage import StorageUsageInput, StorageUsageOutput
from .models.table_create import TableCreateInput, TableCreateOutput
from .models.table_delete_rows import TableDeleteRowsInput, TableDeleteRowsOutput
from .models.table_describe import TableDescribeInput, TableDescribeOutput
from .models.table_drop import TableDropInput, TableDropOutput
from .models.table_insert_rows import TableInsertRowsInput, TableInsertRowsOutput
from .models.table_list import TableListInput, TableListOutput
from .models.table_query import TableQueryInput, TableQueryOutput
from .models.temporal_recall import TemporalRecallInput, TemporalRecallOutput
from .models.video_analyze_start import VideoAnalyzeStartInput, VideoAnalyzeStartOutput
from .models.video_analyze_status import VideoAnalyzeStatusInput, VideoAnalyzeStatusOutput


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

    def revoke_key(self, **kwargs: Any) -> AccessRevokeKeyOutput:
        payload = AccessRevokeKeyInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("revokeKeyTool", payload)
        return AccessRevokeKeyOutput.model_validate(result)

    def revoke_share(self, **kwargs: Any) -> AccessRevokeShareOutput:
        payload = AccessRevokeShareInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("revokeShareTool", payload)
        return AccessRevokeShareOutput.model_validate(result)

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

    def get_chat_link(self, **kwargs: Any) -> GetChatLinkOutput:
        payload = GetChatLinkInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("getChatLinkTool", payload)
        return GetChatLinkOutput.model_validate(result)

    def revoke_chat_link(self, **kwargs: Any) -> RevokeChatLinkOutput:
        payload = RevokeChatLinkInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("revokeChatLinkTool", payload)
        return RevokeChatLinkOutput.model_validate(result)

    def set_agent_identity(self, **kwargs: Any) -> SetAgentIdentityOutput:
        payload = SetAgentIdentityInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("setAgentIdentityTool", payload)
        return SetAgentIdentityOutput.model_validate(result)


class CaptureNamespace:
    def __init__(self, call_tool):
        self._call_tool = call_tool

    def memory_questions(self, **kwargs: Any) -> MemoryQuestionsOutput:
        payload = MemoryQuestionsInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("memoryQuestionsTool", payload)
        return MemoryQuestionsOutput.model_validate(result)


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

    def create_scheduled_action(self, **kwargs: Any) -> CreateScheduledActionOutput:
        payload = CreateScheduledActionInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("createScheduledActionTool", payload)
        return CreateScheduledActionOutput.model_validate(result)

    def delete_scheduled_action(self, **kwargs: Any) -> DeleteScheduledActionOutput:
        payload = DeleteScheduledActionInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("deleteScheduledActionTool", payload)
        return DeleteScheduledActionOutput.model_validate(result)

    def get_schedule_link(self, **kwargs: Any) -> GetScheduleLinkOutput:
        payload = GetScheduleLinkInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("getScheduleLinkTool", payload)
        return GetScheduleLinkOutput.model_validate(result)

    def get_schedule_status(self, **kwargs: Any) -> GetScheduleStatusOutput:
        payload = GetScheduleStatusInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("getScheduleStatusTool", payload)
        return GetScheduleStatusOutput.model_validate(result)

    def list_scheduled_actions(self, **kwargs: Any) -> ListScheduledActionsOutput:
        payload = ListScheduledActionsInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("listScheduledActionsTool", payload)
        return ListScheduledActionsOutput.model_validate(result)

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

    def set_schedule_entitlement(self, **kwargs: Any) -> SetScheduleEntitlementOutput:
        payload = SetScheduleEntitlementInput(**kwargs).model_dump(by_alias=True, exclude_none=True)
        result = self._call_tool("setScheduleEntitlementTool", payload)
        return SetScheduleEntitlementOutput.model_validate(result)


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

