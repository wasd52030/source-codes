#include <iostream>
using namespace std;

int gcd(int a, int b)
{
	if (b==0 && a!=0)
	{
		return a;
	}
	else if (b>0 && a!=0)
	{
		return gcd(b, a % b);
	}
}
int main()
{
	int a, b;
	while (true)
	{
		cin >> a >> b;
		if (a==0 || b==0)
		{
			break;
		}
		else
		{
			cout << "GCD: " << gcd(a, b)<<"\n";
		}
	}
	system("pause");
    return 0;
}