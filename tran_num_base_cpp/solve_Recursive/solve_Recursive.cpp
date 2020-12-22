//遞迴解
#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
using namespace std;
string out = "";
vector<string> calc;

string tran_base(int x, int y)
{
	out = "";
	if (x == 0)
	{
		reverse(calc.begin(), calc.end());

		for (int i = 0; i < calc.size(); i++)
		{
			if (calc.at(i) == "10")
			{
				calc.at(i) = "A";
			}
			else if (calc.at(i) == "11")
			{
				calc.at(i) = "B";
			}
			else if (calc.at(i) == "12")
			{
				calc.at(i) = "C";
			}
			else if (calc.at(i) == "13")
			{
				calc.at(i) = "D";
			}
			else if (calc.at(i) == "14")
			{
				calc.at(i) = "E";
			}
			else if (calc.at(i) == "15")
			{
				calc.at(i) = "F";
			}
		}

		for (auto k : calc)
		{
			out += k;
		}
		calc.clear(); //清空vector中的資料
		calc.shrink_to_fit(); //清空vector所佔的記憶體
		return out;
	}
	else
	{
		calc.push_back(to_string(x % y));
		return tran_base(x / y, y);
	}
}

int main()
{
	int a, b;
	while (true)
	{
		cout << "Please input two positive numbers: ";
		cin >> a >> b;
		if (a == 0 || b == 0)
		{
			break;
		}
		else
		{
			cout << "(" << a << ")_10 = (" << tran_base(a, b) << ")_" << b << "\n";
		}
	}
	system("pause");
	return 0;
}