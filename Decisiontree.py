import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, classification_report
from sklearn.preprocessing import LabelEncoder
data=pd.read_csv("C:/Users/Dell/Downloads/archive/loan_approval.csv")
data.head()
data.tail()
data.shape()
data.info
data.describe()
le=LabelEncoder()
for column in data.columns:
    if data[column].dtype=='object':
        data[column]=le.fit_transform(data[column])
x=data.drop("loan_approved",axis=1)
y=data["loan_approved"]
x_train,x_test,y_train,y_test=train_test_split(x,y,train_size=0.8,random_state=42)
model=DecisionTreeClassifier()
model.fit(x_train,y_train)
y_pred=model.predict(x_test)
print('Accuracy=',accuracy_score(y_test,y_pred))
print('Classification=',classification_report(y_test,y_pred))
