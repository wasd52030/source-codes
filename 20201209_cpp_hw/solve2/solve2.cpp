#include <stdio.h>
#include <stdlib.h>
#include <time.h>


void main()
{
	srand(time(NULL));
	while (1)
	{
		int a, i, judge, number, b, min, s, k, p;
		int ans[6] = { 0 };
		int ansnew[6] = { 0 };
		scanf_s("%d", &a);
		if (a <= 0)
		{
			break;
		}

		for (number = 0; number < a; number++)
		{
			i = 0;

			while (i < 6)
			{
				judge = 0;
				b = 1 + rand() % 49;

				//判定重複
				for (int j = 0; j < 6; j++)
				{
					if (b == ans[j])
					{
						judge = 1;
					}
				}
				if (judge != 1)
				{
					ans[i] = b;
					i++;
				}
			}

			//排序
			for (k = 0; k < 6; k++)
			{
				min = 99;
				for (p = 0; p < 6; p++)
				{
					if (ans[p] < min)
					{
						min = ans[p];
						s = p;
					}
				}
				ans[s] = 99;
				ansnew[k] = min;
			}

			//輸出
			for (k = 0; k < 6; k++)
			{
				printf("%d ", ansnew[k]);
			}
			printf("\n");
		}
		printf("\n");
	}
	system("pause");
}