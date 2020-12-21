#include <iostream>
#include <ctime>
using namespace std;

int moneycnt(int money, int cnt)
{
	int g = money;
	if (cnt>0 && cnt<3)
	{
		g += 800;
	}
	else if (cnt>2 && cnt<5)
	{
		g += 400;
	}
	else if (cnt>4 && cnt<8)
	{
		g += 100;
	}
	else if (cnt>8 && cnt<10)
	{
		g -= 200;
	}
	else if (cnt>10)
	{
		g -= 600;
	}
	cout << "win\nyou have guessed " << cnt << "times\n";
	cout << "Now you have "<<g<<" dollars\n";
	return g;
}

int main()
{
    int in=8, ans, cnt=0;
	int money = 1000;
	int max = 100, min = 0;
	srand(time(NULL));
	while (true)
	{
		if (money <= 0)
		{
			cout << "you mdfk no money! get out!\n";
			break;
		}
		else if(in == 0)
		{
			break;
		}
		ans = rand() % 100 + 1;
		while (true)
		{
			cout << "ans=" << ans << "\n";
			cout << "pls input a num->";
			cin >> in;

			if (in == 0)
			{
				break;
			}
			if (in == ans)
			{
				cnt++;
				money=moneycnt(money, cnt);
				cnt = 0;
				break;
			}
			else if (in < ans)
			{
				min = in;
				cnt++;
				cout << "ans is larger than" << min << "\n";
			}
			else if (in > ans)
			{
				max = in;
				cnt++;
				cout << "ans is smaller than" << max << "\n";
			}
			cout << "you have guessed " << cnt << " times" << "\n\n";
		}
	}
	system("pause");
    return 0;
}