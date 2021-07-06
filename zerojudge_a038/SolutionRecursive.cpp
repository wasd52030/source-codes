#include <stdio.h>

int solution(int in, int r = 0)
{
    if (in == 0) return r;
    r = (r * 10) + (in % 10);
    solution(in / 10, r);
}

int main(int argc, char const *argv[])
{
    int x;
    while (scanf("%d", &x) != EOF)
    {
        printf("%d\n", solution(x));
    }
    return 0;
}