# a054: 電話客服中心

## 1、題
試使用輸入之九位數字推算其可能的身分證字母。

很多人都知道，身分證號碼的最後一碼是「檢查碼」，它是用前 9 碼所推算出來的，其推算的規則如下：

1. 先依照下表將英文字母轉換為 2 位數字，再加上第 2 到第 9 位的 8 位數字一共有 10 位數字。

    <table border="1">
        <tbody>
            <tr>
                <td>
                    <p align="center">A (10)</p>
                </td>
                <td>
                    <p align="center">台北市</p>
                </td>
                <td>
                    <p align="center">G&nbsp;(16)</p>
                </td>
                <td>
                    <p align="center">宜蘭縣</p>
                </td>
                <td>
                    <p align="center">M (21)</p>
                </td>
                <td>
                    <p align="center">南投縣</p>
                </td>
                <td>
                    <p align="center">S (26)</p>
                </td>
                <td>
                    <p align="center">高雄縣</p>
                </td>
                <td>
                    <p align="center">Y (31)</p>
                </td>
                <td>
                    <p align="center">陽明山</p>
                </td>
            </tr>
            <tr>
                <td>
                    <p align="center">B (11)</p>
                </td>
                <td>
                    <p align="center">台中市</p>
                </td>
                <td>
                    <p align="center">H (17)</p>
                </td>
                <td>
                    <p align="center">桃園縣</p>
                </td>
                <td>
                    <p align="center">N (22)</p>
                </td>
                <td>
                    <p align="center">彰化縣</p>
                </td>
                <td>
                    <p align="center">T (27)</p>
                </td>
                <td>
                    <p align="center">屏東縣</p>
                </td>
                <td>
                    <p align="center">Z (33)</p>
                </td>
                <td>
                    <p align="center">連江縣</p>
                </td>
            </tr>
            <tr>
                <td>
                    <p align="center">C (12)</p>
                </td>
                <td>
                    <p align="center">基隆市</p>
                </td>
                <td>
                    <p align="center">I (34)</p>
                </td>
                <td>
                    <p align="center">嘉義市</p>
                </td>
                <td>
                    <p align="center">O (35)</p>
                </td>
                <td>
                    <p align="center">新竹市</p>
                </td>
                <td>
                    <p align="center">U (28)</p>
                </td>
                <td>
                    <p align="center">花蓮縣</p>
                </td>
                <td>
                    <p align="center">&nbsp;</p>
                </td>
                <td>
                    <p align="center">&nbsp;</p>
                </td>
            </tr>
            <tr>
                <td>
                    <p align="center">D&nbsp;(13)</p>
                </td>
                <td>
                    <p align="center">台南市</p>
                </td>
                <td>
                    <p align="center">J (18)</p>
                </td>
                <td>
                    <p align="center">新竹縣</p>
                </td>
                <td>
                    <p align="center">P (23)</p>
                </td>
                <td>
                    <p align="center">雲林縣</p>
                </td>
                <td>
                    <p align="center">V (29)</p>
                </td>
                <td>
                    <p align="center">台東縣</p>
                </td>
                <td>
                    <p align="center">&nbsp;</p>
                </td>
                <td>
                    <p align="center">&nbsp;</p>
                </td>
            </tr>
            <tr>
                <td>
                    <p align="center">E&nbsp;&nbsp;(14)</p>
                </td>
                <td>
                    <p align="center">高雄市</p>
                </td>
                <td>
                    <p align="center">K (19)</p>
                </td>
                <td>
                    <p align="center">苗栗縣</p>
                </td>
                <td>
                    <p align="center">Q (24)</p>
                </td>
                <td>
                    <p align="center">嘉義縣</p>
                </td>
                <td>
                    <p align="center">W (32)</p>
                </td>
                <td>
                    <p align="center">金門縣</p>
                </td>
                <td>
                    <p align="center">&nbsp;</p>
                </td>
                <td>
                    <p align="center">&nbsp;</p>
                </td>
            </tr>
            <tr>
                <td>
                    <p align="center">F&nbsp;&nbsp;(15)</p>
                </td>
                <td>
                    <p align="center">台北縣</p>
                </td>
                <td>
                    <p align="center">L (20)</p>
                </td>
                <td>
                    <p align="center">台中縣</p>
                </td>
                <td>
                    <p align="center">R (25)</p>
                </td>
                <td>
                    <p align="center">台南縣</p>
                </td>
                <td>
                    <p align="center">X (30)</p>
                </td>
                <td>
                    <p align="center">澎湖縣</p>
                </td>
                <td>
                    <p align="center">&nbsp;</p>
                </td>
                <td>&nbsp;</td>
            </tr>
        </tbody>
    </table>


