#include <iostream>
using namespace std;

void main()
{
	int a = 1, b = 1;

	while (true)
	{
		printf("%d*%d=%d\t", a, b, a * b);
		b++;

		if (b > 9)
		{
			b = 1;
			a++;
			printf("\n");
		}

		if (a == 10)
			break;
	}
	system("pause");
}