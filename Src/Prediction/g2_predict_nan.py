"""
Created on Tue Jan  8 09:27:59 2019

group 2
@author: Moustapha S, Serigne D, Paul L, Fallou B, Ismail H.

"""

import numpy as np
from tqdm import tqdm, tqdm_notebook
import pandas as pd

'''
Function kkn

Input : - id_user user ID
        - distance
        - k user number default all
Output : list of k closest users of user_id

The function calculates and returns the k user closest to user_id

'''


def knn(id_user, distance, k="all"):
    return distance[id_user].sort_values().index[
            1: int(k)+1 if k != "all" else len(distance)]


'''
Function predit

Input : - df DataFrame or dictionary of sets of tuple (item,rating)
        - distance
Output : df DataFrame predit

The function predicts the NANs from the notes of the closest users

'''

def predit_df(df, distance, jpnb,  k):
    dfold = df.copy()
    dfnew = df.copy()
    if jpnb:
        for u in tqdm_notebook(dfnew.index, desc = 'Predit: Computing k-nearest neighbors'):
            ukkn = knn(u, distance)
            index = dfnew.loc[u, dfnew.loc[u].isna()].index
            if len(index) > 0:
                for p in tqdm_notebook(index, desc = 'Predit: Finding and replacing NaN values'):
                    datanotna = dfold[p][dfold[p].notna()]
                    dfnew.loc[u, p] = np.mean(datanotna[[
                            j for j in ukkn if j in datanotna.index]][:k])
    else:
        for u in tqdm(dfnew.index, desc = 'Predit: Computing k-nearest neighbors'):
            ukkn = knn(u, distance)
            index = dfnew.loc[u, dfnew.loc[u].isna()].index
            if len(index) > 0:
                for p in tqdm(index, desc = 'Predit: Finding and replacing NaN values'):
                    datanotna = dfold[p][dfold[p].notna()]
                    dfnew.loc[u, p] = np.mean(datanotna[[
                            j for j in ukkn if j in datanotna.index]][:k])
    return dfnew
    
    

def dic_to_df(dico):
    #converts dictionnaries set into dict of dict-arrays
    un_gradez = {keys: [{v[0]:v[1]}for v in list(values)] for keys, values in dico.items()}
    #creates a dataset with user_id as index and n columns where n is max length of array
    df_un = pd.DataFrame.from_dict(un_gradez, orient='index')
    #convert the dict in the cells into columns
    cool = df_un.columns
    for c in cool:
        df_un = pd.concat([df_un.drop([c], axis=1), df_un[c].apply(pd.Series)], axis=1)

    #groups same name columns together
    def sjoin(x): return next((item for item in x if (item is not None and not np.isnan(item) )), np.nan)
    tqdm.pandas(desc = "predit_dic: Grouping columns together")
    return df_un.groupby(level=0, axis=1).progress_apply(lambda x: x.apply(sjoin, axis=1))
    


def predit(df, distance, jpnb = False, k = 10):
    if isinstance(df, dict):
        df_un = dic_to_df(df)
        return predit_df(df_un,distance, jpnb, k)
    elif isinstance(df, pd.DataFrame):
        return predit_df(df,distance)

def recalculate(df, dfunbias):
    mean = lambda c : df[c][df[c].notna()].mean()
    std = lambda c: df[c][df[c].notna()].std(ddof = 0)
    dfunbiascopy = dfunbias.copy()
    for c in dfunbiascopy.columns:
        dfunbiascopy[c] = dfunbiascopy[c] * std(c) + mean(c)
    return dfunbiascopy
