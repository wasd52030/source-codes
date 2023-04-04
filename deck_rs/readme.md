# pokeDeck_rs

如題，是關於撲克牌組的程式

目前只有實作抽牌而已


會寫這東西是學弟發了`DeckOfCards.java`這玩意給我，說是書上的範例，問說怎麼跑不動，我就問他說啊你的`Card`class勒？他就曉得怎麼辦了，可系可賀。那時也正好閒著沒事幹，用kotlin寫了一個類似的東西`deck_kt.kt`，而這玩意就是其rust的實現

一直以來都有聽聞`tauri`這玩意，一個類似`electron`的玩意，都是用網頁技術做Desktop程式的框架，差別在於`electron`的畫面跟系統介接層也是javascript，而`tauri`的畫面跟系統介接層是用`rust`這門語言來寫的；且相對於`electron`的執行檔是直接包一個`chromium`進去，`tauri`的執行檔是呼叫系統的WebView的，因此`tauri`的執行檔大小相較於`electron`小許多

可以說是為了`tauri`才學`rust`這門語言的XDDD，寫起來跟其他程式語言基本差別不會太多，該有的feature都齊備，應該就剩它獨有的`所有權`與`借用`這兩個機制需要花多心力去理解

