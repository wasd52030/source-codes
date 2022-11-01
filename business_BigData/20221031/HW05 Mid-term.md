# HW05 Mid-term
<div style="text-align:right; font-size:20px;">C109152304 許智程</div>
<br>

請利用資料集 OnLine_Sale.xlsx 進行以下資料預處理及分析:
1. 新增3個欄位，建立每筆資料的銷售成本 (單位成本 x 銷售數量)、 銷售收入 (單位售價 x 銷售數量) 及 收益 (銷售收入 - 銷售成本)。
- 注：結果以csv檔輸出，採UTF-8編碼，直接用excel開啟會導致亂碼，於是採用excel導入csv檔的方式呈現
![image-20221101214357559](.\online_sales.png)


2. 分析商品種類的分佈、特徵、及資料變異等視覺化分析。
![image-20221101214357559](.\plots\hist_commodity-type.png)


3. 針對 "單位售價" 與 "收益 " 此兩個欄位，執行下列任意兩種正規化的方法:  RobustScaler()、StandardScaler()、MinMaxScaler()、 MaxAbsScaler()、Normalizer()。
   1. 單位售價
      -  RobustScaler
![image-20221101214357559](.\plots\unitPrice_Normalization-RobustScaler.png)

      - StandardScaler
![image-20221101214357559](.\plots\unitPrice_Normalization-StandardScaler.png)
   2. 收益
      - MinMaxScaler
![image-20221101214357559](.\plots\revenue_Normalization-MinMaxScaler.png)

      - MaxAbsScaler
![image-20221101214357559](.\plots\revenue_Normalization-MaxAbsScaler.png)

4. 針對 a ~ d，任選任何一種圖形化呈現 (例如:  圓餅圖、長條圖) 
   
   <ol type='a'>
           <li>男性與女性 銷售總額的比率為何?</li>
           <li>哪一個國家的男性總銷售金額最高 ?</li>
           <li>法國男性與女性銷售總額的比率為何?</li>
           <li>哪一個國家的總銷售金額最高 ?</li>
    </ol>
   
5. 根據顧客是否會回購，建立一個預測分類器 (例: Decision Tree Classifier, Logistic Regression, 或Random Forest Classifier)及其預測的結果(評估)。

