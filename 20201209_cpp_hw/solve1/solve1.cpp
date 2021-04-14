#include <bits/stdc++.h>
using namespace std;

int main()
{
    srand(time(NULL));
    array<int, 6> data;
    vector<int> lottery;
    int in, cnt = 0;
    while (true)
    {
        cin >> in;
        if (in <= 0)
            break;
        else
        {
            for (int i = 0; i < in; i++)
            {
                lottery.clear();  //把上次取剩的元素清空
                for (int i = 0; i < 49; i++)
                {
                    lottery.push_back(i + 1);  //初始化lottery vector,重新將1-49放入
                }

                for (int j = 0; j < 6; j++)
                {
                    int k = (rand() % lottery.size()); //求隨機數字，用以取vector中的值
                    data[j] = lottery[k];
                    swap(lottery[k], lottery[lottery.size() - 1]); //把取過的數字跟vector中的最後一個數字交換
                    lottery.pop_back(); //砍掉用過的數字
                }

                sort(data.begin(), data.end());
                for (int i : data)
                {
                    cout << i << " ";
                }
                cout << "\n";
            }
            cout << "\n";
        }
    }
    system("pause");
    return 0;
}