import pandas as pd
from sklearn import tree
from sklearn.tree import export_graphviz
from graphviz import Source
import json
# from dtreeviz.trees import *
from dtreeviz import dtreeviz

# load data from csv file
data = pd.read_csv('data/test.csv')

# convert categorical variables to numerical values
data = pd.get_dummies(data, columns=['Category 1', 'Category 2'])

# convert target variable 'Decision' to numerical values
data['Decision'] = data['Decision'].map({'Y': 1, 'N': 0})

# split data into feature and target variables
X = data.drop(['Decision'], axis=1)
y = data['Decision']

# create and fit decision tree model
clf = tree.DecisionTreeClassifier()
clf = clf.fit(X, y)

# visualize the decision tree
# tree.plot_tree(clf)

# Export decision tree to JSON
# viz = dtreeviz(clf, X, y, target_name='Decision', feature_names=list(X.columns))
# viz.save("tree.svg")

dot_data = tree.export_graphviz(clf, out_file=None, feature_names=list(X.columns), class_names=['Y','N'], filled=True, rounded=True, special_characters=True)
graph = Source(dot_data)

# export decision tree to json
graph_json = json.dumps(json.loads(graph.pipe(format='json')))

# write json object to a file
with open("tree.json", "w") as f:
    f.write(graph_json)
