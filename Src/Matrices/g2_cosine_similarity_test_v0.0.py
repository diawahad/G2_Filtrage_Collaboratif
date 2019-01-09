import pandas as pd
import numpy as np
from scipy.spatial.distance import cosine
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.preprocessing import scale
from g2_to_matrix import to_matrix
from g2_to_matrix import unbias
from g2_to_matrix import to_dict

filepath_rating='/home/mickael/Documents/data_v3/ratings_V3.csv'
filepath_product='/home/mickael/Documents/data_v3/products_V3.csv'

def cosinus_similarity(matrice):
    matrice = to_matrix(filepath_rating, filepath_product)
    matrice = unbias(matrice, axis = 1, mean = True)
    return(cosine_similarity(matrice))


'''
df.fillna(value=5.5, inplace=True)
sim = cosine_similarity(df)
print(sim)
'''

'''
a = np.array([6,3,8,float("NaN"),6,4,3,5])
b = np.array([float("NaN"),7,9,2,5,9,5,7])
df = pd.concat([pd.Series(x) for x in [a,b]], axis=1)
'''

def calculcosin (u,v):
    df0 = pd.concat([pd.Series(x) for x in [u,v]], axis=1)
    df1 = df0.dropna()
    return(cosine(df1[0].values , df1[1].values))

def similarity_user_user(matrice_centree):
    df = matrice_centree
    variables = df.index
    size = df.shape[0]
    mat = np.zeros((size,size))
    for i,v in enumerate (variables):
        for j,k in enumerate (variables):
            mat[i,j] = calculcosin(df.transpose()[v].values, df.transpose()[k].values)
    return (pd.DataFrame(mat,index=df.index,columns=df.index))

print(similarity_user_user(df))

'''
x = (1,5,6,9,7,5,6)
y = (5,8,6,9,7,2,3)
z = (6,8,7,4,2,3,4)
a = (8,7,5,3,1,5,6)

a = np.array([6,3,8,5,6,4,3,5])
b = np.array([4,7,9,2,5,9,5,7])
c = np.array([6,8,7,4,2,3,4,8])
d = np.array([8,7,5,3,1,5,6,5])

x = np.random.rand(1,8)
y = np.random.rand(1,8)
z = np.random.rand(1,8)
a = np.random.rand(1,8)
'''

'''lists = [a, b, c, d]
print(lists)
df = pd.concat([pd.Series(x) for x in lists], axis=1)
df = df.transpose()'''
