# 在windows上用vscode寫c++，使用xmake+mingw-w64_clangd

reference $\rightarrow$ https://www.bilibili.com/video/BV1gM4y1Z7Zx

##  安裝設定

1. 裝mingw-w64並設定環境變數
2. 裝xmake，安裝時建議勾選`Add to Path`
3. 裝vscode
4. 裝下面的Extension
   1. C/C++ (微軟官方)
   2. xmake
      1. 到設定把`Xmake: Debug Config Type`調成`codelldb`
   3. clangd 
      1. 這東西會跟微軟官方的C/C++ Extension的intelliSenseEngine衝到，依照提示關掉即可
      2. 如果抓不到的話建議手動設定clangd的地址
   4. codelldb
5. 重開vscode

## 程式撰寫、執行、debug

1. 用vscode開啟任意資料夾
2. Ctrl-Shift-P，執行`xmake:CreateProject`，通常打xmake:Crea...就會出現
3. `target Platform`選`mingw`
4. `toolchain`選`clang`
5. 先按`build`編譯才能執行、debug