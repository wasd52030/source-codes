#include <iostream>
using namespace std;

int main()
{
    Loop:
        cout << "loop";
        goto Loop;
    return 0;
}