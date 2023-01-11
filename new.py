# import pandas as pd
# from sklearn import tree

# # Read in the csv data
# data = pd.read_csv("data/test.csv")

# # Define the features and target
# X = data[["Category 1", "Category 2"]]
# y = data["Decision"]

# # Create the decision tree model
# clf = tree.DecisionTreeClassifier()
# clf = clf.fit(X, y)

# # Print the decision tree
# tree.plot_tree(clf)

import pandas as pd
from sklearn import tree
from sklearn.tree import export_graphviz
from graphviz import Source
import json

# load data from csv file
data = pd.read_csv('data/test.csv')

# convert categorical variables to numerical values
data = pd.get_dummies(data, columns=['Category 1', 'Category 2'])

# split data into feature and target variables
X = data.drop(['Decision'], axis=1)
y = data['Decision']

# create and fit decision tree model
clf = tree.DecisionTreeClassifier()
clf = clf.fit(X, y)

# visualize the decision tree
tree.plot_tree(clf)

# export decision tree to Graphviz file
# export_graphviz(clf, out_file='tree.dot', feature_names=X.columns)

# # convert Graphviz file to JSON
# with open('tree.dot') as f:
#     dot_graph = f.read()
# s = Source.from_file('tree.dot')
# s.format = 'json'
# stuff = s.render()
# print(stuff)
# json_data = json.loads(s.render())
# print(json_data)

# # save JSON data to a file
# with open('tree.json', 'w') as f:
#     json.dump(json_data, f)