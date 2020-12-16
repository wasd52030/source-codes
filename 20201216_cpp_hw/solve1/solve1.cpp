#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main()
{
    string x; //輸入字串
    cin >> x;
    vector<string> x_bar; //將輸入字串反轉，方便對數字的位數
    string g;
    for (int i=0;i<x.size();i++)
    {
        g = x[i];
        x_bar.push_back(g);
    }

    reverse(x_bar.begin(), x_bar.end()); //反轉vector
    string chinum[] = { "零","壹","貳","參","肆","伍","陸","柒","捌","玖" };
    vector<string> out;

    for (int i = 0; i < x_bar.size(); i++)
    {
        g = x_bar[i];
        int x = atoi(g.c_str());
        switch (i)
        {
            case 0:
                out.push_back(chinum[x]);
                break;
            case 1:
                if (x != 0)
                {
                    out.push_back(chinum[x] + "拾");
                }
                else
                {
                    out.push_back(chinum[x]);
                }
                break;
            case 2:
                if (x!=0)
                {
                    out.push_back(chinum[x] + "佰");
                }
                else
                {
                    out.push_back(chinum[x]);
                }
                break;
            case 3:
                if (x != 0)
                {
                    out.push_back(chinum[x] + "仟");
                }
                else
                {
                    out.push_back(chinum[x]);
                }
                break;
            case 4:
                if (x != 0)
                {
                    out.push_back(chinum[x] + "萬");
                }
                else
                {
                    out.push_back("萬");
                }
                break;
            case 5:
                if (x != 0)
                {
                    out.push_back(chinum[x] + "拾");
                }
                else
                {
                    out.push_back(chinum[x]);
                }
                break;
            case 6:
                if (x != 0)
                {
                    out.push_back(chinum[x] + "佰");
                }
                else
                {
                    out.push_back(chinum[x]);
                }
                break;
            case 7:
                if (x != 0)
                {
                    out.push_back(chinum[x] + "仟");
                }
                else
                {
                    out.push_back(chinum[x]);
                }
                break;
        }
    }

    reverse(out.begin(), out.end());
    out.erase(unique(out.begin(), out.end()), out.end()); //去掉重複的零
    
    if (out[1] == "零")
    {
        out.erase(out.begin() + 1);
        out.insert(out.begin() + 2, "零");
    }

    if (out[out.size() - 1] == "零") //去掉最後一位的零
        out.pop_back();

    for (string k : out)
        cout << k;

    cout << "\n";
    system("pause");
}
