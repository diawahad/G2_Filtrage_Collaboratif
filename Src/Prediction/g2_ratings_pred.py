from tqdm import tqdm, tqdm_notebook
import numpy as np
import pandas as pd

# %%

'''
Function recalculate

Input : - df : DataFrame
        - dfunbias : Unbias Dataframe
        - jpnb : if you execute the function with Jupyter (Default : "False")

Output : - Rebias DataFrame

The function rebias an unbias Dataframe.
'''


def recalculate(df, dfunbias, jpnb=False):
    mean = (lambda c: df[c][df[c].notna()].mean())
    std = (lambda c: df[c][df[c].notna()].std(ddof=0))
    dfunbias = dfunbias.apply(lambda x: x.fillna(x.median()))
    if jpnb:
        try:
            for c in tqdm_notebook(dfunbias.columns,
                                   desc='Recalculate: Removing Bias'):
                dfunbias[c] = round(dfunbias[c] * std(c) + mean(c)).astype(int)
        except ValueError:
            print(dfunbias[c])
    else:
        try:
            for c in tqdm(dfunbias.columns,
                          desc='Recalculate: Removing Bias'):
                dfunbias[c] = round(dfunbias[c] * std(c) + mean(c)).astype(int)
        except ValueError:
            print(dfunbias[c])
    return dfunbias
