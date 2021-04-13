#!/bin/bash

if [ $(id -u) -eq 0 ]; then
	read -p  "需要root權限嗎？(1為需要,0為不需要)：" rootyn
	read -p "前綴名稱： " username
	read -p "密碼："   password
	read -p "群組名稱：" group
	read -p "起始編號：" nstart
	read -p "跳幾號："   nsetp
	read -p "結束編號：" nend
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
	
	groupadd $group
	echo "群組 $group 成功建立"

	pass=$(perl -e 'print crypt($ARGV[0], "password")' $password)
	current=$nstart
	breat=0
	max=10

	while [ $current -le "$nend" ]
	do
		grep -E "^$username$current" /etc/passwd > /dev/null

		if [ $? -eq 0 ]; then
			echo "帳戶$username$current已經存在"
			continue
		fi
		
		if [ $current -lt $max ]; then
		
			if [ $rootyn -eq 1 ]; then
				useradd -m -s $login -p $pass -g $group -o -u 0 $username$breat$current
			else
				useradd -m -s $login -p $pass -g $group $username$breat$current
			fi
			
			echo "帳戶$username$breat$current成功建立"
			current=$((current+nsetp))
		fi

		if [ $current -ge $max ]; then
		
			if [ $rootyn -eq 1 ]; then
				useradd -m -s $login -p $pass -g $group -o -u 0 $username$current
			else
				useradd -m -s $login -p $pass -g $group $username$current
			fi
			
            echo "帳戶$username$current成功建立"
            current=$((current+nsetp))
        fi
		
	done
else
	echo "只有root權限之使用者才能執行"
fi

	
