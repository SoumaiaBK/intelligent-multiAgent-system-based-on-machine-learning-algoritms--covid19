from bs4 import BeautifulSoup
import requests
from flask import abort, Flask, jsonify, request
from pymongo import MongoClient
import pandas as pd
from flask import abort, Flask, jsonify, request, json

#Connexion avec la base de donnée MongoDB
cluster = MongoClient("mongodb://localhost:27017/?readPreference=primary&appname=MongoDB%20Compass%20Community&ssl=false") 
db = cluster["db_covid19"]

def scraping_data_1():
    collection_Scraping_data1 = db["Scraping_data1"]
    page = requests.get('https://www.worldometers.info/coronavirus/')
    soup = BeautifulSoup(page.text, 'html.parser')
    #scrapping the days
    soup_days=soup.find_all(attrs={"class": "tabbable-panel-cases"})[0].find_next_sibling()
    ss=str(soup_days)
    ss[293+13:1736].split(',')
    list_days=ss[293+13:1736].split(',')
    #scrapping daily deaths cases in the world wide
    soup_deaths=soup.find_all(attrs={"class": "tabbable-panel-deaths"})[0].find_next_sibling()
    soup_deaths_string=str(soup_deaths)
    soup_deaths_string[9426+7:10140].split(',')
    list_deaths=soup_deaths_string[9426+7:10140].split(',')
    #scrapping daily active cases in the world wide
    soup_cases=soup.find_all(attrs={"class": "tabbable-panel-cases"})[0].find_next_sibling()
    soup_cases_string=str(soup_cases)
    soup_cases_string[9818+7:10755].split(',')
    list_cases=soup_cases_string[9818+7:10755].split(',')
    # Chargement dans la bdd MongoDN
    df=pd.DataFrame(data={'Days':list_days, 'Cases': list_cases,'Deaths': list_deaths})
    data = json.loads(df.T.to_json()).values()
    collection_Scraping_data1.delete_many({})
    collection_Scraping_data1.insert_many(data)