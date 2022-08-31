from lib2to3.pgen2 import driver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
import time
from selenium import webdriver
import chromedriver_binary
import pandas as pd
import re
import os

content = input()

if '市' in content:
  m = re.search('市', content)
  m1 =m.end()
  content = content[:m1]+' '+content[m1:]

if '区' in content:
  n = re.search('区', content)
  n1 = n.end()
  content = content[:n1]+' '+content[n1:]

if '町' in content:
  v = re.search('町', content)
  v1 = v.end()
  content = content[:v1]+' '+content[v1:]

if '丁目' in content:
  b = re.search('丁目', content)
  b1 = b.end()
  content = content[:b1]+' '+content[b1:]
  b = re.search('丁目', content)
  b2 = b.start() -1 
  content = content[:b2]+' '+content[b2:]

if 'r"\d+"' in content:
  z = re.search('r"\d+"', content)
  z1 = z.start()-1
  content = content[:z1]+' '+content[z1:]

list2 = re.findall(r'\d+', content)
l = re.search(list2[0], content)
l1= l.start()-1
content = content[:l1]+' '+content[l1:]

list =content.split()
print(list)




if list[0] == '千葉県千葉市':
  if len(list)<5:
    s1 = list[1]
    s2 = list[2]
    s3 = '丁目なし'
    s4 = list[3]
  else:
    s1 = list[1]
    s2 = list[2]
    s3 = list[3]
    s4 = list[4]
  

  driver = webdriver.Chrome()
  driver.get("http://s-page.tumsy.com/chibagesui/index.html")
  time.sleep(5)

  # 同意する
  iframe = driver.find_element(By.XPATH,"/html/frameset/frame")
  driver.switch_to.frame(iframe)
  time.sleep(5)

  driver.execute_script("window.scrollBy(0, document.body.scrollHeight);")

  actionChains = ActionChains(driver)
  
  actionChains.click(driver.find_element(By.XPATH,"//*[@id='LinkButton1']")).perform()
  # driver.switch_to.default_content()
  time.sleep(5)
  
  d1 = driver.find_element(By.XPATH,"//*[@id='ELM_CMB_LEV1']")
  select = Select(d1)
  select.select_by_visible_text(s1)
  time.sleep(5)
  d2 = driver.find_element(By.XPATH,"//*[@id='ELM_CMB_LEV2']")
  select = Select(d2)
  select.select_by_visible_text(s2)
  time.sleep(5)
  d3 = driver.find_element(By.XPATH,"//*[@id='ELM_CMB_LEV3']")
  select = Select(d3)
  select.select_by_visible_text(s3)
  time.sleep(5)
  d4 = driver.find_element(By.XPATH,"//*[@id='ELM_CMB_LEV4']")
  select = Select(d4)
  time.sleep(5)
  select.select_by_visible_text(s4)
  time.sleep(5)

  actionChains.click(driver.find_element(By.XPATH,"//*[@id='btnAddSchDlgOK']")).perform()
  time.sleep(5)
  FILENAME = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'image/B-1.png')
  driver.save_screenshot(FILENAME)
  driver.quit()

else:
  print("千葉県千葉市ではない") 
