from ._artifact_delivery import ArtifactDelivery, validate_tool_output
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
from .models.archive_artifact_template import ArchiveArtifactTemplateInput, ArchiveArtifactTemplateOutput
from .models.bulk_delete_notes import BulkDeleteNotesInput, BulkDeleteNotesOutput
from .models.cost_usage import CostUsageInput, CostUsageOutput
from .models.create_artifact_template import CreateArtifactTemplateInput, CreateArtifactTemplateOutput
from .models.create_channel import CreateChannelInput, CreateChannelOutput
from .models.create_secure_vault import CreateSecureVaultInput, CreateSecureVaultOutput
from .models.create_webhook import CreateWebhookInput, CreateWebhookOutput
from .models.delete_note import DeleteNoteInput, DeleteNoteOutput
from .models.delete_vault import DeleteVaultInput, DeleteVaultOutput
from .models.fact_history import FactHistoryInput, FactHistoryOutput
from .models.file_asset_get import FileAssetGetInput, FileAssetGetOutput
from .models.file_asset_save import FileAssetSaveInput, FileAssetSaveOutput
from .models.get_artifact_template import GetArtifactTemplateInput, GetArtifactTemplateOutput
from .models.get_chat_link import GetChatLinkInput, GetChatLinkOutput
from .models.get_message_note import GetMessageNoteInput, GetMessageNoteOutput
from .models.get_vault_app_link import GetVaultAppLinkInput, GetVaultAppLinkOutput
from .models.get_vault_contract import GetVaultContractInput, GetVaultContractOutput
from .models.library_ingest import LibraryIngestInput, LibraryIngestOutput
from .models.list_artifact_templates import ListArtifactTemplatesInput, ListArtifactTemplatesOutput
from .models.list_channel_members import ListChannelMembersInput, ListChannelMembersOutput
from .models.list_channel_messages import ListChannelMessagesInput, ListChannelMessagesOutput
from .models.list_memory_tags import ListMemoryTagsInput, ListMemoryTagsOutput
from .models.list_shared_with_me import ListSharedWithMeInput, ListSharedWithMeOutput
from .models.list_vaults import ListVaultsInput, ListVaultsOutput
from .models.list_webhooks import ListWebhooksInput, ListWebhooksOutput
from .models.memory_backlinks import MemoryBacklinksInput, MemoryBacklinksOutput
from .models.memory_capture import MemoryCaptureInput, MemoryCaptureOutput
from .models.memory_export import MemoryExportInput, MemoryExportOutput
from .models.memory_get import MemoryGetInput, MemoryGetOutput
from .models.memory_graph_path import MemoryGraphPathInput, MemoryGraphPathOutput
from .models.memory_graph_universe import MemoryGraphUniverseInput, MemoryGraphUniverseOutput
from .models.memory_list import MemoryListInput, MemoryListOutput
from .models.memory_put import MemoryPutInput, MemoryPutOutput
from .models.memory_questions import MemoryQuestionsInput, MemoryQuestionsOutput
from .models.memory_search import MemorySearchInput, MemorySearchOutput
from .models.memory_suggest import MemorySuggestInput, MemorySuggestOutput
from .models.memory_upload import MemoryUploadInput, MemoryUploadOutput
from .models.merge_memory_tags import MergeMemoryTagsInput, MergeMemoryTagsOutput
from .models.my_mentions import MyMentionsInput, MyMentionsOutput
from .models.poll_channel import PollChannelInput, PollChannelOutput
from .models.post_message import PostMessageInput, PostMessageOutput
from .models.prepare_memory_write import PrepareMemoryWriteInput, PrepareMemoryWriteOutput
from .models.provision_defaults import ProvisionDefaultsInput, ProvisionDefaultsOutput
from .models.react_message import ReactMessageInput, ReactMessageOutput
from .models.record_fact import RecordFactInput, RecordFactOutput
from .models.remove_channel_member import RemoveChannelMemberInput, RemoveChannelMemberOutput
from .models.reply_message import ReplyMessageInput, ReplyMessageOutput
from .models.resolve_memory_tags import ResolveMemoryTagsInput, ResolveMemoryTagsOutput
from .models.revoke_chat_link import RevokeChatLinkInput, RevokeChatLinkOutput
from .models.revoke_vault_app_link import RevokeVaultAppLinkInput, RevokeVaultAppLinkOutput
from .models.revoke_webhook import RevokeWebhookInput, RevokeWebhookOutput
from .models.route_memory import RouteMemoryInput, RouteMemoryOutput
from .models.set_agent_identity import SetAgentIdentityInput, SetAgentIdentityOutput
from .models.storage_usage import StorageUsageInput, StorageUsageOutput
from .models.table_create import TableCreateInput, TableCreateOutput
from .models.table_delete_rows import TableDeleteRowsInput, TableDeleteRowsOutput
from .models.table_describe import TableDescribeInput, TableDescribeOutput
from .models.table_drop import TableDropInput, TableDropOutput
from .models.table_insert_rows import TableInsertRowsInput, TableInsertRowsOutput
from .models.table_list import TableListInput, TableListOutput
from .models.table_query import TableQueryInput, TableQueryOutput
from .models.temporal_recall import TemporalRecallInput, TemporalRecallOutput
from .models.update_artifact_template import UpdateArtifactTemplateInput, UpdateArtifactTemplateOutput
from .models.upsert_memory_tag import UpsertMemoryTagInput, UpsertMemoryTagOutput
from .models.validate_memory_write import ValidateMemoryWriteInput, ValidateMemoryWriteOutput
from .models.video_analyze_start import VideoAnalyzeStartInput, VideoAnalyzeStartOutput
from .models.video_analyze_status import VideoAnalyzeStatusInput, VideoAnalyzeStatusOutput


