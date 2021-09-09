# golang_sortlib_example

golang中有一個lib叫sort，實作了4種排序演算法：Insertion Sort、Merge Sort、Heap sort和Quick Sort。只要實作sort.Interface的三個方法：求數據集合長度的 Len() 方法、比較元素大小的 Less() 方法和交換元素位置的 Swap() 方法，就可以順利進行排序，至於使用的演算法會從上述4個中挑一個對當前狀況最優的來使用。

這裡拿[a915. 二维点排序 - 高中生程式解題系統 (zerojudge.tw)](https://zerojudge.tw/ShowProblem?problemid=a915)來當例子，code請移置main.go查看喔 ~

