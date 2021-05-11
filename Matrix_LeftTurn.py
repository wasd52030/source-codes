#矩陣左旋

#map(func,iterable) -> 對可迭代物件iterable中的每一個元素做參數去執行函數func
#func(*x) -> 可把傳入的參數打包成一個tuple傳進函數func中
#func(*iterable) -> 把可迭代物件iterable中的每一個元素分別傳入函數func中
#zip(iterable) 將可迭代物件iterable作為參數，將物件中對應的元素打包成多個tuple，然后返回由這些tuple组成的物件
#可以用list(zip(iterable))將zip傳回的物件轉成list
#例: list(zip([[1,2,3],[4,5,6],[7,8,9]])) =>會得到[(1,4,7),(2,5,8),(3,6,9)]

def f(x):
    return list(map(list,zip(*x)))[::-1]

print(f([[1,2,3],[4,5,6],[7,8,9]]))