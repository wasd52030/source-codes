# a040: 阿姆斯壯數

## 1、題
所謂 Armstrong number 指的是一個 n 位數的整數，它的所有位數的 n 次方和恰好等於自己。
例：1634=1^4 + 6^4 + 3^4 + 4^4
請依題目需求在一定範圍內找出該範圍內的所有 armstrong numbers。



| 測資資訊：                                                   |
| ------------------------------------------------------------ |
| 記憶體限制： 512 MB<br/>公開 測資點#0 (14%): 1.0s , <1K<br/>公開 測資點#1 (14%): 1.0s , <1K<br/>公開 測資點#2 (14%): 1.0s , <1K<br/>公開 測資點#3 (14%): 1.0s , <1K<br/>公開 測資點#4 (14%): 1.0s , <1K<br/>公開 測資點#5 (15%): 1.0s , <1K<br/>公開 測資點#6 (15%): 1.0s , <1K |



| 輸入說明                                                     | 輸出說明                                                     |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| 輸入共一行包含兩個數字n, m(n<m, n>0, m<=1000000)，代表所有尋找 armstrong number 的範圍。 | 將所有範圍內的 armstrong number 依序由小到大輸出，如果沒有找到請輸出 none。 |



| 範例輸入 #1 | 範例輸出 #1     |
| ----------- | --------------- |
| 100 999     | 153 370 371 407 |

| 範例輸入 #2 | 範例輸出 #2 |
| ----------- | ----------- |
| 10 99 | none   |

原題：[a040.  阿姆斯壯數 - 高中生程式解題系統 (zerojudge.tw)](https://zerojudge.tw/ShowProblem?problemid=a040)



## 2、解(C++)

遞迴上癮了XD。

這裡就不講廢話了，上code。

因著可以用預設參數，就用c++了~

```c++
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
```

