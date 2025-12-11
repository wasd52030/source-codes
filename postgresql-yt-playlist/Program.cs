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
    };

    DbService dbService = new DbService();

    await dbService.InsertDataAsync(customTitleData!.videos);
    foreach (var x in videosLangChecks)
    {
        var data = JsonSerializer.Deserialize<VideosLangCheckJson>(x);
        await dbService.InsertDataAsync(data!.items);
    }

    // Console.WriteLine(customTitle);

    // videosLangChecks.ToList().ForEach(x => Console.WriteLine(x));
}


await Main();