import pandas as pd
import numpy as np
# from sklearn.model_selection import train_test_split
# from sklearn.linear_model import LinearRegression
from flask import Flask, jsonify, request, json, url_for, redirect, abort
from sklearn import metrics
from fbprophet import Prophet


def predict():
    df = pd.read_csv('C:/Users/soumaya/DataSets/v2/covid_19_clean_complete.csv', parse_dates=['Date'])
    confirmed = df.groupby('Date').sum()['Confirmed'].reset_index()
    confirmed.columns = ['ds', 'y']
    confirmed['ds'] = pd.to_datetime(confirmed['ds'])
    m = Prophet(interval_width=0.95)
    m.fit(confirmed)
    future = m.make_future_dataframe(periods=7)
    forecast = m.predict(future)
    df = forecast.to_numpy()
    predicted = [l[3] for l in df]
    day = [l[0] for l in df]
    # print('predicted : ',predicted )
    # print(forecast.yhat)
    return jsonify(day = day, predicted = predicted)
    

