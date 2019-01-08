"""
Created on Mon Jan  7 15:33:15 2019

Group 2
@author: Alice A, Corentin L, Charlotte M, Alexis D, Paul L, Ismail H.
"""
# coding: utf-8

import pandas as pd
import numpy as np
from tqdm import tqdm
from sklearn.preprocessing import scale


'''
Function toMatrix

Input : - csv rating file path
        - csv products file path
Output : User/Products Rating Matrix for movies
The function transforms the ratings and the products files to a matrix :
    rows : users
    columns : products
    values : ratings
'''


def to_matrix(filepath_rating, filepath_product):
    df_rating = pd.read_csv(filepath_rating, header=0, sep=";", nrows=int(100))
    df_prod = pd.read_csv(filepath_product, header=0, sep=";")
    df_join = pd.merge(df_rating, df_prod)
    df_join = df_join.loc[:, ['rating_id', 'user_id', 'product_id', 'rating',
                              'date_rating', 'subtype_id']]
    df_join = df_join.loc[df_join['subtype_id'] == 1.0]

    df_join = df_join.pivot(index='user_id', columns='product_id',
                            values='rating')
    return df_join

'''
Function unbias

Input : 
    df - DataFrame to be unbiased
    axis - 0 by default, if any other value Transposes the dataframe
        to unbias by user instead of items
    mean - False by default, replaces missing values with 5.5 which is
        the median value in the Sens Critique rating system
Output: Unbiased matrix
The function centers and reduces the given dataframe, item by item
Ignores missing  values
'''

def unbias(df,axis = 0, mean = False):
    if axis !=0:
        df = df.T
    if mean:
        df.fillna(5.5, inplace = True) 

    return scale(df)

print(unbias(to_matrix('../data_v3/ratings_V3.csv','../data_v3/products_V3.csv'), True))
