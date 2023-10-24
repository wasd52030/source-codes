using _20231016.Models;
using Microsoft.EntityFrameworkCore;

namespace _20231016.Data;

public class ApplicationDBContext : DbContext
{
    public ApplicationDBContext(DbContextOptions<ApplicationDBContext> options) : base(options)
    {
    }

    public DbSet<Employee> Employees { get; set; }
}