using Microsoft.EntityFrameworkCore;

namespace MvcMain.Models;


public class BlogContext : DbContext
{
    public BlogContext(DbContextOptions<BlogContext> options) : base(options)
    {
    }
    public virtual DbSet<User> Users { get; set; }
    public virtual DbSet<Blog> Blogs { get; set; }
    public virtual DbSet<Post> Posts { get; set; }

    protected override void OnConfiguring(DbContextOptionsBuilder optionsBuilder)
        => optionsBuilder.UseSqlite("Data Source=./Data/blog.db;");

    protected override void OnModelCreating(ModelBuilder modelBuilder)
    {
        modelBuilder.Entity<User>().HasData(
             new User { Id = 1, UserName = "Kevin", Email = "kevin@gmail.com" },
             new User { Id = 2, UserName = "David", Email = "david@gmail.com" },
             new User { Id = 3, UserName = "Mary", Email = "mary@gmail.com" }
            );

        modelBuilder.Entity<Blog>().HasData(
                new Blog { BlogId = 1, BlogName = "Kevin's Blog", Url = "blogs.com.tw/kevin", UserId = 1 },
                new Blog { BlogId = 2, BlogName = "David's Blog", Url = "blogs.com.tw/david", UserId = 2 },
                new Blog { BlogId = 3, BlogName = "Mary's Blog", Url = "blogs.com.tw/mary", UserId = 3 }
            );

        modelBuilder.Entity<Post>().HasData(
                new Post { PostId = 1, Title = "ASP.NET Core", Content = "ASP.NET Core Tutorial", BlogId = 1 },
                new Post { PostId = 2, Title = "Entity Framework Core", Content = "Entity Framework Core Tutorial", BlogId = 1 },
                new Post { PostId = 3, Title = "Vue.js", Content = "Vue.js Tutorial", BlogId = 2 },
                new Post { PostId = 4, Title = "Bootstrap 4", Content = "Bootstrap 4 Tutorial", BlogId = 3 }
            );
    }
}