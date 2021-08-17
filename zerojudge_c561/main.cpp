#include <stdio.h>

//數字反轉
int solution(int i, int o = 0)
{
    if (i == 0) return o;
    o = o * 10 + i % 10;
    solution(i / 10, o);
}

int main(int argc, char const *argv[])
{
    int k = 0, max = 0;
    while (scanf("%d", &k) != EOF)
    {
        for (int i = 0; i < k; i++)
        {
            int d = 0;
            scanf("%d", &d);
            max = (solution(d) > max) ? solution(d) : max;
        }
        printf("%d\n", max);
    }
    return 0;
}
