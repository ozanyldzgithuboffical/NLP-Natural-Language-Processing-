# -*- coding: utf-8 -*-
"""
Created on Thu Nov 21 16:47:04 2019

@author: ozanyildiz
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#Regular Expression Library
import re

#stop word library
import nltk
from nltk.stem.porter import PorterStemmer
down_status=nltk.download('stopwords')
from nltk.corpus import stopwords

#create object
ps=PorterStemmer()
#read restaturant comments csv file
comments=pd.read_csv('RestaurantReviews.csv')
commentsWithoutSign=[]
#Review columns first row and replace with sub=>substitute
for i in range(0,1000):
    comment=re.sub('[^a-zA-Z]',' ',comments['Review'][i])
    #make all letters to small
    comment=comment.lower()
    #tokenization
    comment=comment.split()
    commentsWithoutSign.append(comment)
    