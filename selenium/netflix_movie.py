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
driver.get("https://www.netflix.com/browse/genre/34399")

titles = driver.find_elements_by_class_name('nm-collections-title-name')
movie =[]
for title in titles :
    page_1 = title.text
    movie.append(page_1)

tag = []
tags = driver.find_elements_by_class_name("nm-collections-row-name")
for genre in tags :
    list = genre.text
    tag.append(list)

netflix = pd.DataFrame(movie,columns=['Title'])
netflix.index = netflix.index + 1

driver.close()

conn = sqlite3.connect(DB_FILENAME)
cur = conn.cursor()

cur.execute("DROP TABLE IF EXISTS Netflix;")
netflix.to_sql('Netflix',conn)
conn.commit()
