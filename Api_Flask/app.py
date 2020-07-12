import pandas as pd
from flask import abort, Flask, jsonify, request, json
# from flair.models import TextClassifier
# from flair.data import Sentence
from pymongo import MongoClient
from bson.json_util import dumps
import requests
from bs4 import BeautifulSoup
from flask_cors import CORS
from scraping_data_1 import scraping_data_1
from scraping_data_2 import scraping_data_2
from Scarping_nouvelles import Scarping_nouvelles
from ChargementEnDB import ChargementEnDB
from preprocessing import preprocessing_data
# from analyseSentiments import analyseSentiments
from clustering import clustering
from prediction import predict

app = Flask(__name__ )
CORS(app)

#Connexion avec la base de donnée MongoDB
cluster = MongoClient("mongodb://localhost:27017/?readPreference=primary&appname=MongoDB%20Compass%20Community&ssl=false") 
db = cluster["db_covid19"]
collection_NewsScrapped = db['NewsScrapped'] 

# classifier = TextClassifier.load('en-sentiment')
 
@app.route('/')
def index():
    return "Hello world !"

# DataVisualisation :
# Visualisation 1 : /Maroc + nbre des cas+décès+guéris --------------------------------------------------------------------------------------- 
@app.route('/getGraphe1', methods = ["GET"])
def graphe_maroc():
    if request.method == "GET": 
        df=pd.read_excel('C:/Users/soumaya/DataSets/covid19/scrap_morocco.xlsx')
        df2 = df.fillna(0)
        df3 = df2.to_numpy()
        regions = [l[0] for l in df3]
        Confirmed = [l[1] for l in df3]
        Deaths = [l[2] for l in df3]
        Recovered = [l[3] for l in df3]
        return jsonify(regions = regions, Confirmed= Confirmed,Deaths=Deaths,Recovered=Recovered)

# Visualisation 2 : /date + nbre des cas+décès---------------------------------------------------------------------------------------
@app.route('/getGraphe2', methods = ["GET"])
def graphe_selon_Date():
    if request.method == "GET": 
        collection_Scraping_data1 = db["Scraping_data1"]      
        df =collection_Scraping_data1.find({})
        jours = list()
        cas = list()
        deces= list()
        for res in df :
           jours.append(res["les jours"])
           cas.append(res["les cas confirmes"])
           deces.append(res["Deces"])
        return jsonify(jours = jours, cas =cas ,deces = deces)

# Visualisation 3 : /pays ---------------------------------------------------------------------------------------
@app.route('/getGraphe3', methods = ["GET"])
def graphe_selon_pays():
    if request.method == "GET": 
        collection_Scraping_data2 = db["Scraping_data2"]      
        df =collection_Scraping_data2.find({})
        pays = list()
        cas = list()
        deces= list()
        for res in df :
           pays.append(res["country"])
           cas.append(res["total_cases"])
           deces.append(res["total_deaths"])
        return jsonify(pays = pays, cas =cas ,deces = deces)

# Scrapping Data 1  : Maroc / Jours + Nbre des cas + Nbre de décès
@app.route('/scraping_data1', methods = ["GET"])
def scraping_data1():
    scraping_data_1()   
    return jsonify("data1 scrappés et chargés dans la BD !!") , 200

# Scrapping Data 2  : Pays / Nbre des cas + Nbre de décès
@app.route('/scraping_data2', methods = ["GET"])
def scraping_data2():
    scraping_data_2()   
    return jsonify("data2 scrappés et chargés dans la BD !!") , 200

# Scapping les nouvelles
@app.route('/scrapping_news', methods=['GET']) 
def ScrappingNews():
    numOfPages = request.args['numOfPages'] 
    Scarping_nouvelles(numOfPages)
    return jsonify("Les nouvelles scrappées !!") , 200

# Preprocessing
@app.route('/preprocessing', methods=['GET'])
def preprocessing():
    preprocessing_data()
    return jsonify("Les nouvelles traitées !!") , 200

# Charger les données dans MongoDB
@app.route('/ChargementEnDB', methods=['GET'])
def loadToDB():
    ChargementEnDB()
    return jsonify("Les nouvelles chargées dans la BD !!") , 200

# Analyser les sentiments des nouvelles
# @app.route('/analyseSent', methods=['GET'])
# def startAnalysis():
#     analyseSentiments()
#     return jsonify("Les nouvelles analysées !!") , 200

# Analyser le sentiment d'une nouvelle
# @app.route('/analyserUnSent', methods=['POST'])
# def analyzeSentiment():
#     message = request.args['text']
#     sentence = Sentence(message)
#     classifier.predict(sentence)
#     print('Sentence sentiment: ', sentence.labels)
#     label = sentence.labels[0]
#     labscore = (label.score)*100
#     response = {'result': label.value, 'confidence':"%.2f" % labscore}
#     return jsonify(response), 200

# Get les nouvelles : en spécifiant le nombre et p/n
@app.route('/getNews', methods=['GET'])
def getNews():
    number = request.args['number']
    sentiment = request.args['sentiment']
    if sentiment=="n":
        res = collection_NewsScrapped.find({ "Result": "NEGATIVE"} , {"Titre": 1,"Result": 1, "_id": 0}).limit(int(number))
    elif sentiment=="p":
        res = collection_NewsScrapped.find({ "Result": "POSITIVE" } , {"Titre": 1,"Result": 1, "_id": 0}).limit(int(number))
    else:
        res = collection_NewsScrapped.find({}, {"Titre": 1,"Result": 1, "_id": 0}).limit(int(number))
    list_res = list(res)
    return jsonify(list_res) , 200

# Get les statistiques sur l'analyse des sentiments
@app.route('/statAnalysis', methods=['GET'])
def getSentimentStatistics():
    all_news = collection_NewsScrapped.count_documents({})
    neg = 100*collection_NewsScrapped.count_documents({ "Result": "NEGATIVE"})/all_news
    pos = 100*collection_NewsScrapped.count_documents({ "Result": "POSITIVE" })/all_news
    resp = {'all': all_news, 'positives':pos, 'negatives':neg}
    return jsonify(resp) , 200

# Clustering
@app.route('/clustering', methods = ["GET"])
def getClusters():
    return clustering()

# Prediction
@app.route('/prediction', methods = ["GET"])
def prediction():
    return predict()


if __name__ == "__main__":
    app.debug = True  
    app.run()