import pytest
from gendiff import generate_diff


test_data = [
    ('tests/fixtures/file1.json', 'tests/fixtures/file2.json', 'tests/fixtures/expected_diff.txt', None),
    ('tests/fixtures/file1.yaml', 'tests/fixtures/file2.yaml', 'tests/fixtures/expected_diff.txt', None),
    ('tests/fixtures/file1_nested.yaml', 'tests/fixtures/file2_nested.yaml', 'tests/fixtures/expected_diff_nested.txt', None),
    ('tests/fixtures/file1_nested.json', 'tests/fixtures/file2_nested.json', 'tests/fixtures/expected_diff_nested.txt', None),
    ('tests/fixtures/file1_nested.yaml', 'tests/fixtures/file2_nested.yaml', 'tests/fixtures/expected_diff_nested_plain.txt', 'plain'),
    ('tests/fixtures/file1.yaml', 'tests/fixtures/file2.yaml', 'tests/fixtures/expected_diff_json.txt', 'json')
]


@pytest.mark.parametrize("file1, file2, expected_file, format_name", test_data)
def test_generate_diff(file1, file2, expected_file, format_name):
    with open(expected_file) as f:
        expected_result = f.read().strip()
    assert generate_diff(file1, file2, format_name) == expected_result
