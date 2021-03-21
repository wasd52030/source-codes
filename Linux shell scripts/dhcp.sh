
#!/bin/bash

if [ $(id -u) -eq 0 ]; then
	echo  "請先用ifconfig指令查網卡資訊"
	echo  "請先將selinux關閉再執行此腳本才有效"
	read -p "網卡名稱：" netcard
	read -p "起始IP：" startip
	read -p "終止IP：" endip
	read -p "子網路遮罩：" submask
	read -p "時限：" time
	read -p "預設閘道：" getway
	read -p "DNS伺服器：" dns
	
	echo -e "">> /etc/dnsmasq.conf
	echo "port=0" >> /etc/dnsmasq.conf
	echo "interface=$netcard" >> /etc/dnsmasq.conf
	echo "dhcp-range=$startip,$endip,$submask,$time " >> /etc/dnsmasq.conf
	echo "dhcp-option=3,$getway" >> /etc/dnsmasq.conf
	echo "dhcp-option=6,$dns" >> /etc/dnsmasq.conf

	dnsmasq --test
	systemctl enable dnsmasq
	systemctl start dnsmasq
	firewall-cmd --add-service=dhcp --permanent
	firewall-cmd  --reload
	firewall-cmd  --list-services
	echo  "可以用systemctl status dnsmasq 觀察 dhcp狀態"
else
	echo "只有root權限之使用者才能執行"
fi

	
