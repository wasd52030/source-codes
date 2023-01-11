using YoutubeExplode;
using YoutubeExplode.Videos.Streams;

string removeSpecialChar(string input)
{
    foreach (var item in new string[] { @"*", @"/", "\n", "\"", "|", ":", "?" })
    {
        input = input.Replace(item, "");
    }

    return input;
}

async Task<Dictionary<string, string>> getPlayListInfo(YoutubeClient yt, string url)
{
    var playlist = await yt.Playlists.GetAsync(url);
    Dictionary<string, string> info = new Dictionary<string, string>();
    info.Add("title", playlist.Title);
    info.Add("owner", playlist.Author?.ChannelTitle!);
    return info;
}

async Task download(YoutubeClient yt, string url)
{
    await foreach (var video in yt.Playlists.GetVideosAsync(url))
    {
        var vinfo = await yt.Videos.GetAsync(video.Url);
        var vtitle = vinfo.Title;
        vtitle = removeSpecialChar(vtitle);
        var list = await yt.Videos.Streams.GetManifestAsync(video.Url);
        var videoInfo = list.GetAudioOnlyStreams().GetWithHighestBitrate();
        await yt.Videos.Streams.DownloadAsync(videoInfo, $@"./{vtitle}.mp3");
        Console.WriteLine(@$"{vtitle}.mp3 download complete");
    }
}

//reference -> https://csharpkh.blogspot.com/2017/10/c-async-void-async-task.html
async Task main()
{
    var t1 = DateTime.UtcNow;

    // reference -> https://github.com/Tyrrrz/YoutubeExplode
    var yt = new YoutubeClient();

    string url = "https://www.youtube.com/playlist?list=PLdx_s59BrvfXJXyoU5BHpUkZGmZL0g3Ip";
    var playListInfo = await getPlayListInfo(yt, url);
    Console.Write(
        $"請輸入Youtube PlayList網址，預設為{playListInfo["owner"].Replace("by", "").Trim()}的{playListInfo["title"]}: "
    );
    string? userInput = Console.ReadLine();
    string name = $"YT-{playListInfo["title"]}";

    if (!string.IsNullOrEmpty(userInput))
    {
        url = userInput;
        playListInfo = await getPlayListInfo(yt, url);
        name = $"YT-{playListInfo["title"]}";
    }
    name = removeSpecialChar(name);
    if (!Directory.Exists($"./{name}"))
    {
        Directory.CreateDirectory($"./{name}");
    }
    Directory.SetCurrentDirectory($"./{name}");
    await download(yt, url);

    var t2 = DateTime.UtcNow;
    Console.WriteLine($"執行時間: {(t2 - t1)}");
}

await main();
