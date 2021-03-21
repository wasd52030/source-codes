#!/bin/bash
if [ $(id -u) -eq 0 ]; then
	# as root user
	read -p "前墜名稱: " username
	read -p "數量:" quantity
	current=1
	breat=0
	max=10
	mkdir /etc/vsftpd/vsftpd_user_conf
	echo "Main DIR (/etc/vsftpd/vsftpd_user_conf) has been created."
	while [ $current -le "$quantity" ]; do
		if [ $current -lt $max ]; then
			touch /etc/vsftpd/vsftpd_user_conf/$username$breat$current
			echo "帳戶 $username$breat$current 的file已建立.（位在/etc/vsftpd/vsftpd_user_conf/$username$breat$current/）"
			echo "local_root=/home/$username$breat$current" >>/etc/vsftpd/vsftpd_user_conf/$username$breat$current
			echo "帳戶 $username$breat$current Fin."
			current=$(($current + 1))

		fi
		if [ $current -ge $max ]; then
			touch /etc/vsftpd/vsftpd_user_conf/$username$current
			echo "帳戶 $username$current 的file已建立.（位在/etc/vsftpd/vsftpd_user_conf/$username$current/）"
			echo "local_root=/home/$username$current" >>/etc/vsftpd/vsftpd_user_conf/$username$current
			echo "帳戶 $username$current Fin."
			current=$(($current + 1))

		fi

	done

	[ $? -eq 0 ] && echo "所有使用者之資料夾與權限已建立完畢！！" || echo "失敗"
else
	echo "只有root使用者能夠執行!"
fi
