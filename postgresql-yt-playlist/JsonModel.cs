using System.Text.Json.Serialization;

public class PlaylistInfo
{
    public string id { get; set; }
    public string owner { get; set; }
    public string title { get; set; }
    public int position { get; set; }
}

public class VideoData
{
    public string id { get; set; }
    public string title { get; set; }
    public string comment { get; set; }
    public string CoverUrl { get; set; }
    public List<PlaylistInfo> playlists { get; set; } = new List<PlaylistInfo>();
    public string lang { get; set; } // 來自第二個 JSON
}

public class CustomTitleJson
{
    public List<VideoData> videos { get; set; }
}

public class VideosLangCheckJson
{
    [JsonPropertyName("items")] public List<VideoData> items { get; set; }
}