namespace MvcMain.Logger;

public class ApplicationLoggerConfiguration
{
    public int EventId { get; set; }
    public Dictionary<LogLevel, ConsoleColor> LogLevels { get; set; } = new()
    {
        [LogLevel.Error] = ConsoleColor.Red,
        [LogLevel.Warning] = ConsoleColor.Yellow,
        [LogLevel.Information] = ConsoleColor.Green,
    };
}