class AccessNamespace:

    def __init__(self, call_tool):
        self._call_tool = call_tool

    def issue_key(self, **kwargs: Any) -> AccessIssueKeyOutput | ArtifactDelivery:
        payload = AccessIssueKeyInput(**kwargs).model_dump(by_alias=True, exclude_unset=True)
        result = self._call_tool('issueKeyTool', payload)
        return validate_tool_output(result, AccessIssueKeyOutput)

    def list_keys(self, **kwargs: Any) -> AccessListKeysOutput | ArtifactDelivery:
        payload = AccessListKeysInput(**kwargs).model_dump(by_alias=True, exclude_unset=True)
        result = self._call_tool('listKeysTool', payload)
        return validate_tool_output(result, AccessListKeysOutput)

    def revoke_key(self, **kwargs: Any) -> AccessRevokeKeyOutput | ArtifactDelivery:
        payload = AccessRevokeKeyInput(**kwargs).model_dump(by_alias=True, exclude_unset=True)
        result = self._call_tool('revokeKeyTool', payload)
        return validate_tool_output(result, AccessRevokeKeyOutput)

    def set_scope(self, **kwargs: Any) -> AccessSetScopeOutput | ArtifactDelivery:
        payload = AccessSetScopeInput(**kwargs).model_dump(by_alias=True, exclude_unset=True)
        result = self._call_tool('setScopeTool', payload)
        return validate_tool_output(result, AccessSetScopeOutput)

    def share_vault(self, **kwargs: Any) -> AccessShareVaultOutput | ArtifactDelivery:
        payload = AccessShareVaultInput(**kwargs).model_dump(by_alias=True, exclude_unset=True)
        result = self._call_tool('shareVaultTool', payload)
        return validate_tool_output(result, AccessShareVaultOutput)

    def swap_vault(self, **kwargs: Any) -> AccessSwapVaultOutput | ArtifactDelivery:
        payload = AccessSwapVaultInput(**kwargs).model_dump(by_alias=True, exclude_unset=True)
        result = self._call_tool('swapVaultTool', payload)
        return validate_tool_output(result, AccessSwapVaultOutput)

    def invite_account(self, **kwargs: Any) -> AccessInviteAccountOutput | ArtifactDelivery:
        payload = AccessInviteAccountInput(**kwargs).model_dump(by_alias=True, exclude_unset=True)
        result = self._call_tool('inviteAccountTool', payload)
        return validate_tool_output(result, AccessInviteAccountOutput)

    def switch_account(self, **kwargs: Any) -> AccessSwitchAccountOutput | ArtifactDelivery:
        payload = AccessSwitchAccountInput(**kwargs).model_dump(by_alias=True, exclude_unset=True)
        result = self._call_tool('switchAccountTool', payload)
        return validate_tool_output(result, AccessSwitchAccountOutput)

    def approve_sender(self, **kwargs: Any) -> AccessApproveSenderOutput | ArtifactDelivery:
        payload = AccessApproveSenderInput(**kwargs).model_dump(by_alias=True, exclude_unset=True)
        result = self._call_tool('approveSenderTool', payload)
        return validate_tool_output(result, AccessApproveSenderOutput)

    def remove_approved_sender(self, **kwargs: Any) -> AccessRemoveApprovedSenderOutput | ArtifactDelivery:
        payload = AccessRemoveApprovedSenderInput(**kwargs).model_dump(by_alias=True, exclude_unset=True)
        result = self._call_tool('removeApprovedSenderTool', payload)
        return validate_tool_output(result, AccessRemoveApprovedSenderOutput)

    def list_approved_senders(self, **kwargs: Any) -> AccessListApprovedSendersOutput | ArtifactDelivery:
        payload = AccessListApprovedSendersInput(**kwargs).model_dump(by_alias=True, exclude_unset=True)
        result = self._call_tool('listApprovedSendersTool', payload)
        return validate_tool_output(result, AccessListApprovedSendersOutput)

    def inbox_settings(self, **kwargs: Any) -> AccessInboxSettingsOutput | ArtifactDelivery:
        payload = AccessInboxSettingsInput(**kwargs).model_dump(by_alias=True, exclude_unset=True)
        result = self._call_tool('inboxSettingsTool', payload)
        return validate_tool_output(result, AccessInboxSettingsOutput)

    def share_note(self, **kwargs: Any) -> AccessShareNoteOutput | ArtifactDelivery:
        payload = AccessShareNoteInput(**kwargs).model_dump(by_alias=True, exclude_unset=True)
        result = self._call_tool('shareNoteTool', payload)
        return validate_tool_output(result, AccessShareNoteOutput)

    def note_inbox(self, **kwargs: Any) -> AccessNoteInboxOutput | ArtifactDelivery:
        payload = AccessNoteInboxInput(**kwargs).model_dump(by_alias=True, exclude_unset=True)
        result = self._call_tool('noteInboxTool', payload)
        return validate_tool_output(result, AccessNoteInboxOutput)

    def accept_share(self, **kwargs: Any) -> AccessAcceptShareOutput | ArtifactDelivery:
        payload = AccessAcceptShareInput(**kwargs).model_dump(by_alias=True, exclude_unset=True)
        result = self._call_tool('acceptShareTool', payload)
        return validate_tool_output(result, AccessAcceptShareOutput)

    def decline_share(self, **kwargs: Any) -> AccessDeclineShareOutput | ArtifactDelivery:
        payload = AccessDeclineShareInput(**kwargs).model_dump(by_alias=True, exclude_unset=True)
        result = self._call_tool('declineShareTool', payload)
        return validate_tool_output(result, AccessDeclineShareOutput)

    def unlink_share(self, **kwargs: Any) -> AccessUnlinkShareOutput | ArtifactDelivery:
        payload = AccessUnlinkShareInput(**kwargs).model_dump(by_alias=True, exclude_unset=True)
        result = self._call_tool('unlinkShareTool', payload)
        return validate_tool_output(result, AccessUnlinkShareOutput)

    def revoke_share(self, **kwargs: Any) -> AccessRevokeShareOutput | ArtifactDelivery:
        payload = AccessRevokeShareInput(**kwargs).model_dump(by_alias=True, exclude_unset=True)
        result = self._call_tool('revokeShareTool', payload)
        return validate_tool_output(result, AccessRevokeShareOutput)

    def get_chat_link(self, **kwargs: Any) -> GetChatLinkOutput | ArtifactDelivery:
        payload = GetChatLinkInput(**kwargs).model_dump(by_alias=True, exclude_unset=True)
        result = self._call_tool('getChatLinkTool', payload)
        return validate_tool_output(result, GetChatLinkOutput)

    def revoke_chat_link(self, **kwargs: Any) -> RevokeChatLinkOutput | ArtifactDelivery:
        payload = RevokeChatLinkInput(**kwargs).model_dump(by_alias=True, exclude_unset=True)
        result = self._call_tool('revokeChatLinkTool', payload)
        return validate_tool_output(result, RevokeChatLinkOutput)

    def get_vault_app_link(self, **kwargs: Any) -> GetVaultAppLinkOutput | ArtifactDelivery:
        payload = GetVaultAppLinkInput(**kwargs).model_dump(by_alias=True, exclude_unset=True)
        result = self._call_tool('getVaultAppLinkTool', payload)
        return validate_tool_output(result, GetVaultAppLinkOutput)

    def revoke_vault_app_link(self, **kwargs: Any) -> RevokeVaultAppLinkOutput | ArtifactDelivery:
        payload = RevokeVaultAppLinkInput(**kwargs).model_dump(by_alias=True, exclude_unset=True)
        result = self._call_tool('revokeVaultAppLinkTool', payload)
        return validate_tool_output(result, RevokeVaultAppLinkOutput)

    def set_agent_identity(self, **kwargs: Any) -> SetAgentIdentityOutput | ArtifactDelivery:
        payload = SetAgentIdentityInput(**kwargs).model_dump(by_alias=True, exclude_unset=True)
        result = self._call_tool('setAgentIdentityTool', payload)
        return validate_tool_output(result, SetAgentIdentityOutput)

