from bs4 import BeautifulSoup
import requests
import pandas as pd

def Scarping_nouvelles(numOfPages):
  formats='html.parser'
  tags='h3'
  news_dict=[]
  numOfPages=int(numOfPages)
  numOfPages=numOfPages+1
  for i in range(1, numOfPages):
      url="https://www.moroccoworldnews.com/news-2/page/{}".format(i)
      response = requests.get(url)
      soup = BeautifulSoup(response.content,formats)
      for div in soup.findAll("div", {'class':'td-ss-main-sidebar'}): 
        div.decompose() 
      for div1 in soup.findAll("div", {'class':'td-subcategory-header'}):
        div1.decompose() 
      for head in soup.find_all(tags, {'class':'entry-title td-module-title'}):
        titre=head.find('a').get('title')
        news_dict.append({'Titre': titre})
       
  news_df=pd.DataFrame(news_dict)
  news_df.to_csv("NewsScrapped.csv" ,index=False, encoding='utf8')
       
     



