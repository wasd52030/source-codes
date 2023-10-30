using System.ComponentModel;

namespace MvcMain.Models;

public record Employee
{
    [DisplayName("員工編號")]
    public int id { get; set; }

    [DisplayName("員工姓名")]
    public string name { get; set; }

    [DisplayName("連絡電話")]
    public string phone { get; set; }

    [DisplayName("電子郵件")]
    public string? email { get; set; }
};