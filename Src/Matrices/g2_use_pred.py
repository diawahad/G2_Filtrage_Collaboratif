# !/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 10 09:25:47 2019

@author: Serigne D, Alexis D.
"""

import sys
from sklearn.preprocessing import scale
import os
import pandas as pd
from g2_to_matrix import to_matrix, to_dict, unbias
from g2_similarity_user_user import similarity_user_user_mat
from g2_similarity_user_user import similarity_user_user_dic
from g2_predict_nan import predit_df, predit, recalculate

# %%


'''
Function collaborative_filtering

Input : - filepath_rating : csv rating file path
        - filepath_product : csv products file path
        - k : number of neighbors (default : 1)
        - t : to choose between matrix or dico (default : 'matrix')
        - t_user : to choose between the matrix users/items or items/users
        (default : 'user')
        - modality (float) : - Movie : 1.0 (default)
                             - Book : 2.0
                             - Serie : 4.0
        - filesize : number of the rows of the file to read (default : 1e3)

Output : Predicted Matrix Users/Products

The function returns the predicted matrix Users/Products
'''


def collaborative_filtering(filepath_rating, filepath_product, k=1,
                            t='matrix', t_user='user', modality=1.0,
                            rating_rows=1e3, prod_rows=1e5, jpnb=False):
    matrix_user_item = to_matrix(filepath_rating, filepath_product, t_user,
                                 modality, rating_rows, prod_rows)
    matrix_user_item_scale = pd.DataFrame(scale(matrix_user_item),
                                          index=matrix_user_item.index,
                                          columns=matrix_user_item.columns)
    if t == 'matrix':
        distance = similarity_user_user_mat(matrix_user_item)
    else:
<<<<<<< HEAD
<<<<<<< HEAD
        d_item_item = to_dict(filepath_ratings, filepath_products, t_user)
        df_item_item = similarity_user_user_dic(d_item_item)
    df_knn = predit(m_item_item, df_item_item)
    return df_knn
=======
        matrice_creuse = to_dict(filepath_ratings, filepath_products, t_user, modality, rating_rows, prod_rows)
=======
        matrice_creuse = to_dict(filepath_rating, filepath_product, t_user,
                                 modality, rating_rows, prod_rows)
>>>>>>> master
        distance = similarity_user_user_dic(matrice_creuse)
<<<<<<< HEAD
    df_knn_CR = predit_df(matrix_user_item_scale, distance, k)

<<<<<<< HEAD
#%%
path = "/home/formationsid/Documents/osirimV/data_v3/"
prod = path + "products_V4.csv"
rate = path + "ratings_V3.csv"
rate_sample = '/home/formationsid/Documents/osirimV/data_v3/sample.csv'
#rate = path + "data_train_val.csv"
#rate = path + "Train_movie.csv"

prediteF = Collaborative_filtering(rate,prod,2,'matrix','user',2,1e5,'all')
#prediteB = item_item(rate,prod,2,'matrix','user',2,2e7)
#prediteS = item_item(rate,prod,2,'matrix','user',4,2e7)
#prediteM = item_item(rate,prod,2,'matrix','user','multi',2e7)

#prediteF.to_csv('/home/formationsid/Documents/osirimV/data_v3/prediteFilmSample1e6V.csv',index=False,header=1,sep=';')
#prediteB.to_csv('/users/sidcritique/sdiaw/Src/outputs/prediteB.csv',idex=False,header=1,sep=';')
#prediteS.to_csv('/users/sidcritique/sdiaw/Src/outputs/prediteS.csv',index=False,header=1,sep=';')
#prediteM.to_csv('/users/sidcritique/sdiaw/Src/outputs/prediteM.csv',index=False,header=1,sep=';')
>>>>>>> master
=======
    valpred = recalculate(matrix_user_item, df_knn_CR)
=======
    #df_knn = predit_df(matrix_user_item, distance, jpnb, k)
    df_knn_CR = predit_df(matrix_user_item_scale, distance, jpnb, k)
    
    valpred = recalculate(matrix_user_item,df_knn_CR)
>>>>>>> master
    return valpred
>>>>>>> master