class CaptureNamespace:

    def __init__(self, call_tool):
        self._call_tool = call_tool

    def memory_questions(self, **kwargs: Any) -> MemoryQuestionsOutput | ArtifactDelivery:
        payload = MemoryQuestionsInput(**kwargs).model_dump(by_alias=True, exclude_unset=True)
        result = self._call_tool('memoryQuestionsTool', payload)
        return validate_tool_output(result, MemoryQuestionsOutput)

    def prepare_memory_write(self, **kwargs: Any) -> PrepareMemoryWriteOutput | ArtifactDelivery:
        payload = PrepareMemoryWriteInput(**kwargs).model_dump(by_alias=True, exclude_unset=True)
        result = self._call_tool('prepareMemoryWriteTool', payload)
        return validate_tool_output(result, PrepareMemoryWriteOutput)

    def validate_memory_write(self, **kwargs: Any) -> ValidateMemoryWriteOutput | ArtifactDelivery:
        payload = ValidateMemoryWriteInput(**kwargs).model_dump(by_alias=True, exclude_unset=True)
        result = self._call_tool('validateMemoryWriteTool', payload)
        return validate_tool_output(result, ValidateMemoryWriteOutput)

    def memory_capture(self, **kwargs: Any) -> MemoryCaptureOutput | ArtifactDelivery:
        payload = MemoryCaptureInput(**kwargs).model_dump(by_alias=True, exclude_unset=True)
        result = self._call_tool('memoryCaptureTool', payload)
        return validate_tool_output(result, MemoryCaptureOutput)

