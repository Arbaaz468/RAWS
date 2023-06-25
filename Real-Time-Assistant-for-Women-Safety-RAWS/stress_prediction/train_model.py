# -*- coding: utf-8 -*-
"""
Created on Fri Dec 24 15:01:14 2021

@author: amitr
"""

import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import joblib

#load data set
dataset = pd.read_csv(r'train_data_set.csv')

X = dataset.drop(['label','post_id','Text'], axis=1)
Y = dataset['label']

#Labeling the data
from sklearn.preprocessing import LabelEncoder
labelencoder = LabelEncoder()
X['subreddit'] = labelencoder.fit_transform(X['subreddit'])
#X['Text'] = labelencoder.fit_transform(X['Text'])

#standerize the data
from sklearn.preprocessing import StandardScaler
stsc = StandardScaler()
X = stsc.fit_transform(X)


#Training and testing data (divide the data into two part)
from sklearn.model_selection import train_test_split
X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.30,random_state=0)


#implement Linear regression
from sklearn.linear_model import LinearRegression
model = LinearRegression()
model.fit(X_train,Y_train)

Y_predict = model.predict(X_test)

Y_predict_new = []
for i in Y_predict:
    if i>=0.6:
        Y_predict_new.append(1)
    else:
        Y_predict_new.append(0)

#find accurecy score
from sklearn.metrics import accuracy_score
accuracy = accuracy_score(Y_test, Y_predict_new)

filename = 'train_model.sav'
joblib.dump(model,filename)