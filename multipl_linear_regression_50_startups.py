# -*- coding: utf-8 -*-
"""Multipl Linear Regression-50_Startups.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1RYu5SG8rJsTd3ND_dm_Jp2vua_2aKbYB
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

data=pd.read_csv("50_Startups.csv")

data.head(10)

data.drop(["State"],axis=1,inplace=True)

data.head()

corr=data.corr()

sns.heatmap(corr,annot=True)

x=data.drop(["Profit"],axis=1)

y=data["Profit"]

from sklearn.preprocessing import StandardScaler
sc=StandardScaler()

x=sc.fit_transform(x)
x

from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=32)

from sklearn.linear_model import LinearRegression
lr=LinearRegression()
lr.fit(x_train,y_train)

print("Training Accuracy: ",lr.score(x_train,y_train))
print("Testing Accuracy: ",lr.score(x_test,y_test))

y_pred=lr.predict(x_test)

calculation = pd.DataFrame(np.c_[y_test,y_pred], columns = ["Original Salary","PredictSalary"])
calculation.head(5)

print(lr.coef_)

print(lr.intercept_)

feature = [165349.20,136897.80,471784.10]
scale_feature = sc.transform([feature])
scale_feature

y_predict=lr.predict(scale_feature)
y_predict