class ChannelsNamespace:

    def __init__(self, call_tool):
        self._call_tool = call_tool

    def create_channel(self, **kwargs: Any) -> CreateChannelOutput | ArtifactDelivery:
        payload = CreateChannelInput(**kwargs).model_dump(by_alias=True, exclude_unset=True)
        result = self._call_tool('createChannelTool', payload)
        return validate_tool_output(result, CreateChannelOutput)

    def post_message(self, **kwargs: Any) -> PostMessageOutput | ArtifactDelivery:
        payload = PostMessageInput(**kwargs).model_dump(by_alias=True, exclude_unset=True)
        result = self._call_tool('postMessageTool', payload)
        return validate_tool_output(result, PostMessageOutput)

    def reply_message(self, **kwargs: Any) -> ReplyMessageOutput | ArtifactDelivery:
        payload = ReplyMessageInput(**kwargs).model_dump(by_alias=True, exclude_unset=True)
        result = self._call_tool('replyMessageTool', payload)
        return validate_tool_output(result, ReplyMessageOutput)

    def list_channel_messages(self, **kwargs: Any) -> ListChannelMessagesOutput | ArtifactDelivery:
        payload = ListChannelMessagesInput(**kwargs).model_dump(by_alias=True, exclude_unset=True)
        result = self._call_tool('listChannelMessagesTool', payload)
        return validate_tool_output(result, ListChannelMessagesOutput)

    def react_message(self, **kwargs: Any) -> ReactMessageOutput | ArtifactDelivery:
        payload = ReactMessageInput(**kwargs).model_dump(by_alias=True, exclude_unset=True)
        result = self._call_tool('reactMessageTool', payload)
        return validate_tool_output(result, ReactMessageOutput)

    def my_mentions(self, **kwargs: Any) -> MyMentionsOutput | ArtifactDelivery:
        payload = MyMentionsInput(**kwargs).model_dump(by_alias=True, exclude_unset=True)
        result = self._call_tool('myMentionsTool', payload)
        return validate_tool_output(result, MyMentionsOutput)

    def list_channel_members(self, **kwargs: Any) -> ListChannelMembersOutput | ArtifactDelivery:
        payload = ListChannelMembersInput(**kwargs).model_dump(by_alias=True, exclude_unset=True)
        result = self._call_tool('listChannelMembersTool', payload)
        return validate_tool_output(result, ListChannelMembersOutput)

    def remove_channel_member(self, **kwargs: Any) -> RemoveChannelMemberOutput | ArtifactDelivery:
        payload = RemoveChannelMemberInput(**kwargs).model_dump(by_alias=True, exclude_unset=True)
        result = self._call_tool('removeChannelMemberTool', payload)
        return validate_tool_output(result, RemoveChannelMemberOutput)

    def poll_channel(self, **kwargs: Any) -> PollChannelOutput | ArtifactDelivery:
        payload = PollChannelInput(**kwargs).model_dump(by_alias=True, exclude_unset=True)
        result = self._call_tool('pollChannelTool', payload)
        return validate_tool_output(result, PollChannelOutput)

    def get_message_note(self, **kwargs: Any) -> GetMessageNoteOutput | ArtifactDelivery:
        payload = GetMessageNoteInput(**kwargs).model_dump(by_alias=True, exclude_unset=True)
        result = self._call_tool('getMessageNoteTool', payload)
        return validate_tool_output(result, GetMessageNoteOutput)

