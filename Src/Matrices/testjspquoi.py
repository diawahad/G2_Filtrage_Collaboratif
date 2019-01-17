#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 11 09:30:22 2019

@author: ddm-turing3
"""

import sys
import pandas as pd

sys.path.append("/home/ddm-turing3/Bureau/SensCritique/G2_Filtrage_Collaboratif/Src/Matrices")
sys.path.append("/home/ddm-turing3/Bureau/SensCritique/G2_Filtrage_Collaboratif/Src/Prediction")
from g2_to_matrix import to_matrix, unbias 
from g2_predict_nan import predit, predit_df
from g2_ratings_pred import conversion_df,recalculate
from g2_similarity_user_user import similarity_user_user_dic

ratings_path = '/home/ddm-turing3/Bureau/SensCritique/data_v3/ratings_V3.csv'
products_path = '/home/ddm-turing3/Bureau/SensCritique/data_v3/products_V4.csv'

grades = to_matrix(ratings_path,products_path)
#Les notes originales
grades.head(10)
un_grades = unbias(grades)
#Notes sans Biais
print(un_grades)
dist = similarity_user_user_dic(un_grades)
#Distance User X User
dist.head(10)

#converts dictionnaries set into dict of dict-arrays
un_gradez = {keys: [{v[0]:v[1]}for v in list(values)] for keys, values in un_grades.items()}
#creates a dataset with user_id as index and n columns where n is max length of array
df_un = pd.DataFrame.from_dict(un_gradez, orient='index')
#convert the dict in the cells into columns
cool = df_un.columns
for c in cool:
    df_un = pd.concat([df_un.drop([c], axis=1), df_un[c].apply(pd.Series)], axis=1)

#groups same name columns together
def sjoin(x): return next((item for item in x if (item is not None and not np.isnan(item) )), np.nan)
df_un = df_un.groupby(level=0, axis=1).apply(lambda x: x.apply(sjoin, axis=1))
df_un.head(10)

un_new = predit_df(df_un,dist)
#notes predites
un_new.head(10) 
gradz_new = recalculate(grades,un_new)
#Notes predites et reconverties de 1 à 10
gradz_new.head(10)