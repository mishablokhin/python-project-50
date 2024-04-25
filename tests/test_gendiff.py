import pytest
import os
from gendiff import generate_diff


def get_fixture_path(filename):
    return os.path.join('tests', 'fixtures', filename)


test_data = [
    ('file1.json', 'file2.json', 'expected_diff.txt', None),
    ('file1.yaml', 'file2.yaml', 'expected_diff.txt', None),
    ('file1_nested.yaml', 'file2_nested.yaml', 'expected_diff_nested.txt', None),
    ('file1_nested.json', 'file2_nested.json', 'expected_diff_nested.txt', None),
    ('file1_nested.yaml', 'file2_nested.yaml', 'expected_diff_nested_plain.txt', 'plain'),
    ('file1.yaml', 'file2.yaml', 'expected_diff_json.txt', 'json')
]


@pytest.mark.parametrize("file1, file2, expected_file, format_name", test_data)
def test_generate_diff(file1, file2, expected_file, format_name):
    file1 = get_fixture_path(file1)
    file2 = get_fixture_path(file2)
    expected_file = get_fixture_path(expected_file)
    with open(expected_file) as f:
        expected_result = f.read()
    assert generate_diff(file1, file2, format_name) == expected_result
