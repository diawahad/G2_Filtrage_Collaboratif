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
os.chdir("/home/formationsid/Documents/G2/G2_Filtrage_Collaboratif/Src/Matrices/")
from g2_to_matrix import to_matrix, to_dict, unbias
from g2_similarity_user_user import similarity_user_user_mat
from g2_similarity_user_user import similarity_user_user_dic
os.chdir("/home/formationsid/Documents/G2/G2_Filtrage_Collaboratif/Src/Prediction/")
from g2_predict_nan import predit_df, predit, recalculate


def Collaborative_filtering(filepath_ratings, filepath_products, k=1, t='matrix',
              t_user='user', modality=1.0, rating_rows = 1e3, prod_rows = 1e5):
    matrix_user_item = to_matrix(filepath_ratings, filepath_products, t_user, modality, rating_rows, prod_rows)
    matrix_user_item_scale = pd.DataFrame(scale(matrix_user_item),index=matrix_user_item.index,columns=matrix_user_item.columns)
    if t == 'matrix':
        distance = similarity_user_user_mat(matrix_user_item)
    else:
        matrice_creuse = to_dict(filepath_ratings, filepath_products, t_user, modality, rating_rows, prod_rows)
        distance = similarity_user_user_dic(matrice_creuse)
    #df_knn = predit_df(matrix_user_item, distance, k)
    df_knn_CR = predit_df(matrix_user_item_scale, distance, k)
    
    valpred = recalculate(matrix_user_item,df_knn_CR)
    return valpred



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