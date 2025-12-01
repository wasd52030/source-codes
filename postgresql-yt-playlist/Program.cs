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


await MergeService.RunAsync();