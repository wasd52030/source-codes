#include <iostream>

struct point
{
	int x, y;
};

int main()
{
	int d = 0;
	point ps[1000];
	while (scanf("%d", &d) != EOF)
	{
		for (int i = 0; i < d; i++)
		{
			point a;
			scanf("%d %d", &a.x, &a.y);
			ps[i] = a;
		}

		//先排x軸，如果x軸相同再排y軸
		for (int i = 0; i < d; i++)
		{
			for (int j = 0; j < d - 1 - i; j++)
			{
				if (ps[j].x > ps[j + 1].x)
				{
					std::swap(ps[j], ps[j + 1]);
				}

				if (ps[j].x == ps[j + 1].x)
				{
					if (ps[j].y > ps[j + 1].y)
					{
						std::swap(ps[j], ps[j + 1]);
					}
				}
			}
		}

		for (int i = 0; i < d; i++)
		{
			printf("%d %d\n", ps[i].x, ps[i].y);
		}
	}

	return 0;
}