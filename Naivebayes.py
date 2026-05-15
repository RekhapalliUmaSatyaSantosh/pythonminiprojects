import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score, classification_report
from sklearn.preprocessing import LabelEncoder
data=pd.read_csv(r"C:\Users\Dell\Downloads\archive (1)\work_from_home_burnout_dataset.csv")
data.head()
data.tail()
data.shape
data.info
data.describe()
le=LabelEncoder()
for column in data.columns:
    if data[column].dtype=='object':
        data[column]=le.fit_transform(data[column])
x=data.drop("day_type",axis=1)
y=data["day_type"]
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.3)
gnb=GaussianNB()
y_pred=gnb.fit(x_train,y_train).predict(x_test)
print('Accuracy=',accuracy_score(y_test,y_pred))
print('Classification=',classification_report(y_test,y_pred))
