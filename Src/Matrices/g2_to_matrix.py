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

Input : - filepath_rating : csv rating file path
        - filepath_product : csv products file path
        - variable : to choose between the matrix user/product or product/user
        (default : 'user')
        - modality (float) : - Movie : 1.0 (default : 1.0)
                             - Book : 2.0
                             - Serie : 4.0
        - rating_rows : number of the rows of the file rating to read
        (default : 1e3)
        - prod_rows : number of the rows of the file product to read
        (default : 1e5)

Output : User/Products Rating Matrix

The function transforms the ratings and the products files to a matrix :
    rows : users
    columns : products
    values : ratings
'''


def to_matrix(filepath_rating, filepath_product, variable='user',
              modality=1.0, rating_rows=1e3, prod_rows=1e5):
    if isinstance(rating_rows, int) or isinstance(rating_rows, float):
        df_rating = pd.read_csv(filepath_rating, header=0, sep=";",
                                nrows=int(rating_rows))
    else:
        df_rating = pd.read_csv(filepath_rating, header=0, sep=";")
    if isinstance(prod_rows, int) or isinstance(prod_rows, float):
        df_prod = pd.read_csv(filepath_product, header=0, sep=";",
                              nrows=int(1e5))
    else:
        df_prod = pd.read_csv(filepath_product, header=0, sep=";")

    if (isinstance(modality, int) or isinstance(modality, float)):
        df_prod = df_prod.loc[df_prod['subtype_id'] == modality]

    df_join = pd.merge(df_rating, df_prod, on='product_id')
    df_join = df_join.loc[:, ['rating_id', 'user_id', 'product_id', 'rating',
                              'date_rating', 'subtype_id']]

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

Input : - filepath_rating : csv rating file path
        - filepath_product : csv products file path
        - variable : to choose between the matrix user/product or product/user
        (default : 'user')
        - modality (float) : - Movie : 1.0 (default : 1.0)
                             - Book : 2.0
                             - Serie : 4.0
        - rating_rows : number of the rows of the file rating to read
        (default : 1e3)
        - prod_rows : number of the rows of the file product to read
        (default : 1e5)

Output : User/Products Rating dictionary

The function transforms the ratings and the products files to a dictionary :
    key : users
    values : set of (products,rate) tuples
'''


def to_dict(filepath_rating, filepath_product, variable='user',
            modality=1.0, rating_rows=1e3, prod_rows=1e5):
    if isinstance(rating_rows, int) or isinstance(rating_rows, float):
        df_rating = pd.read_csv(filepath_rating, header=0, sep=";",
                                nrows=int(rating_rows))
    else:
        df_rating = pd.read_csv(filepath_rating, header=0, sep=";")
    if isinstance(prod_rows, int) or isinstance(prod_rows, float):
        df_prod = pd.read_csv(filepath_product, header=0, sep=";",
                              nrows=int(1e5))
    else:
        df_prod = pd.read_csv(filepath_product, header=0, sep=";")

    if (isinstance(modality, int) or isinstance(modality, float)):
        df_prod = df_prod.loc[df_prod['subtype_id'] == modality]

    df_join = pd.merge(df_rating, df_prod, on='product_id')
    df_join = df_join.loc[:, ['rating_id', 'user_id', 'product_id', 'rating',
                              'date_rating', 'subtype_id']]
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
<<<<<<< HEAD
Function to_2d

Input : - csv rating file path
        - csv products file path

Output : User/Products Rating dictionary for movies

The function transforms the ratings and the products files to a dictionary :
    key : users
    values : set of (products,rate) tuples