2. 由左至右，第一位乘 1，第二位乘 9，第三位乘 8，第四位乘 7...，以此類推，最後一位乘 1。

3. 求各位相對數字乘積的總和 s。

4. 求 s 的個位數 m。(檢查碼只有一位數，因此若 c = 10 時，則檢查碼為 0。)

5. 檢查碼 c = 10 - m 。

假設某人的身份證號碼前 9 碼為 F13024567，那麼他的最後一位檢查碼的計算過程如下：

&nbsp;&nbsp;   F      1  3  0  2  4  5  6  7
  1   5   1  3  0  2  4  5  6  7

*1   9   8  7  6  5  4  3  2  1  <- 加權值

  1 + 45 +  8 + 21 +  0 + 10 + 16 + 15 + 12 +  7 = 135

檢查碼 = 10 - (135 % 10) = 5

根據上面的規則，A12345678、M12345678 和 W12345678 這三個號碼的檢查碼都是 9。因此，如果在電話上所輸入的後 9 碼是 123456789 時，它的第一位英文字母可能是 A，也可能是 M 或 W。


| 輸入說明                                    | 輸出說明                                     |
| ------------------------------------------- | -------------------------------------------- |
| 輸入只有一行，含有一個身份證號碼的後 9 碼。 | 將可能的第一位大寫字母依字母順序輸出於一行。 |

| 範例輸入 #1 | 範例輸出 #1 |
| ----------- | ----------- |
| 130245675   | FS          |

| 範例輸入 #2 | 範例輸出 #2 |
| ----------- | ----------- |
| 123456789 | AMW |

| 測資資訊：                                                   |
| ------------------------------------------------------------ |
| 記憶體限制： 512 MB<br/>公開 測資點#0 (5%): 1.0s , <1K<br/>公開 測資點#1 (5%): 1.0s , <1K<br/>公開 測資點#2 (5%): 1.0s , <1K<br/>公開 測資點#3 (5%): 1.0s , <1K<br/>公開 測資點#4 (5%): 1.0s , <1K<br/>公開 測資點#5 (5%): 1.0s , <1K<br/>公開 測資點#6 (5%): 1.0s , <1K<br/>公開 測資點#7 (5%): 1.0s , <1K<br/>公開 測資點#8 (5%): 1.0s , <1K<br/>公開 測資點#9 (5%): 1.0s , <1K<br/>公開 測資點#10 (5%): 1.0s , <1K<br/>公開 測資點#11 (5%): 1.0s , <1K<br/>公開 測資點#12 (5%): 1.0s , <1K<br/>公開 測資點#13 (5%): 1.0s , <1K<br/>公開 測資點#14 (5%): 1.0s , <1K<br/>公開 測資點#15 (5%): 1.0s , <1K<br/>公開 測資點#16 (5%): 1.0s , <1K<br/>公開 測資點#17 (5%): 1.0s , <1K<br/>公開 測資點#18 (5%): 1.0s , <1K<br/>公開 測資點#19 (5%): 1.0s , <1K |

原題：[a054.  電話客服中心 - 高中生程式解題系統 (zerojudge.tw)](https://zerojudge.tw/ShowProblem?problemid=a054)



## 2、解(C++)

這裡就不講廢話了，上code。

```c++
#include <stdio.h>

int main()
{
	int k = 0;
	//ROC ID ENG->NUM
	int enn[] = {10, 11, 12, 13, 14, 15, 16, 17, 34, 18, 19, 20, 21, 22, 35, 23, 24, 25, 26, 27, 28, 29, 32, 30, 31, 33};
	int lenofenn = sizeof(enn) / sizeof(enn[0]);

	while (scanf("%d", &k) != EOF)
	{
		int cnt = 0, chk = k % 10, q[30]={0}, i = 1; //i=1 -> 最後一位(去掉檢查碼)之加權值

		//將輸入的數字去掉最後一位(檢查碼)
		k /= 10;

		//取得剩下的八位數字(逆序)乘上對應之加權之總和
		while (k > 0)
		{
			cnt += (k % 10) * i;
			i++;
			k /= 10;
		}

		//窮舉所有英文字母
		for (int i = 0; i < lenofenn; i++)
		{
			//加上英文轉數字和其對應之加權
			q[i] += (enn[i] / 10) + (enn[i] % 10 * 9) + cnt;

			//求檢查碼
			int x = 10 - (q[i] % 10);
			x = x == 10 ? 0 : x;

			//如果求得的數字與輸入的最後一位相符，則輸出index對應的字母
			if (x == chk)
				printf("%c",(char)(65 + i));
		}
		printf("\n");
	}
	return 0;
}
```

