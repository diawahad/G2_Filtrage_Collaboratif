import pandas as pd
import numpy as np
from scipy.spatial.distance import cosine
from sklearn.metrics.pairwise import cosine_similarity
from toMatrix import toMatrix

filepath_rating='/home/mickael/Documents/data_v3/ratings_V3.csv'
filepath_product='/home/mickael/Documents/data_v3/products_V3.csv'

df = toMatrix(filepath_rating, filepath_product)

print(df)

'''x = (1,5,6,9,7,5,6)
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

lists = [a, b, c, d]
print(lists)
df = pd.concat([pd.Series(x) for x in lists], axis=1)
df = df.transpose()

sim = cosine_similarity(df)
print(sim)

def cosinus_similarity(matrice):
    return(cosine_similarity(matrice.transpose()))
'''

