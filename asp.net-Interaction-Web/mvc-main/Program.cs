using Microsoft.EntityFrameworkCore;
using MvcMain.Logger;
using MvcMain.Middlewares;
using MvcMain.Models;


var builder = WebApplication.CreateBuilder(args);

// Add services to the container.
builder.Services.AddControllersWithViews();

builder.Services.AddLogging(logging =>
{
    logging.ClearProviders();
    logging.AddApplicationLogger();
});


//sqlite northwind db
builder.Services.AddDbContext<NorthwindContext>();

//sqlite blog db
builder.Services.AddDbContext<BlogContext>();


// MySql db
// builder.Services.AddDbContext<ApplicationDBContext>(options =>
// {
//     options.UseMySql(
//         builder.Configuration.GetConnectionString("DefaultConnection"),
//         new MySqlServerVersion(new Version(5, 7, 43))
//     );
// });

var app = builder.Build();

// Configure the HTTP request pipeline.
if (!app.Environment.IsDevelopment())
{
    app.UseExceptionHandler("/Home/Error");
    // The default HSTS value is 30 days. You may want to change this for production scenarios, see https://aka.ms/aspnetcore-hsts.
    app.UseHsts();
    app.UsePathBase("/C109152304");
}

app.UseHttpsRedirection();
app.UseStaticFiles();

app.UseRouting();

app.UseRequestLog();

app.UseAuthorization();


app.MapControllerRoute(
    name: "default",
    pattern: "{controller=Home}/{action=Index}/{id?}"
);

app.MapControllers();

app.Run();