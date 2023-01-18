from anytree import Node, RenderTree
import json
from anytree.exporter import DotExporter

def json_to_decision_tree(data):
    root = Node("root")
    build_decision_tree(data, root)
    return root

def build_decision_tree(data, parent_node):
    for key, value in data.items():
        if isinstance(value, dict):
            node = Node(key, parent=parent_node)
            build_decision_tree(value, node)
        else:
            Node(f"{key}:{value}", parent=parent_node)

def render_tree(input_json, output_png):
    with open(input_json, 'r') as f:
        data = json.load(f)

    root = json_to_decision_tree(data)
    DotExporter(root).to_picture(output_png)

render_tree('cars.json', "cars_decision_tree.png")
render_tree('sports.json', "sports_decision_tree.png")
