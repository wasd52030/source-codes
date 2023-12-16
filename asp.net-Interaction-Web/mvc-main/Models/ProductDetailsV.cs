namespace MvcMain.Models;

public partial class ProductDetailsV
{
    public long? ProductId { get; set; }

    public string? ProductName { get; set; }

    public long? SupplierId { get; set; }

    public long? CategoryId { get; set; }

    public string? QuantityPerUnit { get; set; }

    public byte[]? UnitPrice { get; set; }

    public long? UnitsInStock { get; set; }

    public long? UnitsOnOrder { get; set; }

    public long? ReorderLevel { get; set; }

    public string? Discontinued { get; set; }

    public string? CategoryName { get; set; }

    public string? CategoryDescription { get; set; }

    public string? SupplierName { get; set; }

    public string? SupplierRegion { get; set; }
}
