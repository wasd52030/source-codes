namespace MvcMain.Middlewares;

public class RequestLogMiddleware
{
    private readonly RequestDelegate next;
    private readonly ILogger<RequestLogMiddleware> logger;

    public RequestLogMiddleware(RequestDelegate next, ILogger<RequestLogMiddleware> logger)
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

public static class RequestLogMiddlewareExtensions
{
    public static void UseRequestLog(this IApplicationBuilder app)
    {
        app.UseMiddleware<RequestLogMiddleware>();
    }
}