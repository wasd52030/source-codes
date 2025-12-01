using System.Data;
using Dapper;
using Npgsql;

public class DbService
{
    private const string ConnectionString = "Host=localhost;Port=5432;Database=Youtube-Playlist-DB;Username=postgres;Password=password";

    public async Task InsertDataAsync(List<VideoData> mergedVideos)
    {
        using IDbConnection db = new NpgsqlConnection(ConnectionString);
        db.Open();
        using var transaction = db.BeginTransaction();

        try
        {
            foreach (var video in mergedVideos)
            {
                // A. 寫入 videos table (使用 ON CONFLICT DO NOTHING 避免重複插入)
                var videoSql = @"
                    INSERT INTO videos (video_id, title, comment, cover_url, lang) 
                    VALUES (@id, @title, @comment, @CoverUrl, @lang)
                    ON CONFLICT (video_id) DO NOTHING;";
                
                await db.ExecuteAsync(videoSql, video, transaction);

                // B. 處理播放列表資訊和關聯
                foreach (var p in video.playlists)
                {
                    // B1. 寫入 playlists table (使用 ON CONFLICT DO NOTHING 避免重複插入)
                    var playlistSql = @"
                        INSERT INTO playlists (playlist_id, title, owner)
                        VALUES (@id, @title, @owner)
                        ON CONFLICT (playlist_id) DO NOTHING;";
                    
                    await db.ExecuteAsync(playlistSql, new { p.id, p.title, p.owner }, transaction);

                    // B2. 寫入 video_playlist_links 連接表
                    var linkSql = @"
                        INSERT INTO video_playlist_links (video_id, playlist_id, position)
                        VALUES (@VideoId, @PlaylistId, @Position)
                        ON CONFLICT (video_id, playlist_id) 
                        DO UPDATE SET position = EXCLUDED.position;"; // 如果已存在，則更新 position
                    
                    await db.ExecuteAsync(linkSql, new 
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
}