class FactsNamespace:

    def __init__(self, call_tool):
        self._call_tool = call_tool

    def record_fact(self, **kwargs: Any) -> RecordFactOutput | ArtifactDelivery:
        payload = RecordFactInput(**kwargs).model_dump(by_alias=True, exclude_unset=True)
        result = self._call_tool('recordFactTool', payload)
        return validate_tool_output(result, RecordFactOutput)

    def history(self, **kwargs: Any) -> FactHistoryOutput | ArtifactDelivery:
        payload = FactHistoryInput(**kwargs).model_dump(by_alias=True, exclude_unset=True)
        result = self._call_tool('factHistoryTool', payload)
        return validate_tool_output(result, FactHistoryOutput)

class FilesNamespace:

    def __init__(self, call_tool):
        self._call_tool = call_tool

    def file_asset_save(self, **kwargs: Any) -> FileAssetSaveOutput | ArtifactDelivery:
        payload = FileAssetSaveInput(**kwargs).model_dump(by_alias=True, exclude_unset=True)
        result = self._call_tool('file_asset_save', payload)
        return validate_tool_output(result, FileAssetSaveOutput)

    def file_asset_get(self, **kwargs: Any) -> FileAssetGetOutput | ArtifactDelivery:
        payload = FileAssetGetInput(**kwargs).model_dump(by_alias=True, exclude_unset=True)
        result = self._call_tool('file_asset_get', payload)
        return validate_tool_output(result, FileAssetGetOutput)

class GraphNamespace:

    def __init__(self, call_tool):
        self._call_tool = call_tool

    def memory_backlinks(self, **kwargs: Any) -> MemoryBacklinksOutput | ArtifactDelivery:
        payload = MemoryBacklinksInput(**kwargs).model_dump(by_alias=True, exclude_unset=True)
        result = self._call_tool('noteBacklinksTool', payload)
        return validate_tool_output(result, MemoryBacklinksOutput)

    def memory_graph_universe(self, **kwargs: Any) -> MemoryGraphUniverseOutput | ArtifactDelivery:
        payload = MemoryGraphUniverseInput(**kwargs).model_dump(by_alias=True, exclude_unset=True)
        result = self._call_tool('graphUniverseTool', payload)
        return validate_tool_output(result, MemoryGraphUniverseOutput)

    def memory_graph_path(self, **kwargs: Any) -> MemoryGraphPathOutput | ArtifactDelivery:
        payload = MemoryGraphPathInput(**kwargs).model_dump(by_alias=True, exclude_unset=True)
        result = self._call_tool('graphPathTool', payload)
        return validate_tool_output(result, MemoryGraphPathOutput)

class LibraryNamespace:

    def __init__(self, call_tool):
        self._call_tool = call_tool

    def ingest(self, **kwargs: Any) -> LibraryIngestOutput | ArtifactDelivery:
        payload = LibraryIngestInput(**kwargs).model_dump(by_alias=True, exclude_unset=True)
        result = self._call_tool('libraryIngestTool', payload)
        return validate_tool_output(result, LibraryIngestOutput)

