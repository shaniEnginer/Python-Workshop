# %matplotlib inline
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
# plt.plot([2,34,45,3], [34,56,57,67])
# plt.show()
from sklearn.tree import     DecisionTreeClassifier 
data = pd.read_csv("train.csv").as_matrix() # Converting this to The matrices Of pexiels  
# print(data)
clf=  DecisionTreeClassifier()
#  Spliting the data for traning 
x_train = data[0:21000, 1:] # spliting the data 
label = data[0:21000, 0]
#  Classifier Function
clf.fit(x_train, label)
# Testing data sets ls
x_test = data[21000:, 1:]
actual_label = data[21000:, 0]
d = x_test[]
d.shape=(28, 28)
plt.imshow(225 - d, cmap='gray')
print(clf.predict([x_test[8]]))
plt.show()