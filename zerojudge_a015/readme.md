# a015: 矩陣的翻轉

## 1、題目
請寫一程式來實現轉置矩陣。

定義如下：[轉置矩陣 - 維基百科，自由的百科全書](https://zh.wikipedia.org/wiki/%E8%BD%AC%E7%BD%AE%E7%9F%A9%E9%98%B5)



| 測資資訊：                                               |
| -------------------------------------------------------- |
| 記憶體限制： 512 MB<br/>公開 測資點#0 (100%): 1.0s , <1K |



| 輸入說明                                                     | 輸出說明             |
| ------------------------------------------------------------ | -------------------- |
| 第一行會有兩個數字，分別為 列(row)<100 和 行(column)<100，緊接著就是這個矩陣的內容 | 直接輸出翻轉後的矩陣 |



| 範例輸入 #1                 | 範例輸出 #1            |
| --------------------------- | ---------------------- |
| 2 3 <br />3 1 2 <br />8 5 4 | 3 8<br />1 5 <br />2 4 |

**提示 ：測資檔會包含多組矩陣資料**

原題：[a015. 矩陣的翻轉 - 高中生程式解題系統 (zerojudge.tw)](https://zerojudge.tw/ShowProblem?problemid=a015)

## 2、解(JAVA)

題目的提示「測資檔會包含多組矩陣資料」隱晦的要求「輸入有若干矩陣並轉置直到 EOF 結束」！

這裡用Scanner中的 hasNext 函式來做到類似C的 while(scanf("%d %d",&a, &b)!=EOF)。

這裡就不講廢話了，上code。

```java
import java.util.*;

public class main {

    public static void main(String[] args) {
        Scanner s = new Scanner(System.in);
        int row, column;
        while (s.hasNext()) {
            row = s.nextInt();
            column = s.nextInt();
            int[][] A = new int[row][column];
            for (int i = 0; i < row; i++) {
                for (int j = 0; j < column; j++) {
                    A[i][j] = s.nextInt();
                }
            }

            for (int i = 0; i < column; i++) {
                for (int j = 0; j < row; j++) {
                    System.out.printf("%d ", A[j][i]);
                }
                System.out.println();
            }
        }
        s.close();
    }
}
```



