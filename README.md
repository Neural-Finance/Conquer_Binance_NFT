# Conquer_Binance_NFT

### Motivation
I have gone around Opensea, Dappradar, ETH Chain to see their NFT (Non-Fungible Token) price and volume data. Unfortunately, all of them has very strict anti-websrcaper policy. Basically, I tried to pretend myself as a web browser, also trying to fill in the requested payload data, or trying to find some tricks/rules among the url links. None of them worked. Maybe they count on selling data to make money. You can chose to buy data API access from Opensea and DappRadar. 

Or you can choose to use selenium to deal with it, to the best of my knowledge, selenium + advanced knowledge of anti-captcha, can solve any webscrapying problem, but it just very very stupid and not elegent.

Here I give a modern method to deal with **Binance NFT data** (https://www.binance.com/zh-CN/nft/ranking?tab=collection&chain=ETH), if some one, have the need to deal with ETH chain or Opensea, and would like treat me several couple of coffee, I would consider spending more time. 

![Image text](https://github.com/Neural-Finance/Conquer_Binance_NFT/blob/main/fig/Binance-NFT-Page.png)


### Project Structure
```
Step1- Setup Selenium + Geckodriver + Firefox Web Browser
```

```
Step2- Collection_list.py
```

```
Step3- Download_data.py
```

### Step1, Set Up Selenium+Geckodriver+Firefox
You need be very careful with **their version compatibility problem**, you may go to the web page for more details: (https://liushilive.github.io/github_selenium_drivers/md/Firefox.html)

And once, you download the firefox, please definitely go to the setting page, to close the <automatic update> options. It's very important! Otherwise it will update to the latest version.

Among these matched versions, I tried this pair and it worked: 	<Firefox v79.0+ win32> + <python 3.6, selenium 3.141.0> + <Geckodriver 0.29.0>

<Geckodriver 0.29.0>:  https://npm.taobao.org/mirrors/geckodriver/v0.29.0/geckodriver-v0.29.0-win32.zip

<Firefox v79.0+ win32>: https://www.afterdawn.com/software/network/browsers/firefox.cfm/v79_0


### Step2, Generate New URL
We should know the name of all collection, so we need webscrapying this page: https://www.binance.com/zh-CN/nft/ranking?tab=collection&chain=ETH

However, it's very hard to scrapy, the requested data is secretly encoded. Common ways really can not solve it, thus we need use step 1 to scarpy it and get the **special number** for each collection url.

![Image text](https://github.com/Neural-Finance/Conquer_Binance_NFT/blob/main/fig/Special-number1.png)

![Image text](https://github.com/Neural-Finance/Conquer_Binance_NFT/blob/main/fig/Special-number2.png)


### Step3, Download Data

As we can see below, in order to request the table data of price and volume, we need this **special number**, slightly observe it and generate the new url! 

![Image text](https://github.com/Neural-Finance/Conquer_Binance_NFT/blob/main/fig/Special-number3.png)

**Finally, you can get the total trading volume, ground price, number of transactions in each day, for each collection.** Let's stop here together, think about what may drive the price, **give me comments and let's go deeper together.**

![Image text](https://github.com/Neural-Finance/Conquer_Binance_NFT/blob/main/fig/Saved-data.png)


**Update to 2023-07-08**, the data can be download from (https://pan.baidu.com/s/1WodnvaZPtsB2IC7t77N0LA?pwd=4zws). But I really suggest you go over this process, after all, the selenium can guarantee to solve the worst cases in web scrapying, and producing new data day by data is meaningful!
