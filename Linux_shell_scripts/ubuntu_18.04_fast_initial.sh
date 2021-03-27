#建議以家目錄以外的目錄執行

if [ -f "/$BASH_SOURCE" ]; then
	echo -e "\nok\n"
else
	sudo mv $BASH_SOURCE /
	echo -e "\n已移動到根目錄\n請從根目錄執行以獲得最佳效果\n"
    exit 0
fi

export LANG=en_us
xdg-user-dirs-gtk-update

#設置個人常用命令別名
echo -e "" >> ~/.bashrc
echo "alias dir=\"ls -alhF\"" >> ~/.bashrc
echo "alias cls=\"clear\"" >> ~/.bashrc
echo "alias apt-init=\"sudo apt update && sudo apt upgrade\"" >> ~/.bashrc
source ~/.bashrc

#裝vim和open-vm-tools
echo -e "\n開始安裝vim和open-vm-tools\n"
sudo apt update && sudo apt upgrade
sudo apt install -y vim

#裝open-vm-tools
echo -e "\n開始安裝open-vm-tools\n"
sudo apt install -y open-vm-tools open-vm-tools-desktop
#sed 插入 => sed -i 'nistring' <檔名>
#其中 nistring 要拆解成 ni + string 來看， ni 的意思就是在第 n 行插入，而 string 就是我們要插入的內容。
sudo sed -i '2iAfter=display-manager.service' /lib/systemd/system/open-vm-tools.service

#裝python3 tkinter和python3 pip
echo -e "\n開始安裝python3 tkinter和python3 pip\n"
sudo apt install -y python3-tk
sudo apt install -y python3-pip

#裝wget和相關套件(如果沒有的話)
echo -e "\n開始安裝wget和相關套件\n"
sudo apt install -y software-properties-common apt-transport-https wget

#裝VScode
echo -e "\n開始安裝VScode\n"
wget -q https://packages.microsoft.com/keys/microsoft.asc -O- | sudo apt-key add -
sudo add-apt-repository "deb [arch=amd64] https://packages.microsoft.com/repos/vscode stable main"
sudo apt update
sudo apt install -y code

#裝chrome
echo -e "\n開始安裝chrome\n"
sudo wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
sudo apt install -y ./google-chrome-stable_current_amd64.deb

#移除chrome安裝檔
echo -e "\n把chrome安裝檔移除\n"
sudo rm -rf ./google-chrome-stable_current_amd64.deb

echo "將於5秒後自動重新開機"
sleep 5
shutdown -r now