'''


<<<<<<< HEAD
def to_2d(filepath_rating, filepath_product):
    df_rating = pd.read_csv(filepath_rating, header=0, sep=";", nrows=int(1e3))
    df_prod = pd.read_csv(filepath_product, header=0, sep=";", nrows=int(1e5))
    df_join = pd.merge(df_rating, df_prod, on='product_id')
=======
def to_2d(filepath_rating, filepath_product, modality=1.0, rating_rows = 1e3, prod_rows = 1e5):
    if isinstance(rating_rows,int) or isinstance(rating_rows,float):
        df_rating = pd.read_csv(filepath_rating, header=0, sep=";", nrows=int(rating_rows))
    else:
        df_rating = pd.read_csv(filepath_rating, header=0, sep=";")
    
    if isinstance(prod_rows,int) or isinstance(prod_rows,float):
        df_prod = pd.read_csv(filepath_product, header=0, sep=";", nrows=int(prod_rows))
    else:
        df_prod = pd.read_csv(filepath_product, header=0, sep=";")
    
    if (isinstance(modality,int) or isinstance(modality,float)):
        df_prod = df_prod.loc[df_prod['subtype_id'] == modality]
    
    df_join = pd.merge(df_rating, df_prod, on='prodcut_id')
>>>>>>> master
    df_join = df_join.loc[:, ['rating_id', 'user_id', 'product_id', 'rating',
                              'date_rating', 'subtype_id']]
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
=======
>>>>>>> master
Function unbias

Input : - df : DataFrame to be unbiased
        - axis : 0 by default, if any other value Transposes the dataframe
        to unbias by user instead of items
        - mean : False by default, replaces missing values with 5.5 which is
        the median value in the Sens Critique rating system
        - to_df : to choose between a dictionary or a DataFrame
        (default : False)

Output: Unbiased matrix

The function centers and reduces the given dataframe, item by item.
Ignores missing values.
'''


def unbias(df, axis=0, mean=False, to_df=False):
    try:
        if axis == 0:
            df = df.T
        elif axis != 1:
            raise Exception('axis',
                            'Axis has only two possible values 0 and 1')
        if mean:
            df = df.fillna(5.5)
        if to_df:
            df = df.apply(lambda x: (x-x.mean())/np.sqrt(
                    x.var()) if np.sqrt(x.var()) > 0.00001 else (
                            x-x.mean())/0.00001)
            return df.T
        dico = {}
        columns = df.columns
        for col in columns:
            index = df[col][df[col].notna()].index
            dico[col] = set(zip(index, scale(df[col][index])))
        return dico
    except Exception as ex:
        print(ex)

# %%


'''
Function list_genre

Input : - filepath_rating : csv rating file path

Ouput : List with all the categories of movies

The function returns a list that include all the differents categories of
products.
'''


def list_genre(filepath_product, modality=1.0, prod_rows=1e5):
    df_product = pd.read_csv(filepath_product, header=0, sep=";",
                             nrows=int(prod_rows))
    df_product = df_product.loc[df_product['subtype_id'] == modality]
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

Input : - filepath_product : csv product file path
        - modality (float) : - Movie : 1.0 (default : 1.0)
                             - Book : 2.0
                             - Serie : 4.0
        - prod_rows : number of the rows of the file product to read
        (default : 1e5)

Ouput : DataFrame object group by the attribute

The function return a matrix moviesXcategories. When a movie belongs to a
certain categorie, we put the value 1 in the related slot instead of a 0.
'''


def categories_movies(filepath_product, modality=1.0, prod_rows=1e5):
    if isinstance(prod_rows, int) or isinstance(prod_rows, float):
        df_prod = pd.read_csv(filepath_product, header=0, sep=";",
                              nrows=int(prod_rows))
    else:
        df_prod = pd.read_csv(filepath_product, header=0, sep=";")

    s = df_prod[df_prod['subtype_id'] == modality]
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


# %%

'''
Function most_rated_items

Input : - filepath_rating : csv rating file path
        - filepath_product : csv product file path
        - modality (float) : - Movie : 1.0 (default)
                             - Book : 2.0
                             - Serie : 4.0
        - rating_rows : number of the rows of the file rating to read
        (default : 1e3)
        - prod_rows : number of the rows of the file product to read
        (default : 1e5)

Ouput : DataFrame with product_id, subtype_id(modality), rating_count

