"""
Created on Mon Jan  7 15:33:15 2019

Group 2
@author: Alice A, Corentin L, Charlotte M, Alexis D
"""
# coding: utf-8

import pandas as pd
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
    df_rating = pd.read_csv(filepath_rating, header=0, sep=";", nrows=int(1e6))
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

Input : DataFrame to be unbiased
Output: Unbiased matrix
The function centers and reduces the given dataframe, item by item
Ignores missing  values
'''

def unbias(df):
    return scale(df)

