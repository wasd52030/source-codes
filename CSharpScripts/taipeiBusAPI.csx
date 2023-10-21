#r "nuget: Microsoft.AspNetCore.WebUtilities, 2.2.0"

using System.Net.Http;
using Microsoft.AspNetCore.WebUtilities;
using System.Text.Json;
using System.Threading.Tasks;

// 查詢台北公車
var api = $"https://ptx.transportdata.tw/MOTC/v2/Bus/EstimatedTimeOfArrival/City/Taipei/307";
var filter = $"stopId eq '15250'"; // 站牌代號
var query = new Dictionary<string, string>()
{
    ["$filter"] = filter,
    ["$top"] = 1.ToString(),
    ["$format"] = "JSON"
};

// QueryHelpers => Nuget => Microsoft.AspNetCore.WebUtilities
var url = QueryHelpers.AddQueryString(api, query);

var request = new HttpRequestMessage
{
    Method = HttpMethod.Get,
    RequestUri = new Uri(url)
};
request.Headers.Add("User-Agent", "Mozilla/5.0 (Windows NT 10.0; Win64; x64)");

var client = new HttpClient();

var response = await client.SendAsync(request);
if (response.IsSuccessStatusCode is false)
{
    throw new Exception(response.StatusCode.ToString());
}

var body = await response.Content.ReadAsStringAsync();
client.Dispose();

body.Dump();