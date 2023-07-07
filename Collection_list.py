import time
import pandas as pd
import requests
import re
import jsons
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options


urllist = []
driver = webdriver.Firefox()
driver.get("https://www.binance.com/zh-CN/nft/ranking?tab=collection&chain=ETH")
time.sleep(11)


for page in range(5):
    while True:
        try:
            html = driver.page_source
            soup = BeautifulSoup(html, 'html.parser')
            class_ = soup.find_all('div', class_='css-1ezltp')
            for row in class_:
                text = row.findAll('a', class_='css-1xxn6ao')[0]
                pattern = r'href="([^"]*)"'
                match = re.findall(pattern, str(text))[0]
                url = 'https://www.binance.com' + match
                urllist.append(url)
            break
        except:
            pass

    next_button = driver.find_element_by_id('next-page')
    next_button.click()
    time.sleep(11)



driver.quit()
res = pd.DataFrame()
res['URL'] = urllist
res.to_csv("./URL.csv")