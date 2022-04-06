import csv
import pandas as pd
import sqlite3
import os

DB_FILENAME = 'OTT.db'
DB_FILEPATH = os.path.join(os.getcwd(), DB_FILENAME)

with open('disney_plus_titles.csv', 'r',encoding='UTF8') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    datas = [x for x in reader]

column=datas.pop(0)
disney = pd.DataFrame(datas,columns=column)

conn = sqlite3.connect(DB_FILENAME)
cur = conn.cursor()

disney.to_sql('disney',conn)
conn.commit()
