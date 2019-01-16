"""
Created on Tue Jan  8 10:45:59 2019

Group 2
@author: Alice A, Alexis D, Corentin L, Charlotte M, Audrey D
"""
# coding: utf-8

import pandas as pd

# %%


'''
Function groupby_product_date

Input : - csv rating file path
        - csv products file path
Output : Products/Dates Counts(Rating) Matrix for movies

The function counts the number of ratings per movies per dates :
    rows : products
    columns : dates
    values : counts(ratings)

Ex : df_test = groupby_product_date('C:/Users/alice/Documents/SID/S1/G2_
Projet/donnees/ratings_V3.csv','C:/Users/alice/Documents/SID/S1/G2_ Projet/
donnees/products_V3.csv', int(1e5))
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
Output : - dico_slow
         - dico_fast

The function, for each movie, recovers the date and the number of ratings given
for this date.
These numbers of ratings are splited between the slow variables and/or the
fast variables (thanks to the slow threshold and the fast threshold).
The function returns 2 dictionaries for the slow variables (dico_slow) and the
fast variables (dico_fast).

Ex : dico_slow, dico_fast = variable_speed(df_test, 3, 6)
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
