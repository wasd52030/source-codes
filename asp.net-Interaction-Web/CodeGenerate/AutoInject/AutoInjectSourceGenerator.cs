using Microsoft.CodeAnalysis;
using Microsoft.CodeAnalysis.CSharp.Syntax;
using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.Linq;
using System.Text;

namespace CodeGenerate.AutoInject;

[Generator]
public class AutoInjectSourceGenerator : ISourceGenerator
{
    private GeneratorExecutionContext _context;
    public void Execute(GeneratorExecutionContext context)
    {
        _context = context;

        foreach (var tree in context.Compilation.SyntaxTrees)
        {
            if (tree.FilePath.EndsWith("g.cs")) continue;
            ProcessTree(tree);
        }
    }

    private void ProcessTree(SyntaxTree? tree)
    {
        var root = tree?.GetRoot();
        var classNodes = root?.DescendantNodes().OfType<ClassDeclarationSyntax>();
        var classNodeWithPartial = classNodes.Where(n => n.Modifiers.ToString().Contains("partial"));
        foreach (var classNode in classNodeWithPartial)
        {
            ProcessClass(classNode);
        }
    }

    private void ProcessClass(ClassDeclarationSyntax classNode)
    {
        if (!classNode.AttributeLists.ToString().Contains("AutoInject")) return;

        var root = classNode.SyntaxTree?.GetRoot();
        var nodes = root.DescendantNodes();

        // find using 
        // find namespace
        var usingNodes = nodes.OfType<UsingDirectiveSyntax>();
        var namespaceNode = nodes.OfType<NamespaceDeclarationSyntax>().FirstOrDefault();

        if (namespaceNode == null) return;

        // build cs file
        var strBuild = new StringBuilder();
        foreach (var node in usingNodes)
        {
            strBuild.AppendLine(node.ToString());
        }

        var namespaceName = namespaceNode.Name;
        strBuild.AppendLine($"namespace {namespaceName}");
        strBuild.AppendLine("{");

        var modifiers = classNode.Modifiers;
        var baseList = classNode.BaseList;
        strBuild.AppendLine($"{modifiers} class {classNode.Identifier} {baseList}");
        strBuild.AppendLine("{");

        var fieldNodes = classNode.DescendantNodes().OfType<FieldDeclarationSyntax>();
        var fieldNodeWithAutoInject = fieldNodes.Where(n =>
        {
            return n.AttributeLists.ToString().Contains("AutoInject");
        });

        var className = classNode.Identifier.ToString();
        var pairs = new List<Tuple<string, string>>();
        Debug.WriteLine(6);
        foreach (var field in fieldNodeWithAutoInject)
        {
            //Debug.WriteLine(field.Modifiers);
            //Debug.WriteLine(field.Declaration.ToString());
            pairs.Add(
                Tuple.Create(
                    field.Declaration.Type.ToString(),
                    field.Declaration.Variables.ToString()
                )
            );
            //strBuild.Append($"{field.Modifiers} {field.Declaration.ToString()}");
        }
        var paraListText = string.Join(",", pairs.Select(p => $"{p.Item1} {FieldText2ParaText(p.Item2)}"));
        strBuild.AppendLine($"public {className}({paraListText})");
        strBuild.AppendLine("{");
        foreach (var fieldName in pairs.Select(s => s.Item2))
        {
            strBuild.AppendLine($"{fieldName}={FieldText2ParaText(fieldName)};");
        }
        strBuild.AppendLine("}");

        strBuild.AppendLine("}");

        strBuild.AppendLine("}");

        try
        {
            Debug.WriteLine(strBuild.ToString());
            _context.AddSource($"{classNode.Identifier}.g.cs", strBuild.ToString());
        }
        catch (Exception e)
        {
            Debug.WriteLine(e.Message);
        }
    }

    private string FieldText2ParaText(string fieldText)
    {
        return $"{char.ToLower(fieldText[0])}{fieldText.Substring(1)}";
    }

    public void Initialize(GeneratorInitializationContext context)
    {
        // No initialization required for this one
    }
}