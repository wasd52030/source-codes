#!/bin/bash

if [ $(id -u) -eq 0 ]; then

    read -p  "需要root權限嗎？(1為需要,0為不需要)：" rootyn
	read -p "帳戶名稱： " username
	read -p "密碼："   password
	read -p "群組名稱：" group
	echo "下列爲可用的shell,請選擇"
	echo -e ""
	cat /etc/shells
	echo -e ""
    read -p "帳戶殼層（Shell）: " login
	grep -E "^$group" /etc/group > /dev/null

	#if [ $? -ne 0 ]; then
 	#	groupadd $group
	#	echo "群組 $group 成功建立"
	#fi
	
	#建立群組
	groupadd $group
	echo "群組 $group 成功建立"

	pass=$(perl -e 'print crypt($ARGV[0], "password")' $password)
	
	#判斷是否需要給root權限
	if [ $rootyn -eq 1 ]; then
        useradd -m -s $login -p $pass -g $group -o -u 0 $username
    else
        useradd -m -s $login -p $pass -g $group $username
    fi
    
	echo "使用者 $username 成功建立"
	
else
	echo "只有root權限之使用者才能執行"
fi

	
