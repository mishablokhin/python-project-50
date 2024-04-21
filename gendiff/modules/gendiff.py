from gendiff.modules.parse_file import read_data_file
from gendiff.formatters import get_formatter


def build_diff(data1, data2):
    keys = sorted(set(data1.keys()) | set(data2.keys()))
    diff = {}
    for key in keys:
        if key in data1 and key in data2:
            if isinstance(data1[key], dict) and isinstance(data2[key], dict):
                child_diff = build_diff(data1[key], data2[key])
                diff[key] = {
                    'type': 'nested',
                    'children': child_diff
                }
            elif data1[key] != data2[key]:
                diff[key] = {
                    'type': 'changed',
                    'old_value': data1[key],
                    'new_value': data2[key]
                }
            else:
                diff[key] = {'type': 'unchanged', 'value': data1[key]}
        elif key in data1:
            diff[key] = {'type': 'removed', 'value': data1[key]}
        else:
            diff[key] = {'type': 'added', 'value': data2[key]}
    return diff


def generate_diff(file_path1, file_path2, format_name='stylish'):
    dict1 = read_data_file(file_path1)
    dict2 = read_data_file(file_path2)
    diff = build_diff(dict1, dict2)
    formatter = get_formatter(format_name)
    return formatter(diff)
