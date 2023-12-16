namespace MvcMain.Models;

public partial class Invoice
{
    public string? ShipName { get; set; }

    public string? ShipAddress { get; set; }

    public string? ShipCity { get; set; }

    public string? ShipRegion { get; set; }

    public string? ShipPostalCode { get; set; }

    public string? ShipCountry { get; set; }

    public string? CustomerId { get; set; }

    public string? CustomerName { get; set; }

    public string? Address { get; set; }

    public string? City { get; set; }

    public string? Region { get; set; }

    public string? PostalCode { get; set; }

    public string? Country { get; set; }

    public byte[]? Salesperson { get; set; }

    public long? OrderId { get; set; }

    public byte[]? OrderDate { get; set; }

    public byte[]? RequiredDate { get; set; }

    public byte[]? ShippedDate { get; set; }

    public string? ShipperName { get; set; }

    public long? ProductId { get; set; }

    public string? ProductName { get; set; }

    public byte[]? UnitPrice { get; set; }

    public long? Quantity { get; set; }

    public double? Discount { get; set; }

    public byte[]? ExtendedPrice { get; set; }

    public byte[]? Freight { get; set; }
}
