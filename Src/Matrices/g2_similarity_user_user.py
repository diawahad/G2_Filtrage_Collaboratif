
"""
Created on Tue Jan  8 09:27:59 2019

group 2
@author: Alioune G, Serigne D, Mickael A.

"""

import pandas as pd
import numpy as np
from g2_to_matrix import to_matrix 
from g2_to_matrix import to_dict
from scipy.spatial.distance import cosine
from sklearn.metrics.pairwise import cosine_similarity

dic = to_dict("/home/mickael/Documents/data_v3/ratings_V3.csv","/home/mickael/Documents/data_v3/products_V3.csv")
mat = to_matrix("/home/mickael/Documents/data_v3/ratings_V3.csv","/home/mickael/Documents/data_v3/products_V3.csv")

'''
Function calculcosin_mat

Input : - User/Products Rating Matrix for movies

Output : Similarity cosinus User/User Matrix for movies
The function calcul similarity cosinus between users :
    rows : users
    columns : users
    values : Similarity between us
'''

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
            if(v == k):
                mat[i,j] = 0
    return (pd.DataFrame(mat,index=matrice_centree.index,columns=matrice_centree.index))

print(similarity_user_user_mat(mat))

'''
Function calculcosin_dic

Input : - User/Products Rating dictionary for movies

Output : Similarity cosinus User/User Matrix for movies
The function calcul similarity cosinus between users :
    rows : users
    columns : users
    values : Similarity between us
'''

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
            if(v == k):
                mat[i,j] = 0
    return (pd.DataFrame(mat,index=dico.keys(),columns=dico.keys()))

# print(cosine_similarity(df.dropna().transpose()))   
# sim = cosine_similarity(df1)
# print(sim)

print(similarity_user_user_dic(dic))
