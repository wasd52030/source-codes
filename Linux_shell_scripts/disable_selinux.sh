#!/bin/bash

if [ $(id -u) -eq 0 ]; then
	sed -e 's/enforcing/disabled/' -i /etc/selinux/config
	echo "執行完畢"
	echo "5秒後重新開機以完成變更"
	sleep 5s  #延遲5秒後執行下面的指令
	reboot
else
	echo "只有root權限之使用者才能執行"
fi

	
