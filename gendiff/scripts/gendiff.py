import argparse

def main():
    parser = argparse.ArgumentParser(description="Compares two configuration files and shows a difference.")
    parser.add_argument("first_file", help="First file to compare")
    parser.add_argument("second_file", help="Second file to compare")
    parser.add_argument("-f", "--format", default="plain", help="Set format of output")

    args = parser.parse_args()

    # Здесь код сравнения файлов. Пока просто вывод аргументов:
    print(f"Comparing {args.first_file} and {args.second_file} with format {args.format}")


if __name__ == '__main__':
    main()
