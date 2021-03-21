#!/bin/bash

if [ $(id -u) -eq 0 ]; then
	echo  "請先將selinux關閉再執行此腳本才有效"
	read -p "題目要求的Port： " port
	
	echo "Port $port" >> /etc/ssh/sshd_config
	echo "IgnoreRhosts yes" >> /etc/ssh/sshd_config
	
	echo -e "">> /etc/ssh/sshd_config
	sed -e 's/PermitRootLogin yes/PermitRootLogin no/' -i /etc/ssh/sshd_config
	systemctl restart sshd
	echo  "已經把連線的Port改成$port"
	echo  "已經禁止root登入"
	echo  "可以用systemctl status sshd 觀察 ssh狀態"
else
	echo "只有root權限之使用者才能執行"
fi
