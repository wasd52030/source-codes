#include <bits/stdc++.h>
using namespace std;

int main()
{
    long n, i = 2, pow_cnt = 0;
    cin >> n;
    long in_num = n;

    string out = to_string(in_num) + "=";

    while (n > 1)

    {
        while (n % i == 0)
        {
            pow_cnt++;
            n /= i;
        }

        if (pow_cnt != 0)
        {
            if (pow_cnt == 1)
                out += to_string(i) + "*";
            else if (pow_cnt != 1)
                out += to_string(i) + "^" + to_string(pow_cnt) + "*";
        }

        if (i == in_num)
            out = to_string(in_num) + "�O���";

        i++;
        pow_cnt = 0;
    }

    //�[�J�F����X�r��᭱���ˬd�A�קK�L����
    //���string��}�C�ާ@�ɡA�̭����X�Ӫ��F�諬�A�OChar�C
    //c++�̭���Char�n�γ�޸��A���޸���Char�}�C(�]�N�Ostring)
    if (out[out.length() - 1] == '*')
        out = out.erase(out.length() - 1);

    cout << out << "\n";

    return 0;
}
