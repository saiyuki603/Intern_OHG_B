import time

from selenium import webdriver
import chromedriver_binary
from selenium.webdriver.common.by import By

import requests
from bs4 import BeautifulSoup
import time


URL = 'http://www.geocoding.jp/api/'

#def Saitama_gesui(address):
#    driver = webdriver.Chrome()
#
#    driver.get("https://www.geocoding.jp/api/?q=" + address)
#    time.sleep(3)
#    driver.find_element(By.XPATH, '//*[@id="folder1"]/div[2]/div[1]/span[2]')
#    
#    driver.find_element(By.XPATH, '//*[@id="folder1"]/div[2]/div[2]/span[2]')

    #print(latitude)
    #print(longitude)

def coordinate(address):
    """
    addressに住所を指定すると緯度経度を返す。

    >>> coordinate('東京都文京区本郷7-3-1')
    ['35.712056', '139.762775']
    """
    payload = {'q': address}
    xml = requests.get(URL, params=payload)
    soup = BeautifulSoup(xml.content, "xml")
    if soup.find('error'):
        raise ValueError(f"Invalid address submitted. {address}")
    latitude = soup.find('lat').string
    longitude = soup.find('lng').string

    """
    埼玉の下水を検索・スクショ
    """
    gesui_url = 'https://www.sonicweb-asp.jp/saitama_g/map?theme=th_90#scale=500&pos=' + latitude + longitude

x = coordinate('東京都八王子市七国5-4-23')
print(x)