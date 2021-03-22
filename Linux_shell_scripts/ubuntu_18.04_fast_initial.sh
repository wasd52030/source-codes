#建議以家目錄以外的目錄執行

#把非英文的家目錄資料夾更名成英文的
export LANG=en_us
xdg-user-dirs-gtk-update

#設置個人常用命令別名
echo -e "" >> ~/.bashrc
echo "alias dir=\"ls -alhF\"" >> ~/.bashrc
echo "alias cls=\"clear\"" >> ~/.bashrc
echo "alias apt-init=\"sudo apt update && sudo apt upgrade\"" >> ~/.bashrc
source ~/.bashrc

#裝vim和open-vm-tools
sudo apt update && sudo apt upgrade
sudo apt install -y open-vm-tools
sudo apt install -y vim

#裝python3 tkinter和python3 pip
sudo apt install -y python3-tk
sudo apt install -y python3-pip

#裝wget和相關套件(如果沒有的話)
sudo apt install -y software-properties-common apt-transport-https wget

#裝VScode
wget -q https://packages.microsoft.com/keys/microsoft.asc -O- | sudo apt-key add -
sudo add-apt-repository "deb [arch=amd64] https://packages.microsoft.com/repos/vscode stable main"
sudo apt update
sudo apt install -y code

#裝chrome
sudo wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
sudo apt install -y ./google-chrome-stable_current_amd64.deb

#移除firefox
sudo apt -y remove firefox

#移除chrome安裝檔
sudo rm -rf ./google-chrome-stable_current_amd64.deb




