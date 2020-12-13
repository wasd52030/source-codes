#include "pch.h"
#include <iostream>

using namespace System;
using namespace System::Collections::Generic;

int main(array<System::String ^> ^args)
{
	int c = 0;

	while (true)
	{
		int a = Convert::ToInt32(Console::ReadLine());
		int b = Convert::ToInt32(Console::ReadLine());
		c = a + b;

		if (c <= 0)
			break;
		else
		{
			String^ out = c.ToString();
			array<Char>^ out_chr = out->ToCharArray();
			Array::Reverse(out_chr);
			for each (Char^ k in out_chr)
			{
				Console::Write(k);
			}
			Console::WriteLine("\n");
		}
	}
	std::system("pause");
    return 0;
}
