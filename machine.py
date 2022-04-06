import pandas as pd
import numpy as np
import sqlite3
import os

#csv 파일 불러오기
movie = pd.read_csv('movie.csv')
rating =pd.read_csv('rating.csv')
tag = pd.read_csv('tag.csv')
genome_tags = pd.read_csv('genome_tags.csv')
genome_scores = pd.read_csv('genome_scores.csv')

#Data Wrangling
genome_scores['rank']=genome_scores.groupby('movieId')['relevance'].rank(method='min',ascending=False)
condition = genome_scores['rank']==1
n_score = genome_scores[condition]

tags = pd.merge(n_score,genome_tags,on='tagId',how='inner')
tags = tags.sort_values(by=['movieId'], axis=0)
tags = tags.drop(['relevance','rank'],axis=1)
tags.rename(columns={'tag':'key'},inplace=True)

new_tag=pd.merge(tags,tag,on='movieId',how='inner')
new_tag = new_tag.drop(['userId','timestamp'],axis=1)

movie_details=movie.merge(rating,on='movieId')
movie_details.drop(columns=['timestamp'],inplace=True)

number_rating = movie_details.groupby('title')['rating'].count().reset_index()
number_rating.rename(columns={'rating':'number of rating'},inplace=True)
df=movie_details.merge(number_rating,on='title')

df=df[df['number of rating']>=50]
df.drop_duplicates(['title','userId'],inplace=True)
df.drop(columns=['number of rating'],inplace=True)
df['rating']=df['rating'].astype(int)

avg_rate = df.groupby('movieId')['rating'].mean().reset_index()
avg_rate['mean_rating']=avg_rate['rating'].round(1)
avg_rate = avg_rate.drop(columns=['rating'])
mean =movie_details.merge(avg_rate,on='movieId')
mean['recommend'] = mean['mean_rating'] >= 3.5
#Genres 컬럼 |값을 ,로 변환후 3가지의 장르만 남기고 drop
def comma(string):
    return string.replace('|',',')
mean['genres'] = mean['genres'].apply(comma)
main_genre_list = mean.genres.str.split(',')
mean['main_genre'] = main_genre_list.str.get(0)
mean['second_genre'] = main_genre_list.str.get(1)
mean['third_genre'] = main_genre_list.str.get(2)
mean['genre']=mean['main_genre']+','+mean['second_genre']+','+mean['third_genre']
mean =mean.drop(columns=['movieId','genres','userId','main_genre','second_genre','third_genre'])
# DB_FILENAME = 'Rating.db'
# DB_FILEPATH = os.path.join(os.getcwd(), DB_FILENAME)

# conn = sqlite3.connect(DB_FILENAME)
# cur = conn.cursor()

# cur.execute("DROP TABLE IF EXISTS movie_rating;")
# data.to_sql('movie_rating',conn)
# conn.commit()