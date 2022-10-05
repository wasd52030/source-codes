# Windows Chocolate設定預設App安裝路徑

Chocolate，一種在Windows上面近似於Debian系的apt的套件管理工具，簡單來說就是可以用指令一次安裝很多軟體這樣，請參考：https://ithelp.ithome.com.tw/articles/10242201

不過它預設的路徑是在C槽下面，如果想要切到其他位置的話需要設一個環境變數，名稱叫做`ChocolateyInstall`，變數內容填你想要設的安裝路徑，好比說`D:\ProgramData\Chocolatey`，如下圖

![](https://i.imgur.com/Day5vUf.png)

