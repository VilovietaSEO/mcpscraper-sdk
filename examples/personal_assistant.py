from mcpscraper import (
    AssistantApprovalDecision,
    AssistantCursor,
    AssistantIdempotencyKey,
    McpToolsClient,
)


def submit_command(
    client: McpToolsClient,
    assistant_ref: str,
    idempotency_key: AssistantIdempotencyKey,
) -> None:
    client.assistant.command(
        assistant_ref=assistant_ref,
        instruction="Draft a reply, but do not send it without my approval.",
        idempotency_key=idempotency_key,
    )


def list_pending_approvals(
    client: McpToolsClient,
    cursor: AssistantCursor | None = None,
) -> None:
    client.assistant.approvals_list(state="pending", cursor=cursor, page_size=25)


def decide_approval(
    client: McpToolsClient,
    decision: AssistantApprovalDecision,
) -> None:
    client.assistant.approval_decide(**decision.model_dump(by_alias=True))
