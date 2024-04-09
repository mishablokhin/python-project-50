import pytest
from gendiff.modules.gendiff import generate_diff


def test_generate_diff():
    path1 = 'tests/fixtures/file1.json'
    path2 = 'tests/fixtures/file2.json'
    
    # Путь к файлу с ожидаемым результатом
    expected_result_path = 'tests/fixtures/expected_diff.txt'
    
    # Считывание ожидаемого результата из файла
    with open(expected_result_path) as f:
        expected_result = f.read().strip()
    
    assert generate_diff(path1, path2) == expected_result
