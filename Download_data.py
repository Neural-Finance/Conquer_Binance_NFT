import os.path
import time
import numpy as np
import pandas as pd
import requests
import re
import jsons
import datetime



if not os.path.exists("./data/"):
    os.makedirs("./data/")
else:
    filelist = list(os.listdir("./data./"))
    for f in filelist:
        os.remove("./data/"+str(f))


data = pd.read_csv("./URL.csv", index_col=[0])
urllist = list(data['URL'])
for ind,url in enumerate(urllist):
    try:
        tmp = url.split("-")
        number = tmp[-1][:-9]
        new_url = 'https://www.binance.com/bapi/nft/v1/public/nft/collection/chart/trade-floor/%s/0'%str(number)
        response = requests.get(new_url)
        response = response.json()
        data = response['data']

        res = pd.DataFrame()
        res['volume'] = list(data['volume'])
        res['sales'] = list(data['sales'])
        res['floorPrices'] = list(data['floorPrices'])
        start = response['data']['startTime']
        timelist = [datetime.datetime.strftime(datetime.datetime.fromtimestamp(int(start) / 1000) + datetime.timedelta(days=delta), "%Y-%m-%d %H:%M")[:10] for delta in range(len(res))]
        res['time'] = timelist
        res['url'] = [url] + [new_url] + [np.nan]*(len(res)-2)
        res.to_csv("./data/%s.csv"%str(ind))
        print(url)
        time.sleep(np.random.rand(1)*5)
    except:
        print("Sth wrong with: "+str(url))