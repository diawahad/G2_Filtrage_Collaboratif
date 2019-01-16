# !/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 10 09:25:47 2019

@author: Alexis D.
"""

import sys

from g2_to_matrix import to_matrix, to_dict
from g2_similarity_user_user import similarity_user_user_mat
from g2_similarity_user_user import similarity_user_user_dic
from predict_nan import predit

sys.path.append("../Prediction")


def item_item(filepath_ratings, filepath_products, k=1, t='matrix',
              t_user='user'):
    m_item_item = to_matrix(filepath_ratings, filepath_products, t_user)
    if t == 'matrix':
        df_item_item = similarity_user_user_mat(m_item_item)
    else:
        d_item_item = to_dict(filepath_ratings, filepath_products, t_user)
        df_item_item = similarity_user_user_dic(d_item_item)
    df_knn = predit(m_item_item, df_item_item)
    return df_knn
