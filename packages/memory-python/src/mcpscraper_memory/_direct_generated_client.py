from typing import Any, Callable

from .direct_models.assistant_context_packet_create import AssistantContextPacketCreateInput, AssistantContextPacketCreateOutput
from .direct_models.assistant_context_packet_get import AssistantContextPacketGetInput, AssistantContextPacketGetOutput
from .direct_models.assistant_context_packet_lifecycle import AssistantContextPacketLifecycleInput, AssistantContextPacketLifecycleOutput
from .direct_models.assistant_context_packet_list import AssistantContextPacketListInput, AssistantContextPacketListOutput
from .direct_models.assistant_context_packet_share_accept import AssistantContextPacketShareAcceptInput, AssistantContextPacketShareAcceptOutput


class AccessNamespace:
    def __init__(self, call_tool):
        self._call_tool = call_tool



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



class ChannelsNamespace:
    def __init__(self, call_tool):
        self._call_tool = call_tool



class FactsNamespace:
    def __init__(self, call_tool):
        self._call_tool = call_tool



class GraphNamespace:
    def __init__(self, call_tool):
        self._call_tool = call_tool



class LibraryNamespace:
    def __init__(self, call_tool):
        self._call_tool = call_tool



class MemoryNamespace:
    def __init__(self, call_tool):
        self._call_tool = call_tool



class RecallNamespace:
    def __init__(self, call_tool):
        self._call_tool = call_tool



class ScheduleNamespace:
    def __init__(self, call_tool):
        self._call_tool = call_tool



class StorageNamespace:
    def __init__(self, call_tool):
        self._call_tool = call_tool



class TablesNamespace:
    def __init__(self, call_tool):
        self._call_tool = call_tool



class TagsNamespace:
    def __init__(self, call_tool):
        self._call_tool = call_tool



class VaultsNamespace:
    def __init__(self, call_tool):
        self._call_tool = call_tool



class VideoNamespace:
    def __init__(self, call_tool):
        self._call_tool = call_tool



class WebhooksNamespace:
    def __init__(self, call_tool):
        self._call_tool = call_tool
