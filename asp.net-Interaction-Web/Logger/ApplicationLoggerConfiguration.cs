namespace _20231016.Logger;

public class ApplicationLoggerConfiguration
{
    public int EventId { get; set; }
    public Dictionary<LogLevel, ConsoleColor> LogLevels { get; set; } = new()
    {
        [LogLevel.Information] = ConsoleColor.Green
    };
}