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

# %%

'''
Function to_matrix

Input : - csv rating file path
        - csv products file path
Output : User/Products Rating Matrix for movies
The function transforms the ratings and the products files to a matrix :
    rows : users
    columns : products
    values : ratings
'''


def to_matrix(filepath_rating, filepath_product):
    df_rating = pd.read_csv(filepath_rating, header=0, sep=";", nrows=int(1e3))
    df_prod = pd.read_csv(filepath_product, header=0, sep=";", nrows=int(1e5))
    df_join = pd.merge(df_rating, df_prod)
    df_join = df_join.loc[:, ['rating_id', 'user_id', 'product_id', 'rating',
                              'date_rating', 'subtype_id']]
    df_join = df_join.loc[df_join['subtype_id'] == 1.0]

    df_join = df_join.pivot(index='user_id', columns='product_id',
                            values='rating')
    return df_join

'''
Function to_dict

Input : - csv rating file path
        - csv products file path
Output : User/Products Rating dictionary for movies
The function transforms the ratings and the products files to a dictionary :
    key : users
    values : set of (products,rate) tuples
'''

#%%
def to_dict(filepath_rating, filepath_product):
    df_rating = pd.read_csv(filepath_rating, header=0, sep=";", nrows=int(1e3))
    df_prod = pd.read_csv(filepath_product, header=0, sep=";", nrows=int(1e5))
    df_join = pd.merge(df_rating, df_prod)
    df_join = df_join.loc[:, ['rating_id', 'user_id', 'product_id', 'rating',
                              'date_rating', 'subtype_id']]
    df_join = df_join.loc[df_join['subtype_id'] == 1.0]
    df_join = df_join.pivot(index='user_id', columns='product_id',
                            values='rating')
    d_users_rates = {}
    for i in df_join.index:
        s_users = list()
        for j in df_join.columns:
            if not np.isnan(df_join[j][i]):
                s_users.append((j, int(df_join[j][i])))
        d_users_rates[i] = s_users
    return d_users_rates

# %%


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


def unbias(df, axis=0, mean=False):
    if axis != 0:
        df = df.T
    if mean:
        df = df.fillna(5.5)

    return scale(df)

# %%


'''
Function groupby_attribute

Input :
    filepath_rating : csv rating file path (text)
    filepath_product : csv product file path (text)
    attribute : attribute name chosen for the group by (text)
Ouput :
    DataFrameGroupBy object group by the attribute
The function return a DataGroupBy object depending on the input attribute.
To produce a result, we can apply an aggregate to this DataFrameGroupBy object,
which will perform the appropriate apply/combine steps to produce the desired
result.
'''


def groupby_attribute(filepath_rating, filepath_product, attribute):
    df_rating = pd.read_csv(filepath_rating, header=0, sep=";", nrows=int(1e3))
    df_prod = pd.read_csv(filepath_product, header=0, sep=";", nrows=int(1e5))
    df_join = pd.merge(df_rating, df_prod)
    df_join = df_join.groupby(attribute)
    return df_join

# %%
 