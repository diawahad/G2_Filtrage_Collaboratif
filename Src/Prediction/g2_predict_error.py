# -*- coding: utf-8 -*-
"""
Created on Fri Jan 18 15:57:35 2019

@author: chach
"""

import pandas as pd
import numpy as np

# %%

def mae(rate,pred):
    return (np.sqrt(np.abs(rate-pred)).mean())

# %%

def rmse(rate,pred):
    return (np.sqrt((rate-pred)**2).mean())

# %%
    
def calculerror(filephath_rating, filepath_predict,metric):
    rate = pd.read_csv(filephath_rating, sep= ';')
    pred = pd.read_csv(filepath_predict, sep = ';')
    pred.columns = ['rating_id', 'pred']
    ratings = pd.merge(rate, pred, on=["rating_id"])
    if metric == 'rmse':
        value = rmse(ratings.rating,ratings.pred)
    else:
        value = mae(ratings.rating,ratings.pred)
    return (value)

# %%

calculerror('/home/sid2018-1/Documents/projet2019/data_movie/Train_series.csv','/home/sid2018-1/Téléchargements/pred_serie_user_user.csv', 'rse')