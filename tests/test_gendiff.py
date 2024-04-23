import pytest
from gendiff import generate_diff


def file_path(filename):
    return f"tests/fixtures/{filename}"


test_data = [
    (file_path('file1.json'), file_path('file2.json'), file_path('expected_diff.txt'), None),
    (file_path('file1.yaml'), file_path('file2.yaml'), file_path('expected_diff.txt'), None),
    (file_path('file1_nested.yaml'), file_path('file2_nested.yaml'), file_path('expected_diff_nested.txt'), None),
    (file_path('file1_nested.json'), file_path('file2_nested.json'), file_path('expected_diff_nested.txt'), None),
    (file_path('file1_nested.yaml'), file_path('file2_nested.yaml'), file_path('expected_diff_nested_plain.txt'), 'plain'),
    (file_path('file1.yaml'), file_path('file2.yaml'), file_path('expected_diff_json.txt'), 'json')
]


@pytest.mark.parametrize("file1, file2, expected_file, format_name", test_data)
def test_generate_diff(file1, file2, expected_file, format_name):
    with open(expected_file) as f:
        expected_result = f.read()
        assert generate_diff(file1, file2, format_name) == expected_result
