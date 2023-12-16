namespace MvcMain.Models;

public partial class OrderDetail
{
    public long OrderId { get; set; }

    public long ProductId { get; set; }

    public byte[] UnitPrice { get; set; } = null!;

    public long Quantity { get; set; }

    public double Discount { get; set; }

    public virtual Order Order { get; set; } = null!;

    public virtual Product Product { get; set; } = null!;
}