class MemoryNamespace:

    def __init__(self, call_tool):
        self._call_tool = call_tool

    def export(self, **kwargs: Any) -> MemoryExportOutput | ArtifactDelivery:
        payload = MemoryExportInput(**kwargs).model_dump(by_alias=True, exclude_unset=True)
        result = self._call_tool('exportTool', payload)
        return validate_tool_output(result, MemoryExportOutput)

    def get(self, **kwargs: Any) -> MemoryGetOutput | ArtifactDelivery:
        payload = MemoryGetInput(**kwargs).model_dump(by_alias=True, exclude_unset=True)
        result = self._call_tool('getTool', payload)
        return validate_tool_output(result, MemoryGetOutput)

    def list(self, **kwargs: Any) -> MemoryListOutput | ArtifactDelivery:
        payload = MemoryListInput(**kwargs).model_dump(by_alias=True, exclude_unset=True)
        result = self._call_tool('listTool', payload)
        return validate_tool_output(result, MemoryListOutput)

    def put(self, **kwargs: Any) -> MemoryPutOutput | ArtifactDelivery:
        payload = MemoryPutInput(**kwargs).model_dump(by_alias=True, exclude_unset=True)
        result = self._call_tool('putTool', payload)
        return validate_tool_output(result, MemoryPutOutput)

    def search(self, **kwargs: Any) -> MemorySearchOutput | ArtifactDelivery:
        payload = MemorySearchInput(**kwargs).model_dump(by_alias=True, exclude_unset=True)
        result = self._call_tool('searchTool', payload)
        return validate_tool_output(result, MemorySearchOutput)

    def suggest(self, **kwargs: Any) -> MemorySuggestOutput | ArtifactDelivery:
        payload = MemorySuggestInput(**kwargs).model_dump(by_alias=True, exclude_unset=True)
        result = self._call_tool('suggestTool', payload)
        return validate_tool_output(result, MemorySuggestOutput)

    def upload(self, **kwargs: Any) -> MemoryUploadOutput | ArtifactDelivery:
        payload = MemoryUploadInput(**kwargs).model_dump(by_alias=True, exclude_unset=True)
        result = self._call_tool('uploadTool', payload)
        return validate_tool_output(result, MemoryUploadOutput)

    def delete_note(self, **kwargs: Any) -> DeleteNoteOutput | ArtifactDelivery:
        payload = DeleteNoteInput(**kwargs).model_dump(by_alias=True, exclude_unset=True)
        result = self._call_tool('deleteNoteTool', payload)
        return validate_tool_output(result, DeleteNoteOutput)

    def bulk_delete_notes(self, **kwargs: Any) -> BulkDeleteNotesOutput | ArtifactDelivery:
        payload = BulkDeleteNotesInput(**kwargs).model_dump(by_alias=True, exclude_unset=True)
        result = self._call_tool('bulkDeleteNotesTool', payload)
        return validate_tool_output(result, BulkDeleteNotesOutput)

class RecallNamespace:

    def __init__(self, call_tool):
        self._call_tool = call_tool

    def temporal_recall(self, **kwargs: Any) -> TemporalRecallOutput | ArtifactDelivery:
        payload = TemporalRecallInput(**kwargs).model_dump(by_alias=True, exclude_unset=True)
        result = self._call_tool('temporalRecallTool', payload)
        return validate_tool_output(result, TemporalRecallOutput)

class ArtifactsNamespace:

    def __init__(self, call_tool):
        self._call_tool = call_tool

    def list_artifact_templates(self, **kwargs: Any) -> ListArtifactTemplatesOutput | ArtifactDelivery:
        payload = ListArtifactTemplatesInput(**kwargs).model_dump(by_alias=True, exclude_unset=True)
        result = self._call_tool('list_artifact_templates', payload)
        return validate_tool_output(result, ListArtifactTemplatesOutput)

    def get_artifact_template(self, **kwargs: Any) -> GetArtifactTemplateOutput | ArtifactDelivery:
        payload = GetArtifactTemplateInput(**kwargs).model_dump(by_alias=True, exclude_unset=True)
        result = self._call_tool('get_artifact_template', payload)
        return validate_tool_output(result, GetArtifactTemplateOutput)

    def create_artifact_template(self, **kwargs: Any) -> CreateArtifactTemplateOutput | ArtifactDelivery:
        payload = CreateArtifactTemplateInput(**kwargs).model_dump(by_alias=True, exclude_unset=True)
        result = self._call_tool('create_artifact_template', payload)
        return validate_tool_output(result, CreateArtifactTemplateOutput)

    def update_artifact_template(self, **kwargs: Any) -> UpdateArtifactTemplateOutput | ArtifactDelivery:
        payload = UpdateArtifactTemplateInput(**kwargs).model_dump(by_alias=True, exclude_unset=True)
        result = self._call_tool('update_artifact_template', payload)
        return validate_tool_output(result, UpdateArtifactTemplateOutput)

    def archive_artifact_template(self, **kwargs: Any) -> ArchiveArtifactTemplateOutput | ArtifactDelivery:
        payload = ArchiveArtifactTemplateInput(**kwargs).model_dump(by_alias=True, exclude_unset=True)
        result = self._call_tool('archive_artifact_template', payload)
        return validate_tool_output(result, ArchiveArtifactTemplateOutput)

