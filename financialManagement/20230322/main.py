from decimal import Decimal
import decimal
import pandas
import numpy


# 本息平均攤還法
def equalTotalPayment(principal: float, percent: float, year: int):
    principal, percent = Decimal(str(principal)), Decimal(str(percent))

    # 期數(以月計算)
    n = year * 12

    # 每月應付本息金額之平均攤還率
    # 已知年金現值(Present value of annuity，PVOA)=PMT*PVIFA
    # 則PMT=PVOA/PVIFA
    u = sum([1 / ((1 + percent * 1 / 100 * 1 / 12) ** (i + 1)) for i in range(n)])

    # 每月繳款金額
    a = principal / u

    tableBegin, tableEnd = [], []
    tableA, tableB, tableC = [a for _ in range(n)], [], []

    for _ in range(n):
        # 每月償還利息
        b = Decimal(str(principal * ((percent * 1 / 100) * 1 / 12))).quantize(0, decimal.ROUND_HALF_UP)
        tableB.append(b)
        # 每月償還本金
        c = a - b
        tableC.append(c)
        # 期末餘額
        iterFinal = principal - c
        tableEnd.append(iterFinal)

        tableBegin.append(principal)
        principal = iterFinal

    table = pandas.DataFrame(
        {
            "期數": [*range(1, n + 1)],
            "期初金額": tableBegin,
            "每期支付額": tableA,
            "利息費用": tableB,
            "本金償還": tableC,
            "期末欠款": tableEnd,
        }
    )
    table.loc[len(table)] = [
        "總計",
        numpy.nan,
        *[table[col].sum() for col in table.columns.values[2:-1]],
        0,
    ]
    for col in table.columns.values:
        table[col] = table[col].apply(
            lambda x: int(x.quantize(0, decimal.ROUND_HALF_UP))
            if isinstance(x, Decimal)
            else x
        )

    with pandas.ExcelWriter("./result.xlsx") as writer:
        table.to_excel(writer, sheet_name="本息平均攤還法", index=False)


equalTotalPayment(7000000, 1.8, 20)
