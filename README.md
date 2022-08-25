# ntvswebbot
一個python script 去請求學校新公告頁面，然後使用webhook傳到discord頻道上
## 安裝
    python 3.10
    git clone https://github.com/HaeImCH/ntvswebbot.git
    cd ntvswebbot
    pip install -r requirements.txt
    python3 school_news.py

### 我其實沒有想過會是爬蟲
我原本的想法是利用RSS訂閱去查公告標題跟連結

但我發現我們校網居然沒有?

所以我就向我們學校的資訊組長請教是否沒有RSS訂閱

![shot on 2022/8/25 11:07:25](https://media.discordapp.net/attachments/685883249297326120/1012377008287793233/unknown.png)

過了大概兩天還是沒有

所以我就自己去找校網用的系統(Rpage)

發現官方教育訓練的pdf文檔有提及設定RSS的相關模組

![shot on 2022/8/25 11:11:21](https://cdn.discordapp.com/attachments/685883249297326120/1012378538722201600/unknown.png)

所以我又再次去~~煩~~請教學校的資訊組長

![shot on 2022/8/25 11:12:56](https://cdn.discordapp.com/attachments/685883249297326120/1012378985956651059/unknown.png)

還是一樣不理我

以上大概就是完整故事了

謝謝學校的資訊組長又讓我多認識了一點python uwu
