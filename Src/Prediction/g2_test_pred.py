'''
This is a test file to showcase the prediction  feature of our app
'''

import sys
sys.path.append("./Src/Matrices")
from g2_to_matrix import to_matrix, unbias 
from g2_predict_nan import predit
from g2_ratings_pred import conversion_df

ratings_path = '../data_v3/ratings_vv3.csv'
products_path = '../data_v3/productsv3.csv'

grades = to_matrix(ratings_path,products_path)
un_grades = unbias(grades)
dist = ...
un_new = predit(un_grades,dist)
grades_new = conversion_df(un_new,grades)