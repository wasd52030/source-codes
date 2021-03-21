#!/bin/bash
if [ $(id -u) -eq 0 ]; then
	# as root user
	read -p "前綴名稱: " username
	read -p "數量:" quantity
	current=1
	breat=0
	max=10
	while [ $current -le "$quantity" ]; do
		if [ $current -lt $max ]; then
			mkdir /home/$username$breat$current/FTP_user
			echo "帳戶 $username$breat$current 的資料夾已建立.（位在/home/$username$breat$current/FTP_user）"
			chown $username$breat$current /home/$username$breat$current/FTP_user
			chmod 700 /home/$username$breat$current/FTP_user
			echo "帳戶 $username$breat$current 的權限已設定完成.（位在/home/$username$breat$current/FTP_user）"
			current=$(($current + 1))

		fi
		if [ $current -ge $max ]; then
			mkdir /home/$username$current/FTP_user
			echo "帳戶 $username$current 的資料夾已建立.（位在/home/$username$current/FTP_user）"
			chown $username$current /home/$username$current/FTP_user
			chmod 700 /home/$username$current/FTP_user
			echo "帳戶 $username$current 的權限已設定完成.（位在/home/$username$current/FTP_user）"
			current=$(($current + 1))

		fi
	done

	[ $? -eq 0 ] && echo "所有使用者之資料夾與權限已建立完畢！！" || echo "失敗"
else
	echo "只有root使用者能夠執行!"
fi
