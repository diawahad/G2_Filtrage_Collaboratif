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

def  conversionNote(df,id_user,n,id_item):
    tqdm.pandas(desc = "Moyennes")
    M=df.progress_apply(axis=0,func= np.mean)
    tqdm.pandas(desc = "Ecarts types")
    E=df.progress_apply(axis=0,func= np.std)
    return int(n*E[id_item]+M[id_item])