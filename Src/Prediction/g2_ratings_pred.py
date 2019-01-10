from tqdm import tqdm
import numpy as np
import pandas as pd

'''
Function conversionNote

Input : - df: dataFrame user X item center and reduced
        - id_user
        - n: reduced center note
        - id_item
Output : corresponding note is non-centered and not reduced  in its entirety
'''

def conversion_note(df,id_user,n,id_item):
    tqdm.pandas(desc = "Moyennes")
    M=df.progress_apply(axis=0,func= np.mean)
    tqdm.pandas(desc = "Ecarts types")
    E=df.progress_apply(axis=0,func= np.std)
    return int(n*E[id_item]+M[id_item])


#### ------ WARNING ------- ####
####     DOES NOT WORK      ####
#### ------   ---   ------- ####
def conversion_df(df_pred,og_df):
    df_pred.reset_index()
    df_n = df_pred['index']
    tqdm.pandas(desc = 'ce que fait ma boucle')
    df_n = [ df_pred[c].progress_apply(lambda x: conversion_note(og_df,x.index,x[1:],c)) for c in df_pred.columns]
    print(df_n)
    return df_n