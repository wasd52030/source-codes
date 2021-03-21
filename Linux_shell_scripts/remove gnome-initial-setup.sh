#!/bin/bash
#red hat系適用

if [ $(id -u) -eq 0 ]; then
	yum erase gnome-initial-setup
else
	echo "只有root權限之使用者才能執行"
fi
