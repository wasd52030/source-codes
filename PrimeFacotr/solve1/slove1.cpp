#include<bits/stdc++.h>
using namespace std;

int main()
{
    int a, b = 2;
    cout << "pls enter a num :";
    cin >> a;
    int in_num = a;
    vector<int> PrimeFactor;
    map<int, int> PrimePow;
    string out = to_string(a) + "=";

    //b=2,3,4...如果a可以整除b，就把b加入質因數表裡面，並且讓a=a/b，直至無法整除
    //應該類似於短除法
    while (a > 1)
    {
        while (a % b == 0)
        {
            PrimeFactor.push_back(b);
            a /= b;
        }
        b++;
    }

    //用map來存每個質因數有幾次方
    //map賦值:map[key]=value，在這裡，key用來存質因數，value用來存幾次方
    //std::count(vector.begin(),vector.end(),value); -> 在此為求vector中Value重複幾次
    //關於Range-Based-For，也就是以下for的用法，請自行google
    for (auto i : PrimeFactor)
    {
        PrimePow[i] = count(PrimeFactor.begin(), PrimeFactor.end(), i);
    }

    for (auto x : PrimePow)
    {
        if (x.second != 1)
            out += to_string(x.first) + "^" + to_string(x.second) + "*";
        else
            out += to_string(x.first) + "*";

    }

    out = out.erase(out.length() - 1);

    if(PrimeFactor.size()==1) out = to_string(in_num) + "是質數";

    cout << out;
    system("pause");
}