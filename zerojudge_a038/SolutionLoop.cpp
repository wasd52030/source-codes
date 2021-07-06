#include <iostream>
using namespace std;

int main(int argc, char const *argv[])
{
    int a, cnt = 0;
    while (cin>>a)
    {
        int r = 0;
        while (a > 0)
        {
            r = (r * 10) + (a % 10);
            a /= 10;
        }
        cout<<r<<"\n";
    }
    return 0;
}
