#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main()
{
    string x; //��J�r��
    cin >> x;
    vector<string> x_bar; //�N��J�r�����A��K��Ʀr�����
    string g;
    for (int i=0;i<x.size();i++)
    {
        g = x[i];
        x_bar.push_back(g);
    }

    reverse(x_bar.begin(), x_bar.end()); //����vector
    string chinum[] = { "�s","��","�L","��","�v","��","��","�m","��","�h" };
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
                    out.push_back(chinum[x] + "�B");
                }
                else
                {
                    out.push_back(chinum[x]);
                }
                break;
            case 2:
                if (x!=0)
                {
                    out.push_back(chinum[x] + "��");
                }
                else
                {
                    out.push_back(chinum[x]);
                }
                break;
            case 3:
                if (x != 0)
                {
                    out.push_back(chinum[x] + "�a");
                }
                else
                {
                    out.push_back(chinum[x]);
                }
                break;
            case 4:
                if (x != 0)
                {
                    out.push_back(chinum[x] + "�U");
                }
                else
                {
                    out.push_back("�U");
                }
                break;
            case 5:
                if (x != 0)
                {
                    out.push_back(chinum[x] + "�B");
                }
                else
                {
                    out.push_back(chinum[x]);
                }
                break;
            case 6:
                if (x != 0)
                {
                    out.push_back(chinum[x] + "��");
                }
                else
                {
                    out.push_back(chinum[x]);
                }
                break;
            case 7:
                if (x != 0)
                {
                    out.push_back(chinum[x] + "�a");
                }
                else
                {
                    out.push_back(chinum[x]);
                }
                break;
        }
    }

    reverse(out.begin(), out.end());
    out.erase(unique(out.begin(), out.end()), out.end()); //�h�����ƪ��s
    
    if (out[1] == "�s")
    {
        out.erase(out.begin() + 1);
        out.insert(out.begin() + 2, "�s");
    }

    if (out[out.size() - 1] == "�s") //�h���̫�@�쪺�s
        out.pop_back();

    for (string k : out)
        cout << k;

    cout << "\n";
    system("pause");
}
