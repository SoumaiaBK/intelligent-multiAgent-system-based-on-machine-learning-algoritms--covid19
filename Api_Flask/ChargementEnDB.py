
import pandas as pd
from pymongo import MongoClient

#Connexion avec la base de donnée MongoDB
cluster = MongoClient("mongodb://localhost:27017/?readPreference=primary&appname=MongoDB%20Compass%20Community&ssl=false") 
db = cluster["db_covid19"]
collection_NewsScrapped= db["NewsScrapped"]      


def ChargementEnDB():
    news_df=pd.read_csv("NewsScrapped.csv")  
    myData = news_df.to_dict('records')
    collection_NewsScrapped.delete_many({})
    collection_NewsScrapped.insert_many(myData)


