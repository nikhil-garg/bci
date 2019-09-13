#Author : Nikhil Garg
#  changelog:
#  13 September 2019 : Created

# To comment all the lines


import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 
bankdata = pd.read_csv("feature.csv")
X = bankdata.drop('class',axis = 1)
y = bankdata['class']
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size = 0.2)
from sklearn.preprocessing import StandardScaler  
scaler = StandardScaler()  
scaler.fit(X_train)

X_train = scaler.transform(X_train)  
X_test = scaler.transform(X_test)  

from sklearn.svm import SVC
svclassifier = SVC(kernel = 'linear')
svclassifier.fit(X_train, y_train)
y_pred = svclassifier.predict(X_test)
from sklearn.metrics import classification_report, confusion_matrix  
print(confusion_matrix(y_test,y_pred))  
print(classification_report(y_test,y_pred))  

from sklearn.model_selection import cross_val_score
scores = cross_val_score(svclassifier,X,y,cv = 4)
print(scores)
print("Accuracy: %0.2f (+/- %0.2f)" % (scores.mean(), scores.std() * 2))
