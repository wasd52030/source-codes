using System.Globalization;

namespace _20231016.Logger;

class ApplicationLogger : ILogger
{
    private static object Lock = new object();
    private readonly string name;
    private readonly Func<ApplicationLoggerConfiguration> getCurrentConfig;

    public ApplicationLogger(string name, Func<ApplicationLoggerConfiguration> getCurrentConfig)
    {
        (this.name, this.getCurrentConfig) = (name, getCurrentConfig);
    }

    public IDisposable? BeginScope<TState>(TState state) where TState : notnull => default!;

    public bool IsEnabled(LogLevel logLevel) => getCurrentConfig().LogLevels.ContainsKey(logLevel);

    private string GetTimestamp()
    {
        DateTime now = TimeZoneInfo.ConvertTime(DateTime.Now, TimeZoneInfo.Local);
        string str = now.ToString("yyyy/MM/dd HH:mm:ss", CultureInfo.InvariantCulture);
        return str;
    }

    public void Log<TState>(LogLevel logLevel, EventId eventId, TState state, Exception? exception, Func<TState, Exception?, string> formatter)
    {
        lock (Lock)
        {
            var config = getCurrentConfig();
            if (config.EventId == 0 || config.EventId == eventId.Id)
            {
                var color = Console.ForegroundColor;
                var currentTimeStamp=GetTimestamp();
                Console.ForegroundColor = config.LogLevels[logLevel];
                Console.WriteLine($"[{currentTimeStamp}] {logLevel} - {formatter(state, exception)}");
                Console.ForegroundColor = color;
            }
        }
    }
}