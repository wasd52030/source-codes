#!/bin/bash

echo  "請在要改成英文資料夾的使用者下執行"
echo  "在彈出的窗口中詢問是否将目錄轉化爲英文路徑,同意並關閉"

export LANG=en_US
xdg-user-dirs-gtk-update

