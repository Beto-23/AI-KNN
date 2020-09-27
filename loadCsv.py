import pandas as pd
from sklearn.metrics import accuracy_score
from knnPure import KnnClasifier
from sklearn.model_selection import train_test_split
df = pd.read_csv('datasets-short.csv')


x = df['SepalLengthCm'].to_numpy()
y = df['SepalWidthCm'].to_numpy()
tags = df['Species'].to_numpy()
points = []

for i in range(x.size):
    points.append([x[i],y[i]])


K = 3
trainPoints, testPoints = train_test_split(points, test_size=0.1, shuffle=False)
testTags, tagsExpected = train_test_split(tags, test_size=0.1, shuffle=False)


knn = KnnClasifier()
tagsPredicted = knn.predict(testPoints, trainPoints, testTags, K)

print(tagsExpected)
print(tagsPredicted)

a = accuracy_score(tagsExpected, tagsPredicted)

print(a)