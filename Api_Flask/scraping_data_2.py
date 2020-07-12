from bs4 import BeautifulSoup
import requests
from flask import abort, Flask, jsonify, request
from pymongo import MongoClient
import pandas as pd
from flask import abort, Flask, jsonify, request, json
import requests

#Connexion avec la base de donnée MongoDB
cluster = MongoClient("mongodb://localhost:27017/?readPreference=primary&appname=MongoDB%20Compass%20Community&ssl=false") 
db = cluster["db_covid19"]

def scraping_data_2():
    collection_Scraping_data2 = db["Scraping_data2"]
    page = requests.get('https://www.worldometers.info/coronavirus/')
    soup = BeautifulSoup(page.text, 'html.parser')
    table = soup.find_all(attrs={"id":"main_table_countries_today"})[0]
    alll = table.find_all(attrs={"class":"mt_a"})
    countries = []
    cases = []
    deaths = []
    for country_element in alll:
        nb_cases = country_element.parent.next_sibling.next_sibling.string
        nb_deaths = country_element.parent.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.string
        countries.append(country_element.string)
        cases.append(nb_cases)
        deaths.append(nb_deaths)

    df=pd.DataFrame(data={'country':countries, 'total_cases': cases,'total_deaths': deaths})
    # df.to_csv('C:/Users/soumaya/DataSets/covid19/dataNada3.csv', sep=';')
    data = json.loads(df.T.to_json()).values()
    collection_Scraping_data2.delete_many({})
    collection_Scraping_data2.insert_many(data)