#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main()
{
    char d[][10] = { "零","壹","貳","參","肆","伍","陸","柒","捌","玖" };
    char r[][4] = { "", "拾","佰","仟" };
    char b[][3] = { "", "萬" };
    char x[9];
    char out[100];
    memset(out, '\0', 100);
    scanf_s("%s", &x, sizeof(x));
    if (atoi(x) > 0)
    {
        int zerocnt = 0;
        for (size_t i = 0; i < strlen(x); i++)
        {
            int p = strlen(x) - i - 1;
            char a[] = { x[i] }; //atoi之參數須為C式字串
            int q = p / 4;
            int m = p % 4;
            if (a[0] == '0')
            {
                zerocnt++;
            }
            else
            {
                if (zerocnt > 0)
                {
                    strcat_s(out, d[0]); //純C中串接字串之函式
                }
                zerocnt = 0;
                strcat_s(out, d[atoi(a)]);
                strcat_s(out, r[m]);
            }
            if (m == 0 && zerocnt < 4)
            {
                strcat_s(out, b[q]);
            }
        }
    }
    printf("%s", out);
    system("pause");
    return 0;
}