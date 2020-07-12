# from pymongo import MongoClient
# import pandas as pd
# import numpy as np
# from flair.models import TextClassifier
# from flair.data import Sentence 
# import logging

# logging.basicConfig(level=logging.ERROR)


# #Connexion avec la base de donnée MongoDB
# cluster = MongoClient("mongodb://localhost:27017/?readPreference=primary&appname=MongoDB%20Compass%20Community&ssl=false") 
# db = cluster["db_covid19"]
# collection_NewsScrapped= db["NewsScrapped"]

# flair_sentiment = TextClassifier.load('en-sentiment')

# # Analyser les sentiments des nouvelles
# def analyseSentiments():
#     myNews=collection_NewsScrapped.find()
#     df =  pd.DataFrame(myNews)
#     del df['_id']
#     df['Result'] = np.array([analyze_sentiment(Titre)['value'] for Titre in df['Titre']])
#     df['confidence'] = np.array([analyze_sentiment(Titre)['confidence'] for Titre in df['Titre']])
#     collection_NewsScrapped.delete_many({})
#     myData = df.to_dict('records')
#     collection_NewsScrapped.insert_many(myData)

# # Analyser le sentiment d'une nouvelle
# def analyze_sentiment(Titre):
#     s = Sentence(Titre)
#     flair_sentiment.predict(s)
#     total_sentiment = s.labels[0].to_dict()
#     return total_sentiment

