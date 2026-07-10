from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field


class BrowserReplayDownloadInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    session_id: str = Field(..., alias="session_id", description="The session id returned by browser_open or browser_list_sessions.")
    replay_id: str = Field(..., alias="replay_id", description="The replay id returned by browser_replay_start or browser_list_replays.")
    filename: str | None = Field(None, alias="filename", description="Optional local MP4 filename. Defaults to a timestamped replay filename.")


class BrowserReplayDownloadOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")
