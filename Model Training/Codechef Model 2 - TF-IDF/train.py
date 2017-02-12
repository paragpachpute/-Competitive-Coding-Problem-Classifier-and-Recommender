from sklearn import neighbors, svm
import numpy as np
import pandas
import pickle
from training_params import test_size

#df = pandas.read_csv('dp_dataset.csv')
df = pandas.read_csv('words.csv')

df1 = df.ix[:, :-1]
df2 = df.ix[:, -1:]

print 'DataFrame Shape: '+str(df1.shape)
print 'DataFrame2 Shape: '+str(df2.shape)
# X = np.array(df.drop(['class'], 1))
# y = np.array(df['class'])

X = np.array(df1)
y = np.array(df2)

X_train = X[:-int(len(X)*test_size)]
y_train = y[:-int(len(y)*test_size)]

X_test = X[-int(len(X)*test_size):]
y_test = y[-int(len(y)*test_size):]

# clf = neighbors.KNeighborsClassifier()
clf = svm.SVC(probability=True)
clf.fit(X_train, y_train)

with open('classifier.pickle', 'wb') as f:
	pickle.dump(clf, f)


accuracy = clf.score(X_test, y_test)
print accuracy

# for i in range(len(X_test)):
#     print clf.predict_proba(X_test[i])
#     print '\t' + str(y_test[i])