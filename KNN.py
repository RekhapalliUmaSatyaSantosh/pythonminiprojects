import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, classification_report
from sklearn.preprocessing import LabelEncoder,StandardScaler
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
scaler=StandardScaler()
x=scaler.fit_transform(x)
x_train,x_test,y_train,y_test=train_test_split(x,y,train_size=0.8,random_state=42)
model=KNeighborsClassifier(n_neighbors=5)
model.fit(x_train,y_train)
y_pred=model.predict(x_test)
print('Accuracy=',accuracy_score(y_test,y_pred))
print('Classification=',classification_report(y_test,y_pred))
