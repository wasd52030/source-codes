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
            out = to_string(in_num) + "是質數";

        i++;
        pow_cnt = 0;
    }

    //加入了對於輸出字串後面的檢查，避免無腦砍
    //當把string當陣列操作時，裡面取出來的東西型態是Char。
    //c++裡面表Char要用單引號，雙引號表Char陣列(也就是string)
    if (out[out.length() - 1] == '*')
        out = out.erase(out.length() - 1);

    cout << out << "\n";

    return 0;
}
