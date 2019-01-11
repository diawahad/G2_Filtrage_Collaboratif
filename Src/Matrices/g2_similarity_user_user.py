
"""
Created on Tue Jan  8 09:27:59 2019

group 2
@author: Alioune G, Serigne D, Mickael A.

"""

import pandas as pd
import numpy as np
from tqdm import tqdm
from g2_to_matrix import to_matrix
from g2_to_matrix import to_dict
from scipy.spatial.distance import cosine
from sklearn.metrics.pairwise import cosine_similarity

dictionnaire = to_dict("/home/sid2018-1/Documents/projet2019/data_v3/ratings_V3.csv","/home/sid2018-1/Documents/projet2019/data_v3/products_V4.csv")
matrice = to_matrix("/home/sid2018-1/Documents/projet2019/data_v3/ratings_V3.csv","/home/sid2018-1/Documents/projet2019/data_v3/products_V4.csv")

'''
Function calculcosin_mat

Input : - User/Products Rating Matrix for movies

Output : Similarity cosinus User/User Matrix for movies
The function calcul similarity cosinus between users :
    rows : users
    columns : users
    values : Similarity between us
'''


def calculcosin_mat(user1, user2):
    dataframe0 = pd.concat([pd.Series(x) for x in [user1, user2]], axis=1)
    dataframe1 = dataframe0.dropna()
    if (len(dataframe1) == 1):
        val = 1
    else:
        val = cosine(dataframe1[0].values, dataframe1[1].values)
    return(val)


def similarity_user_user_mat(matrice_centree):
    variables = matrice_centree.index
    size = matrice_centree.shape[0]
    mat = np.zeros((size, size))
    for indice1, i1 in enumerate(variables):
        for indice2, i2 in enumerate(variables):
            if(indice2 > indice1):
                value = calculcosin_mat(matrice_centree.transpose()[i1].values,
                                        matrice_centree.transpose()[i2].values)
                mat[indice1, indice2] = value
                mat[indice2, indice1] = value
    return (pd.DataFrame(mat, index=matrice_centree.index,
                         columns=matrice_centree.index))


#print(similarity_user_user_mat(matrice))

'''
Function calculcosin_dic

Input : - User/Products Rating dictionary for movies

Output : Similarity cosinus User/User Matrix for movies
The function calcul similarity cosinus between users :
    rows : users
    columns : users
    values : Similarity between us
'''


def calculcosin_dic(user1, user2):
    dataframe1 = pd.merge(user1, user2, on='item_id')
    if (len(dataframe1) == 1):
        val = 1
    else:
        val = cosine(dataframe1['rating_x'].values,
                     dataframe1['rating_y'].values)
    return(val)


def similarity_user_user_dic(dico):
    variables = dico.keys()
    size = len(variables)
    dic = np.zeros((size, size))
    for indice1, iter1 in enumerate(tqdm(variables)):
        for indice2, iter2 in enumerate(tqdm(variables)):
            if(indice2 > indice1):
                valeur_iter2 = pd.DataFrame(list(dico[iter2]),
                                            columns=['item_id', 'rating'])
                valeur_iter1 = pd.DataFrame(list(dico[iter1]),
                                            columns=['item_id', 'rating'])
                value = calculcosin_dic(valeur_iter2, valeur_iter1)
                dic[indice1, indice2] = value
                dic[indice2, indice1] = value
    return (pd.DataFrame(dic, index=dico.keys(), columns=dico.keys()))

# print(cosine_similarity(dataframe.dropna().transpose()))
# similarity = cosine_similarity(dataframe1)
# print(similarity)


#print(similarity_user_user_dic(dictionnaire))
