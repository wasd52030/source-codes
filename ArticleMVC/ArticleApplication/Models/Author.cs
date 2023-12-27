namespace ArticleApplication.Models;

public class Author
{
    public int Id { get; set; }
    public string? Name { get; set; }

    public int? Phone { get; set; }

    public string? Email { get; set; }

    //Navigation Property導覽屬性
    public virtual ICollection<Article>? Articles { get; set; }
}