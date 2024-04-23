from gendiff.parse_file import get_content
from gendiff.formatters import format_diff


def build_diff(data1, data2):
    keys = sorted(set(data1.keys()) | set(data2.keys()))
    diff = {}
    for key in keys:
        if key in data1 and key in data2:
            diff[key] = handle_key_in_both(data1, data2, key)
        elif key in data1:
            diff[key] = {'type': 'removed', 'value': data1[key]}
        elif key in data2:
            diff[key] = {'type': 'added', 'value': data2[key]}
    return diff


def handle_key_in_both(data1, data2, key):
    if isinstance(data1[key], dict) and isinstance(data2[key], dict):
        return handle_nested_diff(data1, data2, key)
    elif data1[key] != data2[key]:
        return handle_changed_value(data1, data2, key)
    else:
        return {'type': 'unchanged', 'value': data1[key]}


def handle_nested_diff(data1, data2, key):
    child_diff = build_diff(data1[key], data2[key])
    return {
        'type': 'nested',
        'children': child_diff
    }


def handle_changed_value(data1, data2, key):
    return {
        'type': 'changed',
        'old_value': data1[key],
        'new_value': data2[key]
    }


def generate_diff(file_path1, file_path2, format_name='stylish'):
    dict1 = get_content(file_path1)
    dict2 = get_content(file_path2)
    diff = build_diff(dict1, dict2)
    return format_diff(diff, format_name)
