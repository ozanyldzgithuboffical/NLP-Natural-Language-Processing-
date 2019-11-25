# -*- coding: utf-8 -*-
"""
Created on Thu Nov 21 16:47:04 2019

@author: ozanyildiz
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#Used  to create test amd train data
from sklearn.model_selection import train_test_split
#naive bayes
from sklearn.naive_bayes import GaussianNB
#confusion matrix
from sklearn.metrics import confusion_matrix
#Regular Expression Library
import re

#stop word library
import nltk
from nltk.stem.porter import PorterStemmer
down_status=nltk.download('stopwords')
from nltk.corpus import stopwords

#feature extraction
from sklearn.feature_extraction.text import CountVectorizer

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
    #find word stem if it is not a stop word
    comment=[ps.stem(word) for word in comment if not word in set(stopwords.words('english'))]
    #convert comment word list to string
    comment=' '.join(comment)
    commentsWithoutSign.append(comment)
    
 #count vectorizer   
cv=CountVectorizer(max_features=2000)
#X =>independent variable
X=cv.fit_transform(commentsWithoutSign).toarray()
#Y=>dependent variable
Y=comments.iloc[:,1].values

#split the data to test & train
X_Train,Y_Train,X_Test,Y_Test=train_test_split(X,Y,test_size=0.25,random_state=0)
gnbayes=GaussianNB()
gnbayes.fit(X_Train,Y_Train)
Y_Predict=gnbayes.predict(X_Test)

#compare between Y_Test and Predicted Y
cm=confusion_matrix(Y_Test,Y_Predict)
print(cm)


