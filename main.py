import os
import pickle
import prefix_tree as pt
import parse_data as pd

root_directory = "Archive"

def build_and_save_tree():
    tree = pt.PrefixTree()

    for root, _, files in os.walk(root_directory):
        for filename in files:
            if filename.endswith(".txt"):
                file_path = os.path.join(root, filename)
                lines = pd.parse_data(file_path)
                offset = 0
                for line in lines:
                    tree.insert(filename, line, offset)
                    offset += len(line) + 1

    # Save the PrefixTree object using pickle
    with open('prefix_tree.pkl', 'wb') as f:
        pickle.dump(tree, f)


if __name__ == "__main__":
    build_and_save_tree()