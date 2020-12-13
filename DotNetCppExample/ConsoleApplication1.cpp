#include "pch.h"
#include <iostream>

using namespace System;
using namespace System::Collections::Generic;
using namespace System::Text::RegularExpressions;

void DotNetListExample()
{
    List<int>^ data = gcnew List<int>;
    Random^ k = gcnew Random();
    for (int i = 0; i <= 100; i++)
    {
        int x = k->Next(0,101);
        data->Add(x);
    }

    Console::Write("before sort\n");
    for each (int k in data)
    {
        Console::Write(k.ToString() + " ");
    }

    data->Sort();
    Console::WriteLine();
    Console::WriteLine();

    Console::Write("after sort\n");
    for each (int k in data)
    {
        Console::Write(k.ToString() + " ");
    }
}

String^ DotNetRegexExample(String^ in)
{
    String^ out=Regex::IsMatch(in, ".*ab.*ba.*") ? "true" : "false";
    return out;
}

int main(array<System::String ^> ^args)
{
    Console::WriteLine("---.Net C++ Regex Example---");
    Console::Write("pls input you want to check : ");
    String^ in = Console::ReadLine();
    Console::WriteLine(DotNetRegexExample(in));
    Console::WriteLine();
    Console::WriteLine("---.Net List Example---");
    DotNetListExample();
    Console::WriteLine();
    system("pause");
    return 0;
}

