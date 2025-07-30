import argparse
import json

def main():
    parser = argparse.ArgumentParser(description="Compares two configuration files and shows a difference.")
    parser.add_argument("first_file", help="First file to compare")
    parser.add_argument("second_file", help="Second file to compare")
    parser.add_argument("-f", "--format", default="plain", help="Set format of output")

    args = parser.parse_args()

    # Чтение и парсинг файлов
    try:
        with open(args.first_file, 'r') as f:
            data1 = json.load(f)
        with open(args.second_file, 'r') as f:
            data2 = json.load(f)
    except FileNotFoundError as e:
        print(f"Error: File not found: {e.filename}")
        exit(1)
    except json.JSONDecodeError as e:
        print(f"Error: Invalid JSON: {e}")
        exit(1)

    # Здесь код сравнения файлов (пока просто вывод):
    print(f"Comparing {args.first_file} and {args.second_file} with format {args.format}")
    print("Data from first file:", data1)
    print("Data from second file:", data2)


if __name__ == '__main__':
    main()
