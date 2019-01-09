from tqdm import tqdm
import numpy as np
import pandas as pd


def notes(df,id_user,n,id_item):
    tqdm.pandas(desc = "Moyennes")
    M=df.progress_apply(axis=0,func= np.mean)
    tqdm.pandas(desc = "Ecarts types")
    E=df.progress_apply(axis=0,func= np.std)
    return int(n*E[id_item]+M[id_item])