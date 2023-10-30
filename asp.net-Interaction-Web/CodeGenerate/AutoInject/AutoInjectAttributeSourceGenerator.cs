using Microsoft.CodeAnalysis;
using System;
using System.Diagnostics;
using System.Text;

namespace CodeGenerate.AutoInject;

[Generator]
public class AutoInjectAttributeSourceGenerator : ISourceGenerator
{
    public void Execute(GeneratorExecutionContext context)
    {
        context.AnalyzerConfigOptions.GlobalOptions.TryGetValue("build_property.RootNamespace", out var rootNamespace);
        var attributeName = removeSourceGeneratorPostfix<AutoInjectAttributeSourceGenerator>();

        var strBuild = new StringBuilder();
        strBuild.AppendLine($"namespace {rootNamespace}.Attributes;");
        strBuild.AppendLine($"[AttributeUsage(AttributeTargets.Class | AttributeTargets.Property | AttributeTargets.Field, AllowMultiple = false)]");
        strBuild.AppendLine($"class {attributeName} : Attribute");
        strBuild.AppendLine("{");
        strBuild.AppendLine("}");

        try
        {
            context.AddSource($"{attributeName}.g.cs", strBuild.ToString());
        }
        catch (Exception e)
        {
            Debug.WriteLine(e.Message);
        }
    }

    private string removeSourceGeneratorPostfix<T>() where T : ISourceGenerator
    {
        var attributeName = typeof(T).Name;
        return attributeName.Remove(attributeName.Length - "SourceGenerator".Length, "SourceGenerator".Length);
    }

    public void Initialize(GeneratorInitializationContext context)
    {

    }
}
