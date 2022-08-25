import requests
import time
from bs4 import BeautifulSoup
import json

while True:
    prefix = str('[INFO] [' + str(time.ctime()) + '] ')

    url = 'https://www.ntvs.ntpc.edu.tw/p/403-1000-54-1.php'

    #headers = {'user-agent':'Mozilla/5.0 (Windows NT 10.0;Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)Chrome/65.0.3325.181 Safari/537.36 '}
    headers = {'user-agent':'Give RSS/1.0 https://thisisch.net/2.0 https://discord.com/invite/PWtPeRAFJ2/3.0'}

    resp = requests.get(url, headers=headers)
    # 轉成 BeautifulSoup 物件
    soup = BeautifulSoup(resp.text, "html.parser")

    #getting latest news
    latest_news_name = soup.select(f'div.mtitle')[0].text.strip()
    latest_news_link = soup.select('div.mtitle a[href]')
    latest_news_link = latest_news_link[0]['href']

    print ('done initiating')#cuz pterodactyl need
    print (prefix + '\n==========')
    print ('Debug info:\n' + latest_news_name + "\n" + latest_news_link)
    print ('==========')
    #latest_news_name = 'a'

    while True:
        prefix = str('[INFO] [' + str(time.ctime()) + '] ')
        time.sleep(1)
        resp2 = requests.get(url, headers=headers)
        soup2 = BeautifulSoup(resp2.text, "html.parser")

        #finding latest news
        latest_news_name_temp = soup2.select(f'div.mtitle')[0].text.strip()
        latest_news_link = soup2.select('div.mtitle a[href]')
        
        if latest_news_name == latest_news_name_temp:
            print ('==========')
            print (prefix + "結果相同，無須動作\n" + '目前標題為: '+ latest_news_name)
            print ('==========')
        else:
            print(prefix + '結果不同，將發送通知: ')
            #最新消息名字
            latest_news_name = latest_news_name_temp

            print(prefix + '取得連結中...')
            #最新消息連結
            latest_news_link = soup2.select('div.mtitle a[href]')
            latest_news_link = latest_news_link[0]['href']

            print(prefix + '列印結果:\n')
            print(latest_news_name)
            print('\n============================================\n')
            print(latest_news_link)
            #傳送webhook
            print(prefix + '傳送WebHook到Discord伺服器...')
            webhookurl = '#########################################[url here]#########################################'
            data = {'content':'<@&1012036005974507522>\n__最新消息出現:__\n\n> ' + latest_news_name + '\n__連結: [點我](' + latest_news_link + ')__'}
            r = requests.post(webhookurl, data=json.dumps(data), headers={'Content-Type': 'application/json'})
            print(data)
            print(prefix + '傳送完成!Loop重來...\n')
            print('\n============================================\n')