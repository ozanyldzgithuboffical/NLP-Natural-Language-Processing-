# -*- coding: utf-8 -*-
"""
Created on Thu Nov 21 16:47:04 2019

@author: ozanyildiz
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as pltç
#Regular Expression Library
import re

comments=pd.read_csv('RestaurantReviews.csv')
commentsWithoutSign=[]
#Review columns first row and replace with sub=>substitute
for i in range(0,1000):
    comment=re.sub('[^a-zA-Z]',' ',comments['Review'][i])
    commentsWithoutSign.append(comment)
    