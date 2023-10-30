using Microsoft.CodeAnalysis;
using System;

namespace CodeGenerate;

[Generator]
public class HelloSourceGenerator : ISourceGenerator
{
    public void Execute(GeneratorExecutionContext context)
    {
        // Find the main method
        
    }

    public void Initialize(GeneratorInitializationContext context)
    {
        // No initialization required for this one
    }
}