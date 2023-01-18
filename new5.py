import csv
import json
from collections import defaultdict
import math

# Helper function to calculate the entropy of a dataset
def entropy(data):
    # print(type(data))
    outcomes = defaultdict(int)
    for row in data:
        for stuff in row:
            print(stuff)
            outcomes[stuff['Decision']] += 1
    entropy = 0
    for outcome in outcomes.values():
        probability = outcome / len(data)
        entropy -= probability * math.log(probability, 2)
    return entropy

# Helper function to split a dataset on a given attribute
def split_dataset(data, attribute):
    partitions = defaultdict(list)
    for row in data:
        partitions[row[attribute]].append(row)
    return partitions

# Helper function to build the decision tree
def build_tree(data, attributes, default):
    outcomes = [row['Decision'] for row in data]
    if outcomes.count(outcomes[0]) == len(outcomes):
        return outcomes[0]
    elif not data or not attributes:
        return default
    else:
        default = max(set(outcomes), key=outcomes.count)
        best_attribute = min(attributes, key=lambda attr: entropy(split_dataset(data, attr).values()))
        tree = {best_attribute: {}}
        partitions = split_dataset(data, best_attribute)
        for partition in partitions:
            subtree = build_tree(partitions[partition], [attr for attr in attributes if attr != best_attribute], default)
            tree[best_attribute][partition] = subtree
    return tree

# Main function to read input files and write output file
def decision_tree(input_file1, output_file):
    data = []
    with open(input_file1, 'r') as f1:
        reader = csv.DictReader(f1)
        headers = reader.fieldnames
        for row in reader:
            data.append(row)
    attributes = headers[:-1]
    # attributes = list(range(len(headers) - 1))
    tree = build_tree(data, attributes, None)
    with open(output_file, 'w') as f:
        json.dump(tree, f)

# Example usage:
decision_tree('data/test.csv', 'output.json')
