from sklearn import tree

features = [
    [150, 0],
    [170, 0],
    [120, 1],
    [100, 1]
]

labels = ["apple", "apple" , "orange", "orange"]

clf = tree.DecisionTreeClassifier()
clf = clf.fit(features, labels)

print(f"The fruit is {clf.predict([[160, 1]])[0]}")
