import json
import os
import pytest
from gendiff.scripts.gendiff import generate_diff

# Создаем временные JSON-файлы для тестирования
@pytest.fixture
def json_files(tmpdir):
    file1 = tmpdir.join("file1.json")
    file2 = tmpdir.join("file2.json")

    # Содержимое первого файла
    data1 = {"key1": "value1", "key2": "value2"}
    file1.write(json.dumps(data1))

    # Содержимое второго файла
    data2 = {"key1": "value1", "key2": "value3"}
    file2.write(json.dumps(data2))

    return str(file1), str(file2)

def test_generate_diff_same_files(json_files):
    file1, file2 = json_files

    # Перезаписываем второй файл содержимым первого
    with open(file2, 'w') as f:
        f.write(open(file1).read())

    expected = "{\n}"

    assert generate_diff(file1, file2) == expected

def test_generate_diff_different_files(json_files):
    file1, file2 = json_files

    expected = """{
  - key2: value2
  + key2: value3
}"""

    assert generate_diff(file1, file2) == expected

def test_generate_diff_missing_keys(json_files):
    file1, file2 = json_files
    # Создадим файл без одного из ключей
    data3 = {"key1": "value1"}
    with open(file2, 'w') as f:
        json.dump(data3, f)

    expected = """{
  - key2: value2
}"""

    assert generate_diff(file1, file2) == expected
