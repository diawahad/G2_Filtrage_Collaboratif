from tqdm import tqdm
import numpy as np
import pandas as pd

'''
Function recalculate

Input : - df DataFrame 
        - dfunbias Dtaframe with predict score 
Output : - Dataframe
the function returns a DataFrame containing the scores with the original scale  
'''

def recalculate(df, dfunbias):
    mean = lambda c : df[c][df[c].notna()].mean()
    std = lambda c: df[c][df[c].notna()].std(ddof = 0)

    for c in tqdm(dfunbias.columns, desc = 'Recalculate: Removing Bias' ):
        dfunbias[c] = round(dfunbias[c] * std(c) + mean(c)).astype(int)
    return dfunbias