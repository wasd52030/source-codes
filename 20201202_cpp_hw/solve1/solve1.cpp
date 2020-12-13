#include "pch.h"
#include <iostream>
using namespace System;
using namespace System::Collections::Generic;
int r;

int k(int x)
{
	if (x < 10)
	{
		r = (r * 10) + (x % 10);
		return r;
	}
	else
	{
		r = (r * 10) + (x % 10);
		k(x / 10);
		return r;
	}
	r = 0;
}

int main(array<System::String^>^ args)
{
	int c = 0;
	while (true)
	{
		int a = Convert::ToInt32(Console::ReadLine());
		int b = Convert::ToInt32(Console::ReadLine());
		c = a + b;
		if (c <= 0)
			break;
		r = 0;
		Console::WriteLine(k(c));
		Console::WriteLine();
	}
	std::system("pause");
	return 0;
}