using MvcMain.Models;
using Microsoft.EntityFrameworkCore;

namespace MvcMain.Data;

public class ApplicationDBContext : DbContext
{
    public ApplicationDBContext(DbContextOptions<ApplicationDBContext> options) : base(options)
    {
    }

    // public DbSet<Employee> Employees { get; set; }
}