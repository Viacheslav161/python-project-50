import argparse


def main():
    # Создаем парсер аргументов командной строки
    parser = argparse.ArgumentParser(description='Compares two configuration files and shows a difference.')

    # Определяем позиционные аргументы
    parser.add_argument('first_file', help='first configuration file')
    parser.add_argument('second_file', help='second configuration file')

    # Парсим аргументы
    args = parser.parse_args()

    # Здесь вы можете добавить логику для сравнения файлов
    print(f'Comparing files:\n  First file: {args.first_file}\n  Second file: {args.second_file}')


if name == 'main':
    main()
