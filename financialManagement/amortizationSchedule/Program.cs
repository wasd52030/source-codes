//本息平均攤還法
async Task equalTotalPayment(Decimal principal, Decimal percent, int year)
{
    // 期數(以月計算)
    int n = year * 12;

    // 每月應付本息金額之平均攤還率
    // 已知年金現值(Present value of annuity，PVOA)=PMT*PVIFA
    // 則PMT=PVOA/PVIFA
    var u = Enumerable.Repeat(0m, n)
                      .Select((_, i) => 1 / Math.Pow((double)(1 + percent * 1 / 100 * 1 / 12), i + 1))
                      .Sum();

    // 每月繳款金額
    var a = principal / Convert.ToDecimal(u);

    using (var file = new StreamWriter("./本息平均攤還法.csv"))
    {
        await file.WriteAsync("期數,期初金額,每期支付額,利息費用,本金償還,期末欠款\n");
        Decimal bSum = 0m, cSum = 0m;

        for (int i = 0; i < n; i++)
        {
            // 每月償還利息
            var b = principal * percent * 1 / 100 * 1 / 12;
            bSum += b;

            // 每月償還本金
            var c = a - b;
            cSum += c;

            // 期末餘額
            var iterFinal = (principal - c) > 0 ? principal - c : 0;

            await file.WriteAsync($"{i + 1},{principal:0},{a:0},{b:0},{c:0},{iterFinal:0}\n");

            principal = iterFinal;
        }

        await file.WriteAsync($"總計,,{Enumerable.Repeat(a, n).Sum():0},{bSum:0},{cSum:0},");
    }
}


await equalTotalPayment(700_0000m, 1.8m, 20);
