//遞迴鬧的歡，效能拉清單
#include <iostream>
#include <cmath>

//求一N位非負整數，其各位數字的N次方和
int solution(int x, int k, int o = 0)
{
    if (x == 0)
        return o;
    o += pow((x % 10), k);
    solution(x / 10, k, o);
}

//求一N位非負整數的位數
int pows(int x, int o = 0)
{
    if (x == 0)
        return o;
    o++;
    pows(x / 10, o);
}

int main(int argc, char const *argv[])
{
    int a, b;

    while (scanf("%d %d", &a, &b) != EOF)
    {
        int x[100]{0}, y = 0;

        for (int i = a; i < b; i++)
        {
            if (solution(i, pows(i)) == i)
            {
                x[y] = i;
                y++;
            }
        }

        if (y == 0)
        {
            printf("none");
        }
        else
        {
            for (int i = 0; i < y; i++)
            {
                printf("%d ", x[i]);
            }
        }
        printf("\n");
    }
    return 0;
}