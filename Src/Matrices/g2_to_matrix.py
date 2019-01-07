
# coding: utf-8

import pandas as pd

'''
Function toMatrix

Input : - csv rating file path
        - csv products file path
Output : User/Products Rating Matrix for movies
'''
def toMatrix(filepath_rating, filepath_product):
#    filepath_rating="C:/Users/alice/Documents/SID/S1/G2_ Projet/donnees/ratings_V3.csv"
    
    df_rating = pd.read_csv(filepath_rating,header=0,sep=";",nrows=int(1e6))
    
#    filepath_product="C:/Users/alice/Documents/SID/S1/G2_ Projet/donnees/products_V3.csv"
    df_prod = pd.read_csv(filepath_product,header=0,sep=";")
    
    df_join = pd.merge(df_rating,df_prod)
    
    
    df_join = df_join.loc[:,['rating_id','user_id','product_id','rating','date_rating','subtype_id']]
    
    df_join = df_join.loc[df_join['subtype_id'] == 1.0]
    
    df_join = df_join.pivot(index='user_id',columns='product_id',values='rating')
    
    return df_join