class StorageNamespace:

    def __init__(self, call_tool):
        self._call_tool = call_tool

    def usage(self, **kwargs: Any) -> StorageUsageOutput | ArtifactDelivery:
        payload = StorageUsageInput(**kwargs).model_dump(by_alias=True, exclude_unset=True)
        result = self._call_tool('storageUsageTool', payload)
        return validate_tool_output(result, StorageUsageOutput)

    def cost_usage(self, **kwargs: Any) -> CostUsageOutput | ArtifactDelivery:
        payload = CostUsageInput(**kwargs).model_dump(by_alias=True, exclude_unset=True)
        result = self._call_tool('costUsageTool', payload)
        return validate_tool_output(result, CostUsageOutput)

class TablesNamespace:

    def __init__(self, call_tool):
        self._call_tool = call_tool

    def create(self, **kwargs: Any) -> TableCreateOutput | ArtifactDelivery:
        payload = TableCreateInput(**kwargs).model_dump(by_alias=True, exclude_unset=True)
        result = self._call_tool('createTableTool', payload)
        return validate_tool_output(result, TableCreateOutput)

    def list(self, **kwargs: Any) -> TableListOutput | ArtifactDelivery:
        payload = TableListInput(**kwargs).model_dump(by_alias=True, exclude_unset=True)
        result = self._call_tool('listTablesTool', payload)
        return validate_tool_output(result, TableListOutput)

    def describe(self, **kwargs: Any) -> TableDescribeOutput | ArtifactDelivery:
        payload = TableDescribeInput(**kwargs).model_dump(by_alias=True, exclude_unset=True)
        result = self._call_tool('describeTableTool', payload)
        return validate_tool_output(result, TableDescribeOutput)

    def insert_rows(self, **kwargs: Any) -> TableInsertRowsOutput | ArtifactDelivery:
        payload = TableInsertRowsInput(**kwargs).model_dump(by_alias=True, exclude_unset=True)
        result = self._call_tool('insertTableRowsTool', payload)
        return validate_tool_output(result, TableInsertRowsOutput)

    def query(self, **kwargs: Any) -> TableQueryOutput | ArtifactDelivery:
        payload = TableQueryInput(**kwargs).model_dump(by_alias=True, exclude_unset=True)
        result = self._call_tool('queryTableTool', payload)
        return validate_tool_output(result, TableQueryOutput)

    def delete_rows(self, **kwargs: Any) -> TableDeleteRowsOutput | ArtifactDelivery:
        payload = TableDeleteRowsInput(**kwargs).model_dump(by_alias=True, exclude_unset=True)
        result = self._call_tool('deleteTableRowsTool', payload)
        return validate_tool_output(result, TableDeleteRowsOutput)

    def drop(self, **kwargs: Any) -> TableDropOutput | ArtifactDelivery:
        payload = TableDropInput(**kwargs).model_dump(by_alias=True, exclude_unset=True)
        result = self._call_tool('dropTableTool', payload)
        return validate_tool_output(result, TableDropOutput)

class TagsNamespace:

    def __init__(self, call_tool):
        self._call_tool = call_tool

    def list_memory_tags(self, **kwargs: Any) -> ListMemoryTagsOutput | ArtifactDelivery:
        payload = ListMemoryTagsInput(**kwargs).model_dump(by_alias=True, exclude_unset=True)
        result = self._call_tool('listTagsTool', payload)
        return validate_tool_output(result, ListMemoryTagsOutput)

    def resolve_memory_tags(self, **kwargs: Any) -> ResolveMemoryTagsOutput | ArtifactDelivery:
        payload = ResolveMemoryTagsInput(**kwargs).model_dump(by_alias=True, exclude_unset=True)
        result = self._call_tool('resolveTagsTool', payload)
        return validate_tool_output(result, ResolveMemoryTagsOutput)

    def merge_memory_tags(self, **kwargs: Any) -> MergeMemoryTagsOutput | ArtifactDelivery:
        payload = MergeMemoryTagsInput(**kwargs).model_dump(by_alias=True, exclude_unset=True)
        result = self._call_tool('mergeTagsTool', payload)
        return validate_tool_output(result, MergeMemoryTagsOutput)

    def upsert_memory_tag(self, **kwargs: Any) -> UpsertMemoryTagOutput | ArtifactDelivery:
        payload = UpsertMemoryTagInput(**kwargs).model_dump(by_alias=True, exclude_unset=True)
        result = self._call_tool('upsertTagTool', payload)
        return validate_tool_output(result, UpsertMemoryTagOutput)

