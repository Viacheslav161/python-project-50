print("Running gendiff/scripts/gendiff.py")
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


import argparse
from gendiff.parser import load_data
def generate_diff(file1_path, file2_path):
    print(f"Loading files: {file1_path}, {file2_path}")
    data1 = load_data(file1_path)
    data2 = load_data(file2_path)
    keys1 = set(data1.keys())
    keys2 = set(data2.keys())
    all_keys = sorted(keys1.union(keys2))
    diff = "{\n"
    for key in all_keys:
        if key in data1 and key in data2:
            if data1[key] != data2[key]:
                diff += f"  - {key}: {data1[key]}\n"
                diff += f"  + {key}: {data2[key]}\n"
        elif key in data1:
            diff += f"  - {key}: {data1[key]}\n"
        elif key in data2:
            diff += f"  + {key}: {data2[key]}\n"
    diff += "}"
    return diff
def main():
    parser = argparse.ArgumentParser(description="Compares two configuration files and shows a difference.")
    parser.add_argument("first_file", help="First file to compare")
    parser.add_argument("second_file", help="Second file to compare")
    parser.add_argument("-f", "--format", default="plain", help="Set format of output")
    args = parser.parse_args()
    diff = generate_diff(args.first_file, args.second_file)
    print(diff)
if __name__ == '__main__':
    main()
