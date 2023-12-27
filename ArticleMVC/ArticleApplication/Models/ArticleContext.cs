using Microsoft.EntityFrameworkCore;

namespace ArticleApplication.Models;

public class ArticleContext : DbContext
{

    public ArticleContext(DbContextOptions<ArticleContext> options) : base(options)
    {
    }

    public virtual DbSet<Author> Authors { get; set; }
    public virtual DbSet<Article> Articles { get; set; }

    protected override void OnConfiguring(DbContextOptionsBuilder optionsBuilder)
        => optionsBuilder.UseSqlite("Data Source=./Data/article.db;");

    protected override void OnModelCreating(ModelBuilder modelBuilder)
    {
        modelBuilder.Entity<Author>().HasData(
             new Author { Id = 1, Name = "Kevin", Email = "kevin@gmail.com",Phone=1231234123 },
             new Author { Id = 2, Name = "David", Email = "david@gmail.com",Phone=114514 },
             new Author { Id = 3, Name = "Mary", Email = "mary@gmail.com" ,Phone=1919810}
        );

        modelBuilder.Entity<Article>().HasData(
                new Article { Id = 1, Title = "Kevin's article", Content = "dllm", LikeCount = 5,CreatedDate=new DateTime(2023,6,25), AuthorId = 1 },
                new Article { Id = 2, Title = "David's article", Content = "asdf", LikeCount = 10, CreatedDate = new DateTime(2023, 8, 27), AuthorId = 2 },
                new Article { Id = 3, Title = "Mary's article", Content = "haiyaa", LikeCount = 15, CreatedDate = new DateTime(2023, 7, 26), AuthorId = 3 }
            );
    }
}