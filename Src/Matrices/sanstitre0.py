#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan  9 15:00:11 2019

@author: sid2018-1
"""
import pandas as pd
import numpy as np
from sklearn.preprocessing import scale

dtf= pd.read_csv("/home/sid2018-1/Documents/projet2019/data_v3/products_V4.csv", header=0, sep=";", nrows=int(1e5))