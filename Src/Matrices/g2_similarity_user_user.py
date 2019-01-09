#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan  8 09:27:59 2019

@author: sid2018-1
"""
import pandas as pd
import numpy as np
from g2_to_matrix import to_matrix 
from g2_to_matrix import to_dict
from scipy.spatial.distance import cosine
from sklearn.metrics.pairwise import cosine_similarity


'''a = np.array([6,3,8,float("NaN"),6,4,3,5])
b = np.array([float("NaN"),7,9,2,5,9,5,7])
c = np.array([7,9,0,3,4,5,float("NaN"),6])
d = np.array([float("NaN"),float("NaN"),float("NaN"),float("NaN"),float("NaN"),float("NaN"),3,float("NaN")])
df = pd.concat([pd.Series(x) for x in [a,b,c,d]], axis=1)'''
df = to_dict("/home/sid2018-1/Documents/projet2019/data_v3/ratings_V3.csv","/home/sid2018-1/Documents/projet2019/data_v3/products_V4.csv")

def calculcosin_mat(u,v):
    df0 = pd.concat([pd.Series(x) for x in [u,v]], axis=1)
    df1 = df0.dropna()
    if (len(df1)== 1 ):
        val = 1
    else:
        val = cosine(df1[0].values , df1[1].values )
    return(val)

def similarity_user_user_mat(matrice_centree):
    variables = matrice_centree.index
    size = matrice_centree.shape[0]
    mat = np.zeros((size,size))
    for i,v in enumerate (variables):
        for j,k in enumerate (variables):
            mat[i,j] = calculcosin_mat(matrice_centree.transpose()[v].values, matrice_centree.transpose()[k].values)
    return (pd.DataFrame(mat,index=matrice_centree.index,columns=matrice_centree.index))

'''print(similarity_user_user_mat(df))'''

def calculcosin_dic (u,v):
    df1 = pd.merge(u,v, on= 'item_id')
    if (len(df1)== 1 ):
        val = 1
    else:
        val = cosine(df1['rating_x'].values , df1['rating_y'].values )
    return(val)

def similarity_user_user_dic(dico):
    variables = dico.keys()
    size = len(variables)
    mat = np.zeros((size,size))
    for i,v in enumerate (variables):
        for j,k in enumerate (variables):
            valk= pd.DataFrame(list(dico[k]), columns = ['item_id','rating'])
            valv=pd.DataFrame(list(dico[v]), columns = ['item_id','rating'])
            mat[i,j] = calculcosin_dic(valk, valv)
        print(i)
    return (pd.DataFrame(mat,index=dico.keys(),columns=dico.keys()))
'''print(cosine_similarity(df.dropna().transpose()))   
sim = cosine_similarity(df1)
print(sim)'''

