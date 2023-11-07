# reference
# https://www.dcard.tw/f/nkust/p/253795454
# B11

(lambda li, total: [func for func in [print(f"對應tuple: {li}",f"學生數: {len(names)}", f"總分: {total}", f"平均: {total/len(names)}", sep="\n"),print(f"成績: {dict(li)[input('學生姓名: ')]}")]])(list(zip(names := ["tom", "mary", "joe"], scores := [85, 76, 58])), sum(scores))