The function returns a DataFrame with the number of ratings and the subtype of
the k first most rated products.
'''


def most_rated_items(filepath_rating, filepath_product, modality=1.0,
                     rating_rows=1e3, prod_rows=1e5):
    if isinstance(rating_rows, int) or isinstance(rating_rows, float):
        df_rating = pd.read_csv(filepath_rating, header=0, sep=";",
                                nrows=int(rating_rows))
    else:
        df_rating = pd.read_csv(filepath_rating, header=0, sep=";")

    if isinstance(prod_rows, int) or isinstance(prod_rows, float):
        df_prod = pd.read_csv(filepath_product, header=0, sep=";",
                              nrows=int(prod_rows))
    else:
        df_prod = pd.read_csv(filepath_product, header=0, sep=";")

    if (isinstance(modality, int) or isinstance(modality, float)):
        df_prod = df_prod.loc[df_prod['subtype_id'] == modality]

    df_join = pd.merge(df_rating, df_prod)
    df_join = df_join.loc[:, ['product_id', 'rating', 'subtype_id']]
    df_join = df_join.groupby(['product_id', 'subtype_id'],
                              as_index=False)['rating'].count()
    df_join = df_join.rename(columns={"rating": "rating_count"})
    df_join = df_join.sort_values(by='rating_count', ascending=False)
    return df_join


# %%

'''
Function ratings_categories_movies

Input : - filepath_rating : csv rating file path
        - filepath_product : csv product file path
        - modality (float) : - Movie : 1.0 (default)
                             - Book : 2.0
                             - Serie : 4.0
        - rating_rows : number of the rows of the file rating to read
        (default : 1e3)
        - prod_rows : number of the rows of the file product to read
        (default : 1e5)

Ouput : DataFrame with user_id, product_id, rating, categories

The function returns a DataFrame with the rating of an user for a product
describes by its categories.
'''


def ratings_categories_movies(filepath_rating, filepath_product, modality=1.0,
                              rating_rows=1e3, prod_rows=1e5):
    if isinstance(rating_rows, int) or isinstance(rating_rows, float):
        df_rating = pd.read_csv(filepath_rating, header=0, sep=";",
                                nrows=int(rating_rows))
    else:
        df_rating = pd.read_csv(filepath_rating, header=0, sep=";")

    df_fpg = categories_movies(filepath_product, modality, prod_rows)
    df_rating = df_rating.loc[:, ['user_id', 'product_id', 'rating']]
    df_merge = pd.merge(df_rating, df_fpg, on='product_id', how='inner')
    return df_merge


# %%

'''
Function rating_categories

Input : - filepath_rating : csv rating file path
        - filepath_product : csv product file path
        - modality (float) : - Movie : 1.0 (default)
                             - Book : 2.0
                             - Serie : 4.0
        - rating_rows : number of the rows of the file rating to read
        (default : 1e3)
        - prod_rows : number of the rows of the file product to read
        (default : 1e5)

Ouput : DataFrame User/Product/Rating/Categories

The function returns a DataFrame . When a products belongs to a
certain categorie, we put the corresponding rating in the related slot instead
of a 1.
'''


def rating_categories(filepath_rating, filepath_product, modality=1.0,
                      rating_rows=1e3, prod_rows=1e5):
    df_fpg = ratings_categories_movies(filepath_rating, filepath_product,
                                       modality, rating_rows, prod_rows)
    genres = list(df_fpg.columns.values[3:42])
    for i in df_fpg.index:
        for j in genres:
            if df_fpg[j][i] == 1.0:
                df_fpg[j][i] = df_fpg['rating'][i]
    return df_fpg


# %%

'''
Function mean_ratings_categories

Input : - filepath_rating : csv rating file path
        - filepath_product : csv product file path
        - modality (float) : - Movie : 1.0 (default)
                             - Book : 2.0
                             - Serie : 4.0

Ouput : DataFrame with the mean rating given by an user for each categories

The function returns a DataFrame with the mean rating of an user for the
each categories.
'''


def mean_rating_categories(filepath_rating, filepath_product, modality=1.0):
    df_fpg = rating_categories(filepath_rating, filepath_product, modality)
    df_fpg[df_fpg == 0.0] = np.nan
    df_fpg = df_fpg.groupby(['user_id']).mean()
    df_fpg = df_fpg.drop(columns=['product_id', 'rating'])
    return df_fpg
