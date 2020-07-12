import pandas as pd

def preprocessing_data():
    news_df=pd.read_csv("NewsScrapped.csv")  
    news_df=news_df.sort_values('Titre', ascending=False)
    news_df=news_df.drop_duplicates(subset='Titre')
    news_df.to_csv("NewsScrapped.csv" ,index=False)
