namespace MvcMain.Models;

public partial class OrderSubtotal
{
    public long? OrderId { get; set; }

    public byte[]? Subtotal { get; set; }
}
