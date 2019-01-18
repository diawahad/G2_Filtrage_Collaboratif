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
                            rating_rows=1e3, prod_rows=1e5):
    matrix_user_item = to_matrix(filepath_rating, filepath_product, t_user,
                                 modality, rating_rows, prod_rows)
    matrix_user_item_scale = pd.DataFrame(scale(matrix_user_item),
                                          index=matrix_user_item.index,
                                          columns=matrix_user_item.columns)
    if t == 'matrix':
        distance = similarity_user_user_mat(matrix_user_item)
    else:
        matrice_creuse = to_dict(filepath_rating, filepath_product, t_user,
                                 modality, rating_rows, prod_rows)
        distance = similarity_user_user_dic(matrice_creuse)
    #df_knn = predit_df(matrix_user_item, distance, k)
    df_knn_CR = predit_df(matrix_user_item_scale, distance, k)
    
    valpred = recalculate(matrix_user_item,df_knn_CR)
    return valpred
