"""
Created on Mon Jan  7 15:33:15 2019

@author: Group 2 !

"""
# coding: utf-8


import pandas as pd
import numpy as np
from tqdm import tqdm
from sklearn.preprocessing import scale


# %%

'''
Function to_matrix

Input : - csv rating file path
        - csv products file path

Output : User/Products Rating Matrix for movies

The function transforms the ratings and the products files to a matrix :
    rows : users
    columns : products
    values : ratings
'''


def to_matrix(filepath_rating, filepath_product, variable='user',rating_rows = 1e3, prod_rows = 1e5):
    if isinstance(rating_rows,int) or isinstance(rating_rows,float):
        df_rating = pd.read_csv(filepath_rating, header=0, sep=";", nrows=int(rating_rows))
    else:
        df_rating = pd.read_csv(filepath_rating, header=0, sep=";")
    if isinstance(prod_rows,int) or isinstance(prod_rows,float):
        df_prod = pd.read_csv(filepath_product, header=0, sep=";", nrows=int(1e5))
    else:
        df_prod = pd.read_csv(filepath_product, header=0, sep=";")
    df_join = pd.merge(df_rating, df_prod, on='product_id')
    df_join = df_join.loc[:, ['rating_id', 'user_id', 'product_id', 'rating',
                              'date_rating', 'subtype_id']]
    df_join = df_join.loc[df_join['subtype_id'] == 1.0]
    if variable == 'user':
        df_join = df_join.pivot(index='user_id', columns='product_id',
                                values='rating')
    else:
        df_join = df_join.pivot(index='product_id', columns='user_id',
                                values='rating')
    return df_join


# %%

'''
Function to_dict

Input : - csv rating file path
        - csv products file path

Output : User/Products Rating dictionary for movies

The function transforms the ratings and the products files to a dictionary :
    key : users
    values : set of (products,rate) tuples
'''


def to_dict(filepath_rating, filepath_product, variable='user', rating_rows = 1e3, prod_rows = 1e5):
    if isinstance(rating_rows,int) or isinstance(rating_rows,float):
        df_rating = pd.read_csv(filepath_rating, header=0, sep=";", nrows=int(rating_rows))
    else:
        df_rating = pd.read_csv(filepath_rating, header=0, sep=";")
    if isinstance(prod_rows,int) or isinstance(prod_rows,float):
        df_prod = pd.read_csv(filepath_product, header=0, sep=";", nrows=int(1e5))
    else:
        df_prod = pd.read_csv(filepath_product, header=0, sep=";")
    df_join = pd.merge(df_rating, df_prod, on='product_id')
    df_join = df_join.loc[:, ['rating_id', 'user_id', 'product_id', 'rating',
                              'date_rating', 'subtype_id']]
    df_join = df_join.loc[df_join['subtype_id'] == 1.0]
    if variable == 'user':
        df_join = df_join.pivot(index='user_id', columns='product_id',
                                values='rating')
    else:
        df_join = df_join.pivot(index='product_id', columns='user_id',
                                values='rating')
    d_users_rates = {}
    for i in df_join.index:
        s_users = set()
        for j in df_join.columns:
            if not np.isnan(df_join[j][i]):
                s_users.add((j, int(df_join[j][i])))
        d_users_rates[i] = s_users
    return d_users_rates


# %%

'''
Function to_2d

Input : - csv rating file path
        - csv products file path

Output : User/Products Rating dictionary for movies

The function transforms the ratings and the products files to a dictionary :
    key : users
    values : set of (products,rate) tuples
'''


