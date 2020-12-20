#include <iostream>
using namespace std;

int main()
{
    string x; //¿é¤J¦r¦ê
    cin >> x;
    string digits[] = { "¹s","³ü","¶L","°Ñ","¸v","¥î","³°","¬m","®Ã","¨h" };
    string radices[] = { "", "¬B","¨Õ","¥a" };
    string bigRadices[] = { "", "¸U" };
    string out;
    if (atoi(x.c_str()) > 0)
    {
        int zerocnt = 0;
        for (int i = 0; i < x.size(); i++)
        {
            int p = x.size() - i - 1;
            string d = x.substr(i, 1);
            int quotient = p / 4;
            int modulus = p % 4;
            if (d == "0")
            {
                zerocnt++;
            }
            else
            {
                if (zerocnt > 0)
                {
                    out += digits[0];
                }
                zerocnt = 0;
                out += digits[atoi(d.c_str())] + radices[modulus];
            }
            if (modulus == 0 && zerocnt < 4)
            {
                out += bigRadices[quotient];
            }
        }
    }
    cout << out << "\n";
    system("pause");
    return 0;
}