using System.CommandLine;
using System.Data;
using System.Text.Json;
using Dapper;
using Npgsql;

async Task PostgresqlTest()
{
    var connstr = "Host=localhost;Port=5432;Database=Youtube-Playlist-DB;Username=postgres;Password=password";

    using IDbConnection db = new NpgsqlConnection(connstr);
    db.Open();
    using var transaction = db.BeginTransaction();

    var videoSql = @"
                INSERT INTO videos (video_id, title, comment, cover_url, lang) 
                VALUES (@video_id, @title, @comment, @cover_url, @lang)
                ON CONFLICT (video_id) DO NOTHING;
                ";

    await db.ExecuteAsync(videoSql, new { video_id = "a", title = "b", comment = "c", cover_url = "d", lang = "e" }, transaction);

    transaction.Commit();
}


async Task Insert(List<VideoData> videos)
{
    YTPlaylistDbService dbService = new YTPlaylistDbService();

    await dbService.InsertAsync(videos);
}

async Task Update(List<VideoData> videos)
{
    YTPlaylistDbService dbService = new YTPlaylistDbService();

    await dbService.UpdateAsync(videos);
}

async Task Main()
{
    string customTitle =
            await File.ReadAllTextAsync(Path.Combine(AppDomain.CurrentDomain.BaseDirectory, "./assets/customTitle.json"));

    var customTitleData = JsonSerializer.Deserialize<CustomTitleJson>(customTitle);

    var videosLangChecks = new List<string>
    {
        await File.ReadAllTextAsync(Path.Combine(AppDomain.CurrentDomain.BaseDirectory, "./assets/Виктор собел-BBBGGGMMM_videosLangCheck.json")),
        await File.ReadAllTextAsync(Path.Combine(AppDomain.CurrentDomain.BaseDirectory, "./assets/Виктор собел-酷東東_videosLangCheck.json")),
        await File.ReadAllTextAsync(Path.Combine(AppDomain.CurrentDomain.BaseDirectory, "./assets/Виктор собел-6_videosLangCheck.json"))
    }.Select(json => JsonSerializer.Deserialize<VideosLangCheckJson>(json));


    var rootCommand = new RootCommand("");

    var insertCommand = new Command(name: "insert", description: "新增到資料庫");
    insertCommand.SetAction(async (ctx) =>
    {
        await Insert(customTitleData!.videos);
        foreach (var videosLangCheck in videosLangChecks)
        {
            await Insert(videosLangCheck!.items);
        }
    });
    rootCommand.Add(insertCommand);
    
    var updateCommand = new Command(name: "upadte", description: "更新資料庫");
    updateCommand.SetAction(async (ctx) =>
    {
        await Update(customTitleData!.videos);
        foreach (var videosLangCheck in videosLangChecks)
        {
            await Update(videosLangCheck!.items);
        }
    });
    rootCommand.Add(updateCommand);





    // Console.WriteLine(customTitle);

    // videosLangChecks.ToList().ForEach(x => Console.WriteLine(x));
}


await Main();