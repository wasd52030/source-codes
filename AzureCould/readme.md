# AzureCould

拿來放Azure修課相關的東西這樣

- 課後作業

  - 20220922 $\rightarrow$ 在azure上開一個vm並架上wordpress
  - 20220929 $\rightarrow$ Remote to azure vm by ssh with Vscode
  - 20221006 $\rightarrow$ 用老師的帳號開一台有顯卡的vm並打上驅動，使`nvidia-smi`正確顯示資訊
  - 20221013 $\rightarrow$ 在azure上開一台vm並架上jupyter server
  - 20221020 $\rightarrow$ 第一次期中作業：在azure上開一台vm並架上Stable_Diffusion
  - 20221103 $\rightarrow$ 把課堂上的Custom Vision訓練完成的模型下載下來，丟到netron上，並試著推導實現方式
  - 20221110 $\rightarrow$ 把老師提供的`testsenti.py`、`testcomputervision.py`、`testcv.py`程式正常執行
  - 20221117 $\rightarrow$ 使文字轉語音、語音辨識的程式正常執行
  - 20221124 $\rightarrow$ 在azML studio的compute架上Stable_Diffusion
  - 20221201 $\rightarrow$ 用azure ML designer做一個模型並部屬成api
  - 20221208 $\rightarrow$第二次期中作業：運用課堂所學到的azure ai相關技巧實作一個小專題

- 常用指令

	- `ssh -i <<location of ssh key file>> <<Remoteuser>>@<<RemoteLocation>>`

- 參考資訊

	- SSH Key Windows Permission denied: https://leesonhsu.blogspot.com/2021/03/ssh-key-windows-permission-denied.html
	
	- Vsocde remote-ssh: https://hackmd.io/@brick9450/vscode-remote
	
	- Save as Root in Vscode Remote - SSH: https://github.com/yy0931/save-as-root
	
	- docker install: https://blog.gtwang.org/virtualization/ubuntu-linux-install-docker-tutorial/
	
	- deployment wordpress by docker: https://qiita.com/vc7/items/e88026c75f2280f95ed4
	
	- azure blob  storage mount to linux:  https://learn.microsoft.com/zh-tw/azure/storage/blobs/storage-how-to-mount-container-linux
	
	- azure-cli: https://blog.miniasp.com/post/2022/07/04/How-to-create-VM-using-Azure-CLI
	
	- ubuntu-drivers: http://samwhelp.github.io/book-ubuntu-qna/read/case/driver/install-driver-package/ubuntu-drivers
	
	- stable diffusion cpkt file: https://huggingface.co/CompVis/stable-diffusion-v-1-4-original
	
	- download file from huggingface hub by python
	
	  ```python
	  from huggingface_hub import hf_hub_download
	  
	  # take https://huggingface.co/CompVis/stable-diffusion-v-1-4-original for example
	  # CompVis/stable-diffusion-v-1-4-original is repo_id
	  # hf_hub_download return the path of download file
	  path=hf_hub_download(repo_id="CompVis/stable-diffusion-v-1-4-original", filename="file-in-repository",use_auth_token="usertoken-in-read-access")
	  print(path)
	  ```
	  
	- Azure Developer Document: https://learn.microsoft.com/zh-tw/azure/developer/
	  
	- change anaconda default python version: https://stackoverflow.com/questions/28436769/how-to-change-default-anaconda-python-environment

