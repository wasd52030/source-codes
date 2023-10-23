namespace _20231016.Middlewares;

public class HttpLogMiddleware
{
    private readonly RequestDelegate next;
    private readonly ILogger<HttpLogMiddleware> logger;

    public HttpLogMiddleware(RequestDelegate next, ILogger<HttpLogMiddleware> logger)
    {
        this.next = next;
        this.logger = logger;
    }

    public async Task Invoke(HttpContext context)
    {
        var req = context.Request;
        var res = context.Response;

        logger.LogInformation("{method} route:{baseurl} statusCode:{StatusCode}", req.Method, req.Path, res.StatusCode);
        logger.LogInformation("userAgent: {userAgent} contenType: {contenType} ip: {ip}", req.Headers["User-Agent"], req.ContentType, context.Connection.RemoteIpAddress);

        await next(context);
    }
}

public static class HttpLogMiddlewareExtensions
{
    public static void UseHttpLog(this IApplicationBuilder app)
    {
        app.UseMiddleware<HttpLogMiddleware>();
    }
}