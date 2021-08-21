# d732: 二分搜尋法

## 1、題
給你一個嚴格遞增的數列A1,A2,A3.....An(1<=n<=100000), 

&下面有幾個問題的詢問數k(1<=K<=100000),

以及k個詢問的整數x,求數列中是否存在一個Ai(1<=i<=n)的值與X相等?



| 測資資訊：                                                   |
| ------------------------------------------------------------ |
| 記憶體限制： 512 MB<br/>公開 測資點#0 (20%): 1.0s , <1M<br/>公開 測資點#1 (20%): 1.0s , <1M<br/>公開 測資點#2 (20%): 1.0s , <1M<br/>公開 測資點#3 (20%): 1.0s , <1M<br/>公開 測資點#4 (20%): 1.0s , <10M |



| 輸入說明                                                     | 輸出說明                                                     |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| 第一行包含兩個整數n,k分別表示數列長度以及詢問數<br />第二行包含n個整數第i(1<=i<=n)個整數依序為數列中Ai的值<br />第三行包含k個詢問的整數x. | 對於每個詢問整數x對應一行輸出: <br />輸出i的值 <br />其中1<=i<=n且Ai=x <br />若沒有這樣的i值請輸出0代替. |



| 範例輸入 #1                         | 範例輸出 #1                    |
| ----------------------------------- | ------------------------------ |
| 5 5 <br />1 3 4 7 9<br />3 1 9 7 -2 | 2<br />1<br />5 <br />4<br />0 |

**提示 ：**

**標籤:**

[搜尋](https://zerojudge.tw/Problems?tag=搜尋)

原題：[d732: 二分搜尋法 - 高中生程式解題系統 (zerojudge.tw)](https://zerojudge.tw/ShowProblem?problemid=d732)

## 2、解(C++)

這一題主要用到二分搜尋這個演算法。
需要注意的是，題目定義給出的數列首位為1、不是0。
這裡就不講廢話了，上code。

```c++
#include <iostream>

int search(int *arr, int key, int left, int right)
{
    int m = left + (right - left) / 2;

    if (left > right)
        return 0;

    if (arr[m] < key)
        return search(arr, key, m + 1, right);

    if (arr[m] > key)
        return search(arr, key, left, m - 1);

    if (arr[m] == key)
        return m + 1;
}

int main(int argc, char const *argv[])
{
    int n, k;
    while (scanf("%d %d", &n, &k) != EOF)
    {
        int data[110000];
        int key[110000];
        for (int i = 0; i < n; i++)
        {
            scanf("%d", &data[i]);
        }

        for (int i = 0; i < k; i++)
        {
            scanf("%d", &key[i]);
        }

        for (int i = 0; i < k; i++)
        {
            printf("%d\n", search(data, key[i], 0, n));
        }
    }
    return 0;
}
```



