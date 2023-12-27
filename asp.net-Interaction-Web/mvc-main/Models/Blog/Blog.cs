using System.ComponentModel.DataAnnotations.Schema;

namespace MvcMain.Models;

public class Blog
{
    public int BlogId { get; set; } //Primary Key
    public string? BlogName { get; set; }
    public string? Url { get; set; }
    public int UserId { get; set; } //Foreign Key欄位

    //Navigation Property導覽屬性
    [ForeignKey("UserId")]
    public virtual User? User { get; set; }
    public virtual ICollection<Post>? Post { get; set; }
}