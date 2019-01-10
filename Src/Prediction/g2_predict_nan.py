import pandas as pd
import numpy as np

'''
Function kkn

Input : - id_user user ID
        - distance 
        - k user number default all
Output : list of k closest users of user_id

The function calculates and returns the k user closest to user_id

'''

def knn(id_user, distance, k = "all"):
    return distance[id_user].sort_values().index[1: int(k)+1 if  k != "all" else len(distance)]


'''
Function predit

Input : - df DataFrame
        - distance 
Output : df DataFrame predit

The function predicts the NANs from the notes of the closest users

'''

def predit_df(df, distance, k = 'all'):
    dfold = df.copy()
    dfnew = df.copy()
    for u in dfnew.index:
        ukkn = knn(u, distance)
        index = dfnew.loc[u, dfnew.loc[u].isna()].index
        if len(index) > 0:
            for p in index:
                datanotna = dfold[p][dfold[p].notna()]
                dfnew.loc[u, p] =  np.mean(datanotna[[j for j in ukkn if j in datanotna.index]][:k])
    return dfnew


def predit(df, distance):
    if isinstance(df, dict):
        return predit_dic(df,distance)
    elif isinstance(df, pd.DataFrame):
        return predit_df(df,distance)

def predit_dic(dico, distance):
    return dico