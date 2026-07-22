from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field


class BrowserReplayDownloadInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    session_id: str = Field(..., alias="session_id", description="The session id returned by browser_open or browser_list_sessions.")
    replay_id: str = Field(..., alias="replay_id", description="The replay id returned by browser_replay_start or browser_list_replays.")
    filename: str | None = Field(None, alias="filename", description="Optional local MP4 filename. Defaults to a timestamped replay filename.")


class BrowserReplayDownloadOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    ok: bool = Field(..., alias="ok", description="Whether the browser-agent action succeeded.")
    tool: str = Field(..., alias="tool", description="")
    session_id: Any = Field(..., alias="session_id", description="Browser session id when the response is scoped to a session.")
    replay_id: Any = Field(..., alias="replay_id", description="Replay id when the response is scoped to a replay.")
    file_path: Any = Field(..., alias="file_path", description="")
    bytes: Any = Field(..., alias="bytes", description="")
    mime_type: Any = Field(..., alias="mime_type", description="")
    download_url: Any = Field(..., alias="download_url", description="")
