# Decision Tree Assessment

The Python code in this repository is capable of generating and rendering an optimal decision tree given a CSV file containing classifiers and a decision variable.

### Dependencies

Only the Python `anytree` library is required to run the rendering code. The calculation code uses standard libraries.

It is recommended to have a Python virtual environment set up with the above mentioned library installed. To install the library the virtual environment must be activated
and then `pip install anytree` can be run on the console.

### Usage

The code is split into two Python scripts. One to calculate the trees and one to render it. The `calculate_trees.py` script must be run first. It will read the CSV files in
the data directory and then generate the JSON output files in the same directory in which the command was executed. Therefore it is recommended to run the command from the
root directory of the repository.

Once the JSON files has been generated, the `render_trees.py` script can be executed. It will generate the PNG images in the same directory.

### Known bugs

- The trees shown in the PNG image has an extra `root` node. Just ignore this node and follow it to the next node. I did not have time to find a way to remove this
- There are many (too) many arrows in the cars PNG. I think this is because there are data with the same names in the dataset. I didn't pursue this issue further
