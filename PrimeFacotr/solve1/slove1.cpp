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

    //b=2,3,4...�p�Ga�i�H�㰣b�A�N��b�[�J��]�ƪ�̭��A�åB��a=a/b�A���ܵL�k�㰣
    //����������u���k
    while (a > 1)
    {
        while (a % b == 0)
        {
            PrimeFactor.push_back(b);
            a /= b;
        }
        b++;
    }

    //��map�Ӧs�C�ӽ�]�Ʀ��X����
    //map���:map[key]=value�A�b�o�̡Akey�ΨӦs��]�ơAvalue�ΨӦs�X����
    //std::count(vector.begin(),vector.end(),value); -> �b�����Dvector��Value���ƴX��
    //����Range-Based-For�A�]�N�O�H�Ufor���Ϊk�A�Цۦ�google
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

    if(PrimeFactor.size()==1) out = to_string(in_num) + "�O���";

    cout << out;
    system("pause");
}