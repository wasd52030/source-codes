# ytPlayListLangStats

一個用來統計Youtube播放清單中由什麼語言組成的小工具

目前可以
- 自動收集影片中聲軌的語言，抓的是`youtube data api v3`的影片`snippet`中的`defaultAudioLanguage`屬性
- 由於上述收集的資料有些影片沒有，如果該影片找不到此屬性，會先打上`ukunown`，需要在收集資料完畢後手動標註
- 依據資料進行統計，顯示於Console中
- 收集資料與統計資料由`main` function的`isDownloading`變數進行切換
  - True: 收集資料
  - False: 統計資料


**請將`Appsettings.json`中的YoutubeAPIKey填上自己的Youtube Data Api Key，並將檔名改成`appsettings.json`**