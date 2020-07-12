import numpy as np 
import pandas as pd 
from flask import Flask, jsonify, request, json, url_for, redirect, abort
from sklearn.cluster import KMeans


def clustering():
    df=pd.read_excel('C:/Users/soumaya/DataSets/covid19/scrap_morocco.xlsx')
    data_kmeans=df[['Confirmed','Deaths']]
    kmeans = KMeans(n_clusters = 3, init = 'k-means++', random_state = 42)
    y_kmeans = kmeans.fit_predict(data_kmeans)
    y_kmeans1=y_kmeans
    y_kmeans1=y_kmeans+1
    cluster = pd.DataFrame(y_kmeans1)
    data_kmeans['cluster'] = cluster
    data_risk= pd.DataFrame()
    data_risk["country"]=df["Region"]
    data_risk["Confirmed"]=y_kmeans1
    lis = list()
    for group in range(1,4):
        countries=data_risk.loc[data_risk['Confirmed']==group]
        listofcoutries= list(countries['country'])
        lis.append(listofcoutries)
    cl1 = lis[0]
    cl2 = lis[1]
    cl3 = lis[2]
    return jsonify(cluster1=cl1,cluster2=cl2,cluster3=cl3)
    # return lis