from typing import List
import pandas


def discountedPaybackPeriod(
    initialInvestment: float, cashFlows: List[float], discountRate: float
):
    t = [
        [0, initialInvestment, 1, initialInvestment, initialInvestment],
    ]

    for i, cash_flow in enumerate(cashFlows):
        p = 1 / (1 + discountRate) ** (i + 1)
        cp = round(cash_flow * p, 0)
        fp = abs(cp - t[i][-1])
        t.append(
            [i + 1, cash_flow, float(f"{p:.4f}"), cp, fp],
        )

    t.append([None] * 5)
    t.append(["折現回收期間", len(cashFlows) - 1 + t[-3][-1] / t[-2][-2]])

    table = pandas.DataFrame(
        t,
        columns=[
            "年度",
            "每年現金流入量",
            f"折現因子(折現率={int(discountRate*100)}%)",
            "現金流量折現值",
            "累積現金流量折現值",
        ],
    )

    with pandas.ExcelWriter("./result.xlsx") as writer:
        table.to_excel(writer, sheet_name="折現回收期間法", index=False)

    print("折現期間回收法的excel表已輸出！")


def modifiedInternalRateOfReturn(
    initial_investment: float, cash_flows: List[float], capitalRate: float
):
    # 期數
    n = len(cash_flows)

    sCIF = sum(
        [
            cash * ((1 + capitalRate) ** (n - index - 1))
            for index, cash in enumerate(cash_flows)
        ]
    )

    MIRR = (sCIF / initial_investment) ** (1 / n) - 1
    MIRR = round(MIRR, 4)

    print(f"MIRR:{MIRR}")


def main():
    n = int(input("請輸入期數: "))

    # 輸入現金流
    cashFlows = [float(input(f"請輸入第{i+1}期金額: ")) for i in range(n)]

    # 折現率
    discountRate = float(input("請輸入折現率: "))

    # 資金成本率
    capitalRate = float(input("請輸入資金成本率: "))

    # 初始投資
    initialInvestment = int(input("請輸入初始投資額: "))

    discountedPaybackPeriod(initialInvestment, cashFlows, discountRate)
    print()
    modifiedInternalRateOfReturn(initialInvestment, cashFlows, capitalRate)


if __name__ == "__main__":
    main()
