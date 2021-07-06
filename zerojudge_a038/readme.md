# a038: 數字翻轉

## 1、題
輸入任意數字，並將其數字全部倒轉



| 測資資訊：                                               |
| -------------------------------------------------------- |
| 記憶體限制： 512 MB<br/>公開 測資點#0 (100%): 1.0s , <1K |



| 輸入說明                                | 輸出說明           |
| --------------------------------------- | ------------------ |
| 輸入一行包含一個整數，且不超過 2^31 | 輸出翻轉過後的數字 |



| 範例輸入 #1 | 範例輸出 #1 |
| ----------- | ----------- |
| 12345       | 54321       |

| 範例輸入 #2 | 範例輸出 #2 |
| ----------- | ----------- |
| 5050      | 505       |

**提示 ：前面有 0 的話應消除**

原題：[a038. 數字翻轉 - 高中生程式解題系統 (zerojudge.tw)](https://zerojudge.tw/ShowProblem?problemid=a038)



## 2、解(C++)

一般來說這題用迴圈就可以解了，不過順便練習遞迴也是不錯。

這裡就不講廢話了，上code。

因著可以用預設參數，就用c++了XD ~

```c++
//遞迴解
#include <stdio.h>

int solution(int in, int r = 0)
{
    if (in == 0) return r;
    r = (r * 10) + (in % 10);
    solution(in / 10, r);
}

int main(int argc, char const *argv[])
{
    int x = 0;
    while (scanf("%d", &x) != EOF)
    {
        printf("%d\n", solution(x));
    }
    return 0;
}
```



```c++
//迴圈解
#include <stdio.h>

int main(int argc, char const *argv[])
{
    int a=0;
    while (scanf("%d", &a) != EOF)
    {
        int r = 0;
        while (a > 0)
        {
            r = (r * 10) + (a % 10);
            a /= 10;
        }
        printf("%d\n", r);
    }
    return 0;
}
```

