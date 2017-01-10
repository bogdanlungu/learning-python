""" Naive Bayes - Gaussian Naive Bayes """
# pylint: disable=C0103

from sklearn.naive_bayes import GaussianNB
import numpy as np

A = np.array([[-1, -1], [-2, -1], [-3, -2], [1, 1], [2, 1], [3, 2]])
B = np.array([1, 1, 1, 2, 2, 2])
clf = GaussianNB() #create classifier

clf.fit(A, B)
print(clf.predict([[1, 1]]))
