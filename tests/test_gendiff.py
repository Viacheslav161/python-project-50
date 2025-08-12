import yaml

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
# Вспомогательная функция для создания временных файлов
def create_temp_file(content, suffix=".json"):
    import tempfile
    temp_file = tempfile.NamedTemporaryFile(mode='w', delete=False, suffix=suffix, encoding='utf-8')
    temp_file.write(content)
    temp_file.close()
    return temp_file.name

@pytest.fixture
def yaml_files(tmpdir):
    file1 = tmpdir.join("file1.yml")
    file2 = tmpdir.join("file2.yml")

    # Содержимое первого файла (YAML)
    data1 = {"key1": "value1", "key2": "value2"}
    file1.write(yaml.dump(data1))

    # Содержимое второго файла (YAML)
    data2 = {"key1": "value1", "key2": "value3"}
    file2.write(yaml.dump(data2))

    return str(file1), str(file2)

def test_generate_diff_yaml_same_files(yaml_files):
    file1, file2 = yaml_files
    with open(file2, 'w') as f:
        f.write(open(file1).read())

    expected = "{\n}"
    assert generate_diff(file1, file2) == expected

def test_generate_diff_yaml_different_files(yaml_files):
    file1, file2 = yaml_files

    expected = """{
  - key2: value2
  + key2: value3
}"""

    assert generate_diff(file1, file2) == expected

def test_generate_diff_yaml_missing_keys(yaml_files):
    file1, file2 = yaml_files
    # Создадим файл без одного из ключей
    data3 = {"key1": "value1"}
    with open(file2, 'w') as f:
        yaml.dump(data3, f)

    expected = """{
  - key2: value2
}"""

    assert generate_diff(file1, file2) == expected
