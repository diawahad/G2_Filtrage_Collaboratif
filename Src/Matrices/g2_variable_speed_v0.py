"""
Created on Tue Jan  8 10:45:59 2019

@author: Group 2 !
"""
# coding: utf-8

import pandas as pd

# %%


'''
Function groupby_product_date

Input : - filepath_rating : csv rating file path
        - filepath_product : csv products file path
        - nrows : number of the rows of the file to read (default : 1e3)

Output : Products/Dates Counts(Rating) Matrix for movies

The function counts the number of ratings per movies per dates :
    rows : products
    columns : dates
    values : counts(ratings)
'''


def groupby_product_date(filepath_rating, filepath_product, nrows):
    df_rating = pd.read_csv(filepath_rating, header=0, sep=";", nrows=nrows)
    df_prod = pd.read_csv(filepath_product, header=0, sep=";")
    df_join = pd.merge(df_rating, df_prod)
    df_join = df_join.loc[df_join['subtype_id'] == 1.0]
    df_join = df_join.loc[:, ['product_id', 'rating', 'date_rating']]
    df_join = df_join.groupby(['product_id', 'date_rating']).count()
    df_join = df_join.unstack().iloc[:, :]
    df_join = df_join.fillna(0).astype(int)
    return df_join

# %%


'''
Function variable_speed

Input : - df : DataFrame of the previous function (groupby_product_date)
        - threshold_slow (integer)
        - threshold_fast (integer)

Output : - dico_slow : dictionary with the slow variables
         - dico_fast : dictionary with the fast variables

The function, for each movie, recovers the date and the number of ratings given
for this date.
These numbers of ratings are splited between the slow variables and/or the
fast variables (thanks to the slow threshold and the fast threshold).
The function returns 2 dictionaries for the slow variables (dico_slow) and the
fast variables (dico_fast).
'''


def variable_speed(df, threshold_slow, threshold_fast):
    dico_slow = {}
    dico_fast = {}
    for i in df.index:
        list_slow = []
        list_fast = []
        for j in df.columns:
            if df[j][i] <= threshold_slow:
                list_slow.append((j[1], df[j][i]))
            elif df[j][i] >= threshold_fast:
                list_fast.append((j[1], df[j][i]))
        if list_slow:
            dico_slow[i] = list_slow
        if list_fast:
            dico_fast[i] = list_fast
    return dico_slow, dico_fast
