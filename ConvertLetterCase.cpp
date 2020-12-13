#include <bits/stdc++.h>
using namespace std;

int main(int argc, char const *argv[])
{
    string in;
    //cin預設下會跳過所有空格，要一次讀整行，請用getline(cin,string)
    getline(cin,in); 

    for(auto x:in)
    {
        switch (x)
        {
            case 65 ... 90:     //ascii code 65-90為大寫的A-Z
                x+=32;
                break;
            case 97 ... 122:    //ascii code 91-122為小寫的A-Z
                x-=32;
                break;
            default:
                break;
        }
        cout<<x;
    }
    return 0;
}
