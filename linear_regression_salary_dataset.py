# -*- coding: utf-8 -*-
"""Linear Regression-Salary Dataset.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1x3EWzRwlJD8deWU5RtIz1-DgqWUApGvq
"""

import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

data=pd.read_csv("Salary_dataset.csv")

data.head()

data.describe()

data.info()

sns.heatmap(data.corr(),annot=True)

x=data["YearsExperience"]
y=data["Salary"]

"""from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=6)
"""

from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2)

x_train.shape,x_test.shape,y_train.shape,y_test.shape

x_train=np.array(x_train).reshape(-1,1)
x_test=np.array(x_test).reshape(-1,1)
y_train=np.array(y_train).reshape(-1,1)
y_test=np.array(y_test).reshape(-1,1)

from sklearn.linear_model import LinearRegression
lr=LinearRegression()
lr.fit(x_train,y_train)
print("Training Accuracy: ",lr.score(x_train,y_train))
print("Testing Accuracy: ",lr.score(x_test,y_test))

lr.intercept_

lr.coef_

y_pred=lr.predict(x_test)

x=float(input("Enter Year of Experience"))

y_prediction=lr.predict([[x]])
print("Salary According to my Model:",y_prediction)

