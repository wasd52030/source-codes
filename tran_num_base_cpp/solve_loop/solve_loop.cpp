//迴圈解
#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
using namespace std;

string tran_base(int x, int y)
{
	int a = 0, b = 0;
	vector<string> data;
	string out = "";

	while (true)
	{
		a = x % y;
		b = x / y;
		x = b;
		data.push_back(to_string(a));
		if (b == 0 && a == 0)
		{
			reverse(data.begin(), data.end());
			data.erase(data.begin());
			break;
		}
	}


	for (int i = 0; i < data.size(); i++)
	{
		if (data.at(i) == "10")
		{
			data.at(i) = "A";
		}
		else if (data.at(i) == "11")
		{
			data.at(i) = "B";
		}
		else if (data.at(i) == "12")
		{
			data.at(i) = "C";
		}
		else if (data.at(i) == "13")
		{
			data.at(i) = "D";
		}
		else if (data.at(i) == "14")
		{
			data.at(i) = "E";
		}
		else if (data.at(i) == "15")
		{
			data.at(i) = "F";
		}
	}

	for (auto i : data)
		out += i;
	return out;
}

int main()
{
	int a, b;
	while (true)
	{
		printf("Please input two positive numbers: ");
		cin >> a >> b;
		if (a == 0 || b == 0)
		{
			break;
		}
		else
		{
			printf("(%d)_10=(%s)_%d\n", a, tran_base(a, b).c_str(), b);
		}
	}
	system("pause");
	return 0;
}