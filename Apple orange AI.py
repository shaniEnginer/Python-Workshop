# this is an ML program which is used for predication that given data related to what fruit
from sklearn import tree
# 1 stands for smooth
#  0 stands for bumpy
features=[[170 , 0],[150 , 0],[130 , 1],[172 ,1] ]
lables=[0 , 0 , 1 , 1]
#  Think of the decision tree is An functions
slc=tree.DecisionTreeClassifier() # 1
# fit find pattren In Data
slc=slc.fit(features , lables) # 2
predic= slc.predict([[100 , 1]]) # 3
print(predic)

