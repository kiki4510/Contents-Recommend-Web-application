from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import os
import sqlite3
import pandas as pd

DB_FILENAME = 'OTT.db'
DB_FILEPATH = os.path.join(os.getcwd(), DB_FILENAME)

driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.get("https://www.tving.com/vod/genre?multiCategoryCode=PCAN")
SCROLL_PAUSE_SEC = 3
# 스크롤 높이 가져옴
last_height = driver.execute_script("return document.body.scrollHeight")

while True:
    # 끝까지 스크롤 다운
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # 3초 대기
    time.sleep(SCROLL_PAUSE_SEC)

    # 스크롤 다운 후 스크롤 높이 다시 가져옴
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height

elem =driver.find_elements_by_class_name("program-item__info-title ")
drama = []
for element in elem :
    list = element.text
    drama.append(list)

driver.close()

tving = pd.DataFrame(drama,columns=['Title'])
tving.index = tving.index + 1

conn = sqlite3.connect(DB_FILENAME)
cur = conn.cursor()

cur.execute("DROP TABLE IF EXISTS Tving_animation ;")
tving.to_sql('Tving_animation',conn)
conn.commit()
