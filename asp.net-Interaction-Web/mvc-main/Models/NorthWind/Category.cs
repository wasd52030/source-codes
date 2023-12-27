namespace MvcMain.Models;

public partial class Category
{
    public long CategoryId { get; set; }

    public string? CategoryName { get; set; }

    public string? Description { get; set; }

    public byte[]? Picture { get; set; }

    public virtual ICollection<Product> Products { get; set; } = new List<Product>();
}
