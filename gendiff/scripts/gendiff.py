import argparse
import json


def generate_diff(file1_path, file2_path):
    """
    Generates a diff between two JSON files.
    """
    with open(file1_path, 'r') as f:
        data1 = json.load(f)
    with open(file2_path, 'r') as f:
        data2 = json.load(f)

    keys1 = set(data1.keys())
    keys2 = set(data2.keys())
    all_keys = sorted(keys1.union(keys2))

    diff = "{\n"
    for key in all_keys:
        if key in data1 and key in data2:
            if data1[key] == data2[key]:
                diff += f"    {key}: {data1[key]}\n"
            else:
                diff += f"  - {key}: {data1[key]}\n"
                diff += f"  + {key}: {data2[key]}\n"
        elif key in data1:
            diff += f"  - {key}: {data1[key]}\n"
        else:
            diff += f"  + {key}: {data2[key]}\n"
    diff += "}"

    return diff


def main():
    parser = argparse.ArgumentParser(description="Compares two configuration files and shows a difference.")
    parser.add_argument("first_file", help="First file to compare")
    parser.add_argument("second_file", help="Second file to compare")
    parser.add_argument("-f", "--format", default="plain", help="Set format of output")

    args = parser.parse_args()

    # Генерируем и выводим diff
    diff = generate_diff(args.first_file, args.second_file)
    print(diff)


if __name__ == '__main__':
    main()
