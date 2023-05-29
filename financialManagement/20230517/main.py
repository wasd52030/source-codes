from typing import List
import pandas


def discountedPaybackPeriod(
    initial_investment: float, cash_flows: List[float], discount_rate: float
):
    t = [
        [0, initial_investment, 1, initial_investment, initial_investment],
    ]

    for i, cash_flow in enumerate(cash_flows):
        p = 1 / (1 + discount_rate) ** (i + 1)
        cp = round(cash_flow * p, 0)
        fp = abs(cp - t[i][-1])
        t.append(
            [i + 1, cash_flow, float(f"{p:.4f}"), cp, fp],
        )

    t.append([None] * 5)
    t.append(["折現回收期間", len(cash_flows) - 1 + t[-3][-1] / t[-2][-2]])

    table = pandas.DataFrame(
        t,
        columns=[
            "年度",
            "每年現金流入量",
            f"折現因子(折現率={int(discount_rate*100)}%)",
            "現金流量折現值",
            "累積現金流量折現值",
        ],
    )

    with pandas.ExcelWriter("./result.xlsx") as writer:
        table.to_excel(writer, sheet_name="折現回收期間法", index=False)

    print("折現期間回收法的excel表已輸出！")


def modifiedInternalRateOfReturn(
    initial_investment: float, cash_flows: List[float], discount_rate: float
):
    # 期數
    n = len(cash_flows)

    sCIF = sum(
        [
            cash * ((1 + discount_rate) ** (n - index - 1))
            for index, cash in enumerate(cash_flows)
        ]
    )

    MIRR = (sCIF / initial_investment) ** (1 / n) - 1
    MIRR = round(MIRR, 4)

    print(f"MIRR:{MIRR}")


def main():
    n = int(input("請輸入期數: "))

    # 輸入現金流
    cash_flows = [float(input(f"請輸入第{i+1}期金額: ")) for i in range(n)]

    # 折現率
    discount_rate = float(input("請輸入折現率: "))

    # 初始投資
    initial_investment = int(input("請輸入初始投資額: "))

    discountedPaybackPeriod(initial_investment, cash_flows, discount_rate)
    print()
    modifiedInternalRateOfReturn(initial_investment, cash_flows, discount_rate)


if __name__ == "__main__":
    main()
