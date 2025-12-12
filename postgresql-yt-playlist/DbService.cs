using System.Data;
using Dapper;
using Npgsql;

public class YTPlaylistDbService
{
    private const string ConnectionString = "Host=localhost;Port=5432;Database=Youtube-Playlist-DB;Username=postgres;Password=password";

    public async Task InsertAsync(List<VideoData> videos)
    {
        using IDbConnection db = new NpgsqlConnection(ConnectionString);
        db.Open();
        using var transaction = db.BeginTransaction();

        try
        {
            foreach (var video in videos)
            {
                var sql_insert_video = @"
                    INSERT INTO videos (video_id, title, comment, cover_url, lang) 
                    VALUES (@id, @title, @comment, @CoverUrl, @lang)
                    ON CONFLICT (video_id) DO NOTHING;";

                await db.ExecuteAsync(sql_insert_video, video, transaction);

                foreach (var p in video.playlists)
                {
                    var sql_insert_playlist = @"
                        INSERT INTO playlists (playlist_id, title, owner)
                        VALUES (@id, @title, @owner)
                        ON CONFLICT (playlist_id) DO NOTHING;";

                    await db.ExecuteAsync(sql_insert_playlist, new { p.id, p.title, p.owner }, transaction);

                    var sql_insert_playlist_item = @"
                        INSERT INTO playlist_item (video_id, playlist_id, position)
                        VALUES (@VideoId, @PlaylistId, @Position)
                        ON CONFLICT (video_id, playlist_id) DO NOTHING;";

                    await db.ExecuteAsync(sql_insert_playlist_item, new
                    {
                        VideoId = video.id,
                        PlaylistId = p.id,
                        p.position
                    }, transaction);
                }
            }

            transaction.Commit();
            Console.WriteLine("成功寫入資料庫");
        }
        catch (Exception ex)
        {
            transaction.Rollback();
            Console.WriteLine($"寫入時發生錯誤: {ex.Message}");
            throw;
        }
    }


    public async Task UpdateAsync(List<VideoData> videos)
    {
        using IDbConnection db = new NpgsqlConnection(ConnectionString);
        db.Open();
        using var transaction = db.BeginTransaction();

        try
        {
            foreach (var video in videos)
            {
                var sql_update_video = @"
                    UPDATE videos 
                    SET title = @title, 
                        comment = @comment, 
                        cover_url = @CoverUrl, 
                        lang = @lang 
                    WHERE video_id = @id;";

                await db.ExecuteAsync(sql_update_video, video, transaction);

                foreach (var p in video.playlists)
                {
                    var sql_update_playlist_item = @"
                        UPDATE playlist_item 
                        SET position = @Position 
                        WHERE video_id = @VideoId AND playlist_id = @PlaylistId;";

                    await db.ExecuteAsync(sql_update_playlist_item, new
                    {
                        VideoId = video.id,
                        PlaylistId = p.id,
                        p.position
                    }, transaction);
                }
            }

            transaction.Commit();
            Console.WriteLine("成功更新資料庫資料");
        }
        catch (Exception ex)
        {
            transaction.Rollback();
            Console.WriteLine($"更新時發生錯誤: {ex.Message}");
            throw;
        }
    }
}