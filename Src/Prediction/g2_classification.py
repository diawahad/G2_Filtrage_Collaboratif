#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 10 14:53:00 2019

@author: sid2018-1
"""
import pandas as pd
import numpy as np
import sys
from g2_predict_nan import knn

from g2_to_matrix import to_matrix
from g2_to_matrix import to_dict
from scipy.spatial.distance import cosine
from g2_similarity_user_user import similarity_user_user_dic
from g2_predict_nan import predit

from g2_similarity_user_user import similarity_user_user_mat
sys.path.append("../Matrices")

# %%


'''
Function find_centers

Input : - filepath_rating : csv rating file path
        - filepath_product : csv products file path
        - k : number of centers
        - value : as item or user (default : 'item')
        - modality (float) : - Movie : 1.0 (default : 1.0)
                             - Book : 2.0
                             - Serie : 4.0

Output : User_id /number of ratings of the k centers

The function calculates the k number of centers for our clustering
    columns : user_id, rating_count
    values : ratings
'''


def find_centers(filepath_rating, filepath_product, k, value='item',
                 modality=1.0):
    df_rating = pd.read_csv(filepath_rating, header=0, sep=";", nrows=int(1e3))
    df_prod = pd.read_csv(filepath_product, header=0, sep=";", nrows=int(1e4))
    df_join = pd.merge(df_rating, df_prod)
    df_join = df_join.loc[df_join['subtype_id'] == modality]
    if (value == 'item'):
        df_join = df_join.loc[:, ['product_id', 'rating', 'subtype_id']]
        df_join = df_join.groupby(['product_id', 'subtype_id'],
                                  as_index=False)['rating'].count()
    else:
        df_join = df_join.loc[:, ['user_id', 'rating']]
        df_join = df_join.groupby(['user_id'],
                                  as_index=False)['rating'].count()
    df_join = df_join.rename(columns={"rating": "rating_count"})
    df_join = df_join.sort_values(by='rating_count', ascending=False)
    df_join = df_join.head(k)
    return df_join

# %%


'''
Function make_clusters

Input : - find_centers : find_centers
        -  distance : user/user or item/item matrix got by calling
        similarity_user_user_dic function
        - value : as user_id or product_id

Output : dictionnary clusters

The function calculates the nearest cluster of our centers and puts the user or
item into this clustering set
    keys : centers'id
    sets : user_id or item_id
'''


def make_clusters(find_centers, distance, value):
    dico = {x: set() for x in find_centers[value].values}
    for v in (distance.index):
        t = dico.keys()
        if v in t:
            dico[v].add((v, v))
        else:
            liste = knn(v, distance, k="all")
            for i, j in enumerate(liste):
                if j in t:
                    dico[j].add((j, v))
                    break
    return dico

# %%


'''
Function add_classes

Input : - filepath : csv rating or product file path
        - dico_class : dictionnary of clusters got by calling make_clusters
        - something_id : value as user_id or product_id (default : 'user_id')

Output : User_id/centers matrix

The function calculates the mean of the ratings of users from the same
clustering
    rows: user_id
    columns : centers_id
    values : mean of ratings
'''


def add_classes(filepath, dico_class, something_id='product_id'):
    dfdico = pd.DataFrame({'Cluster': [np.nan], something_id: [np.nan]})
    df = pd.read_csv(filepath, header=0, sep=";", nrows=int(1e3))
    for v in dico_class.keys():
        if dico_class[v]:
            df2 = pd.DataFrame(list(dico_class[v]), columns=['Cluster',
                               something_id])
            frames = [dfdico, df2]
            dfdico = pd.concat(frames)
    df_merge = pd.merge(dfdico, df, on=something_id, how='left')
    if (something_id == 'product_id'):
        df_merge = df_merge.groupby(['user_id', 'Cluster'],
                                    as_index=False)['rating'].mean()
    else:
        df_merge = df_merge.groupby(['product_id', 'Cluster'],
                                    as_index=False)['rating'].mean()
    return(df_merge)

# %%


'''
Function add_classes_user

Input : - df : DataFrame
        - dico_class : dictionnary of clusters got by calling make_clusters
        - something_id : value as user_id or product_id (default : 'user_id')

Output : User_id/centers matrix

The function calculates the mean of the ratings of users from the same
clustering
    rows: user_id
    columns : centers_id
    values : mean of ratings
'''


def add_classes_user(df, dico_class, something_id='user_id'):
    dfdico = pd.DataFrame({'Cluster2': [np.nan], something_id: [np.nan]})
    for v in dico_class.keys():
        if dico_class[v]:
            df2 = pd.DataFrame(list(dico_class[v]), columns=['Cluster2',
                               something_id])
            frames = [dfdico, df2]
            dfdico = pd.concat(frames)
    df_merge = pd.merge(dfdico, df, on=something_id, how='left')
    df_merge = df_merge.groupby(['Cluster', 'Cluster2'],
                                as_index=False)['rating'].mean()
    return(df_merge)
