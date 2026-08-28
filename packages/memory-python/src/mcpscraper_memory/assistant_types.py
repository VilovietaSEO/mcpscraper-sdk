from .mcp_models.assistant_approval_decide import AssistantApprovalDecideInput
from .mcp_models.assistant_approvals_list import AssistantApprovalsListInput
from .mcp_models.assistant_command import AssistantCommandInput

AssistantApprovalDecision = AssistantApprovalDecideInput
AssistantPageRequest = AssistantApprovalsListInput
AssistantCommand = AssistantCommandInput
AssistantCursor = str
AssistantIdempotencyKey = str

__all__ = [
    "AssistantApprovalDecision",
    "AssistantCommand",
    "AssistantCursor",
    "AssistantIdempotencyKey",
    "AssistantPageRequest",
]
