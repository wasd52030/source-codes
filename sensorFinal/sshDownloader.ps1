# 專門從樹莓派的開發資料夾中下載程式
# 透過 scp 指令用ssh去下載
# reference
#   - https://stackoverflow.com/questions/9427553/how-to-download-a-file-from-server-using-ssh
#   - https://ithelp.ithome.com.tw/articles/10279550

# 目前是在以前備份過的資料夾使用，所以位置直接寫該資料夾下全部的檔案
$ip = Read-Host -Prompt "樹莓派IP"
scp -r "user@$($ip):~/sensorFinal/*" "./"
pause