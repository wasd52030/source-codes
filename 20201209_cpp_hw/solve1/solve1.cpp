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
                lottery.clear();  //��W�����Ѫ������M��
                for (int i = 0; i < 49; i++)
                {
                    lottery.push_back(i + 1);  //��l��lottery vector,���s�N1-49��J
                }

                for (int j = 0; j < 6; j++)
                {
                    int k = (rand() % lottery.size()); //�D�H���Ʀr�A�ΥH��vector������
                    data[j] = lottery[k];
                    swap(lottery[k], lottery[lottery.size() - 1]); //����L���Ʀr��vector�����̫�@�ӼƦr�洫
                    lottery.pop_back(); //�屼�ιL���Ʀr
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