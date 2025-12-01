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

public class InputJson1
{
    public List<VideoData> videos { get; set; }
}

public class InputJson2Item
{
    public string id { get; set; }
    public string title { get; set; }
    public string lang { get; set; }
}

public class InputJson2
{
    public List<InputJson2Item> items { get; set; }
}