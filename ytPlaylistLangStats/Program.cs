using System.Text.Encodings.Web;
using System.Text.Json;
using System.Text.Unicode;
using Microsoft.Extensions.Configuration;

async Task getPlayListData(string url, List<JsonElement> videoList, string apiKey, string pageToken = "", int i = 0)
{
    Uri playListUrl = new Uri(url);
    var playListArguments = playListUrl.Query
                                .Substring(1) // Remove '?'
                                .Split('&')
                                .Select(q => q.Split('='))
                                .ToDictionary(q => q.FirstOrDefault(), q => q.Skip(1).FirstOrDefault());

    UriBuilder apiUrl = new UriBuilder($"https://youtube.googleapis.com/youtube/v3/playlistItems?part=snippet&maxResults=50&playlistId={playListArguments["list"]}&key={apiKey}");
    if (pageToken != "")
    {
        apiUrl.Query = apiUrl.Query.Substring(1) + "&" + $"pageToken={pageToken}";
    }

    HttpClient client = new HttpClient();
    var res = await client.GetStringAsync(apiUrl.Uri);
    using (JsonDocument json = JsonDocument.Parse(res, new JsonDocumentOptions { AllowTrailingCommas = true }))
    {
        JsonElement root = json.RootElement;
        JsonElement items = root.GetProperty("items");
        foreach (var video in items.EnumerateArray())
        {
            videoList.Add(video);
        }
        if (root.TryGetProperty("nextPageToken", out JsonElement token))
        {
            i++;
            Console.WriteLine(i);
            await getPlayListData(url, videoList, apiKey, token.GetString()!, i);
        }
        else
        {
            JsonSerializerOptions options = new JsonSerializerOptions
            {
                Encoder = JavaScriptEncoder.Create(UnicodeRanges.All),
                WriteIndented = true
            };
            await File.WriteAllTextAsync("./data.json", JsonSerializer.Serialize(new { items = videoList }, options));
        }
    }
}

async Task getVideoDetail(string path, string apiKey)
{
    string file = await File.ReadAllTextAsync(path);
    List<Object> details = new List<Object>();
    using (JsonDocument json = JsonDocument.Parse(file, new JsonDocumentOptions { AllowTrailingCommas = true }))
    {
        JsonElement root = json.RootElement;
        JsonElement items = root.GetProperty("items");
        foreach (var video in items.EnumerateArray())
        {
            string? title = video.GetProperty("snippet").GetProperty("title").GetString();
            string? id = video.GetProperty("snippet").GetProperty("resourceId").GetProperty("videoId").GetString();


            HttpClient client = new HttpClient();
            string url = $"https://youtube.googleapis.com/youtube/v3/videos?part=snippet&id={id}&key={apiKey}";
            var res = await client.GetStringAsync(url);
            using (JsonDocument apiRes = JsonDocument.Parse(res, new JsonDocumentOptions { AllowTrailingCommas = true }))
            {
                JsonElement resRoot = apiRes.RootElement;
                var data = resRoot.GetProperty("items").EnumerateArray().ToArray();
                if (data.Count() == 0)
                {
                    Console.WriteLine($"影片id: {id}未找到");
                    continue;
                }
                var detail = new
                {
                    title = title,
                    id = id,
                    lang = (data[0].GetProperty("snippet").TryGetProperty("defaultAudioLanguage", out JsonElement lang))
                            ? lang.GetString()
                            : "ukunown"
                };
                details.Add(detail);
            }
            Console.WriteLine($"影片 {title};id: {id} ok！");
        }

        JsonSerializerOptions options = new JsonSerializerOptions
        {
            Encoder = JavaScriptEncoder.Create(UnicodeRanges.All),
            WriteIndented = true
        };
        await File.WriteAllTextAsync("./videos.json", JsonSerializer.Serialize(new { items = details }, options));
    }
}

async Task dataAnalysis(string path)
{
    string file = await File.ReadAllTextAsync(path);
    Dictionary<string, int> stat = new Dictionary<string, int>();
    using (JsonDocument json = JsonDocument.Parse(file, new JsonDocumentOptions { AllowTrailingCommas = true }))
    {
        JsonElement root = json.RootElement;
        JsonElement videos = root.GetProperty("items");
        foreach (var video in videos.EnumerateArray())
        {
            string? lang = video.GetProperty("lang").GetString();
            if (stat.ContainsKey(lang!))
            {
                stat[lang!] += 1;
            }
            else
            {
                stat.Add(lang!, 1);
            }
        }
    }
    stat = stat.OrderByDescending(l => l.Value).ToDictionary(l => l.Key, l => l.Value);
    stat.Add("total", stat.Values.Sum());

    await File.WriteAllTextAsync(
        Path.Combine(Directory.GetCurrentDirectory(), "result.json"),
        JsonSerializer.Serialize(stat),
        System.Text.Encoding.UTF8
    );
    Console.WriteLine("stat success！");
}

async Task main()
{

    IConfiguration configuration = new ConfigurationBuilder()
            .SetBasePath(Directory.GetCurrentDirectory())
            .AddJsonFile("appsettings.json", optional: true, reloadOnChange: true)
            .Build();

    Configure config = new Configure();
    config.apiKey = configuration.GetValue<string>("YoutubeAPIKey")!;
    config.isDownloading = configuration.GetValue<bool>("isDownloading");

    if (config.isDownloading)
    {
        await getPlayListData(
            "https://www.youtube.com/playlist?list=PLdx_s59BrvfXJXyoU5BHpUkZGmZL0g3Ip",
            new List<JsonElement>(),
            config.apiKey
        );
        await getVideoDetail("./data.json", config.apiKey!);
        Console.Write("因Youtube API能拿到的資料不完整，");
        Console.WriteLine("請再次確認每隻影片的語言");
    }
    else
    {
        await dataAnalysis("./videos.json");
    }
}

await main();