"""
Created on Tue Jan  8 09:27:59 2019

@author: Group 2 !
"""
# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np
from tqdm import tqdm
import os
from g2_to_matrix import to_matrix
from g2_to_matrix import to_dict
from scipy.spatial.distance import cosine
from sklearn.metrics.pairwise import cosine_similarity

# %%

'''
Function calculcosin_mat

Input : - user1 : rating of the first user
        - user2 : rating of the second user

Output : cosine similiraty between these two users

The function computes similarity cosinus between two users.
'''


def calculcosin_mat(user1, user2):
    dataframe0 = pd.concat([pd.Series(x) for x in [user1, user2]], axis=1)
    dataframe1 = dataframe0.dropna()
    if (len(dataframe1) == 1):
        val = 1
    else:
        val = cosine(dataframe1[0].values, dataframe1[1].values)
    return(val)

# %%


'''
Function similarity_user_user_mat

Input : - centred_matrix : Users/Products Rating Matrix (centered) for movies

Output : Matrix similarity User/User

The function computes similarity cosinus between users :
    rows : users
    columns : users
    values : Similarity between users
'''


def similarity_user_user_mat(centred_matrix):
    variables = centred_matrix.index
    size = centred_matrix.shape[0]
    mat = np.zeros((size, size))
    for indice1, i1 in enumerate(variables):
        for indice2, i2 in enumerate(variables):
            if(indice2 > indice1):
                value = calculcosin_mat(centred_matrix.transpose()[i1].values,
                                        centred_matrix.transpose()[i2].values)
                mat[indice1, indice2] = value
                mat[indice2, indice1] = value
    return (pd.DataFrame(mat, index=centred_matrix.index,
                         columns=centred_matrix.index))

# %%


'''
Function calculcosin_dic

Input : - user1 : rating of the first user
        - user2 : rating of the second user

Output : cosine similiraty between these two users

The function computes similarity cosinus between two users.
'''


def calculcosin_dic(user1, user2):
    dataframe1 = pd.merge(user1, user2, on='item_id')
    if (len(dataframe1) == 1):
        val = 1
    else:
        val = cosine(dataframe1['rating_x'].values,
                     dataframe1['rating_y'].values)
    return(val)

# %%


'''
Function similarity_user_user_dic

Input : - dico : Users/Products Rating dictionary for movies

Output : - Matrix similarity User/User

The function computes similarity cosinus between users :
    rows : users
    columns : users
    values : similarity between users
'''


def similarity_user_user_dic(dico):
    variables = dico.keys()
    size = len(variables)
    dic = np.zeros((size, size))
    for indice1, iter1 in enumerate(tqdm(variables)):
        for indice2, iter2 in enumerate(variables):
            if(indice2 > indice1):
                valeur_iter2 = pd.DataFrame(list(dico[iter2]),
                                            columns=['item_id', 'rating'])
                valeur_iter1 = pd.DataFrame(list(dico[iter1]),
                                            columns=['item_id', 'rating'])
                value = calculcosin_dic(valeur_iter2, valeur_iter1)
                dic[indice1, indice2] = value
                dic[indice2, indice1] = value
    return (pd.DataFrame(dic, index=dico.keys(), columns=dico.keys()))