class VaultsNamespace:

    def __init__(self, call_tool):
        self._call_tool = call_tool

    def list_shared_with_me(self, **kwargs: Any) -> ListSharedWithMeOutput | ArtifactDelivery:
        payload = ListSharedWithMeInput(**kwargs).model_dump(by_alias=True, exclude_unset=True)
        result = self._call_tool('listSharedWithMeTool', payload)
        return validate_tool_output(result, ListSharedWithMeOutput)

    def list_vaults(self, **kwargs: Any) -> ListVaultsOutput | ArtifactDelivery:
        payload = ListVaultsInput(**kwargs).model_dump(by_alias=True, exclude_unset=True)
        result = self._call_tool('listVaultsTool', payload)
        return validate_tool_output(result, ListVaultsOutput)

    def add_vault(self, **kwargs: Any) -> AddVaultOutput | ArtifactDelivery:
        payload = AddVaultInput(**kwargs).model_dump(by_alias=True, exclude_unset=True)
        result = self._call_tool('addVaultTool', payload)
        return validate_tool_output(result, AddVaultOutput)

    def create_secure_vault(self, **kwargs: Any) -> CreateSecureVaultOutput | ArtifactDelivery:
        payload = CreateSecureVaultInput(**kwargs).model_dump(by_alias=True, exclude_unset=True)
        result = self._call_tool('createSecureVaultTool', payload)
        return validate_tool_output(result, CreateSecureVaultOutput)

    def delete_vault(self, **kwargs: Any) -> DeleteVaultOutput | ArtifactDelivery:
        payload = DeleteVaultInput(**kwargs).model_dump(by_alias=True, exclude_unset=True)
        result = self._call_tool('deleteVaultTool', payload)
        return validate_tool_output(result, DeleteVaultOutput)

    def provision_defaults(self, **kwargs: Any) -> ProvisionDefaultsOutput | ArtifactDelivery:
        payload = ProvisionDefaultsInput(**kwargs).model_dump(by_alias=True, exclude_unset=True)
        result = self._call_tool('provisionDefaultsTool', payload)
        return validate_tool_output(result, ProvisionDefaultsOutput)

    def get_vault_contract(self, **kwargs: Any) -> GetVaultContractOutput | ArtifactDelivery:
        payload = GetVaultContractInput(**kwargs).model_dump(by_alias=True, exclude_unset=True)
        result = self._call_tool('getVaultContractTool', payload)
        return validate_tool_output(result, GetVaultContractOutput)

    def route_memory(self, **kwargs: Any) -> RouteMemoryOutput | ArtifactDelivery:
        payload = RouteMemoryInput(**kwargs).model_dump(by_alias=True, exclude_unset=True)
        result = self._call_tool('routeMemoryTool', payload)
        return validate_tool_output(result, RouteMemoryOutput)

class VideoNamespace:

    def __init__(self, call_tool):
        self._call_tool = call_tool

    def analyze_start(self, **kwargs: Any) -> VideoAnalyzeStartOutput | ArtifactDelivery:
        payload = VideoAnalyzeStartInput(**kwargs).model_dump(by_alias=True, exclude_unset=True)
        result = self._call_tool('videoAnalyzeStartTool', payload)
        return validate_tool_output(result, VideoAnalyzeStartOutput)

    def analyze_status(self, **kwargs: Any) -> VideoAnalyzeStatusOutput | ArtifactDelivery:
        payload = VideoAnalyzeStatusInput(**kwargs).model_dump(by_alias=True, exclude_unset=True)
        result = self._call_tool('videoAnalyzeStatusTool', payload)
        return validate_tool_output(result, VideoAnalyzeStatusOutput)

class WebhooksNamespace:

    def __init__(self, call_tool):
        self._call_tool = call_tool

    def create_webhook(self, **kwargs: Any) -> CreateWebhookOutput | ArtifactDelivery:
        payload = CreateWebhookInput(**kwargs).model_dump(by_alias=True, exclude_unset=True)
        result = self._call_tool('createWebhookTool', payload)
        return validate_tool_output(result, CreateWebhookOutput)

    def list_webhooks(self, **kwargs: Any) -> ListWebhooksOutput | ArtifactDelivery:
        payload = ListWebhooksInput(**kwargs).model_dump(by_alias=True, exclude_unset=True)
        result = self._call_tool('listWebhooksTool', payload)
        return validate_tool_output(result, ListWebhooksOutput)

    def revoke_webhook(self, **kwargs: Any) -> RevokeWebhookOutput | ArtifactDelivery:
        payload = RevokeWebhookInput(**kwargs).model_dump(by_alias=True, exclude_unset=True)
        result = self._call_tool('revokeWebhookTool', payload)
        return validate_tool_output(result, RevokeWebhookOutput)
