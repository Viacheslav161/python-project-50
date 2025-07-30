import pytest
from gendiff import generate_diff
import json
import os

# Пример тестовых данных (создайте эти файлы)
file1_content = """
{
  "host": "hexlet.io",
  "timeout": 50,
  "proxy": "123.234.53.22",
  "follow": false
}
"""

file2_content = """
{
  "timeout": 20,
  "verbose": true,
  "host": "hexlet.io"
}
"""
expected_diff = """{\n  - follow: false\n    host: hexlet.io\n  - proxy: 123.234.53.22\n  - timeout: 50\n  + timeout: 20\n  + verbose: true\n}"""


file3_content = """
{
  "host": "hexlet.io",
  "timeout": 50,
  "proxy": "123.234.53.22",
  "follow": true
}
"""

file4_content = """
{
  "timeout": 20,
  "verbose": true,
  "host": "hexlet.io",
  "proxy": "123.234.53.22",
  "follow": true
}
"""
expected_diff2 = """{\n  - timeout: 50\n  + timeout: 20\n  + verbose: true\n}"""


# Вспомогательная функция для записи контента в временные файлы
def create_temp_file(content, suffix=".json"):
    import tempfile
    temp_file = tempfile.NamedTemporaryFile(mode='w', delete=False, suffix=suffix, encoding='utf-8')
    temp_file.write(content)
    temp_file.close()
    return temp_file.name

def test_generate_diff():
    file1_path = create_temp_file(file1_content)
    file2_path = create_temp_file(file2_content)

    diff = generate_diff(file1_path, file2_path)
    assert diff == expected_diff

    # Удаляем временные файлы
    os.unlink(file1_path)
    os.unlink(file2_path)

def test_generate_diff2():
    file3_path = create_temp_file(file3_content)
    file4_path = create_temp_file(file4_content)

    diff = generate_diff(file3_path, file4_path)
    assert diff == expected_diff2

    # Удаляем временные файлы
    os.unlink(file3_path)
    os.unlink(file4_path)

