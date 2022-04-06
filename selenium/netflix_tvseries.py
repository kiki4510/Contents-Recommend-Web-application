from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import os
import sqlite3
import pandas as pd

DB_FILENAME = 'OTT.db'
DB_FILEPATH = os.path.join(os.getcwd(), DB_FILENAME)

driver = webdriver.Chrome()
driver.get("https://www.netflix.com/browse/genre/83")

elem = driver.find_elements_by_class_name("nm-collections-title-name")
tvseries = []
for element in elem :
    list = element.text
    tvseries.append(list)

driver.close()

netflix = pd.DataFrame(tvseries,columns=['Title'])
netflix.index = netflix.index + 1

conn = sqlite3.connect(DB_FILENAME)
cur = conn.cursor()

netflix.to_sql('Netflix_series',conn)
conn.commit()
