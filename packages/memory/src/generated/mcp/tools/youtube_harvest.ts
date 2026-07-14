export interface Input {
  /**
   * Use search for topic/keyword requests. Use channel when the user provides @handle, channel ID, or channel URL.
   */
  mode: "search" | "channel";
  /**
   * Required when mode is search. The YouTube search topic in the user’s words.
   */
  query?: string;
  /**
   * YouTube channel handle, channel ID, or URL. Examples: @mkbhd, UC..., https://youtube.com/@mkbhd.
   */
  channelHandle?: string;
  /**
   * Number of videos to return. Default 50, maximum 500.
   */
  maxVideos?: number;
}

export interface Output {
  mode: string;
  videoCount: number;
  channel: {
    title: string | null;
    subscriberCount: string | null;
  } | null;
  videos: {
    videoId: string;
    title: string;
    channelName: string | null;
    views: string | null;
    duration: string | null;
    url: string | null;
  }[];
}
