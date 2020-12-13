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
                lottery.clear();  //рΩ逞じ睲
                for (int i = 0; i < 49; i++)
                {
                    lottery.push_back(i + 1);  //﹍てlottery vector,穝盢1-49
                }

                for (int j = 0; j < 6; j++)
                {
                    int k = (rand() % lottery.size()); //―繦诀计ノvectorい
                    data[j] = lottery[k];
                    swap(lottery[k], lottery[lottery.size() - 1]); //р筁计蛤vectorい程计ユ传
                    lottery.pop_back(); //奔ノ筁计
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