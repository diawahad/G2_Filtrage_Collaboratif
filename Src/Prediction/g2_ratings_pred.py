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
    dfunbiascopy = dfunbias.copy()
    for c in tqdm(dfunbiascopy.columns, desc = 'Recalculate: Removing Bias' ):
        dfunbiascopy[c] = round(dfunbiascopy[c] * std(c) + mean(c)).astype(int)
    return dfunbiascopy