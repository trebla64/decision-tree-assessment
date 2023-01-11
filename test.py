import csv
import json
import math

# Helper function to calculate the number of occurrences of each category
def count_categories(data):
    counts = {}
    for row in data:
        for category in row:
            if category not in counts:
                counts[category] = 0
            counts[category] += 1
    return counts

# Helper function to calculate the gain for a given category
def calc_gain(data, category):
    counts = count_categories(data)
    total_count = sum(counts.values())
    decision_counts = {'Y': 0, 'N': 0}
    for row in data:
        decision_counts[row[-1]] += 1
    entropy = 0
    for decision in decision_counts:
        prob = decision_counts[decision] / total_count
        if prob > 0:
            entropy -= prob * math.log(prob, 2)
    gain = entropy
    for category_value in counts:
        the_category = None
        for i, column in enumerate(data[0]):
            if column == category:
                the_category = i
        subset = [row for row in data if row[the_category] == category_value]
        prob = len(subset) / total_count
        subset_entropy = 0
        subset_decision_counts = {'Y': 0, 'N': 0}
        for row in subset:
            subset_decision_counts[row[-1]] += 1
        for decision in subset_decision_counts:
            prob = subset_decision_counts[decision] / len(subset)
            if prob > 0:
                subset_entropy -= prob * math.log(prob, 2)
        gain -= prob * subset_entropy
    return gain

# Read in the CSV file
data = []
with open('data/test.csv', newline='') as csvfile:
    reader = csv.reader(csvfile)
    next(reader)  # skip header row
    for row in reader:
        data.append(row)

# Calculate the gain for each category
gains = {'Category 1': calc_gain(data, 'Category 1'), 'Category 2': calc_gain(data, 'Category 2')}

# Determine the optimal branching order
optimal_branching_order = [max(gains, key=gains.get)]

# Output the result to a JSON file
with open('result.json', 'w') as jsonfile:
    json.dump({'branching_order': optimal_branching_order}, jsonfile)
