using System;
using System.Collections.Generic;
using System.Data;
using System.Linq;
using System.Text.Json;
using System.Threading.Tasks;
using Dapper;
using Npgsql;

public class MergeService
{
    // ... (Main Method 保持不變，但我們會傳入多個 JSON B)

    public static async Task RunAsync()
    {
        // string jsonA = @"{
        //   ""videos"": [
        //     {
        //       ""id"": ""87moOXPTtSk"",
        //       ""title"": ""A-Title"",
        //       ""comment"": null,
        //       ""CoverUrl"": ""https://i.ytimg.com/vi/87moOXPTtSk/maxresdefault.jpg"",
        //       ""playlists"": [ { ""id"": ""PLdx_s59BrvfXJXyoU5BHpUkZGmZL0g3Ip"", ""owner"": ""Owner"", ""title"": ""Playlist1"", ""position"": 183 } ],
        //       ""lang"": null
        //     },
        //     {
        //       ""id"": ""UI8Iy7kmRxo"",
        //       ""title"": ""B-Title"",
        //       ""comment"": null,
        //       ""CoverUrl"": null,
        //       ""playlists"": [],
        //       ""lang"": ""日"" // 假設來自 A 的影片一開始就有語言
        //     }
        //   ]
        // }";
        string jsonA =
            await File.ReadAllTextAsync(Path.Combine(AppDomain.CurrentDomain.BaseDirectory, "./customTitle.json"));

        // JSON B 陣列
        string[] jsonBs = new string[]
        {
            // JSON B 1: 包含 B 和新的 C
            // @"{ ""items"": [
            //     { ""id"": ""UI8Iy7kmRxo"", ""title"": ""Oblivious"", ""lang"": ""英"" }, 
            //     { ""id"": ""NewVideoC"", ""title"": ""New C Song"", ""lang"": ""德"" }
            // ]}",
            
            // // JSON B 2: 包含 A (語言為空)
            // @"{ ""items"": [
            //     { ""id"": ""87moOXPTtSk"", ""title"": ""A-Title Update"", ""lang"": null } 
            // ]}",

            // // JSON B 3: 包含 A (有語言，應更新)
            // @"{ ""items"": [
            //     { ""id"": ""87moOXPTtSk"", ""title"": ""A-Title Final"", ""lang"": ""日"" } 
            // ]}"
            await File.ReadAllTextAsync(Path.Combine(AppDomain.CurrentDomain.BaseDirectory, "./Виктор собел-BBBGGGMMM_videosLangCheck.json")),
            await File.ReadAllTextAsync(Path.Combine(AppDomain.CurrentDomain.BaseDirectory, "./Виктор собел-酷東東_videosLangCheck.json")),
            await File.ReadAllTextAsync(Path.Combine(AppDomain.CurrentDomain.BaseDirectory, "./Виктор собел-6_videosLangCheck.json"))
        };
        
        List<VideoData> mergedVideos = MergeData(jsonA, jsonBs);

        // #region Merge Debug
        // Console.WriteLine("--- 合併結果 (僅展示 lang 檢查邏輯) ---");
        // foreach (var v in mergedVideos)
        // {
        //     Console.WriteLine($"ID: {v.id}, Title: {v.title}, Lang: {v.lang}");
        // }
        // Console.WriteLine("------------------------------------------");
        // #endregion

        var dbService = new DbService();
        await dbService.InsertDataAsync(mergedVideos);
    }

    /// <summary>
    /// 合併 JSON A 和多個 JSON B，並根據 lang 欄位進行更新。
    /// </summary>
    private static List<VideoData> MergeData(string jsonA, string[] jsonBs)
    {

        var videoMap = new Dictionary<string, VideoData>();


        var dataA = JsonSerializer.Deserialize<InputJson1>(jsonA);
        if (dataA?.videos != null)
        {
            foreach (var video in dataA.videos)
            {
                videoMap[video.id] = video;
            }
        }


        foreach (var jsonB in jsonBs)
        {
            var dataB = JsonSerializer.Deserialize<InputJson2>(jsonB);
            if (dataB?.items != null)
            {
                foreach (var item in dataB.items)
                {
                    if (videoMap.TryGetValue(item.id, out var existingVideo))
                    {
                        if (!string.IsNullOrEmpty(item.lang))
                        {
                            if (string.IsNullOrEmpty(existingVideo.lang))
                            {
                                existingVideo.lang = item.lang;
                            }
                        }

                    }
                    else
                    {
                        var newVideo = new VideoData
                        {
                            id = item.id,
                            title = item.title,
                            lang = item.lang,
                            comment = null,
                            CoverUrl = null,
                            playlists = new List<PlaylistInfo>()
                        };
                        videoMap.Add(newVideo.id, newVideo);
                    }
                }
            }
        }
        return videoMap.Values.ToList();
    }
}