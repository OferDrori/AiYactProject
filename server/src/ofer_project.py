# -*- coding: utf-8 -*-
"""ofer_project.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1HS28msuZDrH5vjMMEYFTgbNj51bft7zR
"""

import pandas as pd # tables
import numpy as np # math
import matplotlib.pyplot as plt #visualiztion
import seaborn as sns

df = pd.DataFrame(pd.read_excel('Choose river DataSet.xlsx'))
df = df.sample(frac=1)
len(df)

# sns.countplot(df['age:'],hue=df['choosen river'])
sns.countplot(df['years of expiriance:'],hue=df['choosen river'])

from sklearn.model_selection import train_test_split  
from sklearn import preprocessing

df.columns
X = df[['age:', 'years of expiriance:', 'how much cildren:', 'location:', 'sex ']]
y = df['choosen river']
X.columns

lb = preprocessing.LabelEncoder()
X['sex '] = lb.fit_transform(X['sex '])

lb = preprocessing.LabelEncoder()
X['location:'] = lb.fit_transform(X['location:'])

lb = preprocessing.LabelEncoder()
y = lb.fit_transform(y)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1)

from sklearn.tree import DecisionTreeClassifier 
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

models = [DecisionTreeClassifier,LogisticRegression,]
for model in models:
  model = model()
  model.fit(X_train,y_train)
  preds = model.predict(X_test)
  print(accuracy_score(y_test,preds))



res = pd.DataFrame()
res['real'] = y_test
res['predict'] = preds



accuracy_score(preds,y_test)

# age:	years of expiriance:	how much cildren:	location:	sex
arr = np.array([40,2,1,0,1])
model.predict(arr.reshape(1,-1))