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

def kkn(id_user, distance, k = "all"):
    return distance[id_user].sort_values().index[1: int(k)+1 if  k != "all" else len(distance)]


'''
Function predit

Input : - df DataFrame
        - distance 
Output : df DataFrame predit

The function predicts the NANs from the notes of the closest users

'''

def predit(df, distance):
    user = df.index
    dfold = df.copy()
    dfnew = df.copy()
    for u in user:
        ukkn = kkn(u, distance)
        for uv in ukkn:
            index = dfnew.loc[u, dfnew.loc[u].isna()].index
            if len(index) == 0:
                break
            else:
                dfnew.loc[u, index] = dfold.loc[uv, index]
    return dfnew