def to_2d(filepath_rating, filepath_product):
    df_rating = pd.read_csv(filepath_rating, header=0, sep=";", nrows=int(1e3))
    df_prod = pd.read_csv(filepath_product, header=0, sep=";", nrows=int(1e5))
    df_join = pd.merge(df_rating, df_prod, on='product_id')
    df_join = df_join.loc[:, ['rating_id', 'user_id', 'product_id', 'rating',
                              'date_rating', 'subtype_id']]
    df_join = df_join.loc[df_join['subtype_id'] == 1.0]
    df_join = df_join.pivot(index='user_id', columns='product_id',
                            values='rating')
    d_users_rates = {}
    for i in df_join.index:
        s_users = list()
        for j in df_join.columns:
            if not np.isnan(df_join[j][i]):
                s_users.append((j, int(df_join[j][i])))
        d_users_rates[i] = s_users
    return d_users_rates


# %%

'''
Function unbias

Input :
    df - DataFrame to be unbiased
    axis - 0 by default, if any other value Transposes the dataframe
        to unbias by user instead of items
    mean - False by default, replaces missing values with 5.5 which is
        the median value in the Sens Critique rating system

Output: Unbiased matrix

The function centers and reduces the given dataframe, item by item
Ignores missing  values
'''


def unbias(df, axis=0, mean=False):
    try:
        if axis == 0:
            df = df.T
        elif axis != 0:
            raise Exception('axis',
                            'Axis has only two possible values 0 and 1')
        if mean:
            df = df.fillna(5.5)
        columns = df.columns
        dico = {}
        for col in columns:
            index = df[col][df[col].notna()].index
            dico[col] = set(zip(index, scale(df[col][index])))
        return dico
    except Exception as ex:
        print(ex)


# %%

'''
Function list_genre

Input :
    filepath_rating : csv rating file path

Ouput :
    List with all the categories of movies

The function return a list that includes all the differents categories of
movies.
'''


def list_genre(filepath_product):
    df_product = pd.read_csv(filepath_product, header=0, sep=";")
    df_product = df_product.loc[df_product['subtype_id'] == 1.0]
    list_genres = []
    for i in df_product['genres']:
        if (type(i) == str):
            r = i.split(',')
            for j in r:
                if j not in list_genres:
                    list_genres.append(j)
    list_genres.sort()
    return list_genres


# %%

'''
Function categories_of_movies

Input :
    filepath_rating : csv rating file path

Ouput :
    DataFrame object group by the attribute

The function return a matrix moviesXcategories. When a movie belongs to a
certain categorie, we put the value 1 in the related slot instead of a 0.
'''


def categories_movies(filepath_product):
    df_prod = pd.read_csv(filepath_product, header=0, sep=";")
    s = df_prod[df_prod['subtype_id'] == 1.0]
    v = s['genres']
    indice = s['product_id'].values
    ind = [int(i) for i in indice]

    list_categories = list_genre(filepath_product)
    mat_c = np.zeros((len(v), len(list_categories)))
    for i in tqdm(range(len(v))):
        for j in range(len(list_categories)):
            if (str(v[i]) in str(list_categories[j])):
                mat_c[i][j] += 1

    df = pd.DataFrame(mat_c, index=ind, columns=list_categories)
    df.insert(0, 'product_id', df.index)
    df = df.set_index(np.arange(0, len(df.index)))

    return df


# categories_of_movies(
#        "/home/ddm-turing3/Bureau/SensCritique/data_v3/products_V4.csv")

# %%

'''
Function most_rated_movies

Input :
    filepath_rating : csv rating file path
    filepath_product : csv product file path
    modalite (float) : - Movie : 1.0
                       - Book : 2.0
                       - Serie : 4.0
    k (integer) : The k first rows of the DataFrame (Ex : 100)

Ouput :
    DataFrame with product_id, subtype_id(modality), rating_count

The function return a DataFrame with the number of ratings and the subtype of
the k first most rated products.
'''


def most_rated_movies(filepath_rating, filepath_product, modalite, k):
    df_rating = pd.read_csv(filepath_rating, header=0, sep=";", nrows=int(1e5))
    df_prod = pd.read_csv(filepath_product, header=0, sep=";")

    df_join = pd.merge(df_rating, df_prod)
    df_join = df_join.loc[:, ['product_id', 'rating', 'subtype_id']]
    df_join = df_join.groupby(['product_id', 'subtype_id'],
                              as_index=False)['rating'].count()
    df_join = df_join.rename(columns={"rating": "rating_count"})
    df_join = df_join.sort_values(by='rating_count', ascending=False)

