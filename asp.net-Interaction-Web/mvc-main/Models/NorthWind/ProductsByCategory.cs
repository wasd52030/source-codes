﻿namespace MvcMain.Models;

public partial class ProductsByCategory
{
    public string? CategoryName { get; set; }

    public string? ProductName { get; set; }

    public string? QuantityPerUnit { get; set; }

    public long? UnitsInStock { get; set; }

    public string? Discontinued { get; set; }
}
