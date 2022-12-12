#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(int argc, char const *argv[])
{
    int coins[] = {0, 0, 0, 0};
    int len_coins = sizeof(coins) / sizeof(int);

    char a[50];
    printf("denominations: "); // 面額種類
    scanf("%s", a);
    int a_len = 0;
    while (a[a_len] != '\0')
        a_len++;
    char b[3];
    int b_cnt = 0, coin_cnt = 0;
    for (int i = 0; i < a_len; i++)
    {
        if (a[i] != ',')
        {
            b[b_cnt] = a[i];
            b_cnt++;
        }
        else
        {
            b_cnt = 0;
            coins[coin_cnt] = atoi(b);
            coin_cnt++;
        }
    }
    coins[coin_cnt] = atoi(b); // 最後一個幣值
    coin_cnt = 0;
    for (int i = 0; i < len_coins; i++)
    {
        if (coins[i] != 0)
        {
            coin_cnt++;
        }
    }

    int x = 0;
    printf("total money: ");
    scanf("%d", &x);

    for (int i = 0; i <= x; i++)
    {
        if (coin_cnt == 1)
        {
            if (i * coins[0] == x)
            {
                printf("(%d)\n", i);
            }
        }
        for (int j = 0; j <= x; j++)
        {
            if (coin_cnt == 2)
            {
                if (i * coins[0] + j * coins[1] == x)
                {
                    printf("(%d,%d)\n", i, j);
                }
            }
            for (int k = 0; k <= x; k++)
            {
                if (coin_cnt == 3)
                {
                    if (i * coins[0] + j * coins[1] + k * coins[2] == x)
                    {
                        printf("(%d,%d,%d)\n", i, j, k);
                    }
                }

                for (int l = 0; l <= x; l++)
                {
                    if (coin_cnt == 4)
                    {
                        if (i * coins[0] + j * coins[1] + k * coins[2] + l * coins[3] == x)
                        {
                            printf("(%d,%d,%d,%d)\n", i, j, k, l);
                        }
                    }
                }
            }
        }
    }

    return 0;
}
