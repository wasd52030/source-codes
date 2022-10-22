# HW03 Apriori Algorithms
<div style="text-align:right; font-size:20px;">C109152304 許智程</div>
<br>

下表為某商店的五筆交易紀錄，試回答下列問題。

<span style="color: red;">設最小支持度(min_support)=2，也就是出現次數以下時，不列入選擇
</span>

| 交易紀錄 | 商品項目-代碼        |
|------|-----------------|
| 601  | 麵包-A、果醬-B、花生醬-C |
| 602  | 麵包-A、花生醬-C      |
| 603  | 麵包-A、花生醬-C、牛奶-D |
| 604  | 麵包-A、啤酒-E       |
| 605  | 牛奶-D、啤酒-E       |

1. 利用Apriori演算法求所有2-項目集的可能規則
<div style="display:flex;">
    <div>
        <table>
            <tr>
                <td>itemset</td>
                <td>sup</td>
            </tr>
            <tr>
                <td>A</td>
                <td>4</td>
            </tr>
            <tr style="color: red;">
                <td>B</td>
                <td>1</td>
            </tr>
            <tr>
                <td>C</td>
                <td>3</td>
            </tr>
            <tr>
                <td>D</td>
                <td>2</td>
            </tr>
            <tr>
                <td>E</td>
                <td>2</td>
            </tr>
        </table>
    </div>
    <div style="display: flex; justify-content: center; align-items: center; margin: 0 30px;">
        ->
    </div>
    <div>
        <table>
            <tr>
                <td>itemset</td>
                <td>sup</td>
            </tr>
            <tr>
                <td>{A,C}</td>
                <td>3</td>
            </tr>
            <tr style="color: red;">
                <td>{A,D}</td>
                <td>1</td>
            </tr>
            <tr style="color: red;">
                <td>{A,E}</td>
                <td>1</td>
            </tr>
            <tr style="color: red;">
                <td>{C,D}</td>
                <td>1</td>
            </tr>
            <tr style="color: red;">
                <td>{C,E}</td>
                <td>0</td>
            </tr>
            <tr style="color: red;">
                <td>{D,E}</td>
                <td>1</td>
            </tr>
        </table>
    </div>
    <div style="display: flex; justify-content: center; align-items: center; margin: 0 30px;">
        ->
    </div>
    <div style="display: flex; justify-content: center; align-items: center;">
        <table>
            <tr>
                <td>itemset</td>
                <td>sup</td>
            </tr>
            <tr>
                <td>{A,C}</td>
                <td>3</td>
            </tr>
        </table>
    </div>
</div>

$$
\therefore \ 所有2-項目集的可能規則為 \ \{A,C\}
$$
2. 試求所有2-項目極可能規則的支持度(Confidence)與信賴度(Support)
<div style="display:flex;">
   <div>
      <table>
         <tr>
            <td>itemset</td>
            <td>sup</td>
         </tr>
         <tr>
            <td>{A,C}</td>
            <td>3</td>
         </tr>
      </table>
   </div>
</div>

支持度(Confidence)與信賴度(Support)的算法如下
$$
\left\{\begin{matrix} 
  Support\{X=>Y\}=P(X\cap Y) \\  
  Confidence\{X=>Y\}=P(Y|X)=\frac{P(X\cap Y)}{P(X)} 
\end{matrix}\right. 
$$
套用上面的式子，得到
$$
\left\{\begin{matrix} 
  Support\{A=>C\}=P(A\cap C)=\frac{3}{5} \\  
  Confidence\{A=>C\}=P(C|A)=\frac{P(A\cap C)}{P(A)}=\frac{\frac{3}{5}}{\frac{4}{5}}=\frac{15}{20}=\frac{3}{4}
\end{matrix}\right. 
$$
3. 令支持度門檻為20%，信賴度門檻為20%，試求被列入候選項目集的規則
$$20\%=\frac{20}{100}=0.2$$
$$
\because\{A,C\}\left\{\begin{matrix} 
  \frac{3}{5}=\frac{6}{10}>\frac{2}{10}   \\  
  \frac{3}{4}=\frac{15}{20}>\frac{2}{10}=\frac{4}{20} 
\end{matrix}\right. 
$$
$$
\therefore \ 被選入的是 \ \{A,C\}
$$
4. 利用Apriori演算法求所有3-項目集的可能規則，求算其支持度(Confidence)與信賴度(Support)，最後列出被選入候選項目集的規則
<div style="display: flex;">
    <div style="display: flex; justify-content: center; align-items: center;">
        <table>
            <tr>
                <td>itemset</td>
                <td>sup</td>
            </tr>
            <tr>
                <td>{A,C}</td>
                <td>3</td>
            </tr>
        </table>
    </div>
    <div style="display: flex; justify-content: center; align-items: center; margin: 0 30px;">
        ->
    </div>
    <div>
        <table>
            <tr>
                <td>itemset</td>
                <td>sup</td>
            </tr>
            <tr style="color: red;">
                <td>{A,C,D}</td>
                <td>1</td>
            </tr>
            <tr style="color: red;">
                <td>{A,C,E}</td>
                <td>0</td>
            </tr>
        </table>
    </div>
</div>

$$
\therefore \ 沒有任何規則被選入候選項目
$$

