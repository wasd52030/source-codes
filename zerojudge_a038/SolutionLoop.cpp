#include <stdio.h>

int main(int argc, char const *argv[])
{
    int a, cnt = 0;
    while (scanf("%d", &a) != EOF)
    {
        int r = 0;
        while (a > 0)
        {
            r = (r * 10) + (a % 10);
            a /= 10;
        }
        printf("%d", r);
    }
    return 0;
}