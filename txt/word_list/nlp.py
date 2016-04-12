#!/usr/bin/python
import pandas as pd
import numpy as np
from sklearn.cross_validation import train_test_split
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.linear_model import LogisticRegression

allFiles = glob.glob("*.csv")
frame = pd.DataFrame()
list_ = []
for file_ in allFiles:
    df = pd.read_csv(file_,index_col=None, header=0)
    list_.append(df)
frame = pd.concat(list_)

print frame.head()

# df = pd.read_csv('architecture.csv')
# df['field'] = 'architecture'
# print df.head()

# df.order.astype(int)

# vectorizer = CountVectorizer()

# Xcv = vectorizer.fit_transform(df['word'])

# print '%d samples, %d features' % Xcv.shape

# vectorizer = CountVectorizer(max_features=5000)

# # convert our documents and their labels into numpy arrays
# Xcv = vectorizer.fit_transform(df['word'])
# # Y = (df['order'] == 'order').values.astype(np.int8)

# # # split the converted data into training and test sets
# # xtrain, xtest, ytrain, ytest = train_test_split(Xcv, Y)