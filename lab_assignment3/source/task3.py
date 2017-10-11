import numpy as np
from sklearn import datasets, metrics
from sklearn.cross_validation import train_test_split
from sklearn import svm
from sklearn.datasets import load_boston
from sklearn import preprocessing

boston= load_boston()
x = boston.data
y = boston.target

# 随机挑选  
train_x_disorder,test_x_disorder,train_y_disorder,test_y_disorder=train_test_split(x,y,train_size=0.8,random_state=33)
#数据标准化  
ss_x=preprocessing.StandardScaler()
train_x_disorder=ss_x.fit_transform(train_x_disorder)
test_x_disorder=ss_x.transform(test_x_disorder)
ss_y=preprocessing.StandardScaler()
train_y_disorder=ss_y.fit_transform(train_y_disorder.reshape(-1,1))
test_y_disorder=ss_y.transform(test_y_disorder.reshape(-1,1))


clf = svm.SVR(kernel='linear')
clf.fit(train_x_disorder, train_y_disorder)

y_pred=clf.predict(test_x_disorder)

print("accuracy of linear kernel is:")
print(metrics.accuracy_score(test_y_disorder,y_pred))

newclf = svm.SVR(kernel='rbf')
newclf.fit(train_x_disorder, train_y_disorder)

y_pred_new=newclf.predict(test_x_disorder)

print("accuracy of RBF kernel is:")
print(metrics.accuracy_score(test_y_disorder,y_pred_new))