using System.ComponentModel.DataAnnotations.Schema;

namespace ArticleApplication.Models;

public class Article
{
    public int Id { get; set; } //Primary Key
    public string? Title { get; set; }
    public string? Content { get; set; }

    public int LikeCount { get; set; }

    public DateTime? CreatedDate { get; set; }

    public int AuthorId { get; set; } //Foreign Key欄位

    [ForeignKey("AuthorId")]
    public virtual Author? Author { get; set; }
}