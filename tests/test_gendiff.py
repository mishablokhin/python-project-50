import pytest
from gendiff.modules.gendiff import generate_diff


def test_generate_diff_json():
    path1 = 'tests/fixtures/file1.json'
    path2 = 'tests/fixtures/file2.json'
    
    expected_result_path = 'tests/fixtures/expected_diff.txt'
    
    with open(expected_result_path) as f:
        expected_result = f.read().strip()
    
    assert generate_diff(path1, path2) == expected_result


def test_generate_diff_yaml():
    path1 = 'tests/fixtures/file1.yaml'
    path2 = 'tests/fixtures/file2.yaml'
    
    expected_result_path = 'tests/fixtures/expected_diff.txt'
    
    with open(expected_result_path) as f:
        expected_result = f.read().strip()
    
    assert generate_diff(path1, path2) == expected_result


def test_generate_diff_nested_yaml():
    path1 = 'tests/fixtures/file1_nested.yaml'
    path2 = 'tests/fixtures/file2_nested.yaml'
    
    expected_result_path = 'tests/fixtures/expected_diff_nested.txt'
    
    with open(expected_result_path) as f:
        expected_result = f.read().strip()
    
    assert generate_diff(path1, path2) == expected_result


def test_generate_diff_nested_json():
    path1 = 'tests/fixtures/file1_nested.json'
    path2 = 'tests/fixtures/file2_nested.json'
    
    expected_result_path = 'tests/fixtures/expected_diff_nested.txt'
    
    with open(expected_result_path) as f:
        expected_result = f.read().strip()
    
    assert generate_diff(path1, path2) == expected_result