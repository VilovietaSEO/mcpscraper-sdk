from typing import Any


class MemoryApiError(Exception):
    def __init__(
        self,
        message: str,
        http_status: int | None = None,
        rpc_code: int | None = None,
        data: Any = None,
        tool_error: Any = None,
    ) -> None:
        super().__init__(message)
        self.http_status = http_status
        self.rpc_code = rpc_code
        self.data = data
        self.tool_error = tool_error
