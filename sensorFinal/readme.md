# envMonitor

這玩意是感測器與物聯網實作的期末報告，大致功能就是檢測亮度與聲音，超出
臨界值會觸發警報

關於臨界值檢測的部分，老師發的感測模組上有數位輸出，超過設定的臨界值會輸出1，反之輸出0，實在很方便，如果要顯示實際的數字的話由於樹莓派這玩意沒法讀類比資料，還要再另外過一層IC？亦或是直接過一層Arduino之類的東西再從Serial讀值？

時隔幾年的重操舊業，偶爾玩玩也是不賴的na ~ 畢竟能上現在的學校有幾乎一半是靠操作單晶片啊XDDDD(轉生到現在的系所又是另外一個故事了XD)，而且用的是python而不是c/c++，難度又降低了許多XDDDDD

在找資料的途中，發現樹莓派操作GPIO的資源有幾乎99%是python，感覺真的有點誇張，c/c++臭了嗎？

不得不提，樹莓派的GPIO編碼方式真的蠻複雜的，且板子上連一種都沒標？？？？各家使用的編碼規則也不一樣，亂七八糟...

- 電路圖 $\rightarrow$ [https://oshwlab.com/wasd52030/sensorfinal](https://oshwlab.com/wasd52030/sensorfinal)

## feature
- 壓電式麥克風: 測出聲音的強度大小
- 光敏電阻: 觀測室內亮度
- 蜂鳴器: 聲音過吵+亮度過低發出警報聲
- LED: 當聲音過吵|亮度太暗時亮起
- LCD螢幕: 顯示聲音和亮度的警報訊息(e.g. 請小聲|請開燈)

## dev log
- 20230318
	- 確立光敏電阻模組、RGB LED與樹莓派的連接與操作
- 20230319
	- 整理光敏電阻模組、RGB LED的code
	- 確立蜂鳴器、聲音感測模組與樹莓派的連接與操作
	- 目前從聲音感測模組讀的是數位訊號，類比待研究
	- 老師給的聲音感測模組要比較靠近、聲音比較大才感應的到
	- bug
		- 當利用蜂鳴器發聲時，會導致其他東西的運作變慢
		- 猜想是蜂鳴器要發出聲音需輸出一段方波，且目前知道的`time.sleep`會阻塞目前程式
- 20230323
	- 確立ili9341 SPI LCD螢幕與樹莓派的連接與操作
		- 利用PIL建立Image,再將Image的數據寫到螢幕上
		- adafruit的ili9341 library強綁定他們額外為樹莓派開發的CircuitPython library，經測試採用BCM腳位編碼
- 20230326
	- 參考adafruit的ili9341 library與網路資料，整理ili9341 SPI LCD螢幕的code
	- 加入讓螢幕顯示中文的能力
	- 利用multithreading讓各個任務互不干擾

## refrernce
- 光敏電阻模組 $\rightarrow$ https://shop.cpu.com.tw/product/46957/info/
- 聲音感測模組 $\rightarrow$ https://blog.jmaker.com.tw/arduino-sound/
- ili9341 spi LCD螢幕 $\rightarrow$ https://blog.csdn.net/chenqide163/article/details/125580594
- adafruit ili9341 spi LCD螢幕 library $\rightarrow$ https://learn.adafruit.com/adafruit-2-8-and-3-2-color-tft-touchscreen-breakout-v2/python-usage