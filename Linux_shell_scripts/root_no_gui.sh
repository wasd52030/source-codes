#!/bin/bash

if [ $(id -u) -eq 0 ]; then
	echo "auth  required  pam_succeed_if.so  user  !=  root  quiet" >> /etc/pam.d/gdm-password
	echo "執行完畢"
else
	echo "只有root權限之使用者才能執行"
fi

	