# FPN = to_FPN("/home/ddm-turing3/Bureau/SensCritique/data_v3/ratings_V3.csv",
#             "/home/ddm-turing3/Bureau/SensCritique/data_v3/products_V4.csv",
#             100)
# FPN = df_join.head(k)

# %%
# Juste Vrai Bon Exact Correct Valide


def to_merge_FPN(filepath_rating, FPN, modalite):
    df_rating = pd.read_csv(filepath_rating, header=0, sep=";", nrows=int(1e5))
    df_merge = pd.merge(df_rating, FPN, on='product_id', how='left')
    df_merge = df_merge.loc[df_merge['subtype_id'] == modalite]
    df_merge = df_merge.loc[:, ['product_id', 'rating_count', 'subtype_id']]
    df_merge = df_merge.rename(columns={"subtype_id": "modality"})
    df_merge = df_merge.groupby(['product_id', 'modality'],
                                as_index=False)['rating_count'].count()
    df_merge = df_merge.sort_values(by='rating_count', ascending=False)
    return df_merge


# to_merge_FPN("/home/ddm-turing3/Bureau/SensCritique/data_v3/ratings_V3.csv",
#             FPN, 1.0)

'''
Function ratings_categories_movies

Input :
    filepath_rating : csv rating file path
    filepath_product : csv product file path

Ouput :
    DataFrame with user_id, product_id, rating, categories

The function return a DataFrame with the rating of an user for a movie
describes by its categories.
'''


def ratings_categories_movies(filepath_rating, filepath_product):
    df_rating = pd.read_csv(filepath_rating, header=0, sep=";", nrows=int(1e3))
    df_fpg = categories_movies(filepath_product)
    df_rating = df_rating.loc[:, ['user_id', 'product_id', 'rating']]
    df_merge = pd.merge(df_rating, df_fpg, on='product_id', how='inner')
    return df_merge


# to_merge_FPG("/home/ddm-turing3/Bureau/SensCritique/data_v3/ratings_V3.csv",
#             "/home/ddm-turing3/Bureau/SensCritique/data_v3/products_V4.csv")

# %%

'''
Function note_film_genre

Input :
    filepath_rating : csv rating file path
    filepath_product : csv product file path

Ouput :
    DataFrame object group by the gender

The function return a matrix moviesXcategories. When a movie belongs to a
certain categorie, we put the corresponding rating in the related slot instead 
of a 1.
'''
    
def note_film_genre(filepath_rating, filepath_product):
    df_fpg = ratings_categories_movies(filepath_rating, filepath_product)
    genres = list(df_fpg.columns.values[3:42])
    for i in df_fpg.index:
        for j in genres:
            if df_fpg[j][i]==1.0:
                df_fpg[j][i]=df_fpg['rating'][i]
    return df_fpg


'''
Function moy_note_film_genre

Input :
    filepath_rating : csv rating file path
    filepath_product : csv product file path

Ouput :
    DataFrame with the mean rating for all the movies genders

The function return a DataFrame with the mean rating of an user for the 
corresponding gender.
'''

def moy_note_film_genre(filepath_rating, filepath_product):
    df_fpg = note_film_genre(filepath_rating, filepath_product)
    df_fpg[df_fpg==0.0] = np.nan
    df_fpg = df_fpg.groupby(['user_id']).mean()
    df_fpg = df_fpg.drop(columns=['product_id', 'rating'])
    df_fpg = df_fpg.fillna(0.0)
    return df_fpg

# df_fpg.to_csv("C:/Users/chach/OneDrive/Documents/SID/M1/Projet/filmpargenre.csv")
